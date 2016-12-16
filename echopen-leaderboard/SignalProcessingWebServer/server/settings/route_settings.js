var settings = require('./settings_model');
var fs = require('graceful-fs');
var plain_fs = require('fs');
var path = require('path');
var net = require('net');
var sha1 = require('sha1');
var through = require('through2');
//var clients = [];
var msg = [];

module.exports = function(app) {
    var clients = {};

    function getLeaf(node) {
        if (node.leftChild) {
            return getLeaf(node.leftChild);
        } else if (node.rightChild) {
            return getLeaf(node.rightChild);
        } else { // node must be a leaf node
            return node;
        }
    }

    function convertIntTo2BytesChar(param) {
        if (param < 128) {
            var null_char = String.fromCharCode(0);
            output = null_char + String.fromCharCode(param);
        } else {
            var null_char = String.fromCharCode(1);
            output = null_char + String.fromCharCode(param - 128);
        }
        return output;
    }

    var server = net.createServer(function(socket) {

        /* 
	    Detecting inward connections, using this method, rather than `socket.on('hello',...);` or 
	    `socket.on('connection',...);`, be cause none of them worked, despite follwing the documentation
	    */
        server.getConnections(function(err, count) {
            var id = 0; //sha1(socket.remoteAddress);
            console.log("id : ", id);
            clients[id] = {
                stream: through(),
                socket: socket,
            }
            clients[id].stream.pipe(socket);
        });
        
		/* Logging errors */
        socket.on('error', function(err) {
            console.error(err)
        });

		/* preparing data to be written into `img.txt` file as soon as data is listened */
        socket.on('data', function(data) {
            if (Ndr < Ndt) {
                for (k = 0; k < data.length; k++) {
                    Buff[Ndr + k] = data[k];
                };
                Ndr = Ndr + data.length;
            };
            if (Ndr == Ndt) {
                writingFile();
            };
        });
        //  socket.on data end

        socket.on('end', function(data) {
            console.log('CONN: disconnected');
            socket.end();
        });
		
  	  	/* 
		Writing ultrasound data requested in `img.txt` file. In a preceding time, header has been added at the top of the file. 
		The header consists in all the ulatrasound params requested
		*/
        function writingFile() {
            var wstream = fs.createWriteStream(path.join(__dirname, "../public/img.txt"), {
                flags: 'a'
            });

            for (k = 0; k < img; k++) {
                for (i = 0; i < nbPix; i++) {
                    wstream.write("\n");
                    for (j = 0; j < lin; j++) {
                        wstream.write(Buff[i + k * nbPixImg + j * nbPix] + " ");
                    }
                };
                wstream.write("\n");
            };
            wstream.end();
        };
    }).listen(9000);

    app.post('/api/sendSettings', function(req, res) {

        var id = req.query.id;

        var settings = req.body;
        var dec = settings.decimation;
        var xo = settings.b_mesu;
        var xf = settings.e_mesu;
        var dr = settings.d_ramp;
        var er = settings.e_ramp;
        var an = settings.angle;
        lin = settings.nb_lin;
        img = settings.nb_img;

        // stringed to see the input send in the console
        var dataString = dec + xo + xf + dr + er + an + lin + img;

        var decimation = convertIntTo2BytesChar(dec);
        var b_mesu = convertIntTo2BytesChar(xo);
        var e_mesu = convertIntTo2BytesChar(xf);
        var d_ramp = convertIntTo2BytesChar(dr);
        var e_ramp = convertIntTo2BytesChar(er);
        var angle = convertIntTo2BytesChar(an);
        var nb_lin = convertIntTo2BytesChar(lin);
        var nb_img = convertIntTo2BytesChar(img);
        // sending in ASCII

        var input = decimation + b_mesu + e_mesu + d_ramp + e_ramp + angle + nb_lin + nb_img;

        var calculPix = (((2 * (xf - xo) * 125) / 1.48) / dec);
        nbPix = Math.floor(calculPix);
        if (nbPix > 16384) {
            nbPix = 16384
        };
        if (img < 2) {
            img = 1
        };
        nbPixImg = nbPix * lin;
        Ndr = 0;
        Ndt = nbPix * lin * img;
        Buff = new Array([Ndt]);

        /* creation of the img.txt file */
        var wstream = fs.createWriteStream(path.join(__dirname, "../public/img.txt"));

         /* the img.txt file is dumped with with all the requested params */
		wstream.write("decimation = " + dec + "/" +
            " xo = " + xo + "/" +
            " xf = " + xf + "/" +
            " dramp = " + dr + "/" +
            " eramp = " + er + "/" +
            " angle = " + an + "/" +
            " nb lign = " + lin + "/" +
            " nb img = " + img);


        /* requested params are sent to the hardware */ 						  
        if (clients[0]) {
            clients[0].stream.write(input);
        }
        console.log("end writing header");
        res.end();
    });
    console.log("lets go port 9000");
};