import { Ng2StateDeclaration } from '@uirouter/angular';
import { CompaniesComponent } from './companies/companies.component';

import { EditComponent } from './company/edit/edit.component';
import { CreateComponent } from './companies/create/create.component';

export const COMPANIES_ROUTES: Ng2StateDeclaration[] = [
  {
    name: 'companies',
    url: '/companies',
    component: CompaniesComponent
  },
  {
    name: 'company-create',
    url: '/companies/create',
    component: CreateComponent
  },
  {
    name: 'company-edit',
    url: '/companies/:id/edit',
    component: EditComponent
  },
]