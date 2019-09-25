var x = document.getElementById("Specifications");
x.style.display = "none";
function myFunctions2() {
    var x = document.getElementById("Specifications");
    if (x.style.display === "none") {
        x.style.display = "block";
        document.getElementById('img').className ='selected-side-icon-right2';
    } else {
        x.style.display = "none";
        document.getElementById('img').className ='selected-side-icon-left2';
    }
}
function myFunctions3() {
    var x = document.getElementById("Specifications");
    if (x.style.display === "none") {
        x.style.display = "block";
        document.getElementById('img').className ='selected-side-icon-right3';
    } else {
        x.style.display = "none";
        document.getElementById('img').className ='selected-side-icon-left3';
    }
}