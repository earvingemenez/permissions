import { Ng2StateDeclaration } from '@uirouter/angular';
import { Logout } from 'src/app/commons/utils/security.util';

import { LoginComponent } from './login/login.component';

export const PUBLIC_ROUTES: Ng2StateDeclaration[] = [
  {
    name: 'login',
    url: '/login',
    component: LoginComponent
  },
  {
    name: 'logout',
    url: '/logout',
    onEnter: Logout
  },
]