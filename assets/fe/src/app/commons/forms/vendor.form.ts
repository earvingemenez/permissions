import { UntypedFormGroup, UntypedFormControl, Validators } from '@angular/forms';
import { Form } from './base.form';

export class VendorForm extends Form {
  
  constructor() {
    const fields: any = {
      //company: new UntypedFormControl(null, [Validators.required]),
      //vendor_type: new UntypedFormControl(null, [Validators.required]),
      name: new UntypedFormControl(null, [Validators.required]),
      vendor_type: new UntypedFormGroup({
        id: new UntypedFormControl(null, [Validators.required]),
      }),
      company: new UntypedFormGroup({
        id: new UntypedFormControl(null, [Validators.required]),
        company_type: new UntypedFormControl(null, []),
      })
    }
    super(fields);
  }

}