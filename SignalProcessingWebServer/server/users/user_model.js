var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var User = new Schema ({
    first_name : String,
    last_name : String,
    email : String,
    password : String,
    confirm_password : String,
    admin : Number
});
module.exports = mongoose.model('User', User);