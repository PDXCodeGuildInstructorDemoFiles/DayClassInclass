'use strict';
var timer;
var counter = 3000;
$('img').click( function () {
    var img = $(this);
    if (img.attr('class') === 'mole') {
        img.attr('src', 'hole.jpg').toggleClass('mole').toggleClass('hole');
    }
});

$('img').on('dragstart', function(event) { event.preventDefault(); });

$('.begin').click( function() {
    timer = setInterval(gametime, counter)
});
// var myFunction = function(){
//     clearInterval(interval);
//     counter *= 10;
//     interval = setInterval(myFunction, counter);
// }
// var interval = setInterval(myFunction, counter);
function gametime () {

    var moleCount = $('.whack-grid').children('.hole');
    if (moleCount.length > 0) {
      var currentHoleVal = Math.floor((Math.random() * moleCount.length));
      var currentHole = $('#' + moleCount[currentHoleVal].id);
      console.log(moleCount[currentHoleVal]);
      currentHole.attr('src', 'mole.jpg').toggleClass('mole').toggleClass('hole');
      clearInterval(timer);
      counter -= counter * (.05);
      timer = setInterval(gametime, counter);
    } else {
      clearInterval(timer);
      alert('You lose');
  }
    }
