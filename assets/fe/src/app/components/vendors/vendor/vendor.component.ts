import { Component, OnInit } from '@angular/core';
import { UIRouterGlobals } from '@uirouter/core';

import { VendorService } from 'src/app/commons/services/vendors/vendor.service';
import { Vendor } from 'src/app/commons/models/vendors.model';

@Component({
  selector: 'app-vendor',
  templateUrl: './vendor.component.html',
  styleUrls: ['./vendor.component.scss']
})
export class VendorComponent implements OnInit {

  constructor(
    private $vendor: VendorService,
    private $router: UIRouterGlobals,
  ) { }

  vendor = {} as Vendor;

  ngOnInit(): void {
    // fetch the vendor details
    this.$vendor.get(this.$router.params['id'])
      .then((resp) => this.vendor = resp)
    ;
  }

}
