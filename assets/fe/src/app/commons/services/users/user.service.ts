import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Permission } from 'src/app/commons/models/users.model';
import { API_USERS } from 'src/app/commons/constants/api.constant';
import { urlsafe } from 'src/app/commons/utils/http.util';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private $http: HttpClient,
  ) { }

  async permissions() {
    const resp = await this.$http.get(urlsafe(API_USERS, 'permissions'))
      .toPromise()
    ;
    return resp as Permission[];
  }

}
