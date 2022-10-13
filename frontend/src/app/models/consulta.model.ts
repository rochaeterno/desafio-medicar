import { Medico } from './medico.model';

export interface Consulta {
  id?: number;
  dia: string;
  horario: string;
  data_agendamento: string;
  medico: Medico;
}
