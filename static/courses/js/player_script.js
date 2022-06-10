let videoList = document.querySelectorAll('.video-list-container .list');

videoList.forEach(vid =>{
   vid.onclick = () =>{
      videoList.forEach(remove =>{remove.classList.remove('active')});
      vid.classList.add('active');
      let src = vid.querySelector('.list-video').src;
      let title = vid.querySelector('.list-title').innerHTML;
      let descr = vid.querySelector('.list-descr').innerHTML;
      document.querySelector('.main-video-container .main-video').src = src;
      document.querySelector('.main-video-container .main-video').play();
      $('.main-video-descr').fadeOut(300);
      setTimeout(change_vid_descr, 300)
      function change_vid_descr(){
         document.querySelector('.main-video-container .main-vid-title').innerHTML = title;
         document.querySelector('.main-video-container .main-vid-descr').innerHTML = descr;
      }
      $('.main-video-descr').fadeIn(300);
   };
});

$(document).ready(function(){
   $('video').bind('contextmenu',function() { return false; });
});