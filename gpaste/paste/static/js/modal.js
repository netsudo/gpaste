var modal = document.getElementById('encrypt-modal');
var btn = document.getElementById("encrypt-button");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    event.preventDefault();
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

