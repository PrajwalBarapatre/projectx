function myFunctions() {
    var x = document.getElementById("Specifications");
    if (x.style.display === "none") {
        x.style.display = "block";
        document.getElementById('img').className ='selected-side-icon-right';
        $('#map_parent').css('width','50%');
        $('#map_parent').css('margin-left','50%');
        console.log("hello1");
        
    } else {
        x.style.display = "none";
        document.getElementById('img').className ='selected-side-icon-left';
        $('#map_parent').css('width','100%');
        $('#map_parent').css('margin-left','0%');
        console.log("hello2");
    }
}
