import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import { Product } from '../models';
import { MyDB } from '../db';
import {ProductService} from "../product.service";

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  title: string;
  products: Product[];
  constructor(private route: ActivatedRoute, private productService: ProductService){
    this.title = "";
    this.products = [];

    }

  ngOnInit(): void {
    this.route.paramMap.subscribe((params)=> {
      let _title = params.get('title');
      if (_title) {
        this.title = _title;
      }
    })
    this.getProductsByTitle()
    // this.products = MyDB.Products.filter(product=>product.Name.toLowerCase().includes(this.title.toLowerCase()));
  }
  likeClicked(product: Product){
      product.liked = !product.liked;
      this.productService.likeAction(product)
  }
  updateProduct(product: Product){
    this.productService.likeAction(product)
  }
  categoryIDtoString(id: number){
    return id.toString()
  }

  getProductsByTitle(){
    this.productService.getProductsByTitle(this.title).subscribe((products) => {
      this.products = products;
    });
  }
}
