
//document.getElementById("gerar").addEventListener("click", function(event) {
//    let generoSelected = document.getElementById("generos").value;
//    let url = "http://127.0.0.1:5000/gerar";
//    if (generoSelected) {
//        url += `?genero=${generoSelected}`;
//    }
//
//    fetch(url)


document.getElementById("gerar").addEventListener("click", function() {
    let generoSelected = document.getElementById("generos").value;
    let url = "http://127.0.0.1:5000/gerar";
    
    if (generoSelected) {
        url += `?generos=${generoSelected}`;
    }
    
    fetch(url)

    
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`); // Trata erros HTTP
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            document.getElementById("gerar").click();
            return;
        }

        document.getElementById("titulo").innerText = data.titulo;
        document.getElementById("genero").innerText = data.genero.join(', '); // Join the list into a string for display
        document.getElementById("link").innerHTML = `<a href="${data.link}" target="_blank">Mais informação</a>`;
        document.getElementById("image_poster").src = "https://image.tmdb.org/t/p/w500" + data.poster;     
        
    })
    .catch(error => {
        console.error("Erro:", error);
        alert("Ocorreu um erro ao buscar o filme. Tente novamente mais tarde.");
    });
});