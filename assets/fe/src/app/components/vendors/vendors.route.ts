import { Ng2StateDeclaration } from '@uirouter/angular';

import { VendorsComponent } from './vendors/vendors.component';
import { EditComponent } from './vendor/edit/edit.component';
import { VendorComponent } from './vendor/vendor.component';

export const VENDORS_ROUTES: Ng2StateDeclaration[] = [
  {
    name: 'vendors',
    url: '/vendors',
    parent: 'side-content',
    component: VendorsComponent,
  },
  {
    name: 'vendor-detail',
    url: '/vendors/:id',
    parent: 'side-content',
    component: VendorComponent
  },
  {
    name: 'vendor-edit',
    url: '/vendors/:id/edit',
    parent: 'side-content',
    component: EditComponent
  },
]