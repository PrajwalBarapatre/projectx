function ValidateEmail(mail) 
{
      if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail))
      {
      $("#mailid").css("border-color","green");
      return ("right email");
      }
      else
      {
      $("#mailid").css("border-color","red");
      return ("enter right email id");
      }

}
function Validatenumber(mail) 
{
      if (/^[-+]?\d+$/.test(mail))
      {
        $("#pass").css("border-color","green");
      return ("right email");
      }
      else
      {
      $("#pass").val('');
      $("#pass").css("border-color","red");
      return ("enter right phone number");
      }
}
$("#pass").on('input', function()  {
  var username = $(this).val();
  tex=Validatenumber(username)
});
$("#mailid").on('input', function()  {
  var username = $(this).val();
  tex=ValidateEmail(username)
});

/*
$("#pass").on('input', function()  {
    var username = $(this).val();
    tex=Validatenumber(username)
    $("#text").text(tex);
    console.log( $(this).val() );
    $.ajax({
      type: 'GET',
      url: "/rooms/likepost",
      data:{
          'username': username
      },
      dataType: 'json',
      success: function (json) {
  //       $("#text").text(json.user);
      }
    });
  
  });*/