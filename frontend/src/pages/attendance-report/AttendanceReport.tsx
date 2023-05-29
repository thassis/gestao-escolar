import React, { useEffect, useMemo, useState } from "react";
import { Box } from '@mui/system';
import SearchIcon from '@mui/icons-material/Search';
import { useNavigate, useSearchParams } from "react-router-dom";

import { 
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

import { BoxList, PaperList } from "./styles";
import { useDebounce } from "shared-components/hooks";
import { Environment } from "shared-components/environment";
import Header from "shared-components/header/Header";import { AlunosServices, IListagemALunos } from "services/alunos/AlunosServices";
;

const AttendanceReport = () => {
  //Definindo os stats
  const [searchParams, setSearchParams] = useSearchParams();
  const [totalCount, setTotalCount] = useState(0);
  const [rows, setRows] = useState<IListagemALunos[]>([]);
  const { debounce } = useDebounce();
  const navigate = useNavigate();

  const busca = useMemo(() => {
    return searchParams.get('busca') || '';
  }, [searchParams]);

  //Pegando a página atual
  const pagina = useMemo(() => {
    return Number(searchParams.get('pagina') || '1');
  }, [searchParams]);

    //Realizar as consultas dentro de um useEffect
  useEffect(() => {
    debounce(() => {
      AlunosServices.getAll(pagina, busca)
        .then((result) => {
          if (result instanceof Error) {
            alert(result.message);
          } else {
            console.log(result);
  
            const adaptedData = [];
            for (const key in result.data) {
              const item = result.data[key];
              
              const dados = Object.values(item);
              //Acessar cada indice do array dados
              for (let i = 0; i < dados.length; i++) {
                const adaptedItem = {
                  id: dados[i].id,
                  name: dados[i].name,
                  born_date: dados[i].born_date.toString(),
                  address: dados[i].address,
                  tutor_name: dados[i].tutor_name,
                  tutor_phone: dados[i].tutor_phone,
                  class_shift: dados[i].class_shift,
                };
                adaptedData.push(adaptedItem);
              }
            }
  
            setTotalCount(result.totalCount);
            setRows(adaptedData);
          }
        });
    });
  }, [busca, pagina]);

  
  return (
    <>
      <Header />

      <Box display='flex' justifyContent='center'>
        <PaperList>
           <TextField
             label="Busca por aluno"
             type="search"
             value={busca}
             onChange={texto => setSearchParams({ busca: texto.target.value, pagina: '1' }, { replace: true })}
             sx={{ flexGrow: 1 }}
           />
           <IconButton type="button" sx={{ p: '10px' }} aria-label="search">
             <SearchIcon />
           </IconButton>
          </PaperList>
      </Box>

      <Typography variant="h4" sx={{ m: 2 }}>Relatório dos Alunos</Typography>
      
      <Box display='flex' flexDirection='row'>
        <Box sx={{ width: '50%', flexBasis: '50%' }}>
          <TableContainer component={Paper} variant='outlined' sx={{ m: 1, height: '100%'}}>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell >Nome dos Alunos</TableCell>
                  <TableCell>Qtd Presença</TableCell>
                  <TableCell>Qtd Faltas</TableCell>
                  <TableCell>Porcentagem de faltas'</TableCell>
                </TableRow>
              </TableHead>
              
              <TableBody>
                {rows.length > 0 ? (
                  rows.map((row) => (
                    <TableRow data-testid="student-row">
                      <TableCell>{row.name}</TableCell>
                      <TableCell>0</TableCell>
                      <TableCell>0</TableCell>
                      <TableCell>Fazer o calculo</TableCell>
                    </TableRow>
                  ))
              ) : (
                <TableRow>
                  <TableCell colSpan={7}>
                    Nenhum aluno encontrado.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>

              {totalCount === 0 &&(
                <caption>{Environment.LISTAGEM_VAZIA}</caption>
              )}

              <TableFooter>
                {(totalCount > 0 && totalCount > Environment.LIMITE_DE_LINHAS) && (
                  <TableRow>
                      <TableCell colSpan={3}>
                      <Pagination 
                          page={pagina}
                          count={Math.ceil(totalCount/Environment.LIMITE_DE_LINHAS)}
                          onChange={(_, newPage) => setSearchParams({busca, pagina: newPage.toString()}, {replace: true})}
                      />
                      </TableCell>
                  </TableRow>
                )}
              </TableFooter>
            </Table>
          </TableContainer>
        </Box>
        <Box sx={{ width: '50%', flexBasis: '50%', marginLeft: '40px' }}>
          Criação do Dashboard
        </Box>
      </Box>
    </>
  );
};

export default AttendanceReport;
function debounce(arg0: () => void) {
  throw new Error("Function not implemented.");
}

