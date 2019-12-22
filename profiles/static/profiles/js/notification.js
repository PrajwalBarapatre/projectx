
var initial_noti = true;


// var div = document.getElementById('notifications_b');
// if (div.style.display !== 'none') {
//     div.style.display = 'none';
    
// }
// else {
    
//     if(initial_noti){
//     $('#noti_Counter_s').html('0');
//     $('#noti_Counter_b').html('0');
//         $.ajax({
//             type:'GET',
//             url:'/profiles/clear_notif',
//             success:function(data){
//                 $('#noti_Counter_s').html('0');
//                 $('#noti_Counter_b').html('0');
//             }
//         })
//             }
//             initial_noti=false;
        
//             div.style.display = 'block';              
// }




// $('#noti_Container_b').on('click',function(e){
//     e.preventDefault();
//     var div = document.getElementById('notifications_b');
//     if (div.style.display !== 'none') {
//         div.style.display = 'none';
        
//     }
//     else {
        
//         if(initial_noti){
//         $('#noti_Counter_s').html('0');
//         $('#noti_Counter_b').html('0');
//             $.ajax({
//                 type:'GET',
//                 url:'/profiles/clear_notif',
//                 success:function(data){
//                     $('#noti_Counter_s').html('0');
//                     $('#noti_Counter_b').html('0');
//                 }
//             })
//                 }
//                 initial_noti=false;           
//                 div.style.display = 'block';              
//     }
    
// })

function notification_start(){
    // e.preventDefault();
    var div = document.getElementById('notifications_b');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
        
    }
    else {
        
        if(initial_noti){
        $('#noti_Counter_s').html('0');
        $('#noti_Counter_b').html('0');
            $.ajax({
                type:'GET',
                url:'clear_notif',
                success:function(data){
                    $('#noti_Counter_s').html('0');
                    $('#noti_Counter_b').html('0');
                }
            })
                }
                initial_noti=false;           
                div.style.display = 'block';              
    }
    
}
function notification_busi(){
    
  var div = document.getElementById('notifications_s');
    if (div.style.display !== 'none') {
        div.style.display = 'none';              
    }
    else {
        div.style.display = 'block';
        if(initial_noti){
          $('#noti_Counter_s').html('0');
   $('#noti_Counter_b').html('0');
    $.ajax({
        type:'GET',
        url:'/clear_notif',
        success:function(data){
            console.log('ajax notif done')
            $('#noti_Counter_s').html('0');
            $('#noti_Counter_b').html('0');
        }
    })
        }
        initial_noti=false;
    }         
}




  
function toggle_chat() {
var c_toggle_w = document.getElementById('toggle_chat');
var c_btn = document.getElementById('chat_btn');
var r_icon = document.getElementById('rotate_icon');
var c_drop = document.getElementById('select2-id_currency-container');
    if (c_toggle_w.style.width !== '30px') {
        c_toggle_w.style.width = '30px';
        c_drop.style.width = '30px';
                    $("#id_currency").select2({    placeholder: 'C',
        dropdownParent: $('.selectdropdown'),width: '30px'});
        document.getElementById("chat_btn").innerHTML = "C";
    }
    else {
        c_toggle_w.style.width = '150px';
        c_drop.style.width = '150px';
    $("#id_currency").select2({    placeholder: 'Currency',
        dropdownParent: $('.selectdropdown'),width: '150px'});
        document.getElementById("chat_btn").innerHTML = "Chat";
    }
    if (r_icon.style.transform !== 'rotate(180deg)') {
        r_icon.style.transform = 'rotate(180deg)';
    }
    else {
        r_icon.style.transform = 'rotate(0deg)';
    }
};



$("#id_currency").select2();

$(document).ready(function(){
    $("#id_currency").change(function () {
        // console.log($(this).val().slice(-3));
        var a = $(this).val().split("**");
        $("#select2-id_currency-container").text(a[3]);
        sessionStorage.setItem("currency", $(this).val());


    });

    var a = sessionStorage.getItem("currency");

    $('#id_currency').val(a).change();
    // console.log(a);
    var b = a.split("**");
    $("#select2-id_currency-container").html(b[3]);
    console.log(b[3]);

    $.getJSON('https://ipapi.co/json/', function(data) {

        console.log(data.country);
        $("#country_code_primary option[id='"+data.country+"']").attr("selected", "selected");
                    myList = [];
                    $('#selUser option').each(function() {
                        myList.push($(this).val())
                    });
        
                    if(sessionStorage.getItem("currency")==null)
                    {
                        for (i = 0; i < myList.length; i++) {
                                var b = myList[i].split("**");
                                console.log(b[1]);
                                if(b[1]==data.country){
                                $('#selUser').val(myList[i]).change();
                                //   $("#select2-selUser-container").text(b[3]);

                            }
                        }
                    }
                    if(sessionStorage.getItem("currency")!=null)
                    {
                            var a = sessionStorage.getItem("currency");
                            $('#selUser').val(a).change();
                            console.log(a);
                            var b = a.split("**");
                            $("#select2-selUser-container").html(b[3]);
                            console.log(b[3]);
                    }

          });

});


