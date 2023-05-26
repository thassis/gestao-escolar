import React, { useEffect, useMemo, useState } from "react";
import { Box } from '@mui/system';
import { useSearchParams } from "react-router-dom";
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import SearchIcon from '@mui/icons-material/Search';
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

import Header from "shared-components/header/Header";import { AlunosServices, IListagemALunos } from "services/alunos/AlunosServices";
import { useDebounce } from "shared-components/hooks";
import { Environment } from "shared-components/environment";
import { BoxList, PaperList } from "./styles";
;

const ListStudent = () => {
  //Definindo os stats
  const [searchParams, setSearchParams] = useSearchParams();
  const [totalCount, setTotalCount] = useState(0);
  const [rows, setRows] = useState<IListagemALunos[]>([]);
  const { debounce } = useDebounce();

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
        //Consulta foi finalizada
          .then((result) => {
            if(result instanceof Error){
              alert(result.message);
            }else{
              console.log(result);
  
              setTotalCount(result.totalCount);
              setRows(result.data);
            }
          });
      });
    }, [busca, pagina]);

    //Lógica para deletar o registro
    const handleDelete = (id: number) => {
      if(window.confirm('Realmente deseja apagar?')){
        AlunosServices.deleteById(id)
          .then((result) => {
            if(result instanceof Error){
              alert(result.message);
            }else{
              setRows(oldRows => {
                return[
                  ...oldRows.filter(row => row.id !== id)
                ];
              });
              alert('Registro apagado com sucesso!');
            }
          });
      }
    };


  
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

      <BoxList >
        <Typography variant="h4" sx={{ m: 2 }}>Lista de Alunos</Typography>

        <TableContainer component={Paper} variant='outlined' sx={{ m: 1, width: 'auto' }}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell width={100}>Editar/Excluir</TableCell>
                <TableCell >Nome dos Alunos</TableCell>
                <TableCell>Turma</TableCell>
                <TableCell>Informações</TableCell>
              </TableRow>
            </TableHead>
    
            <TableBody>
              {rows.map(row => (  
                <TableRow data-testid="student-row">
                <TableCell>
                  <IconButton size="small">
                    <EditIcon />
                  </IconButton>
                  <IconButton size="small" onClick={() => handleDelete (row.id)}>
                    <DeleteIcon />
                  </IconButton>
                </TableCell>
                <TableCell>{row.name}</TableCell>
                <TableCell>{row.class_shift}</TableCell>
                <TableCell>Inglês básico</TableCell>
              </TableRow>
              ))}
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

      </BoxList>
      
    </>
  );
};

export default ListStudent;
function debounce(arg0: () => void) {
  throw new Error("Function not implemented.");
}

