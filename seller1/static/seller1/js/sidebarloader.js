

            $.ajax({
                type:'GET',
                url:'/user_dashboard2',
                success:function(data){
                    var a = data["list"];
                    
                    for(var i=0;i<a.length;i++)
                    {
                    //  console.log(a[i].seller.title);
                     if(a[i].seller.base_type== 'Seller'){
                        $("#multiple_tagger1").append(
                                 "<a href='/seller/user_detail/"+a[i].seller.business_id+"'>"+
                                    "<button type='button' class='btn bg-white mt-2 w-100 text-control' name='button'>"+a[i].seller.title+"</button>"+
                                "</a>"
                          )
                     }
                    if(a[i].seller.base_type== 'Advisor'){
                        $("#multiple_tagger3").append(
                                "<a href='/advisor/user_detail/"+a[i].seller.advisor_id+"'>"+
                                    "<button type='button' class='btn bg-white mt-2 w-100 text-control' name='button'>"+a[i].seller.title+"</button>"+
                                "</a>"
                          )
                     }
                    if(a[i].seller.base_type== 'Investor'){
                        $("#multiple_tagger2").append(
                                 "<a href='/investor/user_detail/"+a[i].seller.investor_id+"'>"+
                                    "<button type='button' class='btn bg-white mt-2 w-100 text-control' name='button'>"+a[i].seller.title+"</button>"+
                                "</a>"
                          )
                     }

                    }
                }
            })




