import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AccountComponent} from "./account/account.component";
import {FavoritesComponent} from "./favorites/favorites.component";
import {PurchasesComponent} from "./purchases/purchases.component";
import {CategoriesComponent} from "./categories/categories.component";
import {ProductDetailComponent} from "./product-detail/product-detail.component";
import { SearchComponent } from './search/search.component';
import { AuthorizationComponent } from './authorization/authorization.component';
import { RegistrationComponent } from './registration/registration.component';
import {AuthoGuard} from "./autho.guard";
import {CarsComponent} from "./cars/cars.component";
import {ChargingComponent} from "./charging/charging.component";
import {ArticleComponent} from "./article/article.component";
import {ArticleDetailComponent} from "./article-detail/article-detail.component";

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'account', component: AccountComponent, canActivate: [AuthoGuard]},
  {path: 'favorites', component: FavoritesComponent},
  {path: 'purchases', component: PurchasesComponent},
  {path: 'categories/:id/products', component: CategoriesComponent},
  {path: 'categories/:category_id/products/:product_id', component: ProductDetailComponent},
  {path: 'search/:title', component: SearchComponent},
  {path: 'login', component: AuthorizationComponent},
  {path: 'registration', component: RegistrationComponent},
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: "cars", component: CarsComponent},
  {path: "charging", component: ChargingComponent},
  {path: "article", component: ArticleComponent},
  {path: "article/:id", component: ArticleDetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {onSameUrlNavigation:'reload'})],
  exports: [RouterModule]
})
export class AppRoutingModule { }