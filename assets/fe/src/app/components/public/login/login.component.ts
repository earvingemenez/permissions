import { Component, OnInit } from '@angular/core';
import { StateService } from '@uirouter/angular';

import { Login } from 'src/app/commons/models/users.model';
import { LoginForm } from 'src/app/commons/forms/public.form';

import { AuthService } from 'src/app/commons/services/users/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(
    private $auth: AuthService,
    private $state: StateService,
  ) { }

  Form = new LoginForm();

  ngOnInit(): void {
  }

  onSubmit({value, valid}: {value: Login, valid: boolean}) {
    if (!valid) return this.Form.form.markAllAsTouched();

    this.$auth.login(value)
      .then(async (resp): Promise<any> => {
        this.$state.go('users-dashboard');
      })
      .catch((err: any) => this.Form.setFormErrors(err.error))
    ;
  }

}
