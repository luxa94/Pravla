(function (angular) {

    'use strict';

    angular
        .module('pravla')
        .service('deviceService', deviceService);

    deviceService.$inject = ['$http'];

    function deviceService($http) {

        return {
            findAll: findAll
        };

        function findAll() {
            return $http.get('devices');
        }
    }
})(angular);