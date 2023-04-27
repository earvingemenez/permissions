import { Component, OnInit } from '@angular/core';
import { StateService, UIRouterGlobals } from '@uirouter/core';

import { CompanyForm } from 'src/app/commons/forms/company.form';
import { Company } from 'src/app/commons/models/companies.model';
import { CompanyService } from 'src/app/commons/services/companies/company.service';

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
  ) { }

  Form = new CompanyForm();

  get companyId(): number {
    return this.$router.params['id'];
  }

  ngOnInit(): void {
    // fetch the company information
    this.$company.get(this.companyId)
      .then((resp) => {
        this.Form.form.patchValue(resp);
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
      .catch((err: any) => this.Form.setFormErrors(err.error))
    ;
  }

}
