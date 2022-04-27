import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

const baseUrl = "http://127.0.0.1:5000/";

@Injectable({
  providedIn: 'root'
})
export class OlapServicesService {

  constructor(private httpClient:HttpClient) { }

  getQ1(): Observable<any> {
    return this.httpClient.get(baseUrl + 'api/q1');
  }
}
