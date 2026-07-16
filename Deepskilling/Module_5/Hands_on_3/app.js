import { courses } from './data.js';

let displayedCourses = [...courses];

const courseGrid =
    document.querySelector('.course-grid');

const totalCreditsElement =
    document.querySelector('#total-credits');

const searchInput =
    document.querySelector('#search-courses');

const sortButton =
    document.querySelector('#sort-btn');

const selectedCourse =
    document.querySelector('#selected-course');

function renderCourses(courseList) {

    courseGrid.innerHTML = '';

    courseList.forEach(course => {

        const article =
            document.createElement('article');

        article.className = 'course-card';

        article.dataset.id = course.id;

        article.innerHTML = `
            <h3>${course.name}</h3>

            <p>Course Code: ${course.code}</p>

            <p>Credits: ${course.credits}</p>

            <p>Grade: ${course.grade}</p>
        `;

        courseGrid.appendChild(article);

    });

    updateTotalCredits(courseList);
}

function updateTotalCredits(courseList) {

    const totalCredits =
        courseList.reduce(
            (sum, course) =>
                sum + course.credits,
            0
        );

    totalCreditsElement.textContent =
        `Total Credits: ${totalCredits}`;
}

renderCourses(displayedCourses);

searchInput.addEventListener('input', () => {

    const searchText =
        searchInput.value.toLowerCase();

    displayedCourses =
        courses.filter(course =>
            course.name
                  .toLowerCase()
                  .includes(searchText)
        );

    renderCourses(displayedCourses);

});

sortButton.addEventListener('click', () => {

    displayedCourses.sort(
        (a, b) =>
            b.credits - a.credits
    );

    renderCourses(displayedCourses);

});

courseGrid.addEventListener('click', event => {

    const card =
        event.target.closest('.course-card');

    if (!card) return;

    const courseId =
        Number(card.dataset.id);

    const course =
        courses.find(
            c => c.id === courseId
        );

    selectedCourse.textContent =
        `Selected Course: ${course.name}
         | Grade: ${course.grade}`;
});