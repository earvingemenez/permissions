export interface Login {
  email: string;
  password: string;
}

export interface Permission {
  user: number;
  model: string;
  can_add: boolean;
  can_delete: boolean;
  fields: FieldPermission[];
}

export interface FieldPermission {
  name: string;
  can_view: boolean;
  can_change: boolean;
}