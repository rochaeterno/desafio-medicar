import { Especialidade } from './especialidade.model';
export interface Medico {
  id?: number;
  crm: string;
  nome: string;
  especialidade: Especialidade;
}
