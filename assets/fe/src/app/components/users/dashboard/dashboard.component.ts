import { Component, OnInit } from '@angular/core';

import { UserService } from 'src/app/commons/services/users/user.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  constructor(
    private $user: UserService,
  ) { }

  ngOnInit(): void {
    // fetch the auth user's permission
    this.$user.permissions()
      .then((resp) => { console.log(resp) })
    ;
  }

}
