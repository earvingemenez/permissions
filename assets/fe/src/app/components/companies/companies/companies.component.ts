import { Component, OnInit } from '@angular/core';

import { CompaniesService } from 'src/app/commons/services/companies/companies.service';
import { CompanyService } from 'src/app/commons/services/companies/company.service';
import { Company, CompanyType } from 'src/app/commons/models/companies.model';

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
  companyTypes = [] as CompanyType[];

  ngOnInit(): void {
    this.$companies.companyTypes()
      .then((resp) => this.companyTypes = resp)
    ;

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

  companyType(id: number) {
    return this.companyTypes.find(i => i.id===id);
  }

}
