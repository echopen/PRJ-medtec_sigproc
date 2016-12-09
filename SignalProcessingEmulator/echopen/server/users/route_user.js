var Users = require('./user_model');
const crypto = require('crypto');

module.exports = function(app) {

    app.use(function(req,res,next){
        if(req.session && req.session.user)
        {
            Users.findOne({email: req.session.user.email},function(err,user){
                if(user){
                    req.user = user;
                }
                next()
            });
        }else{
            next()
        }
    })
    function isAuthentificated(req,res,next){
        if(req.user){
            next()
        }
    }

    app.post('/api/me', function(req, res) {
        if(req.session.user){
            res.json(req.session.user).send();
        }
        else{
            res.status(200).send({});
        }
    });

    app.get('/api/users',isAuthentificated, function(req, res) {
        Users.find(function(err, users) {
            (err ? res.send(err) : res.json(users));
        });
    });

    app.get('/api/user',isAuthentificated, function(req, res) {
        Users.find({email: req.body.email},function(err, user) {
            (err ? res.send(err) : res.json(user));
        });
    });

    app.get('/api/users/:id',isAuthentificated, function(req, res) {
        Users.findById(req.params.id,function(err, user) {
            (err ? res.send(err) : res.json(user));
        });
    });

    app.post('/login', function(req, res) {
        Users.find({email: req.body.email},function(err, user) {
            if (user.length == 0){
                res.status(400).send("wrong login");
            }
            else{
                if (user[0].password !=  req.body.password){
                    res.status(400).send("wrong password")
                }
                else {
                    sess=req.session;
                    req.session.user = user[0];
                    res.json(req.session.user).send();
                }
            }
        });
    });

    app.post('/signup', function(req, res) {
        var user = req.body
        Users.create(req.body, function(err) {
            (err ? res.send(err) : res.status(200).send(user))
        });
    });

    app.post('/api/users/:id',isAuthentificated, function(req, res) {
        if(req.params.id == req.session.user._id || req.session.user.admin == 1) {
            Users.update({_id: req.params.id}, req.body, function (err, user) {
                if (err) {
                    res.send(err)
                }
                else {
                    res.json(user)
                    req.session.user = user[0];
                }
            });
        }
    });

    app.post('/logout',function(req,res){

        req.session.destroy(function(err){
            if(err){
            }
            else
            {
                res.redirect('/');
            }
        });

    });

    app.delete('/api/user/:id',isAuthentificated, function(req, res) {
        if(req.params.id == req.session.user._id || req.session.user.admin == 1)
        {
            Users.remove({_id: req.params.id}, function(err) {
                (err ? res.send(err) : res.status(200).send());
            });
        }
    });
};