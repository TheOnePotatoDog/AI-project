document.addEventListener("DOMContentLoaded", () => {
    const botsContainer = document.getElementById("bots");

    fetch('/api/getBots')
        .then(response => response.json())
        .then(bots => {
            bots.forEach(bot => {
                const botDiv = document.createElement("div");
                botDiv.classList.add("bot");
                botDiv.innerHTML = `<h2>${bot.name}</h2><p>${bot.description}</p>`;
                botsContainer.appendChild(botDiv);
            });
        })
        .catch(error => console.error('Error fetching bots:', error));
});