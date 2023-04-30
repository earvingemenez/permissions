import { Injectable } from '@angular/core';
import { UntypedFormGroup, UntypedFormBuilder, AbstractControl } from '@angular/forms';
import { NgbDate } from '@ng-bootstrap/ng-bootstrap';
import { objectToFormData } from 'src/app/commons/utils/helper.util';

interface DisplayErrorOptions {
  label?: string
  label2?: string // use for matching a password that has a 2nd label
  keyValue?: string
  isArray?: true
}

class FormError {
  #error: string;
  #status: string;

  constructor() {
    this.#error = "";
    this.#status = "";
  }

  get error() {
    return this.#error;
  }

  set error(err: string) {
    this.#error = err;
  }

  get httpstat() {
    return this.#status;
  }

  set httpstat(http: string) {
    this.#status = http;
  }

}

export class Form extends FormError {
  #form: UntypedFormGroup;
  nonFieldErrors!: string;
  subs = {} as any;

  constructor(
    fields: Object
  ) {
    super()
    this.#form = new UntypedFormBuilder().group(fields);
  }

  get form() {
    return this.#form;
  }

  get isValid(): boolean {
    return this.#form.valid;
  }

  get(f: string) {
    return this.#form.get(f);
  }

  valid(f: string) {
    return !(!this.#form.get(f)?.valid && this.#form.get(f)?.touched);
  }

  hasError(f: string, e: string) {
    return this.#form.get(f)?.touched && this.#form.get(f)?.hasError(e);
  }

  getErrorMsg(f: string, e="error") {
    return (this.#form.get(f) as any).errors['error'];
  }

  displayError(key?: AbstractControl | string | null, options?:DisplayErrorOptions){
    if (!key) return;
    
    let { label= 'This', keyValue="", label2="", isArray } = {...options}

    const formControl = typeof key === 'string' ? this.#form.get(key) : key;
    
    const keys = Object.keys(formControl?.errors || {})

    if (!formControl?.touched || keys.length === 0) return "";

    if (keys[0] === "email") {
      label = 'Email'
    }

   
    
    if (["minlength", "maxlength",'min','max'].includes(keys[0])) {
      const error = formControl?.errors?.[keys[0]]
      keyValue = keyValue || error.requiredLength  || error.min
    } else {
      keyValue = keyValue || formControl?.errors?.[keys[0]]?.keyValue 
    }

    label2 = label2 || keyValue 

    const serverErrors = formControl?.errors?.['error']
    //@ts-ignore
    const errMsg: {[key: string]: any} = {
      "minlength": isArray ? 'Minimum of %keyValue% items' : "Minimum of %keyValue% characters",
      "maxlength": isArray ? 'Maximum of %keyValue% items' : "Maximum of %keyValue% characters",
      "maxword": "Maximum of %keyValue% words",
      "minword": "Minium of %keyValue% words",
      "required": "%label% is required",
      "email": "%label% is not valid",
      "match": "%label% must be match to %keyValue%",
      "field_null": "The %keyValue% must not empty",
      "alpha_num": "%label% must contain numbers and letters only",
      "common": "%label% is too common",
      "error": (serverErrors && serverErrors[0]) || "%label% is invalid",
      "card": "%label% is not valid",

      // Add More error messages if it does not exist

    }[keys[0]] || 'errors.invalid' // Get the first error message... 

    //@ts-ignore
    return errMsg.replace("%label%", label).replace("%keyValue%",keyValue).replace('%label2%',label2)
  }
  /* SET BACKEND ERRORS
   * use this to set errors that came from the backend
   */
  setFormErrors(errors: any): void {
    for (let [key, value] of Object.entries(errors)) {
      const control = this.#form.get(key);
      if(control) control.setErrors({'error': value});
    }
    if('non_field_errors' in errors) {
      this.nonFieldErrors = (errors['non_field_errors'] as []).toString();
    }
  }

  /* AUTO VALIDATE
   * force the field to trigger validation
   */
  validate(key: string): void {
    const f = (this.#form.get(key) as any);
    f.markAsTouched(); f.markAsDirty(); f.updateValueAndValidity();
  }

  /* SUBSCRIBE TO FIELD CHANGES
   * specify which fields to subscribe it's value
   */
  onSubscribe(...fields: string[]): void {
    for(let f of fields) {

      this.#form.get(f)?.valueChanges.pipe().subscribe(val => {
        this.subs[f] = val; 
      })

    }
  }

  get formData(){
    return objectToFormData(this.form.value)
  }

  patchValue(instance: any) {
    
    for(let key of Object.keys(instance)) {
      if(typeof instance[key] === 'object') {
        instance[key] = instance[key].id;
      }
    }

    this.#form.patchValue(instance);
  }

}