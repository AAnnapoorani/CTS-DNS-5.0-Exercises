# Module 5: Web Development - HTML, CSS, and JavaScript

## Overview
This module covers front-end web development fundamentals using HTML, CSS, and JavaScript. It includes hands-on projects demonstrating responsive design, interactive user interfaces, and modern web development practices.

## Module Structure
```
Module_5/
├── index.html               # Main landing page
├── style.css                # Global styles
├── Hands_on_1/              # HTML basics
├── Hands_on_2/              # CSS styling
├── Hands_on_3/              # CSS layouts (Flexbox)
├── Hands_on_4/              # CSS layouts (Grid)
├── Hands_on_5/              # JavaScript basics
├── Hands_on_6/              # DOM manipulation
├── Hands_on_7/              # Events and interactivity
├── Hands_on_8/              # Forms and validation
├── Hands_on_9/              # Responsive design
├── Hands_on_10/             # Project showcase
└── Output/                  # Output and generated files
```

## Topics Covered

### HTML Fundamentals
- HTML5 semantic elements
- Document structure
- Forms and inputs
- Accessibility (a11y)
- Meta tags and SEO
- Linking and navigation

### CSS Styling
- Selectors and specificity
- Box model
- Positioning and layout
- Typography
- Colors and backgrounds
- Animations and transitions
- Media queries
- Flexbox
- CSS Grid

### JavaScript
- Variables and data types
- Functions and scope
- DOM manipulation
- Event handling
- ES6+ features
- Async programming (Promises, async/await)
- Fetch API
- Local storage

### Responsive Design
- Mobile-first approach
- Media queries
- Viewport configuration
- Flexible layouts
- Touch events

### Web Performance
- Optimization techniques
- Code splitting
- Lazy loading
- Caching strategies

## Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Text editor or IDE (VS Code recommended)
- Basic understanding of HTML structure
- Command line/terminal familiarity

### Installation

#### Option 1: Using Python's Built-in Server
```bash
# Navigate to module directory
cd Module_5

# Start local server
python -m http.server 8000

# Open browser
# http://localhost:8000
```

#### Option 2: Using Live Server (VS Code Extension)
```bash
# Install Live Server extension in VS Code
# Right-click index.html
# Select "Open with Live Server"
```

#### Option 3: Direct Browser
```bash
# Simply open HTML files directly in browser
# File > Open File > index.html
# Or drag and drop HTML file to browser
```

## Project Structure Best Practices

### Typical Project Layout
```
project/
├── index.html               # Main page
├── css/
│   ├── style.css           # Main stylesheet
│   └── responsive.css      # Responsive styles
├── js/
│   ├── main.js             # Main JavaScript
│   └── utils.js            # Utility functions
├── assets/
│   ├── images/             # Image files
│   ├── fonts/              # Custom fonts
│   └── icons/              # SVG/icon files
└── README.md               # Documentation
```

## HTML Template Example
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Page description">
    <title>Page Title</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h1>Welcome</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="content">
            <h2>Content</h2>
            <p>Your content here</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Your Name</p>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>
```

## CSS Best Practices

### Mobile-First Responsive Design
```css
/* Mobile styles (default) */
body {
    font-size: 14px;
    padding: 10px;
}

.container {
    width: 100%;
}

/* Tablet and up */
@media (min-width: 768px) {
    body {
        font-size: 16px;
        padding: 20px;
    }
    
    .container {
        width: 750px;
        margin: 0 auto;
    }
}

/* Desktop and up */
@media (min-width: 1024px) {
    .container {
        width: 960px;
    }
}
```

### Flexbox Layout
```css
/* Flex container */
.flex-container {
    display: flex;
    justify-content: space-between;  /* horizontal alignment */
    align-items: center;              /* vertical alignment */
    flex-wrap: wrap;                  /* wrap items */
    gap: 20px;                        /* space between items */
}

/* Flex items */
.flex-item {
    flex: 1;                          /* grow equally */
    min-width: 200px;
}
```

### CSS Grid Layout
```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 20px;
}

.grid-item {
    background: #f0f0f0;
    padding: 20px;
    border-radius: 5px;
}
```

## JavaScript Examples

### DOM Manipulation
```javascript
// Select elements
const element = document.getElementById('myId');
const elements = document.querySelectorAll('.myClass');
const divs = document.getElementsByTagName('div');

// Modify content
element.textContent = 'New text';
element.innerHTML = '<strong>Bold text</strong>';
element.setAttribute('data-value', '123');

