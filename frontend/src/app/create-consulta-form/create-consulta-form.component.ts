import { Component, OnInit } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';


interface Food {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-create-consulta-form',
  templateUrl: './create-consulta-form.component.html',
  styleUrls: ['./create-consulta-form.component.scss']
})
export class CreateConsultaFormComponent {

  constructor(private dialogRef: MatDialogRef<CreateConsultaFormComponent>) {

  }

  foods: Food[] = [
    { value: 'steak-0', viewValue: 'Steak' },
    { value: 'pizza-1', viewValue: 'Pizza' },
    { value: 'tacos-2', viewValue: 'Tacos' },
  ];

  closeDialog() {
    this.dialogRef.close();
  }

}
