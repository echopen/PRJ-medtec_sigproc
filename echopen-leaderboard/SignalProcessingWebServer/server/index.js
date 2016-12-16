var mongoose = require('mongoose');
var bodyParser = require('body-parser');
var session = require('express-session');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var app = express();
const MongoStore = require('connect-mongo')(session);

app.use(cookieParser());
app.use(session({
    secret: 'ssshhhhh',
    store: new MongoStore ({ mongooseConnection: mongoose.connection }),
    proxy: true,
    resave: true,
    saveUninitialized: true
}));

app.use(bodyParser.json({limit:'50mb'}));
app.use(bodyParser.urlencoded({ extended: true }));


mongoose.connect('mongodb://localhost/echopen');

app.use(function(req, res) {
    req.next();
});

app.use(express.static(path.join(__dirname + '/../client')));

require('./routes')(app);


app.listen(3700);
console.log("Let's go on port ", process.env.PORT || 3700);
