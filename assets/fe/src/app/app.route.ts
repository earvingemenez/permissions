import { routerConfig } from 'src/app/commons/utils/router.config';

import { PUBLIC_ROUTES } from 'src/app/components/public/public.route';
import { USERS_ROUTES } from 'src/app/components/users/users.route';
import { COMPANIES_ROUTES } from 'src/app/components/companies/companies.route';

export const APP_ROUTES = {
  otherwise: 'not_found',
  states: ([] as any[]).concat(
    PUBLIC_ROUTES,
    USERS_ROUTES,
    COMPANIES_ROUTES,
  ),
  config: routerConfig
}