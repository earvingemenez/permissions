export interface Company {
  id: number;
  name: string;
  country: string;
  company_type: number;
  status: string;
  date_created: string;
  date_updated: string;
}

export interface CompanyType {
  id: number;
  desc: string;
}