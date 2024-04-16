import { Component } from '@angular/core';
import {Product} from "../models";
import {Router} from "@angular/router";
import {MyDB} from "../db";

@Component({
  selector: 'app-purchases',
  templateUrl: './purchases.component.html',
  styleUrls: ['./purchases.component.css']
})
export class PurchasesComponent {
  products: Product[];
  constructor(private router: Router){
    this.products = [];
  }
}
