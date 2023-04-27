import { UntypedFormControl, Validators } from '@angular/forms';
import { Form } from './base.form';

export class CompanyForm extends Form {
  
  constructor() {
    const fields: any = {
      name: new UntypedFormControl(null, [Validators.required]),
      country: new UntypedFormControl(null, [Validators.required]),
      type: new UntypedFormControl(null, []),
      status: new UntypedFormControl(null, [Validators.required]),
    }
    super(fields);
  }

}