import { TestBed } from '@angular/core/testing';

import { OlapServicesService } from './olap-services.service';

describe('OlapServicesService', () => {
  let service: OlapServicesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OlapServicesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
