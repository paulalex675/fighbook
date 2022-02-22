import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service' 

@Component({
  selector: 'app-show-style',
  templateUrl: './show-style.component.html',
  styleUrls: ['./show-style.component.css']
})
export class ShowStyleComponent implements OnInit {

  constructor(private service:SharedService) { }

  StyleList:any=[];

  ngOnInit(): void {
    this.refreshStyleList();
  }


  refreshStyleList(){
    this.service.getStyleList().subscribe(data=>{
      this.StyleList=data;
    });

  }
}
