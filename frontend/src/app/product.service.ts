import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Product} from "./models";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  BASE_URL = "http://127.0.0.1:8000"
  private httpOptions = {
    headers: new HttpHeaders({
      'Authorization': 'JWT ' + localStorage.getItem('token')
    })
  };
  constructor(private client: HttpClient) { }

  likeAction(product: Product){
    this.client.post(`${this.BASE_URL}/likes/`, {product: product.id}, this.httpOptions).subscribe(resp=>{
    }, error => {
    })
  }

  getFavoriteProductsOfUser(): Observable<Product[]>{
    return this.client.get<Product[]>(`${this.BASE_URL}/likes/`, this.httpOptions)
  }
  getProductsByTitle(title:string): Observable<Product[]>{
    return this.client.get<Product[]>(`${this.BASE_URL}/products?title=${title}`)
  }
  getProductsByID(id:number): Observable<Product>{
    return this.client.get<Product>(`${this.BASE_URL}/products/${id}`)
  }

}
