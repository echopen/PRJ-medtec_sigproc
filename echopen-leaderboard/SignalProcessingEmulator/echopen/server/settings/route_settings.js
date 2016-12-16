var settings = require('./settings_model');
fs = require('fs');

module.exports = function(app) {

    app.post('/api/sendSettings', function(req, res) {
        var settings = req.body
        var nbr_img,
            length_ramp,
            position_ramp,
            nbrPix,
            decimation;

        if(settings.nbr_img < 10){
            nbr_img = "0000" + settings.nbr_img
        }
        else if (settings.nbr_img < 100){
            nbr_img = "000" + settings.nbr_img
        }
        else if (settings.nbr_img < 1000){
            nbr_img = "00" + settings.nbr_img
        }
        else if (settings.nbr_img < 10000){
            nbr_img = "0" + settings.nbr_img
        }
        else{}

        if(settings.length_ramp < 10){
            length_ramp = "0000" + settings.length_ramp
        }
        else if (settings.length_ramp < 100){
            length_ramp = "000" + settings.length_ramp
        }
        else if (settings.length_ramp < 1000){
            length_ramp =  "00" + settings.length_ramp
        }
        else if (settings.length_ramp < 10000){
            length_ramp =  "0" + settings.length_ramp
        }
        else{}

        if(settings.position_ramp < 10){
            position_ramp = "0000" + settings.position_ramp
        }
        else if (settings.position_ramp < 100){
            position_ramp = "000" + settings.position_ramp
        }
        else if (settings.position_ramp < 1000){
            position_ramp = "00" + settings.position_ramp
        }
        else if (settings.length_ramp < 10000){
            position_ramp = "0" + settings.position_ramp
        }
        else{}

        if(settings.nbrPix < 10){
            nbrPix = "0000" + settings.nbrPix
        }
        else if (settings.nbrPix < 100){
            nbrPix = "000" + settings.nbrPix
        }
        else if (settings.nbrPix < 1000){
            nbrPix =  "00" + settings.nbrPix
        }
        else if (settings.nbrPix < 10000){
            nbrPix = "0" + settings.nbrPix
        }
        else{}

        if(settings.decimation < 10){
            decimation =  "0000" +  settings.decimation
        }
        else if (settings.decimation < 100){
            decimation = "000" + settings.decimation
        }
        else if (settings.decimation < 1000){
            decimation = "00" + settings.decimation
        }
        else if (settings.decimation < 10000){
            decimation = "0" + settings.decimation
        }
        else{}



        var input = nbr_img + length_ramp + position_ramp + nbrPix + decimation;

        var stream = fs.createWriteStream('/tmp/FIFOCONFIGURATION', {flags:'a'});

        stream.on('open', function() {
            console.log('Stream opened, settings sent');
            stream.write(input);
        });
    });
};
