(function(angular){

    'use strict';

    angular
        .module('pravla')
        .controller('DashboardCtrl', DashboardCtrl);

    DashboardCtrl.$inject = ['$state', 'deviceService', 'ruleService'];

    function DashboardCtrl($state, deviceService, ruleService) {

        var dashboardVm = this;

        dashboardVm.devices = [];
        dashboardVm.rules = [];

        activate();

        function activate() {
            deviceService.findAll()
                .then(function (response) {
                    dashboardVm.devices = response.data;
                    return ruleService.findAll();
                })
                .then(function(response) {
                    dashboardVm.rules = response.data;
                })
                .catch(function(error) {
                    alert("Server error");
                });
        }
    }
})(angular);