var b_box = document.querySelector(".overlay")
var s_box = document.querySelector(".popupbox")
var addbutton = document.getElementById("add-javascript-button")

addbutton.addEventListener("click", function () {
    b_box.style.display = "block"
    s_box.style.display = "block"
})

var popupcencel = document.getElementById("popupcencel")
popupcencel.addEventListener("click", function () {

    event.preventDefault()
    b_box.style.display = "none"
    s_box.style.display = "none"


})

var popupadd = document.getElementById("popupadd")
popupadd.addEventListener("click", function () {

    event.preventDefault()
    b_box.style.display = "none"
    s_box.style.display = "none"

})
var bookcontainer = document.querySelector(".container")
var popuptitle = document.getElementById("popuptitle")
var popupAutor = document.getElementById("popupAutor")
var popuptext = document.getElementById("popuptext")
var popupadd = document.getElementById("popupadd")
var popupdelete = document.getElementById("popupdelete")


popupadd.addEventListener("click", function (event) {
    var div = document.createElement("div")
    div.setAttribute("class", "book-container")
    div.innerHTML = `<h2>${popuptitle.value}</h2>
                    <h3>${popupAutor.value}</h3>
                <p>${popuptext.value}</p>
                <button onclick="update(event)"id="popupdelete">Delete</button>`
    bookcontainer.append(div)
    event.preventDefault(event)
    b_box.style.display = "none"
    s_box.style.display = "none"
})


function update(event) {
    event.target.parentElement.remove()
} 