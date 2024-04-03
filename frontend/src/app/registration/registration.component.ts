import { Component } from '@angular/core';
import {AuthService} from "../auth.service";

export interface NewUser{
  first_name: string,
  last_name: string,
  username: string,
  password: string
}
@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  user: NewUser;
  passError: boolean;
  constructor(private authService: AuthService) {
    this.user = {first_name: "", last_name:"", username: "", password: ""};
    this.passError = false;
  }

  register(){
    console.log(this.user)
    this.authService.register(this.user);
    }
}
