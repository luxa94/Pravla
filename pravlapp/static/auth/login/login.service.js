(function(angular){

    angular
        .module('pravla')
        .service('loginService', loginService);

    loginService.$inject = ['$http'];

    function loginService($http) {

        return {
            login: login
        };

        function login(user) {
            return $http.post('login', user);
        }
    }

})(angular);