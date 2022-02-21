import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditStyleComponent } from './add-edit-style.component';

describe('AddEditStyleComponent', () => {
  let component: AddEditStyleComponent;
  let fixture: ComponentFixture<AddEditStyleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditStyleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddEditStyleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
