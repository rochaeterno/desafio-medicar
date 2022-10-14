import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from 'src/environments/environment';
import { Observable, BehaviorSubject } from 'rxjs';
import { Consulta } from '../models/consulta.model';

@Injectable({
  providedIn: 'root'
})
export class ListConsultasService {
  baseUrl = `${environment.apiUrl}`;

  constructor(
    private http: HttpClient,
  ) { }

  private _consultas = new BehaviorSubject<Consulta[]>([]);

  get consultas(): Consulta[] {
    return this._consultas.value;
  }

  set consultas(consultas: Consulta[]) {
    this._consultas.next(consultas);
  }

  getConsultas(): Observable<Consulta[]> {
    return this.http.get<Consulta[]>(`${this.baseUrl}/consultas/`);
  }

  deleteConsulta(consulta_id: any): Observable<void> {
    return this.http
      .delete<void>(`${this.baseUrl}/consultas/${consulta_id}/`)
  }
}
