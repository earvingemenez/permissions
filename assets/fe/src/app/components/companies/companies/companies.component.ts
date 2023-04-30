import { Component, OnInit } from '@angular/core';

import { CompaniesService } from 'src/app/commons/services/companies/companies.service';
import { CompanyService } from 'src/app/commons/services/companies/company.service';
import { Company } from 'src/app/commons/models/companies.model';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.scss']
})
export class CompaniesComponent implements OnInit {

  constructor(
    private $companies: CompaniesService,
    private $company: CompanyService
  ) { }

  companies = [] as Company[];

  ngOnInit(): void {
    this.load();
  }

  delete(id: number) {
    this.$company.delete(id)
      .then((resp) => {
        alert("Company has been deleted.");
        this.load();
      })
    ;
  }

  load(): void {
    // load the company list
    this.$companies.list()
      .then((resp) => this.companies = resp)
    ;
  }

}
