$('#id_phone_number_primary').attr('oninput','javascript: if (this.value > 999999999999999) this.value = this.value.slice(0, 15);');

$(function() {
  $("#dialog-confirm").dialog({ autoOpen: false }).find("a.cancel").click(function(e){
      e.preventDefault();
      $("#dialog-confirm").dialog("close");
  });
  $("a[href]:not(#dialog-confirm a)").click(function(e) {
      e.preventDefault();
      $("#dialog-confirm").dialog("option", "title", $(this).text()).dialog("open").find("a.ok").attr({href: this.href, target: this.target});
  });
});

$("#id_currency").change(function () {
  
    var a =$("#id_currency").val().split("**");
    $('.currency_tag').text(a[3]);
    $('#id_asking_price').trigger("input");
    $('#id_rev_year').trigger("input");
    $('#id_year_16').trigger("input");
    $('#id_year_15').trigger("input");
    $('#id_year_14').trigger("input");
    $('#id_year_13').trigger("input");
    $('#id_year_17').trigger("input");
    $('#id_year_19').trigger("input");   
    $('#id_loan_amount').trigger("input");
    $('#id_purchase_price').trigger("input");
    $('#id_loan_amount').trigger("input");
    $('#id_average_monthly_revenue').trigger("input");
    $('#id_average_monthly_expense').trigger("input");
    $('#id_hour_fee').trigger("input");
    $('#id_cp_emp').trigger("input");
    $('#id_cap_req').trigger("input");
    $('.usdtagger1').trigger("change");
    $('.usdtagger2').trigger("change");
    $('.usdtagger3').trigger("change");
    $('.usdtagger4').trigger("change");
    $('.usdtagger5').trigger("change");
    $('.usdtagger6').trigger("change");
    $('.usdtagger7').trigger("change");
    $('.usdtagger8').trigger("change");

    
});

$('#id_asking_price').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
  var dum = $("#id_currency").val().split("**");
  var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_1').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_1').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_1').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_1').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_rev_year').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_2').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_2').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_2').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_2').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_year_16').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_3').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_3').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_3').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_3').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_year_15').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_4').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_4').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_4').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_4').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_year_14').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_5').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_5').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_5').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_5').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_year_13').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_6').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_6').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_6').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_6').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_year_17').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_7').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_7').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_7').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_7').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_year_19').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
  var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_7').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_7').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_7').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_7').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_loan_amount').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_8').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_8').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_8').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_8').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_purchase_price').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_9').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_9').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_9').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_9').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_average_monthly_revenue').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_10').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_10').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_10').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_10').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_average_monthly_expense').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_11').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_11').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_11').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_11').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_hour_fee').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_12').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_12').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_12').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_12').text(curencytxt+" "+value+" Billion");
  }

});

$('#id_cp_emp').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_13').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_13').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_13').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_13').text(curencytxt+" "+value+" Billion");
  }

});


$('#id_cap_req').on('input', function() {
  var value = $(this).val();
  var curencytxt = "AFN";
  if($("#id_currency").val()!= null){
    var dum = $("#id_currency").val().split("**");
    var curencytxt = dum[3];
  }

  if(value<1000){

    $('#currency_message_14').text(curencytxt+" "+value);
  }
  else if(value>=1000 && value<1000000 ){
    value=value/1000;
    value=value.toFixed(2);
    $('#currency_message_14').text(curencytxt+" "+value+" Thousand");
  }
  else if(value>=1000000 && value<1000000000 ){
    value=value/1000000;
    value=value.toFixed(2);
    $('#currency_message_14').text(curencytxt+" "+value+" Million");
  }
  else if(value>=1000000000 && value<1000000000000 ){
    value=value/1000000000;
    value=value.toFixed(2);
    $('#currency_message_14').text(curencytxt+" "+value+" Billion");
  }

});


$(document).ready(function(){

  $.ajax({
      type:'GET',
      url:'/user_dashboard2',
      success:function(data){
          var a = data["list"];
          
          for(var i=0;i<a.length;i++)
          {
           console.log(a[i].seller.title);
           if(a[i].seller.base_type== 'Seller'){
              $("#multiple_tagger").append(
                       "<a href='/seller/user_detail/"+a[i].seller.business_id+"'>"+
                          "<button type='button' class='btn btn-primary mt-2 w-100' name='button'>"+a[i].seller.title+"</button>"+
                      "</a>"
                )
           }
          if(a[i].seller.base_type== 'Advisor'){
              $("#multiple_tagger").append(
                      "<a href='/seller/user_detail/"+a[i].seller.advisor_id+"'>"+
                          "<button type='button' class='btn btn-primary mt-2 w-100' name='button'>"+a[i].seller.title+"</button>"+
                      "</a>"
                )
           }
          if(a[i].seller.base_type== 'Investor'){
              $("#multiple_tagger").append(
                       "<a href='/seller/user_detail/"+a[i].seller.investor_id+"'>"+
                          "<button type='button' class='btn btn-primary mt-2 w-100' name='button'>"+a[i].seller.title+"</button>"+
                      "</a>"
                )
           }

          }
      }
  })

});