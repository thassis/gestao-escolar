import { Environment } from '../../shared-components/environment';
import { Api } from '../axios-config';

export interface IListagemALunos {
    id: number;
    name: string;
    born_date: string;
    address: string;
    tutor_name: string;
    tutor_phone: string;
    class_shift: string;
}

export interface IDetalheAlunos {
    id: number;
    name: string;
    born_date: string;
    address: string;
    tutor_name: string;
    tutor_phone: string;
    class_shift: string;
}

//Irá tipar nossos dados
type TPessoasComTotalCount = {
    data: IListagemALunos[];
    totalCount: number;
}

const getAll = async (page = 1, filter = ''): Promise<TPessoasComTotalCount | Error> => {
  try{
    const urlRelative = `/aluno?_page=${page}&_limit=${Environment.LIMITE_DE_LINHAS}&name_like=${filter}`;
    const { data, headers } = await Api.get(urlRelative);

    if(data){
      return {
        data,
        totalCount: Number(headers['x-total-count'] || Environment.LIMITE_DE_LINHAS),
      };
    }
    return new Error('Erro ao listar os registros');
  }catch(error){  
    return new Error((error as {message:string}).message ||'Erro ao listar os registros');
  }
};

const getById = async (id: number): Promise<IDetalheAlunos | Error> => {
  try{
    const { data} = await Api.get(`/aluno/${id}`);
  
    if(data){
      return data;
    }
    return new Error('Erro ao consultar o regitro');
  }catch(error){  
    return new Error((error as {message:string}).message ||'Erro ao consultar o regitro');
  }
};

const create = async (dados: Omit<IDetalheAlunos, 'id'>): Promise<number | Error> => {
  try {
    const response = await Api.post('http://127.0.0.1:8000/create/aluno', dados);
    console.log('Aluno criado com sucesso:', response.data);
    
    if (response.status === 200) {
      const { data } = response;
      return data.id;
    }
    return new Error('Erro ao criar um registro');
  } catch (error) {
    return new Error((error as { message: string }).message || 'Erro ao criar um registro');
  }
};

const updateById = async (id: number, dados: IDetalheAlunos): Promise<void | Error> => {
  try{
    await Api.put(`/aluno/${id}`, dados);
  }catch(error){  
    return new Error((error as {message:string}).message ||'Erro ao atualizar o regitro');
  }
};

const deleteById = async (id: number): Promise<void | Error> => {
  try{
    await Api.delete(`/aluno/${id}`);
  }catch(error){  
    return new Error((error as {message:string}).message ||'Erro ao apagar o regitro');
  }
};

export const AlunosServices = {
  getAll,
  getById,
  create,
  updateById,
  deleteById,
};