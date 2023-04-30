import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { UIRouterModule } from '@uirouter/angular';

import { VendorsComponent } from './vendors/vendors.component';
import { VendorComponent } from './vendor/vendor.component';
import { EditComponent } from './vendor/edit/edit.component';


@NgModule({
  declarations: [
    VendorsComponent,
    VendorComponent,
    EditComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    UIRouterModule,
  ]
})
export class VendorsModule { }
