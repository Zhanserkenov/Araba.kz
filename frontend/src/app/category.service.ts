import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Category, Product} from "./models";

@Injectable({
  providedIn: 'root'
})
export class CategoryService {
  BASE_URL = "http://127.0.0.1:8000"
  constructor(private client: HttpClient) { }

  getCategories(): Observable<Category[]>{
    return this.client.get<Category[]>(`${this.BASE_URL}/categories`)
  }
  getCategoryProducts(categoryID: number): Observable<Product[]>{
    return this.client.get<Product[]>(`${this.BASE_URL}/categories/${categoryID}/products`)
  }
}
