function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function GuardarDatos(){
    const formulario = new FormData(document.getElementById('formulario'));
    const lista = document.getElementById('lista')
fetch('/',{
    method: "POST",
    body: formulario,
    headers:{
        "X-CSRFToken":  getCookie('csrftoken'),  
        "X-Requested-With": "XMLHttpRequest"    
    }
}).then(
    function(response){
        return response.json()
    }
).then(
    function(data){
        arraylista = data.profesores;
        const li = document.createElement('li');
        li.innerHTML = arraylista[arraylista.length -1].nombre +" - "+  arraylista[arraylista.length -1].email
        lista.appendChild(li);
    }
)
}



