import {Component, Input, OnInit} from '@angular/core';
import {Product} from "../models";
import {ActivatedRoute, Router, NavigationEnd} from "@angular/router";
import {MyDB} from "../db";
import {CategoryService} from "../category.service";
import {ProductService} from "../product.service";

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})
export class CategoriesComponent implements OnInit{
  @Input() categoryID: number;
  products: Product[];


  constructor(private route: ActivatedRoute, private categoryService: CategoryService, private productService: ProductService, private router: Router) {
    this.categoryID = 0;
    this.products = [];
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.getCategoryProducts()
      }
    });
  }

  ngOnInit() {
    this.route.paramMap.subscribe((params)=> {
      let _id = params.get('id');
      if (_id) {
        this.categoryID = +_id;
      }
    });
  this.getCategoryProducts()
  }
  getCategoryProducts(){
    this.categoryService.getCategoryProducts(this.categoryID).subscribe((products) => {
      this.products = products;
    });
  }

  updateProduct(product: Product){
    product.liked = !product.liked;
    this.productService.likeAction(product)
  }

  likeClicked(product: Product){

      this.updateProduct(product)

  }
  categoryIDtoString(){
    return this.categoryID.toString()
  }

}
