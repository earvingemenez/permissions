import { Component, OnInit } from '@angular/core';
import { StateService, UIRouterGlobals } from '@uirouter/core';

import { VendorForm } from 'src/app/commons/forms/vendor.form';
import { Vendor, VendorType } from 'src/app/commons/models/vendors.model';
import { VendorService } from 'src/app/commons/services/vendors/vendor.service';
import { VendorsService } from 'src/app/commons/services/vendors/vendors.service';

import { CompaniesService } from 'src/app/commons/services/companies/companies.service';
import { Company, CompanyType } from 'src/app/commons/models/companies.model';

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.scss']
})
export class EditComponent implements OnInit {

  constructor(
    private $router: UIRouterGlobals,
    private $state: StateService,
    private $vendors: VendorsService,
    private $vendor: VendorService,
    private $companies: CompaniesService,
  ) { }

  Form = new VendorForm();
  companies = [] as Company[];
  vendorTypes = [] as VendorType[];

  companyTypes = [] as CompanyType[];

  get vendorId(): number {
    return this.$router.params['id'];
  }

  ngOnInit(): void {
    // fetch list of companies
    this.$companies.list()
      .then((resp) => this.companies = resp)
    ;

    // fetch the list of company types
    this.$companies.companyTypes()
      .then((resp) => this.companyTypes = resp)
    ;

    // fetch list of vendor types
    this.$vendors.vendorTypes()
      .then((resp) => this.vendorTypes = resp)
    ;

    // fetch the vendor details
    this.$vendor.get(this.vendorId)
      .then((resp) => {
        this.Form.patchValue(resp);
      })
    ;
  }

  onSubmit({value, valid}: {value: Vendor, valid: boolean}) {
    if(!valid) return this.Form.form.markAllAsTouched();

    Object.assign(value, {'company': {'id': value.company, 'company_type': 2}})

    this.$vendor.update(this.vendorId, value)
      .then((resp) => {
        alert('Successfully saved changes!');
        this.$state.go('vendors');
      })
      .catch((err: any) => {
        this.Form.setFormErrors(err.error);
        this.Form.form.markAllAsTouched();
      })
    ;
  }

}
