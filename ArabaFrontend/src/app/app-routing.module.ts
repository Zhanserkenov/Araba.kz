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
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {onSameUrlNavigation:'reload'})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
