(function(angular) {

    'use strict';

    angular
        .module('pravla')
        .service('registerService', registerService);

    registerService.$inject = ['$http'];

    function registerService($http) {

        var API_URL = "http://localhost:8000/users";

        return {
            register: register
        };

        function register(user) {
            return $http.post('/users', user);
        }
    }
})(angular);