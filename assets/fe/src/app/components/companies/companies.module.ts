import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { UIRouterModule } from '@uirouter/angular';

import { CompaniesComponent } from './companies/companies.component';
import { CompanyComponent } from './company/company.component';
import { EditComponent } from './company/edit/edit.component';
import { CreateComponent } from './companies/create/create.component';

@NgModule({
  declarations: [
    CompaniesComponent,
    CompanyComponent,
    EditComponent,
    CreateComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    UIRouterModule,
  ]
})
export class CompaniesModule { }
