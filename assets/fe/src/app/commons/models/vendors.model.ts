import { Company } from "./companies.model";

export interface VendorType {
  id: number;
  name: string;
  date_created: string;
  date_updated: string;
} 

export interface Vendor {
  id: number;
  company: Company;
  vendor_type: VendorType;
  name: string;
}