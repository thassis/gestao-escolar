import React, { useEffect, useMemo, useState } from "react";
import {
  Box,
  Button,
  Checkbox,
  IconButton,
  InputLabel,
  MenuItem,
  Pagination,
  Paper,
  Select,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableFooter,
  TableHead,
  TableRow,
  TextField,
  Typography,
} from "@mui/material";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useDebounce } from "shared-components/hooks";
import { Environment } from "shared-components/environment";
import Header from "shared-components/header/Header";
import {
  AlunosServices,
  IListagemALunos,
} from "services/alunos/AlunosServices";
import { BoxForm, BoxList, BoxSelect, PaperList } from "./styles";
import { ATTENDANCE_LIST } from "utils/storageKeys";

type Attendance = {
  date: string;
  isPresent: boolean;
};

interface IRow extends IListagemALunos {
  attendanceList: Attendance[];
}

const AttendanceList = () => {
  const currentYear = new Date().getFullYear();
  const currentMonth = new Date().getMonth();

  const [searchParams, setSearchParams] = useSearchParams();
  const [totalCount, setTotalCount] = useState(0);
  const [rows, setRows] = useState<IRow[]>([]);
  const [selectedMonth, setSelectMonth] = useState(currentMonth);
  const [hasChanges, setHasChanges] = useState(false);

  const busca = useMemo(() => {
    return searchParams.get("busca") || "";
  }, [searchParams]);

  const pagina = useMemo(() => {
    return Number(searchParams.get("pagina") || "1");
  }, [searchParams]);

  const onChangeMonth = (month: number) => {
    console.log(month);
    setSelectMonth(month);
  };

  const getEmptyAttendance = (): Attendance[] => {
    return [...Array(12)].flatMap((_, month) => {
      const days = new Date(currentYear, month + 1, 0).getDate();
      return [...Array(days)].map((_, index) => ({
        isPresent: false,
        date: `${month}-${index + 1}-${currentYear}`,
      }))
    })
  }

  const numberOfDays = new Date(currentYear, selectedMonth, 0).getDate();

  const handleToggleDay = (id: number, date: string) => {
    setHasChanges(true);

    setRows((prevRows) =>
      prevRows.map((row) =>
        row.id === id
          ? {
              ...row,
              attendanceList: row.attendanceList.map((attendance) =>
                attendance.date === date
                  ? { date, isPresent: !attendance.isPresent }
                  : attendance
              ),
            }
          : row
      )
    );
  };

  const onClickSave = () => {
    localStorage.setItem(ATTENDANCE_LIST, JSON.stringify(rows));
    setHasChanges(false);
    
    alert("Dados salvos com sucesso!");
  };

  const getAttendaceByStudentMonth = (row: IRow) => {
    const attendanceByMonth = row.attendanceList.filter(attendance => {
      const month = parseInt(attendance.date.split('-')[0])
      return month === selectedMonth - 1;
    });

    console.log(attendanceByMonth.length)

    return attendanceByMonth.map((attendance, index) => (
      <TableCell key={index}>
        <Checkbox
          checked={attendance.isPresent}
          onChange={() =>
            handleToggleDay(row.id, attendance.date)
          }
        />
      </TableCell>
    ))
  }

  useEffect(() => {
    AlunosServices.getAll(pagina, busca).then((result) => {
      if (result instanceof Error) {
        alert(result.message);
      } else {
        console.log(result);
        const localAttendance = localStorage.getItem(ATTENDANCE_LIST);

        let attendanceList: IRow[] = [];

        if (localAttendance) {
          attendanceList = JSON.parse(localAttendance) as IRow[];
          console.log(attendanceList);
        } else {
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
            }));
          });

          attendanceList = adaptedData.map((data) => ({
            ...data,
            attendanceList: getEmptyAttendance(),
          }));
        }

        setTotalCount(result.totalCount);
        setRows(attendanceList);
      }
    });
  }, [busca, pagina, selectedMonth]);

  return (
    <>
      <Header />

      <BoxList>
        <Typography variant="h4" sx={{ m: 2 }}>
          Lista de Presença
        </Typography>

        <BoxForm>
          <BoxSelect>
            <InputLabel id="month-select-label">Mês</InputLabel>
            <Select
              fullWidth
              labelId="month-select-label"
              id="month-select"
              value={selectedMonth}
              onChange={(e) => onChangeMonth(Number(e.target.value))}
            >
              <MenuItem value={1}>Janeiro</MenuItem>
              <MenuItem value={2}>Fevereiro</MenuItem>
              <MenuItem value={3}>Março</MenuItem>
              <MenuItem value={4}>Abril</MenuItem>
              <MenuItem value={5}>Maio</MenuItem>
              <MenuItem value={6}>Junho</MenuItem>
              <MenuItem value={7}>Julho</MenuItem>
              <MenuItem value={8}>Agosto</MenuItem>
              <MenuItem value={9}>Setembro</MenuItem>
              <MenuItem value={10}>Outubro</MenuItem>
              <MenuItem value={11}>Novembro</MenuItem>
              <MenuItem value={12}>Dezembro</MenuItem>
            </Select>
          </BoxSelect>

          <Button
            variant="contained"
            onClick={() => onClickSave()}
            disabled={!hasChanges}
          >
            Salvar
          </Button>
        </BoxForm>

        <TableContainer
          component={Paper}
          variant="outlined"
          sx={{ m: 1, width: "auto" }}
        >
          <Table>
            <TableHead>
              <TableRow>
                <TableCell width={150}>Nome</TableCell>
                {[...Array(numberOfDays)].map((_, index) => (
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
                  {getAttendaceByStudentMonth(row)}
                </TableRow>
              ))}
            </TableBody>

            {totalCount === 0 && (
              <caption>{Environment.LISTAGEM_VAZIA}</caption>
            )}

            <TableFooter>
              {totalCount > 0 && totalCount > Environment.LIMITE_DE_LINHAS && (
                <TableRow>
                  <TableCell colSpan={3}>
                    <Pagination
                      page={pagina}
                      count={Math.ceil(
                        totalCount / Environment.LIMITE_DE_LINHAS
                      )}
                      onChange={(_, newPage) =>
                        setSearchParams(
                          { busca, pagina: newPage.toString() },
                          { replace: true }
                        )
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
