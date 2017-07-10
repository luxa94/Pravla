(function (angular) {

    'use strict';

    angular
        .module('pravla')
        .service('ruleService', ruleService);

    ruleService.$inject = ['$http'];

    function ruleService($http) {

        return {
            findAll: findAll,
            add : add
        };

        function findAll() {
            return $http.get('rules');
        }

        function add(rule) {
            return $http.post('rules', rule);
        }
    }
})(angular);