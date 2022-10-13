import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HomeScreenHeaderComponent } from './home-screen-header.component';

describe('HomeScreenHeaderComponent', () => {
  let component: HomeScreenHeaderComponent;
  let fixture: ComponentFixture<HomeScreenHeaderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HomeScreenHeaderComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HomeScreenHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
