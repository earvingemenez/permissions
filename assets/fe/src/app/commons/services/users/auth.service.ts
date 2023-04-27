import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { AUTH_KEY } from 'src/app/commons/constants/config.constant';
import { Login } from 'src/app/commons/models/users.model';

import { API_USERS } from 'src/app/commons/constants/api.constant';
import { urlsafe } from 'src/app/commons/utils/http.util';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private $http: HttpClient,
  ) { }

  set token(key: any) {
    (window as Window).localStorage[AUTH_KEY] = JSON.stringify(key);
  }

  get token() {
    const d = (window as Window).localStorage[AUTH_KEY];
    return !d ? {'token': null}: JSON.parse(d);
  }

  get authenticated(): boolean {
    return Boolean(this.token.token);
  }

  async login(data: Login) {
    const resp = await this.$http.post(urlsafe(API_USERS, 'login'), data)
      .toPromise();

    this.token = resp;
    return resp;
  }

}
