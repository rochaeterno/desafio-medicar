import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateConsultaFormComponent } from './create-consulta-form.component';

describe('CreateConsultaFormComponent', () => {
  let component: CreateConsultaFormComponent;
  let fixture: ComponentFixture<CreateConsultaFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateConsultaFormComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateConsultaFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
