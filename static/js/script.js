$(function(){
    // 개별메뉴 
    $('nav>ul>li').mouseenter(function(){
        $('.submenu').slideDown(100); //0.1초
    });
    $('nav>ul>li').mouseleave(function(){
        $('.submenu').slideUp(100);
    });
    // 좌우슬라이드 (변수,증감연산자,비교연산자,if문)
        var x = 0; 
        setInterval (function(){
            if(x < 2) {
                x++;
            } else {   
                x = 0;
            }
            var sp = x * (-1200)+'px';
                    // 0 * -1200
                    // 1 * -1200
                    // 2 * -1200 
            $('.slideList').animate({left:sp},400); // 0.4
            console.log(x);
        },3000); // 3초

    // 텝메뉴
    $('h2').on('click',function(){
        $(this).addClass('on')
        .siblings('h2').removeClass('on');
    });


    // 레이어팝업 

    $('.layerPopup').on('click',function(e){
        e.preventDefault(); // 링크차단메서드
        $('#popup').fadeIn();
    });
    $('.close').on('click',function(){
        $('#popup').fadeOut();
    });

    //.mouseenter -> 마우스가 선택한 요소에 들어왔을때
    // setInterval : 일정시간동안 반복하여 실행
// .addClass -> 클래스생성
// .removeClass -> 클래스 삭제 
// .siblings() -> 형제요소 선택 
// .on -> 이벤트 등록 메서드 




});