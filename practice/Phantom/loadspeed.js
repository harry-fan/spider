//计算一个网页的加载速度

var page = require('webpage').create();
var system = require('system');
var t, address;
if (system.args.length === 1){
    console.log('Usage: loadspeed.js <some URL>');
    phantom.exit()
}
t = Date.now();
address = system.args[1];
page.open(address, function(status){
    if(status !== 'sucess'){
        console.log('FAIL to load the address');
    }else{
        t = Date.now() - t;
        console.log('Loading ' + system.args[1]);
        console.log('Loading time' + t + ' msec');
    }
    phantom.exit();
});

//phantomjs loadspeed.js http://www.cnblogs.com
