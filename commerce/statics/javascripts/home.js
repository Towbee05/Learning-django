const btn = document.querySelector("#toggle-btn")
const nav = document.querySelector(".nav-bar")
const links = document.querySelector(".btn-container")

btn.addEventListener("click", function(){
    if ((nav.classList.contains("show-navbar"))){
        nav.classList.remove("show-navbar")
        links.classList.remove("show-navbar")
    }
    
    else{
        nav.classList.add("show-navbar")
        links.classList.add("show-navbar")

    }
})
