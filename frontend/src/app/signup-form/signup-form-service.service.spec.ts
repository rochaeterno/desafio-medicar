import { TestBed } from '@angular/core/testing';

import { SignupFormServiceService } from './signup-form-service.service';

describe('SignupFormServiceService', () => {
  let service: SignupFormServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SignupFormServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
