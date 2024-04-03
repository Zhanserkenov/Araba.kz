import {Component, OnInit} from '@angular/core';
import {  Router, CanActivate } from '@angular/router';
import {AuthService} from "../auth.service";
import {MyDB} from "../db";
import {Product} from "../models";

export interface User{
  first_name: string,
  last_name: string,
  username: string,
}
@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements CanActivate, OnInit {
  Authorized: boolean;
  products: Product[];
  user: User;
  constructor(private router: Router, private authService: AuthService){
    this.Authorized = false;
    this.products = [];
    this.user = {username:"", first_name:"", last_name:""};
  }

  ngOnInit(): void {
        this.getUser()
    }



  canActivate() {
    alert(1)
    if (this.Authorized) {
        return true;
    }

    this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>{
      this.router.navigate(["login"])
  });
    return false;
}
  logout(){
    this.authService.logout()
    this.router.navigate(['../login'])
  }

  getUser(){
    this.authService.getUser().subscribe((user) => {
      this.user = {
        first_name: user['first_name'],
        last_name: user['last_name'],
        username: user['username']
      };
      console.log(this.user) // here it is printing correct data
    }, error => {
      console.log(error);
    });
  }
}
