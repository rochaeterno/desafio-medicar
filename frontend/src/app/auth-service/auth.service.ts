import { Injectable } from '@angular/core';

import { BehaviorSubject, Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { User } from '../models/user.model';
import { Auth } from '../models/auth.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  baseUrl = `${environment.apiUrl}`;

  constructor(private http: HttpClient,) { }

  private _user = new BehaviorSubject<User[]>([]);
  private _token = new BehaviorSubject<Auth>({ refresh: '', access: '' });

  get user(): User[] {
    return this._user.value;
  }

  set user(user: User[]) {
    this._user.next(user);
  }

  get token(): Auth {
    return this._token.value;
  }

  set token(token: Auth) {
    this._token.next(token);
  }

  login(user: User): Observable<Auth> {
    return this.http.post<Auth>(`${this.baseUrl}/api/token/`, user)
  }
}


