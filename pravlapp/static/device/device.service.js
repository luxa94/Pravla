(function (angular) {

    'use strict';

    angular
        .module('pravla')
        .service('deviceService', deviceService);

    deviceService.$inject = ['$http'];

    function deviceService($http) {

        return {
            find: find,
            findAll: findAll,
            add: add,
            edit: edit
        };

        function find(id) {
            return $http.get(`devices/${id}`);
        }

        function findAll() {
            return $http.get('devices');
        }

        function add(device) {
            return $http.post('devices', device);
        }

        function edit(device) {
            return $http.put('devices', device);
        }
    }
})(angular);