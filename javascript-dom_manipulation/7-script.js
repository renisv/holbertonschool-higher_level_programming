async function getData() {
    try {
        const result = await fetch("https://swapi-api.hbtn.io/api/films/?format=json");
        if (result.status === 200) {
            return result.json();
        } else {
            throw new Error("data not exists for the moment");
        }
    } catch (error) {
        console.log("error---", error);
        throw new Error("data not exists for the moment");
    }
}
getData()
    .then((result) => {
        const movies = result.results;
        const moviesList = document.getElementById("list_movies");
        movies.forEach(element => {
            const movieTitleContainer = document.createElement('li');
            movieTitleContainer.textContent += element.title;
            moviesList.appendChild(movieTitleContainer);
        });
    })
    .catch((error) => {
        return error;
    })