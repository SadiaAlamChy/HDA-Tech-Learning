import { Component, OnInit } from '@angular/core';
// import {ChartDataset, ChartOptions } from 'chart.js';
import {Color, Label, SingleDataSet} from 'ng2-charts';
import {Chart, ChartOptions, ChartType} from "chart.js";
import {OlapServicesService} from "../services/olap-services.service";

@Component({
  selector: 'app-dashboard-home',
  templateUrl: './dashboard-home.component.html',
  styleUrls: ['./dashboard-home.component.css']
})
export class DashboardHomeComponent implements OnInit {

  q1Data = [];
  public pieChartOptions: ChartOptions = {
    responsive: true,
  };
  public pieChartLabels: Label[] = [];
  public pieChartData: SingleDataSet = [];
  public pieChartType: ChartType = 'pie';
  public pieChartLegend = true;
  public pieChartPlugins = [];
  public pieChartColors: Color[] = [
    {'backgroundColor': ['red', 'blue', 'yellow', '#6cebd4', '#ebb26c', '#6cbceb', '#a56ceb']}
  ];

  constructor(private olapServices: OlapServicesService) { }

  ngOnInit(): void {
    console.log("Hello");
    this.reloadData();
  }
  reloadData(){
    this.olapServices.getQ1().subscribe(
      data => {
          console.log(data);
          this.q1Data = data;
          this.setPieChartData();
      });
  }
  setPieChartData() {
    for (const d of this.q1Data){
      this.pieChartLabels.push(d['division']);
      this.pieChartData.push(d['sales']);
      // @ts-ignore
      // this.pieChartColors.push({'backgroundColor': this.random_rgba()});
    }
  }
  random_rgba() {
    const o = Math.round, r = Math.random, s = 255;
    return 'rgba(' + o(r() * s) + ',' + o(r() * s) + ',' + o(r() * s) + ',' + r().toFixed(1) + ')';
  }
}
