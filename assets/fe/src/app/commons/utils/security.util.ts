import { Transition } from '@uirouter/core';
import { AuthService } from 'src/app/commons/services/users/auth.service';

const _services = (t: Transition) => {
  return {
    auth: t.injector().get(AuthService) as AuthService,
    state: t.router.stateService,
  };
}

export const LoginRequired = (t: Transition): any => {
  const { auth, state } = _services(t);
  
  if(!auth.authenticated) {
    return state.target('public-login', { next: window.location.href });
  }
}
  
export const Logout = (t: Transition): any => {
  const { auth, state } = _services(t);
  
  if(auth.authenticated) auth.token = {};

  location.reload();
  location.href = '/login';
}