import { Component, OnInit } from '@angular/core';

import { VendorsService } from 'src/app/commons/services/vendors/vendors.service';
import { VendorService } from 'src/app/commons/services/vendors/vendor.service';
import { Vendor } from 'src/app/commons/models/vendors.model';

@Component({
  selector: 'app-vendors',
  templateUrl: './vendors.component.html',
  styleUrls: ['./vendors.component.scss']
})
export class VendorsComponent implements OnInit {

  constructor(
    private $vendors: VendorsService,
    private $vendor: VendorService,
  ) { }

  vendors = [] as Vendor[];

  ngOnInit(): void {
    this.load();
  }

  load(): void {
    this.$vendors.list()
      .then((resp) => this.vendors = resp)
    ;
  }

  delete(id: number) {
    this.$vendor.delete(id)
      .then((resp) => {
        alert("Vendor has successfully been deleted.");
        this.load();
      })
    ;
  }

}
