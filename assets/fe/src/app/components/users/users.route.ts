import { Ng2StateDeclaration } from '@uirouter/angular';
import { DashboardComponent } from './dashboard/dashboard.component';

export const USERS_ROUTES: Ng2StateDeclaration[] = [
  {
    name: 'users-dashboard',
    url: '/dashboard',
    component: DashboardComponent
  },
]