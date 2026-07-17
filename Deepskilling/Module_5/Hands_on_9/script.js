const cards = document.querySelectorAll(".course-card");

cards.forEach(card => {
    card.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            alert( card.querySelector("h3").textContent + " selected" );

        }
    });
});