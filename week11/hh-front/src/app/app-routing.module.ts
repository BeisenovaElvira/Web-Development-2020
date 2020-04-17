import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NewsListComponent } from './news-list/news-list.component';
import { NewsPageComponent } from './news-page/news-page.component';
import { VacanciesPageComponent } from './vacancies-page/vacancies-page.component';

const routes: Routes = [
  { path: '', component: NewsListComponent },
  { path: 'company/:id', component: NewsPageComponent },
  { path: 'company/:id/vacancies/:id', component: VacanciesPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
