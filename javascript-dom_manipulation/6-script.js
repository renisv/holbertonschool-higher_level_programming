async function getData() {
    try {
        const result = await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
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
        //console.log('Fetched data:', result);
        document.getElementById("character").innerHTML += result.name;
    })
    .catch((error) => {
        return error;
    })