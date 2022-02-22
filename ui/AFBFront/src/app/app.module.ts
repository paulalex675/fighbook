import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { StyleComponent } from './style/style.component';
import { ShowStyleComponent } from './style/show-style/show-style.component';
import { AddEditStyleComponent } from './style/add-edit-style/add-edit-style.component';
import { UserComponent } from './user/user.component';
import { ShowUserComponent } from './user/show-user/show-user.component';
import { AddEditUserComponent } from './user/add-edit-user/add-edit-user.component';
import { SharedService } from './shared.service';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SignupComponent } from './authentication/signup/signup.component';


@NgModule({
  declarations: [
    AppComponent,
    StyleComponent,
    ShowStyleComponent,
    AddEditStyleComponent,
    UserComponent,
    ShowUserComponent,
    AddEditUserComponent,
    SignupComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
