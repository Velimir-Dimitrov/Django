navigator.geolocation.getCurrentPosition(
    function (position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        // Fetch data from Django API
        fetch(`/api/weather?lat=${latitude}&lon=${longitude}`)
            .then(response => response.json())
            .then(data => {
                const weatherElement = document.getElementById('weather');

                weatherElement.innerHTML = '';

                if (data.error) {
                    const errorMessage = document.createElement('p');
                    errorMessage.textContent = `Error: ${data.error}`;
                    weatherElement.appendChild(errorMessage);
                } else {
                    const temperature = data.temperature;
                    const condition = data.description.toLowerCase();

                    const unsuitableConditions = [
                        'rain', 'shower', 'storm', 'snow', 'mist', 'thunderstorm'
                    ];


                    const maxOutdoorTemp = 24;
                    const minOutdoorTemp = 4;


                    let weatherMessage = '';


                    if (unsuitableConditions.some(weather => condition.includes(weather))
                        || temperature < minOutdoorTemp
                        || temperature > maxOutdoorTemp) {
                        weatherMessage = "It's better to do your workout inside today.";
                    } else if (temperature > minOutdoorTemp || temperature > maxOutdoorTemp) {
                        weatherMessage = "It looks like a good day to do a workout outside!";
                    } else {
                        weatherMessage = "The weather is fine, but use your best judgment!";
                    }


                    const locationElement = document.createElement('p');
                    locationElement.innerHTML = `<strong>Your location:</strong> ${data.location}`;
                    weatherElement.appendChild(locationElement);

                    const temperatureElement = document.createElement('p');
                    temperatureElement.innerHTML = `<strong>Outside temperature:</strong> ${data.temperature} °C`;
                    weatherElement.appendChild(temperatureElement);

                    const conditionElement = document.createElement('p');
                    conditionElement.innerHTML = `<strong>Weather:</strong> ${data.description}
        <img src="https://openweathermap.org/img/wn/${data.icon}.png" alt="${data.description}">`;
                    weatherElement.appendChild(conditionElement);

                    const recommendationElement = document.createElement('p');
                    recommendationElement.innerHTML = `<strong>Our recommendation:</strong> ${weatherMessage}`;
                    weatherElement.appendChild(recommendationElement);

                }
            })

            .catch(error => {
                document.getElementById('weather').innerHTML = `<p>Error fetching weather data. Try again later.</p>`;
                console.error("Error:", error);
            });
    },
    function (error) {
        document.getElementById('weather').innerHTML = `<p>Unable to access your location. Please allow location services.</p>`;
        console.error("Geolocation Error:", error);
    }
);