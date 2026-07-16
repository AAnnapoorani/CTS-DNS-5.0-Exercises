import { Component } from '@angular/core';

import { HeaderComponent } from './components/header/header';
import { CourseListComponent } from './components/course-list/course-list';
import { StudentProfileComponent } from './components/student-profile/student-profile';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    HeaderComponent,
    CourseListComponent,
    StudentProfileComponent
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {}