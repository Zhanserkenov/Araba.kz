import { Component } from '@angular/core';
import {ProductDetailComponent} from "../product-detail/product-detail.component";
import {Product} from "../models";
import {ActivatedRoute} from "@angular/router";
import {MyDB} from "../db";


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  products: Product[];

  constructor() {
    this.products = [];
  }

}
