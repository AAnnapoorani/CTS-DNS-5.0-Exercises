const loading =
    document.getElementById("loading");

const notifications =
    document.getElementById("notifications");

const errorContainer =
    document.getElementById("error-container");

const retryButton =
    document.getElementById("retry-btn");

/* AXIOS REQUEST INTERCEPTOR */

axios.interceptors.request.use(config => {
    console.log( `API call started: ${config.url}` );
    return config;
});

/* AXIOS FETCH FUNCTION */

async function apiFetch(url) {
    try {
        const response = await axios.get(url);
        return response.data;
    }

    catch(error) {
        throw error;
    }
}

/* RENDER NOTIFICATIONS */

function renderNotifications(posts) {
    notifications.innerHTML = "";
    const messages = [
        "Assignment 3 submission deadline is tomorrow. Submit before 11:59 PM.",
        "Mid-semester examination timetable has been published.",
        "New Data Structures study materials have been uploaded.",
        "Placement training registration is now open.",
        "Attendance records have been updated in the portal.",
        "Technical symposium registrations are now available.",
        "New e-books have been added to the digital library.",
        "AI Workshop scheduled this Friday in Seminar Hall 2.",
        "Course feedback forms are now available.",
        "Project review presentations will begin next Monday."
    ];

    posts.forEach((post, index) => {
        const card = document.createElement("div");
        card.className = "notification-card";
        card.innerHTML = `<h3>Notification ${index + 1}</h3>
                          <p>${messages[index]}</p>`;
        notifications.appendChild(card);
    });
}

/* LOAD DATA USING AXIOS */

async function loadNotifications() {
    loading.style.display = "block";
    errorContainer.textContent = "";
    retryButton.style.display = "none";
    notifications.innerHTML = "";
    try {
        const posts =
            await axios.get(
                "https://jsonplaceholder.typicode.com/posts",
                {
                    params: {
                        userId: 1
                    }
                }
            );
        renderNotifications(
            posts.data.slice(0, 10)
        );
    }
    catch(error) {
        errorContainer.textContent = "Failed to load notifications.";
        retryButton.style.display = "block";

        console.error(error);

    }

    finally {

        loading.style.display =
            "none";

    }
}

retryButton.addEventListener(
    "click",
    loadNotifications
);

loadNotifications();

/* ==================================
   FETCH VS AXIOS COMPARISON

   1. Fetch requires response.json()
      Axios parses JSON automatically.

   2. Fetch does not throw for
      HTTP errors automatically.
      Axios throws errors for
      non-2xx responses.

   3. Axios supports interceptors,
      request timeout and params
      more conveniently.
================================== */