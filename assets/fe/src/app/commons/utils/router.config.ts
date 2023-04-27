import { UIRouter } from '@uirouter/core';

export function routerConfig(router: UIRouter) {
  router.transitionService.onSuccess({},(trans)=>{
    const params = trans.router.globals.params 
    if (!params['#']) {
      document.body.scrollTop = document.documentElement.scrollTop = 0;
    } else {
      document.getElementById(params['#'])?.scrollIntoView()
    }
  })

  router.urlService.config.type("safeString",{
    // Take an array of ints [1,2,3] and return a string "1-2-3"
    encode: (text: string) => encodeURI(text),
    
    // Take an string "1-2-3" and return an array of ints [1,2,3]
    decode: (str) =>  decodeURI(str), 

    // Match the encoded string in the URL
    pattern: new RegExp(".*"),

    // Ensure that the (decoded) object is an array, and that all its elements are numbers
    is: (obj) => typeof obj === 'string',

    // Compare two arrays of integers
    equals: (str, str2) => str.length === str2.length,
  })
}