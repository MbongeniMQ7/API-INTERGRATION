// Select elements
const searchBtn = document.getElementById("search-btn");
const destinationInput = document.getElementById("destination-input");
const cityDetailsContainer = document.getElementById("city-details-container");

// Add event listener to search button
searchBtn.addEventListener("click", cityDetails);

async function cityDetails() {
    const destinationName = destinationInput.value.trim(); // Fix the incorrect property used

    if (!destinationName) {
        cityDetailsContainer.innerHTML = "<p>Please enter a destination.</p>";
        return;
    }
    // Show loader (optional)
    cityDetailsContainer.innerHTML = "<p>Loading...</p>";

    try {
        const response = await fetch(
            `https://geocoding-api.open-meteo.com/v1/search?name=${destinationName}&count=1&format=json`
        );
        const data = await response.json();

        if (!data.results || data.results.length === 0) {
            cityDetailsContainer.innerHTML = "<p>No city found.</p>";
            return;
        }

        const city = data.results[0]; // Get the first search result

        // Display city details
        cityDetailsContainer.innerHTML = `
            <h3>${city.name}, ${city.country}</h3>
            <p>Latitude: ${city.latitude}</p>
            <p>Longitude: ${city.longitude}</p>
        `;
    } catch (error) {
        cityDetailsContainer.innerHTML = `<p>Error fetching data. Please try again later.</p>`;
        console.error("Error:", error);
    }
}
