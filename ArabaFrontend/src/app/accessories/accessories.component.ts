import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-accessories',
  templateUrl: './accessories.component.html',
  styleUrls: ['./accessories.component.css']
})
export class AccessoriesComponent {
  accessoriesData: any[] = []; // Variable to hold car data

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.fetchAccessoriesData(); // Call the fetchCarData function when the component initializes
  }

  fetchAccessoriesData() {
    // Function to fetch car data from the API
    this.http.get<any[]>('http://127.0.0.1:8000/api/accessories/').subscribe(
        (data) => {
          this.accessoriesData = data; // Assign the fetched data to the carData variable
        },
        (error) => {
          console.error('Error fetching accessories data:', error); // Log error if fetching data fails
        }
    );
  }
}
