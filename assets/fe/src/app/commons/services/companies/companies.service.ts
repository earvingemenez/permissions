import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { API_COMPANIES } from 'src/app/commons/constants/api.constant';
import { Company } from 'src/app/commons/models/companies.model';

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {

  constructor(
    private $http: HttpClient,
  ) { }

  async list() {
    const resp = await this.$http.get(API_COMPANIES)
      .toPromise()
    ;
    return resp as Company[];
  }

  async create(data: Company) {
    const resp = await this.$http.post(API_COMPANIES, data)
      .toPromise()
    ;
    return resp as Company;
  }

}
