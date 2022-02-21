import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowStyleComponent } from './show-style.component';

describe('ShowStyleComponent', () => {
  let component: ShowStyleComponent;
  let fixture: ComponentFixture<ShowStyleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowStyleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ShowStyleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
