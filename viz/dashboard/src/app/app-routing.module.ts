import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {DashboardHomeComponent} from "./dashboard-home/dashboard-home.component";
import {DashboardAccountComponent} from "./dashboard-account/dashboard-account.component";

const routes: Routes = [
  {path: 'home', component: DashboardHomeComponent},
  {path: 'account', component: DashboardAccountComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {

}
