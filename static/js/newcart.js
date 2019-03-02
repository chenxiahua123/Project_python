$(document).ready(function(){
    console.log('进入成功')
    $('.count .plus').click(function () {
        console.log('单机成功')

        var productid=$(this).attr('productid')
        // console.log(productid)

        data={
            'productid':productid
        }


        $.get('/app01/addcart',data,function (response) {
            // console.log(response.status)
            if (response.status==0){
                window.open('/app01/login',target='_self')
            }else if (response.status==1){
                console.log('进入成功3333333')
                console.log('6666')
                console.log(productid)
                console.log('7777')
                console.log(response)
                console.log('8888')
                $('#span11').html(response.number)
                console.log(response.number)
                console.log('9999')


            }




        })
    })

    $('.count .minus').click(function () {
        console.log('进入减成功')

        var productid=$(this).attr('productid')

        console.log(productid)

        data={
            'productid':productid
        }

        $.get('/app01/minuscart',data,function (response) {

            if (response.status==0){
                window.open('/app01/login',target='_self')
            }else if (response.status==1){
                $('#span11').html(response.number)
                console.log(response)
            }

        })




    })


})