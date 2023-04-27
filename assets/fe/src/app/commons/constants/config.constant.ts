/* 18 random characters that will represent as the
 * key name of the user token in the client side.
 */
export const AUTH_KEY = 'CqFHc2SG4ESynG8UDN';

/* HOST
 */
export const HOST = `${(window as any).location?.host}`;
export const PROTOCOL = (window as Window).location.protocol === 'https:' ? 'wss://': 'ws://';


/* API URL
 */
export const API_URL = '/api/';
