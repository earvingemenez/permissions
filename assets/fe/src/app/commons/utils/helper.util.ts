import { NgbDate } from "@ng-bootstrap/ng-bootstrap";

// takes a {} object and returns a FormData object
export const objectToFormData = (data: any)=> {
  const toFormData = ((f) => f(f))(
    (h: any) => (f: any) => f((x: any) => h(h)(f)(x))
  )((f: any) => (fd = new FormData()) => (pk: any) => (d: any) => {
    if (d instanceof Object) {                                      
      Object.keys(d).forEach((k) => {
        const v = d[k];
        if (pk) k = `${pk}[${k}]`;
        if (v instanceof Object && !(v instanceof Date) && !(v instanceof File)) {
          return f(fd)(k)(v);
        } else {
          fd.append(k, v || "");
        }
      });
    }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    return fd;
  })()();

  return toFormData(data)
}

/* Check if object is empty.
 */
export const objIsEmpty = (obj: Object) => {
  return Object.keys(obj).length === 0;
}


/* Handle loading spinner easily and error
 */

export const usePromise = async <T>(promise: Promise<T>): Promise<[T, any]> => {
  try {
    const result = await promise;
    return [result, null]
  }
  catch (error) {
    return [null as any, error]
  }
}

export interface WaiterState {
  unexpected: boolean,
  notFound: boolean,
  loading: boolean,
  error: boolean,
  touched: boolean
  handle: (pm: Promise<any>) => Promise<[any, any]>
  clearState: ()=> void
  onSuccess?: (data: any)=> any
  onError?: (data: any)=> any
}

export const HttpHandler = () => {
  const defaultState  = {
    unexpected: false,
    notFound: false,
    loading: false,
    error: false,
    touched: false
  }
  const state: WaiterState = {
    ...defaultState,
    handle: async (pm)=>{
      !state.touched && (state.touched = true)

      state.clearState()
      
      state.loading = true;
      const [res,err] = await usePromise(pm);
      if (!err) state.onSuccess && state.onSuccess(res)

      if (err && err.status) { 
        if (err.status >= 500) { 
          state.unexpected = true
        } else if (err.status === 404) { 
          state.notFound = true
        } 
        state.error = true;
        state.onError && state.onError(err)
      }
      
      

      state.loading = false;
      return [res,err]
    },
    clearState: function (){
      const temp = this.touched 
      Object.assign(this,defaultState)
      this.touched = temp
    }
  };

  return state;
}