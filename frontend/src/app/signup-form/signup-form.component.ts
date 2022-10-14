import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { SignupFormServiceService } from './signup-form-service.service'

@Component({
  selector: 'app-signup-form',
  templateUrl: './signup-form.component.html',
  styleUrls: ['./signup-form.component.scss']
})
export class SignupFormComponent implements OnInit {
  signup: any;

  constructor(
    private createUserService: SignupFormServiceService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.signup = {}
  }

  onSubmit() {
    if (this.signup.password != this.signup.password_confirm) {
      console.log('A senhas inseridas devem ser iguais.');
      return;
    } else {
      this.createUserService.criarUsuario(this.signup).subscribe((res) => {
        this.router.navigate(['/'])
      })
    }
  }
}
