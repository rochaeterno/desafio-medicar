import { TestBed } from '@angular/core/testing';

import { ListConsultasService } from './list-consultas.service';

describe('ListConsultasService', () => {
  let service: ListConsultasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ListConsultasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
