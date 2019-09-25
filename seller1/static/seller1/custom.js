 // When the user scrolls down 20px from the top of the document, slide down the navbar
 window.onscroll = function() {scrollFunction()};
                
 function scrollFunction() {
     if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {                        
         $('#navbar').removeClass('bg-t');  
         $('#navbar').addClass('bg-change');        

     } else {                      
         $('#navbar').removeClass('bg-change');
         $('#navbar').addClass('bg-t');
     }
 }
 var x = document.getElementById("Specifications");
 x.style.display = "block";
 function myFunctions() {
     var x = document.getElementById("tab_Business");
     if (x.style.display === "none") {
         x.style.display = "block";
         document.getElementById('img').className ='selected-side-icon-right';
     } else {
         x.style.display = "none";
         document.getElementById('img').className ='selected-side-icon-left';
     }
 }
