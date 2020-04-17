import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import{VacancyService} from '../vacancy.service'
import { CompanyService } from "../company.service";
import { Company, Vacancy } from "../../models"

@Component({
  selector: 'app-vacancies-page',
  templateUrl: './vacancies-page.component.html',
  styleUrls: ['./vacancies-page.component.css']
})
export class VacanciesPageComponent implements OnInit {
  vacancy:Vacancy
  constructor(private companyService: CompanyService,private vacancyService: VacancyService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getVacancy();
  }
  getVacancy() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.vacancyService.getVacancy(id).subscribe(vacancy => this.vacancy = vacancy);
  }

}
