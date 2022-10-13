import { Injectable } from '@angular/core';

import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { Agenda } from '../models/agenda.model';
import { Especialidade } from '../models/especialidade.model';
import { Medico } from '../models/medico.model';
import { Consulta } from '../models/consulta.model';

@Injectable({
  providedIn: 'root'
})
export class CreateConsultaFormServiceService {
  baseUrl = `${environment.apiUrl}`;

  constructor(
    private http: HttpClient,
  ) { }

  private _agendas = new BehaviorSubject<Agenda[]>([]);
  private _medicos = new BehaviorSubject<Medico[]>([]);
  private _especialidades = new BehaviorSubject<Especialidade[]>([]);

  get agendas(): Agenda[] {
    return this._agendas.value;
  }

  get medicos(): Medico[] {
    return this._medicos.value;
  }

  get especialidades(): Especialidade[] {
    return this._especialidades.value;
  }

  set especialidades(especialidades: Especialidade[]) {
    this._especialidades.next(especialidades);
  }

  set agendas(agendas: Agenda[]) {
    this._agendas.next(agendas);
  }

  set medicos(medicos: Medico[]) {
    this._medicos.next(medicos);
  }


  getAgendasByMedico(medico_id: number): Observable<Agenda[]> {
    return this.http.get<Agenda[]>(`${this.baseUrl}/agendas?medico=${medico_id}`);
  }

  getMedicosByEspecialidade(especialidade_id: number): Observable<Medico[]> {
    return this.http.get<Medico[]>(`${this.baseUrl}/medicos?especialidade=${especialidade_id}`);
  }

  getEspecialidades(): Observable<Especialidade[]> {
    return this.http.get<Especialidade[]>(`${this.baseUrl}/especialidades/`);
  }

  criarConsulta(new_consulta: any): Observable<Consulta> {
    return this.http.post<Consulta>(`${this.baseUrl}/consultas/`, new_consulta);
  }

  resetFormData() {
    this.agendas.splice(0);
    this.medicos.splice(0);
  }
}
