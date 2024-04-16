import {Component, OnInit} from '@angular/core';
import {Product} from "../models";
import {ActivatedRoute} from "@angular/router";
import {MyDB} from "../db";
import {ProductService} from "../product.service";

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit{
  product: Product;
  product_id: number;
  constructor(private route: ActivatedRoute, private productService: ProductService) {
    this.product_id = 0;
    this.product =
      {id: 0,
      name:'null',
      description:'null',
      category: 0,
        price:0,
      img: 'null',
      liked: false
    };
    };

  ngOnInit(): void {
    this.route.paramMap.subscribe((params)=> {
      let _product_id = params.get('product_id');
      if (_product_id) {
        this.product_id = +_product_id;
      }
    })
    this.getProductByID()
  }
  getProductByID(){
    this.productService.getProductsByID(this.product_id).subscribe((product) => {
      this.product = product;
    });
  }
}
