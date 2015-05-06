/*! Responsive Menu */
// http://tympanus.net/codrops/2013/05/08/responsive-retina-ready-menu/

// The function to change the class
var changeClass = function (r,className1,className2) {
  var regex = new RegExp("(?:^|\\s+)" + className1 + "(?:\\s+|$)");
  if( regex.test(r.className) ) {
    r.className = r.className.replace(regex,' '+className2+' ');
    }
    else{
    r.className = r.className.replace(new RegExp("(?:^|\\s+)" + className2 + "(?:\\s+|$)"),' '+className1+' ');
    }
    return r.className;
};
//  Creating our button in JS for smaller screens
var menuElements = document.getElementById('site-nav');
menuElements.insertAdjacentHTML('afterBegin','<button type="button" role="button" id="menutoggle" class="navtoogle navicon-lines-button x" aria-hidden="true"><span class="navicon-lines"></span>menu</button>');

//  Toggle the class on click to show / hide the menu
document.getElementById('menutoggle').onclick = function() {
  changeClass(this, 'navtoogle active', 'navtoogle');
};
// http://tympanus.net/codrops/2013/05/08/responsive-retina-ready-menu/comment-page-2/#comment-438918
document.onclick = function(e) {
  var mobileButton = document.getElementById('menutoggle'),
    buttonStyle =  mobileButton.currentStyle ? mobileButton.currentStyle.display : getComputedStyle(mobileButton, null).display;

  if(buttonStyle === 'block' && e.target !== mobileButton && new RegExp(' ' + 'active' + ' ').test(' ' + mobileButton.className + ' ')) {
    changeClass(mobileButton, 'navtoogle active', 'navtoogle');
  }
};

/*! Plugin options and other jQuery stuff */

// FitVids options
$(function() {
    $("article").fitVids();
});
