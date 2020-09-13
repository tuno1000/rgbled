'use strict';

const log4js = require('log4js');

log4js.configure({
appenders : {
system : {type : 'file', filename : 'textToRgbLed.log'}
},
categories : {
default : {appenders : ['system'], level : 'debug'},
}
});
const logger = log4js.getLogger('system');

try{

	var http = require('http');
	var url = require('url');

	var server = http.createServer(function(req, res) {

  		var url_parse = url.parse(req.url, true);
 
  		logger.debug(url_parse.query.text);
  		logger.debug(url_parse.query.rgb);
  		logger.debug(url_parse.query.viewTime);
 
  		console.log(url_parse.query.text);
  		console.log(url_parse.query.rgb);
  		console.log(url_parse.query.viewTime);

  		const execSync = require('child_process').execSync;
  		const exec = require('child_process').exec;

  		logger.debug(req.url);
  		console.log(req.url);

  		switch (true) {
    			case /\/viewTextToRgbLed\?/.test(req.url):
      			var text = url_parse.query.text;
      			text = text.replace('"','_',text);
      			text = text.replace(' ','_',text);
      			execSync('sh /data/nodejs/viewText.sh "' + text  + '" ' + url_parse.query.viewTime + ' ' + url_parse.query.rgb);
      			res.writeHead(302, {
         			'Location': 'http://192.168.1.201/'
      			});
      			break;
    		case /\/viewNewsToRgbLed/.test(req.url):
      			exec('/data/nodejs/viewYahooNews.sh ' + url_parse.query.rgb);
      			res.writeHead(302, {
         			'Location': 'http://192.168.1.201/'
      			});
      			break;
    		case /\/stopNews/.test(req.url):
      			exec('sh /data/nodejs/stop_viewYahooNews.sh');
      			res.writeHead(302, {
         			'Location': 'http://192.168.1.201/'
      			});
      			break;
    		case /\/welcomeMsg/.test(req.url):
      			var text = url_parse.query.text;
      			text = text.replace('"','_',text);
      			text = text.replace(' ','_',text);
      			exec('/usr/bin/python3 /root/py/welcomeMsg.py "' + text  + '" ' + url_parse.query.rgb + " &");
      			res.writeHead(302, {
         			'Location': 'http://192.168.1.201/'
      			});
      			break;
    		case /\/stopwelcomeMsg/.test(req.url):
      			exec('sh /data/nodejs/stop_welcomeMsg.sh');
      			res.writeHead(302, {
         			'Location': 'http://192.168.1.201/'
      			});
      			break;
    		case /\/EMERGENCY/.test(req.url):
      			exec('/root/rpi-rgb-led-matrix/examples-api-use/demo --led-no-hardware-pulse --led-rows=16 --led-cols=32 -D 1 -c 2 -t 10 /var/tmp/emergency.ppm');
      			res.writeHead(302, {
         			'Location': 'http://192.168.1.201/'
      			});
      			break;
  		}

  		res.end();
	}).listen(8080);
} catch (err) {
	logger.debug(err.name + ': ' + err.message);
	process.exit(-1);
}
