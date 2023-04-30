import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { API_VENDORS } from 'src/app/commons/constants/api.constant';
import { Vendor } from 'src/app/commons/models/vendors.model';
import { urlsafe } from 'src/app/commons/utils/http.util';

@Injectable({
  providedIn: 'root'
})
export class VendorService {

  constructor(
    private $http: HttpClient,
  ) { }

  async get(id: number) {
    const resp = await this.$http.get(urlsafe(API_VENDORS, id))
      .toPromise()
    ;
    return resp as Vendor;
  }

  async update(id: number, data: Vendor) {
    const resp = await this.$http.put(urlsafe(API_VENDORS, id), data)
      .toPromise()
    ;
    return resp as Vendor;
  }

  async delete(id: number) {
    const resp = await this.$http.delete(urlsafe(API_VENDORS, id))
      .toPromise()
    ;
    return resp as Vendor;
  }
}
