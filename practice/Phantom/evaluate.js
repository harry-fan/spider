// evaluate方法可以返回一个对象，返回值仅限于对象

var url = 'http://www.cnblogs.com';
var page = require('webpage').create();
page.open(url, function(status){
    var title = page.evaluate(function(){
        return document.title;
    });
    console.log('page title is:' + title);
    phantom.exit();
})
