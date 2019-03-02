// $(document).ready(function(){
//
//     var mySwiper = new Swiper(".swiper-container",{
//                     autoplay:1000,
//         // ,--每秒中轮播一次
//                     loop:true,
//         // ,--可以让图片循环轮播
//                     autoplayDisableOnInteraction:false,
//         // ,--在点击之后可以继续实现轮播
//                     pagination:".swiper-pagination",
//         // ,--让小圆点显示
//                     paginationClickable:true,
//         // ,--实现小圆点点击
//                     prevButton:".swiper-button-prev",
//         // ,--实现上一页的点击
//                     nextButton:".swiper-button-next",
//         // ,--实现下一页的点击
// 　　　　　　　　　　　　effect:"flip"
//     // --可以实现3D效果的轮播
//                 })
//
//
// })

$(function () {
    var mySwiper = new Swiper(".swiper-container",{
                    autoplay:1000,
        // ,--每秒中轮播一次
                    loop:true,
        // ,--可以让图片循环轮播
                    autoplayDisableOnInteraction:false,
        // ,--在点击之后可以继续实现轮播
                    pagination:".swiper-pagination",
        // ,--让小圆点显示
                    paginationClickable:true,
        // ,--实现小圆点点击
                    prevButton:".swiper-button-prev",
        // ,--实现上一页的点击
                    nextButton:".swiper-button-next",
        // ,--实现下一页的点击
　　　　　　　　　　　　effect:"flip"
    // --可以实现3D效果的轮播
                })
})