// Add/remove classes
element.classList.add('active');
element.classList.remove('inactive');
element.classList.toggle('highlight');

// Create elements
const newDiv = document.createElement('div');
newDiv.textContent = 'New element';
document.body.appendChild(newDiv);
```

### Event Handling
```javascript
// Click event
const button = document.querySelector('button');
button.addEventListener('click', function(event) {
    console.log('Button clicked');
    event.preventDefault();
});

// Form submission
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    // Handle form data
    const formData = new FormData(form);
    console.log(Object.fromEntries(formData));
});

// Keyboard events
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        console.log('Enter pressed');
    }
});
```

### Fetch API
```javascript
// GET request
fetch('https://api.example.com/data')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

// POST request
fetch('https://api.example.com/data', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name: 'John', age: 30 })
})
    .then(response => response.json())
    .then(data => console.log(data));

// Async/await approach
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}
```

### Form Validation
```javascript
function validateForm(form) {
    const name = form.querySelector('input[name="name"]').value;
    const email = form.querySelector('input[name="email"]').value;
    const errors = [];

    if (name.trim() === '') {
        errors.push('Name is required');
    }

    if (!email.includes('@')) {
        errors.push('Invalid email format');
    }

    if (errors.length > 0) {
        alert(errors.join('\n'));
        return false;
    }

    return true;
}

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    if (validateForm(this)) {
        this.submit();
    }
});
```

## Responsive Breakpoints
- **Mobile**: 320px - 479px
- **Tablet**: 480px - 767px
- **Desktop**: 768px - 1023px
- **Large Desktop**: 1024px+

## Accessibility Tips
1. Use semantic HTML (header, nav, main, article, footer)
2. Include alt text for images
3. Ensure keyboard navigation works
4. Use ARIA labels when needed
5. Maintain sufficient color contrast
6. Use proper heading hierarchy
7. Provide focus indicators
8. Support screen readers

## Performance Optimization
1. Minimize CSS and JavaScript
2. Compress images
3. Use CSS instead of JavaScript for animations
4. Lazy load images and iframes
5. Cache static assets
6. Minify HTML/CSS/JS
7. Use CDNs for third-party libraries
8. Reduce CSS specificity

## Browser DevTools
- Inspect elements and styles
- Debug JavaScript
- Monitor network requests
- Check responsive design
- Analyze performance
- Test accessibility

## Common CSS Pitfalls
1. Using too much specificity
2. Not resetting default margins/padding
3. Forgetting vendor prefixes for older browsers
4. Not testing on multiple devices
5. Using px instead of relative units (em, rem)

## JavaScript Best Practices
1. Use const/let instead of var
2. Avoid global variables
3. Use meaningful variable names
4. Add error handling
5. Comment complex logic
6. Keep functions small and focused
7. Use template literals for strings
8. Validate user input

## Testing

### Manual Testing Checklist
- [ ] Test on multiple browsers
- [ ] Test on mobile devices
- [ ] Test keyboard navigation
- [ ] Test with screen readers
- [ ] Test form validation
- [ ] Test loading states
- [ ] Test error messages
- [ ] Check console for errors

### Automated Testing
```bash
# Using Selenium for browser testing
pip install selenium

# See Module_6 for testing examples
```

## Learning Objectives
- Create semantic HTML documents
- Style web pages with CSS
- Add interactivity with JavaScript
- Build responsive designs
- Implement form validation
- Optimize web performance
- Ensure accessibility
- Debug and test web applications

## Output Files
- Generated screenshots and test results in `Output/` directory
- Build artifacts (if using build tools)

## Tools and Resources

### Essential Tools
- VS Code
- Chrome DevTools
- Firefox DevTools
- Lighthouse
- Can I Use (caniuse.com)

### Online Resources
- MDN Web Docs
- CSS-Tricks
- JavaScript.info
- W3Schools
- CodePen

## Further Reading
- Responsive Web Design (Ethan Marcotte)
- Eloquent JavaScript (Marijn Haverbeke)
- CSS Secrets (Lea Verou)
- Web Content Accessibility Guidelines (WCAG)

## Notes
- Each hands_on folder builds progressively
- Start with Hands_on_1 for HTML basics
- Hands_on_10 demonstrates full project integration
- Use browser DevTools frequently
- Practice writing clean, semantic HTML

## Author
CTS DNS 5.0 Exercises

## License
Educational - Use for learning purposes
