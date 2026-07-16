import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Course } from '../../models/course';

@Component({
  selector: 'app-course-card',
  standalone: true,
  templateUrl: './course-card.html',
  styleUrl: './course-card.css'
})
export class CourseCardComponent {

  @Input() course!: Course;

  @Output() enrollCourse =
    new EventEmitter<Course>();

  enroll() {
    this.enrollCourse.emit(this.course);
  }
}