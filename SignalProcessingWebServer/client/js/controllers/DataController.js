angular.module('app')
    .controller('DataController', function($scope, $http, $location, $route, $window) {
        var _this = this;
        this.process = "ko";
		
		function checkSanityData(settings){
			if(constructBool(settings)){
				$scope.data.process = 'ko';
				console.log("ko");
			}
			else{
				$scope.data.process = 'ok';
				console.log("ok");
			}
		};
		
		function constructBool(settings){
			return (settings.decimation != 1 && settings.decimation!=8)|| 
			(settings.b_mesu<0||settings.b_mesu>97) || 
			(settings.e_mesu<1||settings.e_mesu>194) ||
			(!settings.e_mesu) ||
			(settings.d_ramp<0||settings.d_ramp>255) ||
			(settings.e_ramp<1||settings.e_ramp>255) ||
			(!settings.e_ramp) ||	
			(settings.angle<1||settings.angle>180) ||
			(settings.nb_lin<1||settings.nb_lin>255) ||	
			(settings.nb_img<1||settings.nb_img>50);
		};
 
        /** @brief set process variable for the time between the sendSettings and getData functions
         @param no param
         @return no return */
        this.setProcess = function(){
			checkSanityData(this.settings);
        };

        /** @brief set all data in the datas variable for display this in data page html
         @param no param
         @return set datas variable*/
        this.getData = function(){
            $http.get('/api/Data',$scope.main.user2)
                .then(function (res) {
                    _this.datas = res.data;
                });
        };
        if($scope.main.user != undefined){
            this.getData();
        }

        /** @brief recovered the data and save it in dbb
         @param object img : image recovered of the c server
         @return redirect to data.html */
        this.sendData = function(img){
            this.data = {};
            var date = new Date();
            this.data.created = date.toUTCString();
            this.data.idUser = $scope.main.user._id;
            this.data.images = img;
            $http.post('/api/sendData', this.data);
            $location.path('/users/data')
        };

        /** @brief recovered the settings from the settings page html and send it on the c server
         @param object settings : all the parameters entered by the user or set it by default
         @return no return */
        this.sendSettings = function(){
            $http.post('/api/sendSettings', this.settings);
            $http.get('/api/receive').then(function(res){
                $scope.data.sendData(res.data)
            })
        };

        /** @brief download image request in the client user
         @param object datum : image request
         @return no return */
        this.sendImages = function(datum){
            $http.get('/api/'+ datum._id + '/sendImages', datum).then(
                $window.open("http://92.243.29.92:3700/images/"+datum._id)
            ).then($route.reload())};
	
        /** @brief delete data
         @param string id : image._id
         @return no return */
        this.removedata = function(id) {
            $http.delete('/api/data/' + id);
            $route.reload();
        };
    });
