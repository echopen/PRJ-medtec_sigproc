angular.module('app')
    .controller('MainController', function($scope, $http, $location) {
        _this = this;
        this.user;
        this.user2;
        this.session = "ko";
        this.login = {status: ''};

        /** @brief checks if a session is active
         @param no param
         @return set main user*/
        $http.post('/api/me')
            .then(function (res) {
                if (res.data._id)
                {
                    $scope.main.user = res.data;
                    $scope.main.user2 = res.data;
                    $scope.main.login = {status: 'ok'}
                    $scope.main.session = "ok"
                }
                else{
                    $location.path('/users/SignIn')
                }
            });

        /** @brief set main user2 for EditUser and dataUser page html
         @param objet user : current user or requested
         @return set main user2*/
        this.setuser2 = function(user){
            $scope.main.user2 = user;
        };

        /** @brief close the active session
         @param no param
         @return set main user at {}*/
        this.signout = function() {
            $http.post('/logout')
                .then(function (res) {
                    $scope.main.session = "ko";
                    $scope.main.user = {};
                    $location.path('/users/SignIn')
                });
        };

    })
