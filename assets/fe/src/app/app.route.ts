import { routerConfig } from 'src/app/commons/utils/router.config';

import { GLOBALS_ROUTES } from 'src/app/components/globals/globals.route';
import { PUBLIC_ROUTES } from 'src/app/components/public/public.route';
import { USERS_ROUTES } from 'src/app/components/users/users.route';
import { VENDORS_ROUTES } from 'src/app/components/vendors/vendors.route';
import { COMPANIES_ROUTES } from 'src/app/components/companies/companies.route';

export const APP_ROUTES = {
  otherwise: 'not_found',
  states: ([] as any[]).concat(
    GLOBALS_ROUTES,
    PUBLIC_ROUTES,
    USERS_ROUTES,
    VENDORS_ROUTES,
    COMPANIES_ROUTES,
  ),
  config: routerConfig
}