import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ArticleService {

  constructor(private http: HttpClient) { }

  getArticles(): Observable<any[]> {
    return this.http.get<any[]>('http://127.0.0.1:8000/api/article/');
  }

  getArticleById(id: number): Observable<any> {
    return this.http.get<any>('http://127.0.0.1:8000/api/article/' + id);
  }
}