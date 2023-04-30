import { Component, OnInit } from '@angular/core';
import { UIRouterGlobals } from '@uirouter/core';

import { CompanyService } from 'src/app/commons/services/companies/company.service';
import { Company } from 'src/app/commons/models/companies.model';

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.scss']
})
export class CompanyComponent implements OnInit {

  constructor(
    private $company: CompanyService,
    private $router: UIRouterGlobals,
  ) { }

  company = {} as Company;

  ngOnInit(): void {
    // fetch the company details
    this.$company.get(this.$router.params['id'])
      .then((resp) => this.company = resp)
    ;
  }

}
