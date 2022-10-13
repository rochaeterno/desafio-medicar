import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginScreenComponent } from './login-screen/login-screen.component';
import { LoginFormComponent } from './login-form/login-form.component';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { SignupFormComponent } from './signup-form/signup-form.component';
import { HomeScreenComponent } from './home-screen/home-screen.component';
import { HomeScreenHeaderComponent } from './home-screen-header/home-screen-header.component';
import { ListConsultasComponent } from './list-consultas/list-consultas.component';
import { MatTableModule } from '@angular/material/table';
import { MatDialogModule } from '@angular/material/dialog';
import { CreateConsultaFormComponent } from './create-consulta-form/create-consulta-form.component';
import { MatSelectModule } from '@angular/material/select';

@NgModule({
  declarations: [
    AppComponent,
    LoginScreenComponent,
    LoginFormComponent,
    SignupFormComponent,
    HomeScreenComponent,
    HomeScreenHeaderComponent,
    ListConsultasComponent,
    CreateConsultaFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    MatCheckboxModule,
    MatTableModule,
    MatDialogModule,
    MatSelectModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
