import { Medico } from './medico.model';

export interface Agenda {
    id?: number;
    dia: string;
    horarios: Array<string>;
    medico: Medico;
}