function listado() {
  $.ajax({
    url: "/personas/Inicio/",
    type: "get",
    dataType: "json",
    succes: function (response) {
      console.log(response);
    },
  });
}

alert("hola mundo");

 <script>
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        function GuardarDatos() {
            var form = new FormData(document.getElementById('form-suscripcion'));
            var lista = document.getElementById('ul-suscriptor');
            //
            fetch("/", {
                method: "POST",
                body: form,
                headers: {
                    "X-CSRFToken": getCookie('csrftoken'),
                    "X-Requested-With": "XMLHttpRequest"
                }
            }).then(
                function(response) {
                    return response.json()
                }
            ).then(
                function(data) {
                    array_sus = data.suscriptores;
                    var li = document.createElement('li');
                    li.innerHTML = array_sus[array_sus.length - 1].full_name + array_sus[array_sus.length - 1].email 
                    //
                    lista.appendChild(li);
                }
            )
        }
    </script>
