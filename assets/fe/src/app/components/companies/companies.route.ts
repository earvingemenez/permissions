import { Ng2StateDeclaration } from '@uirouter/angular';
import { CompaniesComponent } from './companies/companies.component';

import { EditComponent } from './company/edit/edit.component';
import { CreateComponent } from './companies/create/create.component';
import { CompanyComponent } from './company/company.component';

export const COMPANIES_ROUTES: Ng2StateDeclaration[] = [
  {
    name: 'companies',
    url: '/companies',
    parent: 'side-content',
    component: CompaniesComponent
  },
  {
    name: 'company-create',
    url: '/companies/create',
    parent: 'side-content',
    component: CreateComponent
  },
  {
    name: 'company-detail',
    url: '/companies/:id',
    parent: 'side-content',
    component: CompanyComponent
  },
  {
    name: 'company-edit',
    url: '/companies/:id/edit',
    parent: 'side-content',
    component: EditComponent
  },
]