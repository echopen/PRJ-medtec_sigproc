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
            .when('/users/SignIn', {
                templateUrl: 'views/user/SignIn.html',
                controller: 'UserController as usr'
            })
            .when('/download', {
                templateUrl: 'views/data/download.html',
                controller: 'DataController as data'
            })
            .otherwise({
                templateUrl: 'views/data/settings.html',
                controller: 'MainController as main'
            });

        $locationProvider.html5Mode(true);

    }]);