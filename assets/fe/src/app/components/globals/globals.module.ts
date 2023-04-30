import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UIRouterModule } from '@uirouter/angular';

import { SidecontentComponent } from './layouts/sidecontent/sidecontent.component';



@NgModule({
  declarations: [
    SidecontentComponent
  ],
  imports: [
    CommonModule,
    UIRouterModule,
  ]
})
export class GlobalsModule { }
