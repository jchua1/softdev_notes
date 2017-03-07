var master = document.getElementById('master');
var a = document.getElementById('a');
var b = document.getElementById('b');

master.addEventListener('click', function(e) {
    alert('Clicked item in master list!');
    e.target.style.color = "red";
}, false);

a.addEventListener('click', function(e) {
    alert('Clicked item in list A!');
    e.target.style.color = "blue";
}, false);

b.addEventListener('click', function(e) {
    alert('Clicked item in list B!');
    e.target.style.color = "blue";
    e.stopPropagation();
}, false);
    
