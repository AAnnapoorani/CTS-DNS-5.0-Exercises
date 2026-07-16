import { Injectable } from '@angular/core';
import { Course } from '../models/course';
@Injectable({ providedIn: 'root' })
export class CourseService {
  private courses: Course[] = [
    { id: 1, title: 'Data Structures', credits: 4, instructor: 'Dr. Kumar' },
    { id: 2, title: 'Database Management Systems', credits: 3, instructor: 'Dr. Priya' },
    { id: 3, title: 'Operating Systems', credits: 4, instructor: 'Dr. Anand' },
    { id: 4, title: 'Computer Networks', credits: 3, instructor: 'Dr. Ravi' },
    { id: 5, title: 'Web Development', credits: 4, instructor: 'Dr. Meena' }
  ];
  getCourses() {
    return this.courses;
  }
}