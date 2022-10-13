import { TestBed } from '@angular/core/testing';

import { CreateConsultaFormServiceService } from './create-consulta-form-service.service';

describe('CreateConsultaFormServiceService', () => {
  let service: CreateConsultaFormServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CreateConsultaFormServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
