async function getData() {
    try {
        const result = await fetch("https://hellosalut.stefanbohacek.com/?lang=fr");
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
        const helloContainer = document.getElementById("hello");
        helloContainer.innerHTML += result.hello
    })
    .catch((error) => {
        return error;
    })