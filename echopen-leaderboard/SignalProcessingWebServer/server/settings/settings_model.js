var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var Settings = new Schema ({
    decimation : Number,
    b_mesu : Number,
    e_mesu : Number,
    d_ramp : Number,
    e_ramp : Number,
    angle : Number,
    nb_lin : Number,
    nb_img : Number

});
module.exports = mongoose.model('Settings', Settings);