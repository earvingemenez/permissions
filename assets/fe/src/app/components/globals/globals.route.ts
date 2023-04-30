import { Ng2StateDeclaration } from '@uirouter/angular';
import { SidecontentComponent } from './layouts/sidecontent/sidecontent.component';

export const GLOBALS_ROUTES: Ng2StateDeclaration[] = [
  {
    name: 'side-content',
    component: SidecontentComponent,
    url: '?{requestType:string}'
  },
]