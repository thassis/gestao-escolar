import React, { useEffect, useMemo, useState } from "react";
import {
  Box,
  Checkbox,
  IconButton,
  Pagination,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableFooter,
  TableHead,
  TableRow,
  TextField,
  Typography
} from "@mui/material";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useDebounce } from "shared-components/hooks";
import { Environment } from "shared-components/environment";
import Header from "shared-components/header/Header";
import { AlunosServices, IListagemALunos } from "services/alunos/AlunosServices";
import { BoxList, PaperList } from "./styles";

interface IRow extends IListagemALunos {
  days: boolean[];
}

const AttendanceList = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [totalCount, setTotalCount] = useState(0);
  const [rows, setRows] = useState<IRow[]>([]);
  const { debounce } = useDebounce();
  const navigate = useNavigate();

  const busca = useMemo(() => {
    return searchParams.get("busca") || "";
  }, [searchParams]);

  const pagina = useMemo(() => {
    return Number(searchParams.get("pagina") || "1");
  }, [searchParams]);

  useEffect(() => {
    debounce(() => {
      AlunosServices.getAll(pagina, busca)
        .then((result) => {
          if (result instanceof Error) {
            alert(result.message);
          } else {
            console.log(result);
  
            const adaptedData = Object.values(result.data).flatMap((item) => {
              const dados = Object.values(item);
              return dados.map((dado) => ({
                id: dado.id,
                name: dado.name,
                born_date: dado.born_date.toString(),
                address: dado.address,
                tutor_name: dado.tutor_name,
                tutor_phone: dado.tutor_phone,
                class_shift: dado.class_shift,
                days: Array.from({ length: 30 }, () => false),
              }));
            });
  
            setTotalCount(result.totalCount);
            setRows(adaptedData);
          }
        });
    });
  }, [busca, pagina]);
  

  const handleToggleDay = (id: number, index: number) => {
    setRows((prevRows) =>
      prevRows.map((row) =>
        row.id === id
          ? {
              ...row,
              days: [
                ...row.days.slice(0, index),
                !row.days[index],
                ...row.days.slice(index + 1)
              ]
            }
          : row
      )
    );
  };

  return (
    <>
      <Header />

      <BoxList>
        <Typography variant="h4" sx={{ m: 2 }}>
          Lista de Presença
        </Typography>

        <TableContainer component={Paper} variant="outlined" sx={{ m: 1, width: "auto" }}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell width={150}>Nome</TableCell>
                {[...Array(30)].map((_, index) => (
                  <TableCell key={index} width={20}>
                    {index + 1}
                  </TableCell>
                ))}
              </TableRow>
            </TableHead>

            <TableBody>
              {rows.map((row) => (
                <TableRow data-testid="student-row" key={row.id}>
                  <TableCell>{row.name}</TableCell>
                  {row.days.map((day, index) => (
                    <TableCell key={index}>
                      <Checkbox checked={day} onChange={() => handleToggleDay(row.id, index)} />
                    </TableCell>
                  ))}
                </TableRow>
              ))}
            </TableBody>

            {totalCount === 0 && <caption>{Environment.LISTAGEM_VAZIA}</caption>}

            <TableFooter>
              {totalCount > 0 && totalCount > Environment.LIMITE_DE_LINHAS && (
                <TableRow>
                  <TableCell colSpan={3}>
                    <Pagination
                      page={pagina}
                      count={Math.ceil(totalCount / Environment.LIMITE_DE_LINHAS)}
                      onChange={(_, newPage) =>
                        setSearchParams({ busca, pagina: newPage.toString() }, { replace: true })
                      }
                    />
                  </TableCell>
                </TableRow>
              )}
            </TableFooter>
          </Table>
        </TableContainer>
      </BoxList>
    </>
  );
};

export default AttendanceList;
