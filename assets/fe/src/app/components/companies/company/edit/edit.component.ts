import { Component, OnInit } from '@angular/core';
import { StateService, UIRouterGlobals } from '@uirouter/core';

import { CompanyForm } from 'src/app/commons/forms/company.form';
import { Company, CompanyType } from 'src/app/commons/models/companies.model';
import { CompanyService } from 'src/app/commons/services/companies/company.service';
import { CompaniesService } from 'src/app/commons/services/companies/companies.service';

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.scss']
})
export class EditComponent implements OnInit {

  constructor(
    private $router: UIRouterGlobals,
    private $state: StateService,
    private $company: CompanyService,
    private $companies: CompaniesService,
  ) { }

  Form = new CompanyForm();
  companyTypes = [] as CompanyType[];

  get companyId(): number {
    return this.$router.params['id'];
  }

  ngOnInit(): void {
    // fetch the company types list
    this.$companies.companyTypes()
      .then((resp) => this.companyTypes = resp)
    ;

    // fetch the company information
    this.$company.get(this.companyId)
      .then((resp) => {
        this.Form.patchValue(resp);
      })
    ;
  }

  onSubmit({value, valid}: {value: Company, valid: boolean}) {
    if (!valid) return this.Form.form.markAllAsTouched();

    this.$company.update(this.companyId, value)
      .then((resp) => {
        alert('Successfully changed!');

        this.$state.go('companies');
      })
      .catch((err: any) => {
        this.Form.setFormErrors(err.error);
        this.Form.form.markAllAsTouched();
      })
    ;
  }

}
