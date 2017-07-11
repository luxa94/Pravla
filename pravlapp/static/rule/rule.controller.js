(function(angular) {

    'use strict';

    angular
        .module('pravla')
        .controller('RuleCtrl', RuleCtrl);

    RuleCtrl.$inject = ['$stateParams', 'ruleService'];

    function RuleCtrl($stateParams, ruleService) {

        var ruleVm = this;

        ruleVm.rule = {};

        ruleVm.edit = edit;

        activate();

        function activate() {
            ruleService.find($stateParams.id)
                .then(function(response) {
                    ruleVm.rule = response.data;
                }).catch(function(error) {
               console.log("Server error");
            });
        }

        function edit() {
            ruleService.edit(ruleVm.rule)
                .then(function(response) {
                    ruleVm.rule = response.data;
                }).catch(function(error) {
                console.log("Server error");
            });
        }

    }
})(angular);