angular.module('app')
    .controller('UserController', function($scope, $http, md5, $location, $route) {
        var _this = this;

        /** @brief check name regex
         @param string name : name in req.body.name
         @return return true or false */
        function validateName(name) {
            var re = /^[A-Za-z]+$/;
            return re.test(name);
        }

        /** @brief check email regex
         @param string email : email in req.body.email
         @return return true or false */
        function validateEmail(email) {
            var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(email);
        }

        /** @brief set all users in users variable for display this in indexUser.html
         @param no param
         @return set user users*/
        this.getUsers = function () {
            $http.get('/api/users')
                .then(function (res) {
                    _this.users = res.data;
                });
        };

        this.getUsers();

        /** @brief set session user after authentification
         @param object user : user.email an user.password
         @return set main user, main user2 and redirect on homepage and crypt the password */
        this.signin = function() {
            var hashedPassword = md5.createHash(this.user.password);

            if(!validateEmail(this.user.email)){
                $scope.loginformat = {status: 'ko'};
                return;
            }
            else {
                $scope.loginformat = {status: 'ok'};
            }

                this.user.password = hashedPassword;
                $http.post('/login', this.user)
                    .then(function (res) {
                        $scope.main.user = res.data;
                        $scope.main.user2 = res.data;
                        $scope.login = {status: 'ok'};
                        $scope.main.session = "ok";
                        $location.path('/');
                    }, function () {
                        $scope.login = {status: 'ko'};
                    });
        };

        /** @brief create an user and save it in dbb
         @param object user : user
         @return set main user, main user2 and redirect on homepage and crypt the password*/
        this.sendUser = function() {
            var hashedPassword;
            var newuser = this.newuser;
            console.log(!validateEmail(newuser.email))
            console.log(!validateName(newuser.first_name))
            console.log(!validateName(newuser.last_name))


            if (!this.newuser || !this.newuser.first_name || !this.newuser.last_name || !this.newuser.email || !this.newuser.password || !this.newuser.confirm_password){
                $scope.SignUpEmpty = {status: 'ko'};
                return;
            }
            else{
                $scope.SignUpEmpty = {status: 'ok'};
            }

            if(!validateEmail(newuser.email) || !validateName(newuser.first_name) || !validateName(newuser.last_name)){
                $scope.SignUpformat = {status: 'ko'};
                console.log($scope.SignUpformat)
                return;
            }
            else{
                $scope.SignUpformat = {status: 'ok'};
            }

            if(this.newuser.password != this.newuser.confirm_password)
            {
                $scope.SignUpPassword = {status: 'ko'};
                return;
            }
            else {
                $scope.SignUpPassword = {status: 'ok'};
            }

            $http.post('/verif', this.newuser).then(function(res){
                var user = res.data;

                if(user.length == 0){
                    $scope.EmailExist = {status: 'ok'};
                    hashedPassword = md5.createHash(newuser.confirm_password);
                    newuser.confirm_password = hashedPassword;
                    hashedPassword = md5.createHash(newuser.password);
                    newuser.password = hashedPassword;
                    newuser.admin = 0;

                    $http.post('/signup', newuser).then(function(res){
                        $scope.main.user = res.data;
                        $scope.main.user2 = res.data;
                        $scope.login = {status: 'ok'} ;
                        $scope.main.session = "ok";
                        $location.path('/');
                        $route.reload();
                    });
                }
                else{
                    $scope.EmailExist = {status: 'ko'};
                    return;
                }
            });
        };

        /** @brief edit an user and save it in dbb
         @param object user : user
         @return set main user, main user2 and redirect on homepage and crypt the password*/
        this.editUser = function(user_id) {


            if (!this.us.first_name){
                this.us.first_name = $scope.main.user.first_name;
                $scope.editformat = {status: 'ok'}
            }
            else if(!validateName(this.us.first_name)){
                $scope.editformat = {status: 'ko'};
                return;
            }
            else{
                $scope.editformat = {status: 'ok'};
            }

            if (!this.us.last_name) {
                $scope.editformat = {status: 'ok'}
                this.us.last_name = $scope.main.user.last_name;
            }
            else if(!validateName(this.us.first_name)){
                $scope.editformat = {status: 'ko'}
                return;
            }
            else{
                $scope.editformat = {status: 'ok'}
            }

            if (!this.us.email){
                $scope.editformat = {status: 'ok'}
                this.us.email = $scope.main.user.email;
            }
            else if(!validateEmail(this.us.email)){
                $scope.editformat = {status: 'ko'}
                return;
            }
            else{
                $scope.editformat = {status: 'ok'}
            }

            if (!this.us.password){
                this.us.password = $scope.main.user.password
            }
            else{
                var hashedPassword = md5.createHash(this.us.password);
                this.us.password = hashedPassword;
            }

            if (!this.us.confirm_password){
                this.us.confirm_password = $scope.main.user.confirm_password
            }
            else{
                var hashedPassword = md5.createHash(this.us.confirm_password);
                this.us.confirm_password = hashedPassword;
            }

            $http.post('/editUser/' + user_id, this.us)
                .then(function (res) {
                    $scope.login = {status: 'ok'};
                    $scope.main.session = "ok";
                });
            $scope.main.user = this.us;
            $scope.main.user2 = this.us;
            this.us = {};
        };

        /** @brief Upgrade an user on admin or downgrade on user
         @param object user : user
         @return no return */
        this.Upordown = function(user){
            $http.put('/api/user/upordown', user);
            $route.reload();
        };

        /** @brief delete an user
         @param string id : user._id
         @return no return */
        this.removeUser = function(id) {
            if($scope.main.user == $scope.main.user2){
                $scope.main.user = {};
                $scope.main.user2 = {};
                $scope.main.login = {status: 'ko'}
                $scope.main.session = "ko";
                $http.delete('/api/user/' + id);
                $location.path('/users/SignUp');
                $route.reload();
            }
            else{
                $scope.main.user2 = {};
                $route.reload();
            }
        };
    })