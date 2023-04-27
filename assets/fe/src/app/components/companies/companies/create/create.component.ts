import { Component, OnInit } from '@angular/core';
import { StateService } from '@uirouter/core';

import { CompanyForm } from 'src/app/commons/forms/company.form';
import { Company } from 'src/app/commons/models/companies.model';
import { CompaniesService } from 'src/app/commons/services/companies/companies.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit {

  constructor(
    private $state: StateService,
    private $companies: CompaniesService,
  ) { }

  Form = new CompanyForm();

  ngOnInit(): void {
  }

  onSubmit({value, valid}: {value: Company, valid: boolean}) {
    if (!valid) return this.Form.form.markAllAsTouched();

    this.$companies.create(value)
      .then((resp) => {
        alert("Company has successfully created!");
        this.$state.go('companies');
      })
      .catch((err: any) => this.Form.setFormErrors(err.error))
    ;
  }

}
