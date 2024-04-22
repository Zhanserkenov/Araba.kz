import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { AccountComponent } from './account/account.component';
import { FavoritesComponent } from './favorites/favorites.component';
import { PurchasesComponent } from './purchases/purchases.component';
import { CategoriesComponent } from './categories/categories.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';
import { FormsModule } from '@angular/forms';
import { SearchComponent } from './search/search.component';
import { AuthorizationComponent } from './authorization/authorization.component';
import { RegistrationComponent } from './registration/registration.component';
import {AuthoGuard} from "./autho.guard";
import { HttpClientModule} from "@angular/common/http";
import { CarsComponent } from './cars/cars.component';
import { ChargingComponent } from './charging/charging.component';
import { ArticleComponent } from './article/article.component';
import { ArticleDetailComponent } from './article-detail/article-detail.component';
import { AccessoriesComponent } from './accessories/accessories.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    FooterComponent,
    AccountComponent,
    FavoritesComponent,
    PurchasesComponent,
    CategoriesComponent,
    ProductDetailComponent,
    SearchComponent,
    AuthorizationComponent,
    RegistrationComponent,
    CarsComponent,
    ChargingComponent,
    ArticleComponent,
    ArticleDetailComponent,
    AccessoriesComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,

  ],
  providers: [
    AuthoGuard,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }