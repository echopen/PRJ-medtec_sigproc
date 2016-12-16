angular.module('app')
    .controller('MainController', function($scope, $http, $location) {
        _this = this;
        this.user;
        this.session = "ko";
        this.login = {status: ''}

        this.signout = function() {
            $http.post('/logout')
                .then(function (res) {
                    $scope.main.session = "ko";
                    $scope.main.user = {};
                    $location.path('/users/SignIn')
                });
        };

    }).controller('UserController', function($scope, $http, md5, $location) {
    var _this = this;

    this.getUser = function () {
        $http.get('/api/user')
            .then(function (res) {
                _this.user = res.data[0];
            });
    };

    this.signin = function() {
        var hashedPassword = md5.createHash(this.user.password);
        this.user.password = hashedPassword;
        $http.post('/login', this.user)
            .then(function (res) {
                $scope.main.user = res.data;
                $scope.login = {status: 'ok'};
                $scope.main.session = "ok";
                $location.path('/');
            },function (res){
                $scope.login = {status: 'ko'} ;
            });
    };

    this.sendUser = function() {
        if (!this.newuser || !this.newuser.first_name || !this.newuser.last_name || !this.newuser.email || !this.newuser.password || !this.newuser.confirm_password)
        {
            $scope.SignUpEmpty = {status: 'ko'};
            return;
        }
        else{
            $scope.SignUpEmpty = {status: 'ok'};
        }

        if(this.newuser.password != this.newuser.confirm_password)
        {
            $scope.SignUpPassword = {status: 'ko'};
            return;
        }
        else {
            $scope.SignUpPassword = {status: 'ok'};
        }

        var hashedPassword = md5.createHash(this.newuser.confirm_password);
        this.newuser.confirm_password = hashedPassword;
        var hashedPassword = md5.createHash(this.newuser.password);
        this.newuser.password = hashedPassword;
        this.newuser.admin = 0;

        $http.post('/signup', this.newuser)
            .then(function (res) {
                $scope.main.user = res.data;
                this.newuser = {};
                $scope.login = {status: 'ok'} ;
                $scope.main.session = "ok";
                $location.path('/')
            });

    };

    $http.post('/api/me')
        .then(function (res) {
            if (res.data._id)
            {
                _this.user = res.data
                $scope.main.session = "ok"
            }
        });

}).controller('DataController', function($scope, $http, $location) {
    var _this = this

    this.getData =function(){
        if($scope.main.user == undefined) {

        }else
        {
            $http.get('/api/Data',$scope.main.user)
                .then(function (res) {
                    console.log(res.data);
                    _this.datas = res.data;
                });
        }
    };

    this.getData();

    this.sendData = function(img){
        this.data = {};
        var date = new Date();
        this.data.created = date;
        this.data.idUser = $scope.main.user._id;
        this.data.images = img;
        $http.post('/api/sendData', this.data)
        $location.path('/users/data')
    }

    this.sendSettings = function(){
        if(!this.settings.nbr_img){
            this.settings.nbr_img = 1;
        }

        if(!this.settings.length_ramp){
            this.settings.length_ramp = 100;
        }

        if(!this.settings.position_ramp){
            this.settings.position_ramp = 0;
        }

        if(!this.settings.nbrPix){
            this.settings.nbrPix = 2049;
        }

        if(!this.settings.decimation){
            this.settings.decimation = 1;
        }

        $http.post('/api/sendSettings', this.settings);
        $http.put('/api/SetNbrImg', this.settings);
        $http.get('/api/receive').then(function(res){
            $scope.data.sendData(res.data)


        })
    }
});
