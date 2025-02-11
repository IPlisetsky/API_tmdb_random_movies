document.getElementById("gerar").addEventListener("click", function() {
    let generoSelected = document.getElementById("generos").value;
    let anoValue = document.getElementById("ano").value; // Get the value from the input 'ano'
    let anoInicio = document.getElementById("ano-inicio").value;
    let anoFim = document.getElementById("ano-fim").value;



    let url = "http://127.0.0.1:5000/gerar";
    
    if (generoSelected) {
        url += `?generos=${generoSelected}`;
    }
    
    
    if (anoInicio) {
        url += `&ano-inicio=${anoInicio}`;
    }
    
    if (anoFim) {
        url += `&ano-fim=${anoFim}`;
    }
    

    if (anoValue) {
        url += `&ano=${anoValue}`;
    }
    
    fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            document.getElementById("gerar").click();
            return;
        }

        document.getElementById("titulo").innerText = `${data.titulo} (${data.ano_lancamento})`;
        document.getElementById("genero").innerText = data.genero.join(', ');
        document.getElementById("link").innerHTML = `<a href="${data.link}" target="_blank">Mais informação</a>`;
        document.getElementById("image_poster").src = "https://image.tmdb.org/t/p/w500" + data.poster;     
    })
    .catch(error => {
        console.error("Erro:", error);
        alert("Ocorreu um erro ao buscar o filme. Tente novamente mais tarde.");
    });
});
