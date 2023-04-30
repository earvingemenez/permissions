import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { UIRouterModule } from '@uirouter/angular';

import { GlobalsModule } from 'src/app/components/globals/globals.module';
import { PublicModule } from 'src/app/components/public/public.module';
import { UsersModule } from 'src/app/components/users/users.module';
import { VendorsModule } from 'src/app/components/vendors/vendors.module';
import { CompaniesModule } from 'src/app/components/companies/companies.module';


import { TokenService } from 'src/app/commons/services/interceptors/token.service';

import { AppComponent } from './app.component';
import { APP_ROUTES } from './app.route';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    UIRouterModule.forRoot(APP_ROUTES),
    GlobalsModule,
    PublicModule,
    UsersModule,
    VendorsModule,
    CompaniesModule,
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: TokenService, multi: true},
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
