import { urlsafe } from 'src/app/commons/utils/http.util';
import { API_URL } from './config.constant';

export const API_USERS = urlsafe(API_URL, 'users');
export const API_VENDORS = urlsafe(API_URL, 'vendors');
export const API_COMPANIES = urlsafe(API_URL, 'companies');