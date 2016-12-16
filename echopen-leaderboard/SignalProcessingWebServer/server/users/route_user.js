var Users = require('./user_model');
const crypto = require('crypto');

module.exports = function(app) {

    /** @brief function check if an user is authentificated before action
     @param object session : session in req.body
     @return return next if an user is authentificated */
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
        else{
            res.redirect('/users/SignIn')
        }
    }

    function isAdmin(req,res,next){
        if(req.user.admin == 1){
            next()
        }
        else{
            res.redirect('/')
        }
    }

    /** @brief check if a session is active
     @param object session : session in req.body
     @return return user if a session is active */
    app.post('/api/me', function(req, res) {
        if(req.session.user){
            res.json(req.session.user).send();
        }
        else{
            res.status(200).send({});
        }
    });

    /** @brief return all users in bdd for the indexUser html page
     @param no param
     @return return all users */
    app.get('/api/users',isAuthentificated, isAdmin, function(req, res) {
        Users.find(function(err, users) {
            (err ? res.send(err) : res.json(users));
        });
    });

    /** @brief log an user after check if email an password are correct
     @param object user : user in req.body (email and password)
     @return return user if authentification is a success*/
    app.post('/login', function(req, res) {
        var user = req.body;
        if(!validateEmail(user.email)){
            return;
        }

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

    /** @brief check name regex
     @param string name : name in req.body.name
     @return return true or false */
    function validateName(name) {
        var re = /^[a-z]+$/i;
        return re.test(name);
    }

    /** @brief check email regex
     @param string email : email in req.body.email
     @return return true or false */
    function validateEmail(email) {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }

    /** @brief create an user
     @param object user : user in req.body
     @return return user */
    app.post('/signup', function(req, res) {
        var user = req.body;

        if(!validateEmail(user.email) || !validateName(user.first_name) || !validateName(user.last_name)){
            return;
        }

        Users.create(req.body, function(err) {
            if(err){
                console.log(err)
            }
            else{
                Users.find({email: req.body.email},function(err, user) {
                    req.session.user = user[0];
                    res.json(req.session.user).send();
                });
            }
        })
    });

    /** @brief update informations of an user
     @param string id : user id in url
     @return return user updated */
    app.post('/editUser/:id',isAuthentificated, function(req, res) {
        if(req.params.id == req.session.user._id || req.session.user.admin == 1){
            var query = {'_id': req.params.id};
            var user = req.body;

            if(!validateEmail(user.email) || !validateName(user.first_name) || !validateName(user.last_name)){
                return;
            }
            Users.findOneAndUpdate(query, req.body, function (err) {
                if(err){
                    console.log(err)
                }else{

                }
                Users.find({email: user.email},function(err, user) {
                    req.session.user = user[0];
                    res.json(req.session.user).send();
                });
            });
        }
    });

    /** @brief kill a session
     @param no params
     @return return nothing */
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

    /** @brief upgrade or downgrade an user in admin or an admin in user
     @param object user : user in req.body
     @return return nothing */
    app.put('/api/user/upordown', isAuthentificated, isAdmin, function(req, res) {
        var query = {'_id':req.body._id};

        if(req.body.admin == 0){
            Users.findOneAndUpdate(query,  { $set: { admin: 1 }}, function(err) {
                (err ? res.send(err) : res.status(200).send())
            });
        }
        else{
            Users.findOneAndUpdate(query,  { $set: { admin: 0 }}, function(err) {
                (err ? res.send(err) : res.status(200).send())
            });
        }

    });

    /** @brief check if an email address exist in bdd
     @param object user : user in req.body(email)
     @return return user if email exist or an array empty if this email doesn't exist */
    app.post('/verif',function(req,res){
        var query = {'email':req.body.email};
        Users.find(query,function(err,user){
            (err ? res.send(err) : res.status(200).send(user));
        })
    });

    /** @brief delete an user
     @param string id : user id in url
     @return return nothing */
    app.delete('/api/user/:id',isAuthentificated, function(req, res) {
        if(req.params.id == req.session.user._id || req.session.user.admin == 1)
        {
            Users.remove({_id: req.params.id}, function(err) {
                (err ? res.send(err) : res.status(200).send());
            })
            req.session.destroy();
        }
    });
};