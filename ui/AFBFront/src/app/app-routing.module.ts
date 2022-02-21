import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { UserComponent } from './user/user.component';
import { StyleComponent } from './style/style.component';

const routes: Routes = [
  { path:'user', component:UserComponent },
  { path:'style', component:StyleComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
