var settings = require('./settings_model');
var fs = require('graceful-fs');
var net = require('net');
//var clients = [];
var msg = [];

module.exports= function(app){
net.createServer(function (socket) {

      // Identify this client
    //  socket.name = socket.remoteAddress + ":" + socket.remotePort 
      // Put this new client in the list
    //  clients.push(socket);

      socket.on('error',function(err){ console.error(err)});
       
      // Handle incoming messages from clients.
      socket.on('data', function (data) {

        if(Ndr<Ndt){
            for(k=0;k<data.length;k++){
                Buff[Ndr+k]=data[k];	
            };
            Ndr = Ndr + data.length;
        };
        if(Ndr == Ndt){ writingFile();};

      }); //  socket.on data end

      function writingFile(){
        grille = new Array();
        for(k = 0; k < img ; k++){
            for(i = 0; i < nbPix; i++){
                grille[i + k * nbPixImg] = new Array();
                fs.appendFile('./public/img.txt', '\n');
                    for(j = 0 ; j < lin; j++){
                        grille[i + k * nbPixImg][j]= Buff[k * nbPixImg + i + j * nbPix];
                        if(!isNaN(grille[i + k * nbPixImg][j])){
                            fs.appendFile('./public/img.txt', grille[i + k * nbPixImg][j] + " ");
                        };
                      };
            };
            fs.appendFile('./public/img.txt', '\n');
        };
      };


      // Remove the client from the list when it leaves
     /* socket.on('end', function () {
        clients.splice(clients.indexOf(socket), 1);
        console.log(socket.name + " left the Node Js Server.\n");
      });
      */
  

    app.post('/api/sendSettings', function(req, res) {

        var settings = req.body;
        var dec = settings.decimation;
        var xo = settings.b_mesu;
        var xf = settings.e_mesu;
        var dr = settings.d_ramp;
        var er = settings.e_ramp;
        var an = settings.angle;
        var lin = settings.nb_lin;
        var img = settings.nb_img;   
        // stringed to see the input send in the console
        var dataString = dec + xo + xf + dr + er + an + lin + img;
        console.log(dataString);              
          
        var decimation = String.fromCharCode(dec);
        var b_mesu = String.fromCharCode(xo);
        var e_mesu = String.fromCharCode(xf);
        var d_ramp = String.fromCharCode(dr);
        var e_ramp = String.fromCharCode(er);
        var angle = String.fromCharCode(an);
        var nb_lin= String.fromCharCode(lin);
        var nb_img = String.fromCharCode(img);
        // sending in ASCII
        var input = decimation + b_mesu + e_mesu + d_ramp + e_ramp + angle + nb_lin + nb_img;
     
        var calculPix = (((2*(xf-xo)*125)/1.48)/dec);
        nbPix = Math.floor(calculPix);
        if(nbPix > 16384){ nbPix = 16384};
        if(img <2){img =1};
        nbPixImg = nbPix*lin;
        Ndr = 0;
        Ndt = nbPix * lin * img;
        Buff = new Array([Ndt]);
    
          // creation of the img.txt file 
          fs.writeFile("./public/img.txt", "", function(err){
              if(err){console.log(err)};
                console.log("the file was saved");
          });
          // writing header with settings
          fs.appendFile("./public/img.txt", "decimation = " + dec+ "/"
                          + " xo = "+ xo + "/"
                          + " xf = "+ xf + "/"
                          + " dramp = "+ dr + "/"
                          + " eramp = "+ er + "/"
                          + " angle = "+ an + "/"
                          + " nb lign = "+ lin + "/"
                          + " nb img = "+ img);
          // sending the input to the socket
          socket.write(input);
          res.end();
      }); //  app.post(..sendSettings) end
    }).listen(9000);
      
      console.log("lets go port 9000");

};
