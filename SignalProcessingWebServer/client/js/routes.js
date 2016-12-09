angular.module('app')
    .config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

        $routeProvider
            .when('/', {
                templateUrl: 'views/data/settings.html',
                controller: 'DataController as data'
            })
            .when('/users/SignUp', {
                templateUrl: 'views/user/SignUp.html',
                controller: 'UserController as usr'
            })
            .when('/users/data', {
                templateUrl: 'views/data/data.html',
                controller: 'DataController as data'
            })
            .when('/users/dataUser', {
                templateUrl: 'views/data/dataUser.html',
                controller: 'DataController as data'
            })
            .when('/users/listUsers', {
                templateUrl: 'views/user/indexUser.html',
                controller: 'UserController as usr'
            })
            .when('/users/SignIn', {
                templateUrl: 'views/user/SignIn.html',
                controller: 'UserController as usr'
            })
            .when('/users/EditUser', {
                templateUrl: 'views/user/EditUser.html',
                controller: 'UserController as usr'
            })
            .otherwise({
                templateUrl: 'views/data/settings.html',
                controller: 'MainController as main'
            });

        $locationProvider.html5Mode(true);

    }]);