let lastActiveTab; 

function showTabContent(id){
    lastActiveTab = id ;
    document.getElementById('body').style.display = "none";
    document.getElementById(id).style.display = "block";
    document.getElementById('detail-footer').style.display = "block";
}

function showBody(){
    document.getElementById(lastActiveTab).style.display = "none";
    document.getElementById('body').style.display = "block";
    document.getElementById('detail-footer').style.display = "none";
    lastActiveTab = undefined;
}