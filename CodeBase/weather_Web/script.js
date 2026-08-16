const apikey = "8a105afee79fdcdd02167cf42487de35"
const url = `https://api.openweathermap.org/data/2.5/weather?units=metric&q=`;



const weather = async (city) => {
    console.log(city)

    const api = await fetch(url + city + `&appid=${apikey}`)
    const response = await api.json()

    console.log(response)
    if (response.cod === 200) {
        document.querySelector(".city").innerHTML = response.name
        document.querySelector(".temp").innerHTML = Math.round(response.main.temp) + "°C"
        document.querySelector(".humidity").innerHTML = response.main.humidity + "%"+"<br>huminity"
        document.querySelector(".wind").innerHTML = response.wind.speed + " km/h"+"<br>Wind speed"
        console.log(response.name)
        console.log(response.weather[0].main)
        console.log(response.main.temp)
        document.querySelector(".card").classList.remove("hidden")
        document.querySelector(".error").classList.add("hidden")
        const weatherimg = document.querySelector(".weather_icon")

        if (response.weather[0].main == "Clouds") {
            weatherimg.src = "/Assets/clouds.png"
        }
        else if (response.weather[0].main == "Clear") {
            weatherimg.src ="/Assets/2682848_day_forecast_sun_sunny_weather_icon.png"
         }
        else if (response.weather[0].main == "Rain") {
            weatherimg.src ="/Assets/icons8-storm-94.png"
         }
        else if (response.weather[0].main == "Drizzle") {
            weatherimg.src ="/Assets/icons8-rain-cloud-48.png"
         }
        else if (response.weather[0].main == "Mist") {
            weatherimg.src ="/Assets/clouds.png"
         }




    }
    else {
        let error = document.querySelector(".error")
        error.innerHTML = "city not found"
        error.classList.remove("hidden")
        document.querySelector(".card").classList.add("hidden")
        console.log(`error code${response}`)
    }



}




function update() {
    let data = document.getElementById("inputvalue").value
    weather(data)

}