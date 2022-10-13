import { Component, OnInit } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { ListConsultasService } from '../list-consultas/list-consultas.service';

import { CreateConsultaFormServiceService } from './create-consulta-form-service.service';

@Component({
  selector: 'app-create-consulta-form',
  templateUrl: './create-consulta-form.component.html',
  styleUrls: ['./create-consulta-form.component.scss']
})
export class CreateConsultaFormComponent implements OnInit {
  horarios: string[];
  new_consulta: any;

  constructor(
    private dialogRef: MatDialogRef<CreateConsultaFormComponent>,
    private createConsultaService: CreateConsultaFormServiceService,
    private listService: ListConsultasService,
  ) {
    this.horarios = [];
  }



  get agendas() {
    return this.createConsultaService.agendas;
  }

  get especialidades() {
    return this.createConsultaService.especialidades;
  }

  get medicos() {
    return this.createConsultaService.medicos;
  }

  ngOnInit(): void {
    this.createConsultaService.getEspecialidades().subscribe((especialidades) => {
      this.createConsultaService.especialidades = especialidades;
    });
    this.new_consulta = {}
  }

  closeDialog() {
    this.dialogRef.close();
  }

  especialidadesChange(value: number) {
    this.createConsultaService
      .getMedicosByEspecialidade(value)
      .subscribe((medicos) => (
        this.createConsultaService.medicos = medicos
      ));
    this.horarios = [];
  }

  medicoChange(value: number) {
    this.createConsultaService
      .getAgendasByMedico(value)
      .subscribe((agendas) => (
        this.createConsultaService.agendas = agendas
      ));
    console.log(this.createConsultaService
      .getAgendasByMedico(value)
      .subscribe((agendas) => (
        this.createConsultaService.agendas = agendas
      )))
    this.horarios = [];
  }

  diaChange(value: number) {
    this.horarios = <string[]>(
      this.createConsultaService.agendas.find((data) => data.id == value)?.horarios
    );
  }

  onSubmit(createConsulta: any) {
    this.createConsultaService.criarConsulta(this.new_consulta).subscribe(res => {
      createConsulta.reset()
      this.createConsultaService.resetFormData()
      this.dialogRef.close();
      this.listService.getConsultas().subscribe((consultas) => {
        this.listService.consultas = consultas;
      });
    })
  }
}
