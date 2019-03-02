$(document).ready(function () {
    
    $('.data-con .checkall').click(function (response) {
        console.log('进入成功')

        var cartid=$(this).attr('cartid')

        console.log(cartid)

        data={
            'cartid':cartid
        }

        $.get('/app01/changestatus',data,function (response) {
            console.log(response)

            if (response.status==0){
                window.open('/app01/login',target='_self')
            }else if (response.status==1){
                console.log(response)
            }



        })






    })
    
    
    $('.deleteall').click(function (response) {
        console.log('点击全部删除按钮成功')

        console.log('0000000')
        var cartid=$("input[isselect^='False']").attr('cartid')
        var isselect=$("input[isselect^='False']").attr('isselect')
        console.log(cartid)
        console.log(isselect)
        console.log('1111111')
        data={
            'cartid':cartid,
            'isselect':isselect,
        }


        $.get('/app01/deleteall',data,function (response) {
            console.log(response)
            if (response.status==0){
                window.open('/app01/login',target='_self')
            }else if (response.status==1){

                // console.log(isselect)
                if (response.isselect=='False'){
                    // console.log($("input[isselect^='True']"))
                    console.log(isselect)
                    // console.log(this)
                    // $('.data-con').remove()
                    // console.log($("input[isselect^='True']").parent().parent().parent())
                    $("input[isselect^='False']").parent("th").parent("tr").remove()
                    console.log('执行删除标签成功')

                }


            }
        })


    })
    
    
    
    
    
})