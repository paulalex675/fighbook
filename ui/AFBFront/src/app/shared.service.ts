import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIURL = 'http://127.0.0.1:8000/';
  readonly PhotoUrl = 'http://127.0.0.1:8000/media';

  constructor(private http:HttpClient) { }

  getStyleList():Observable<any[]>{
    return this.http.get<any[]>(this.APIURL + '/syle/');
  }

  addStyle(val:any){
    return this.http.post(this.APIURL + '/syle/', val);
  }

  updateStyle(val:any){
    return this.http.put(this.APIURL + '/syle/', val);
  }

  deleteStyle(val:any){
    return this.http.delete(this.APIURL + '/syle/' + val);
  }

  getUserList():Observable<any[]>{
    return this.http.get<any[]>(this.APIURL + '/user/');
  }

  addUser(val:any){
    return this.http.post(this.APIURL + '/user/', val);
  }

  updateUser(val:any){
    return this.http.put(this.APIURL + '/user/', val);
  }

  deleteUser(val:any){
    return this.http.delete(this.APIURL + '/user/' + val);
  }

  UploadPhoto(val:any){
    return this.http.post(this.APIURL + '/SaveFile', val);
  }

  getAllStyleNames():Observable<any[]>{
    return this.http.get<any[]>(this.APIURL + '/style/');
  }
}
