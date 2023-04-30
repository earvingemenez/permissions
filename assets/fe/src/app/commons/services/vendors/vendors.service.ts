import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { API_VENDORS } from 'src/app/commons/constants/api.constant';
import { Vendor, VendorType } from 'src/app/commons/models/vendors.model';
import { urlsafe } from '../../utils/http.util';

@Injectable({
  providedIn: 'root'
})
export class VendorsService {

  constructor(
    private $http: HttpClient,
  ) { }

  async list() {
    const resp = await this.$http.get(API_VENDORS)
      .toPromise()
    ;
    return resp as Vendor[];
  }

  async vendorTypes() {
    const resp = await this.$http.get(urlsafe(API_VENDORS, 'types'))
      .toPromise()
    ;
    return resp as VendorType[];
  }
}
