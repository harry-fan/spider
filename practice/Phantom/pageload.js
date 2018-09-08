
// 访问一个网页，如果成功，转交到一个图片加载

var page = require('webpage').create();
page.open('http://www.cnblogs.com/', function(status){
            console.log("Status:" + status);
            if (status == 'sucess'){
                page.render('xxx.jpg');
            }
            phantom.exit();
        });

//使用 phantomjs pageload.js 运行，实现加载
