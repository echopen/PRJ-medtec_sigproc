var Data = require('./data.model'),
    fs = require('fs'),
    bite_size = 2049,
    readbytes = 0,
    file,
    godata = [],
    img = [],
    nbr = 1,
    nbrimg = 0,
    i = 0;

module.exports = function(app) {

    var _this = this;

    app.put('/api/SetNbrImg',function(req, res){
        nbr = req.body.nbr_img
    });

    app.get('/api/Data',function(req, res){
        Data.find({idUser: req.session.user._id},function(err, data) {
            (err ? res.send(err) : res.json(data));

        });
    });



    app.get('/api/data', function(req, res) {
        $http.get('/datasend')
            .then(function (res) {
                _this.data = res.data;
            });
        (err ? res.send(err) : res.json(_this.data));
    });

    app.get('/api/receive',function(req, res){

        fs.open('/tmp/FIFOSENDER', 'r', function(err, fd) { file = fd; readsome(); });

        function readsome() {
            var stats = fs.fstatSync(file);
            if(stats.size<readbytes+1) {
                if(nbrimg < nbr )
                {
                console.log('Hehe I am much faster than your writer..! I will sleep for a while, I deserve it!');
                setTimeout(readsome, 0.1);
                }
                else {
                    console.log("it is the end of the transmission")
                    res.json(godata);
                    godata = [];
                    nbrimg = 0;
                    return;
                }
            }
            else {
                fs.read(file, new Buffer(bite_size), 0, bite_size, readbytes, processsome);
            }
        }

        function processsome(err, bytecount, buff) {
            console.log('Read', bytecount, 'and will process it now.');
            if(i < 128)
            {
                if( i == 127) {
                    img.push(buff.toString('utf-8', 0, bytecount));
                    godata.push(img);
                    img = [];
                    nbrimg++;
                    i = 0;
                }
                else{
                    img.push(buff.toString('utf-8', 0, bytecount));
                    i++;
                }
            }
            readbytes+=bytecount;
            process.nextTick(readsome);
        }
    });

    app.post('/api/sendData',function(req, res){
        Data.create(req.body, function(err) {
            (err ? res.send(err) : res.status(200).send())
        });
    });

    app.get('/api/:id/sendImages',function(req,res){
        Data.findById(req.params.id,function(err, datum) {
            var images = datum.images,
                i = 0,
                file = fs.createWriteStream("server/public/images.txt");

            while(i < images.length){
                file.write(images[i] + "\n\n");
                i++;
            }
            file.close();
        });
    });

    app.get('/images',function(req, res){
        res.download("server/public/images.txt", "images.txt", function(err){
            if(err){
                console.log(err)
            }
        });
    });
};

