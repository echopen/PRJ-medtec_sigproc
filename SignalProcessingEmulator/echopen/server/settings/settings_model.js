var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var Settings = new Schema ({
    nbr_img : Number,
    length_ramp : Number,
    position_ramp : Number,
    nbrPix : Number,
    decimation : Number

});
module.exports = mongoose.model('Settings', Settings);