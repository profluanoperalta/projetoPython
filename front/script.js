const apiUrl = 'http://localhost:8000/api/registros';

function enviar() {
  const nome = document.getElementById("nome").value;
  const nascimento = document.getElementById("nascimento").value;
  const data = { nome, nascimento };
  
  fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  alert("Registro Enviado!");
}

function listar() {
  fetch(apiUrl)
  .then(response => response.text())
  .then(data => {
    const registros = document.getElementById("registros");
    if (!data) {
      alert("sem dados");
    } else {
      registros.innerText = JSON.stringify(JSON.parse(data), null, 4);
    }
  })
  .catch(error => {
    alert("Não foi possível conectar à API. Verifique se ela está ligada.");
  });;
}
