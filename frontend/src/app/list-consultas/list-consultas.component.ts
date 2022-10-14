import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { CreateConsultaFormComponent } from '../create-consulta-form/create-consulta-form.component';
import { MatDialog } from '@angular/material/dialog';
import { ListConsultasService } from './list-consultas.service';

@Component({
  selector: 'app-list-consultas',
  templateUrl: './list-consultas.component.html',
  styleUrls: ['./list-consultas.component.scss']
})
export class ListConsultasComponent implements OnInit {
  constructor(
    private dialog: MatDialog,
    private router: Router,
    private listService: ListConsultasService,
  ) { }

  get consultas() {
    return this.listService.consultas;
  }

  ngOnInit(): void {
    this.listAllConsultas()
  }

  displayedColumns: string[] = [
    'Especialidade',
    'Profissional',
    'Data',
    'Hora',
    'actions'
  ];

  openCreateConsultaDialog() {
    this.dialog.open(CreateConsultaFormComponent);
  }

  listAllConsultas() {
    this.listService.getConsultas().subscribe((consultas) => {
      this.listService.consultas = consultas;
    });
  }

  deletarConsulta(consulta_id: number) {
    this.listService.deleteConsulta(consulta_id).subscribe(() => {
      this.listAllConsultas()
    });
  }

  logout() {
    this.router.navigate(['']);
  }
}
