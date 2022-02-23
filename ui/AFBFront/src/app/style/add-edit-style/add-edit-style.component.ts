import { Component, OnInit, Input } from '@angular/core';
import { SharedService } from 'src/app/shared.service' 

@Component({
  selector: 'app-add-edit-style',
  templateUrl: './add-edit-style.component.html',
  styleUrls: ['./add-edit-style.component.css']
})
export class AddEditStyleComponent implements OnInit {

  constructor(private service:SharedService) { }

  @Input() style:any;
  StyleId:string = '';
  StyleName:string = '';


  ngOnInit(): void {
    this.StyleId=this.style.StyleId;
    this.StyleName = this.style.StyleName;
  }

  addStyle(){
    var val ={StyleId:this.StyleId,
              StyleName:this.StyleName};
    this.service.addStyle(val).subscribe(res=>{
      alert(res.toString());
    });
  }

  updateStyle(){
    var val ={StyleId:this.StyleId,
              StyleName:this.StyleName};
    this.service.updateStyle(val).subscribe(res=>{
    alert(res.toString());
    });
  }

}
