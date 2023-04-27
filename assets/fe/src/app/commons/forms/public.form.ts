import { UntypedFormControl, Validators } from '@angular/forms';
import { Form } from './base.form';

export class LoginForm extends Form {
  constructor() {
    const fields: any = {
      email: new UntypedFormControl(null, [Validators.required, Validators.email]),
      password: new UntypedFormControl(null, [Validators.required]),
      remember: new UntypedFormControl(null),
    }
    super(fields);
  }
}