import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { API_COMPANIES } from 'src/app/commons/constants/api.constant';
import { Company } from 'src/app/commons/models/companies.model';
import { urlsafe } from 'src/app/commons/utils/http.util';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  constructor(
    private $http: HttpClient,
  ) { }

  async get(id: number) {
    const resp = await this.$http.get(urlsafe(API_COMPANIES, id))
      .toPromise()
    ;
    return resp as Company;
  }

  async update(id: number, data: Company) {
    const resp = await this.$http.put(urlsafe(API_COMPANIES, id), data)
      .toPromise()
    ;
    return resp as Company;
  }

  async delete(id: number) {
    const resp = await this.$http.delete(urlsafe(API_COMPANIES, id))
      .toPromise()
    ;
    return resp as Company;
  }
}
