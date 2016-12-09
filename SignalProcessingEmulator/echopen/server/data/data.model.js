var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var Data = new Schema ({
    created : String,
    idUser : String,
    images : [{}]
});
module.exports = mongoose.model('Data', Data);