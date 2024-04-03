import {Component, OnInit} from '@angular/core';
import { MyDB } from '../db';
import { Product } from '../models';
import {ProductService} from "../product.service";

@Component({
  selector: 'app-favorites',
  templateUrl: './favorites.component.html',
  styleUrls: ['./favorites.component.css']
})
export class FavoritesComponent implements OnInit{
  products: Product[];

  constructor(private productService: ProductService){
    this.products = [];
  }


  likeClicked(product: Product){
    product.liked = !product.liked;
    this.productService.likeAction(product)
}
categoryIDtoString(id: number){
  return id.toString()
}

  ngOnInit(): void {
    this.getFavoriteProducts()

  }

  getFavoriteProducts(){
    this.productService.getFavoriteProductsOfUser().subscribe((products) => {
      this.products = products;
      console.log(this.products)
    });
  }
}
