import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-signup-form',
  templateUrl: './signup-form.component.html',
  styleUrls: ['./signup-form.component.scss']
})
export class SignupFormComponent implements OnInit {
  signup: any;

  constructor() { }

  ngOnInit(): void {
    this.signup = {}
  }

  onSubmit(data: any) {
    console.log(data)
  }

}
