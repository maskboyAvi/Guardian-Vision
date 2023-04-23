function setUsername() {
    var temp = localStorage.getItem("id");
    console.log(temp);
    document.getElementById("username").innerHTML = temp;
}

function logout() {
    localStorage.clear();
    window.location.href = "/home";
    localStorage.setItem("flagLog", true);
}