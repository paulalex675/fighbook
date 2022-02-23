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

  ModalTitle:string = '';
  ActivateAddEditStyleComp:boolean=false;
  style:any;

  ngOnInit(): void {
    this.refreshStyleList();
  }

  addClick(){
    this.style={
      StyleId:0,
      StyleName:""
    }
    this.ModalTitle="Add Style";
    this.ActivateAddEditStyleComp=true;

  }

  editClick(item){
    this.style=item;
    this.ModalTitle="Edit Style"
    this.ActivateAddEditStyleComp=true;
  }

  deleteClick(item){
    if(confirm("Are you sure you want to delete that??")){
      this.service.deleteStyle(item.StyleId).subscribe(data=>{
        alert(data.toString());
        this.refreshStyleList();
      })
    }
  }

  closeClick(){
    this.ActivateAddEditStyleComp=false;
    this.refreshStyleList();
  }

  refreshStyleList(){
    this.service.getStyleList().subscribe(data=>{
      this.StyleList=data;
    });

  }
}
