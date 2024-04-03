import { Injectable } from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Route, Router, RouterStateSnapshot, UrlTree} from '@angular/router';
import { Observable } from 'rxjs';
import {AuthService} from "./auth.service";
import {MyDB} from "./db";

@Injectable({
  providedIn: 'root'
})
export class AuthoGuard implements CanActivate {
  constructor(private router: Router,
              public authService: AuthService) {
  }
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    if(this.authService.isLoggedIn()){
      return true;
    }
      this.router.navigate(['login']);
      return false;
  }

}
