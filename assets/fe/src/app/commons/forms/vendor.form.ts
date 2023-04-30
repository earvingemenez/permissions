import { UntypedFormControl, Validators } from '@angular/forms';
import { Form } from './base.form';

export class VendorForm extends Form {
  
  constructor() {
    const fields: any = {
      company: new UntypedFormControl(null, [Validators.required]),
      vendor_type: new UntypedFormControl(null, [Validators.required]),
      name: new UntypedFormControl(null, [Validators.required]),
    }
    super(fields);
  }

}