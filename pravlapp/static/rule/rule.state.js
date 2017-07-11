(function(angular) {

    'use strict';

    angular
        .module('pravla')
        .config(ruleState);

    function ruleState($stateProvider) {
        $stateProvider
            .state('rule', {
                url: '/rule/:id',
                templateUrl: 'static/rule/rule.html',
                controller: 'RuleCtrl',
                controllerAs: 'ruleVm'
            });
    }
})(angular);