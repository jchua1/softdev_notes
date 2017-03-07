var pic = document.getElementById("vimage");
var b = document.getElementById("button");

var i = "hi"

var circle = function(x, y) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", 100);
    c.setAttribute("fill", "red");
    c.setAttribute("stroke", "black");
    c.setAttribute("class", i);
    i += " " + i;
    return c;
};

var addCircle = function(e) {
    var x = e.offsetX;
    var y = e.offsetY;
    var c = circle(x, y);
    pic.appendChild(c);
};

var clear = function() {
    //while (pic.lastChild) {
    alert(pic.lastChild.className);
//	pic.removeChild(pic.lastChild);
   // };
};

var highlight = function(e) {
    alert(e.className);
};

pic.addEventListener("click", addCircle);
b.addEventListener("click", clear);
