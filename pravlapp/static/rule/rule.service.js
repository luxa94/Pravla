(function (angular) {

    'use strict';

    angular
        .module('pravla')
        .service('ruleService', ruleService);

    ruleService.$inject = ['$http'];

    function ruleService($http) {

        return {
            findAll: findAll
        };

        function findAll() {
            return $http.get('rules');
        }
    }
})(angular);