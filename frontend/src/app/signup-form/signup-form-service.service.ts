import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


import { Observable, BehaviorSubject } from 'rxjs';
import { environment } from 'src/environments/environment';
import { User } from '../models/user.model';

@Injectable({
  providedIn: 'root'
})
export class SignupFormServiceService {
  baseUrl = `${environment.apiUrl}`;

  constructor(
    private http: HttpClient,
  ) { }

  criarUsuario(signup_form: any): Observable<User> {
    return this.http.post<User>(`${this.baseUrl}/user/`, signup_form);
  }
}
