export interface Category{
  id: number,
  name: string
}

export interface Product{
  id: number;
  name: string;
  description: string;
  category: number;
  price: number;
  img: string;
  liked: boolean;
}
