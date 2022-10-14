import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { AuthService } from '../auth-service/auth.service';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.scss']
})
export class LoginFormComponent implements OnInit {
  login_data: any;

  constructor(private router: Router, private authService: AuthService) { }

  ngOnInit(): void {
    this.login_data = {}
  }

  onSubmit() {
    this.authService.login(this.login_data).subscribe((token) => {
      this.authService.token = token;
      this.router.navigate(['home']);
    })
  }

}
