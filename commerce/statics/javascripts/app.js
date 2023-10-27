const ul = document.querySelector('ul')
const error = document.querySelector('.error-list')
const hideError = function(){
    ul.classList.add("hide-error")
}
setTimeout(hideError, 3000)


const messages = document.querySelector(".messages")
const messageError = function(){
    messages.classList.add("hide-error")
}
setTimeout(messageError, 3000)
