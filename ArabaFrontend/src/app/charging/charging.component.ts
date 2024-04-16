import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-charging',
  templateUrl: './charging.component.html',
  styleUrls: ['./charging.component.css']
})
export class ChargingComponent implements OnInit {
  chargingData: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.fetchChargingData();
  }

  fetchChargingData() {
    this.http.get<any[]>('http://127.0.0.1:8000/api/charging').subscribe(
        (data) => {
          this.chargingData = data;
        },
        (error) => {
          console.error('Error fetching charging data:', error);
        }
    );
  }
}