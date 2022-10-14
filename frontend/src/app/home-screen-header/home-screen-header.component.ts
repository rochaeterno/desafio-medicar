import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home-screen-header',
  templateUrl: './home-screen-header.component.html',
  styleUrls: ['./home-screen-header.component.scss']
})
export class HomeScreenHeaderComponent implements OnInit {

  constructor(private router: Router,) { }

  ngOnInit(): void {
  }

  logout() {
    this.router.navigate(['']);
  }

}
