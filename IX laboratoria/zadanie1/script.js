let azure = Array.from(document.getElementsByClassName("azure"));
let border = Array.from(document.getElementsByClassName("border"));
let bold = Array.from(document.getElementsByClassName("bold"));
let zero_margin = Array.from(document.getElementsByClassName("zero-margin"));

function ustaw() {
azure.forEach(element => {
  element.classList.add("azure");
});

border.forEach(element => {
  element.classList.add("border");
});

bold.forEach(element => {
  element.classList.add("bold");
});

zero_margin.forEach(element => {
  element.classList.add("zero-margin");
});
document.getElementById("h-h1").classList.add("header-h1");
document.getElementById("nav").classList.add("nav");
document.getElementById("ul").classList.add("nav-ul");
document.getElementById("li").classList.add("nav-li");
document.getElementById("li2").classList.add("nav-li");
document.getElementById("aside").classList.add("aside");
document.getElementById("a-h1").classList.add("aside-h1");
document.getElementById("a-h2").classList.add("aside-h2");
document.getElementById("a-li").classList.add("aside-li");
document.getElementById("a-li2").classList.add("aside-li");
document.getElementById("a-li3").classList.add("aside-li");
document.getElementById("main").classList.add("main");
document.getElementById("m-hq").classList.add("main-h1");
document.getElementById("blockquote").classList.add("main-blockquote");
document.getElementById("footer").classList.add("footer");
}

function skasuj() {
azure.forEach(element => {
  element.classList.remove("azure");
});

border.forEach(element => {
  element.classList.remove("border");
});

bold.forEach(element => {
  element.classList.remove("bold");
});

zero_margin.forEach(element => {
  element.classList.remove("zero-margin");
});
document.getElementById("h-h1").classList.remove("header-h1");
document.getElementById("nav").classList.remove("nav");
document.getElementById("ul").classList.remove("nav-ul");
document.getElementById("li").classList.remove("nav-li");
document.getElementById("li2").classList.remove("nav-li");
document.getElementById("aside").classList.remove("aside");
document.getElementById("a-h1").classList.remove("aside-h1");
document.getElementById("a-h2").classList.remove("aside-h2");
document.getElementById("a-li").classList.remove("aside-li");
document.getElementById("a-li2").classList.remove("aside-li");
document.getElementById("a-li3").classList.remove("aside-li");
document.getElementById("main").classList.remove("main");
document.getElementById("m-hq").classList.remove("main-h1");
document.getElementById("blockquote").classList.remove("main-blockquote");
document.getElementById("footer").classList.remove("footer");  
}