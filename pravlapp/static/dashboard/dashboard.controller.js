(function (angular) {

    'use strict';

    angular
        .module('pravla')
        .controller('DashboardCtrl', DashboardCtrl);

    DashboardCtrl.$inject = ['$state', 'deviceService', 'ruleService'];

    function DashboardCtrl($state, deviceService, ruleService) {

        var dashboardVm = this;

        dashboardVm.devices = [];
        dashboardVm.rules = [];
        dashboardVm.newDevice = {};
        dashboardVm.newDevice.readings = [];
        dashboardVm.newRule = {};

        dashboardVm.addReadingToDevice = addReadingToDevice;
        dashboardVm.addDevice = addDevice;
        dashboardVm.addRule = addRule;
        dashboardVm.toDevice = toDevice;

        activate();

        function activate() {
            dashboardVm.newDevice = {};
            dashboardVm.newDevice.readings = [];
            dashboardVm.newRule = {};
            deviceService.findAll()
                .then(function (response) {
                    dashboardVm.devices = response.data;
                    return ruleService.findAll();
                })
                .then(function (response) {
                    dashboardVm.rules = response.data;
                })
                .catch(function (error) {
                    alert("Server error");
                });
        }

        function addReadingToDevice() {
            dashboardVm.newDevice.readings.push(dashboardVm.readingForNewDevice);
            dashboardVm.readingForNewDevice = {};
        }

        function addDevice() {
            dashboardVm.newDevice.active = true;

            deviceService.add(dashboardVm.newDevice)
                .then(function (response) {
                    activate();
                }).catch(function (error) {
                //TODO
            });
        }

        function addRule() {
            dashboardVm.newRule.active = true;

            ruleService.add(dashboardVm.newRule)
                .then(function (response) {
                    activate();
                }).catch(function (error) {
                //TODO
            });
        }

        function toDevice(id) {
            $state.go('device', {'id': id});
        }
    }
})(angular);