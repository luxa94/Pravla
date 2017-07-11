(function (angular) {

    'use strict';

    angular
        .module('pravla')
        .service('ruleService', ruleService);

    ruleService.$inject = ['$http'];

    function ruleService($http) {

        return {
            find: find,
            findAll: findAll,
            add : add,
            edit: edit
        };

        function find(id) {
            return $http.get(`rules/${id}`);
        }

        function findAll() {
            return $http.get('rules');
        }

        function add(rule) {
            return $http.post('rules', rule);
        }

        function edit(rule) {
            return $http.put(`rules/${rule.id}`, rule);
        }
    }
})(angular);