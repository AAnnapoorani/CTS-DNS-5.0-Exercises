import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CourseService } from '../../services/course';
import { CourseCardComponent } from '../course-card/course-card';
import { Course } from '../../models/course';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    CourseCardComponent
  ],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseListComponent {

  searchText = '';

  courses: Course[] = [];
  constructor(
    private courseService: CourseService) {
      this.courses =  this.courseService.getCourses();
    }
  
  enrolledCount = 0;
  onEnroll(course: Course) {
    alert( `Successfully enrolled in ${course.title}`);
  this.enrolledCount++;
}

  get filteredCourses() {
    return this.courses.filter(course =>
      course.title
        .toLowerCase()
        .includes(this.searchText.toLowerCase())
    );
  }
}

