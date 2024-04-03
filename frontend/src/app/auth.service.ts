import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {User}  from "./authorization/authorization.component";
import {User as User2}  from "./account/account.component";
import {NewUser} from "./registration/registration.component";
import {Router} from "@angular/router";
import {Product} from "./models";

const base_url = "http://127.0.0.1:8000"

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private httpOptions = {
    headers: new HttpHeaders({
      'Authorization': 'JWT ' + localStorage.getItem('token')
    })
  };
  constructor(private http: HttpClient, private router: Router) { }

  login(user: User): Observable<{token: string}>{
    return this.http.post<{token:string}>(`${base_url}/login/`, user)
  }

  register(user: NewUser){
    return this.http.post(`${base_url}/registration/`, user).subscribe(resp=>{
      this.router.navigate(['../login'])
    }, error => {
    })
  }
  logout(){
    localStorage.removeItem('token');
  }

  getUser(): Observable<User2>{
    return this.http.get<User2>(`${base_url}/user/`, this.httpOptions)
  }
  getToken() {
    // Получить токен из localStorage
    return localStorage.getItem('token');
  }

  isLoggedIn() {
    // Проверить наличие токена в localStorage
    const token = this.getToken();
    return token != null;
  }
}
