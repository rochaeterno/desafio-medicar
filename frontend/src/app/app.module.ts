import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCheckboxModule } from '@angular/material/checkbox'
import { MatTableModule } from '@angular/material/table';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSelectModule } from '@angular/material/select';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginScreenComponent } from './login-screen/login-screen.component';
import { LoginFormComponent } from './login-form/login-form.component';;
import { SignupFormComponent } from './signup-form/signup-form.component';
import { HomeScreenComponent } from './home-screen/home-screen.component';
import { HomeScreenHeaderComponent } from './home-screen-header/home-screen-header.component';
import { ListConsultasComponent } from './list-consultas/list-consultas.component';
import { CreateConsultaFormComponent } from './create-consulta-form/create-consulta-form.component';
import { ListConsultasService } from './list-consultas/list-consultas.service';
import { CreateConsultaFormServiceService } from './create-consulta-form/create-consulta-form-service.service';
import { AuthService } from './auth-service/auth.service';
import { SignupScreenComponent } from './signup-screen/signup-screen.component';
import { SweetAlert2Module } from '@sweetalert2/ngx-sweetalert2';

@NgModule({
  declarations: [
    AppComponent,
    LoginScreenComponent,
    LoginFormComponent,
    SignupFormComponent,
    HomeScreenComponent,
    HomeScreenHeaderComponent,
    ListConsultasComponent,
    CreateConsultaFormComponent,
    SignupScreenComponent
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
    MatSelectModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    SweetAlert2Module.forRoot()
  ],
  providers: [
    ListConsultasService,
    CreateConsultaFormServiceService,
    AuthService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
