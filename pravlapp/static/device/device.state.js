(function(angular) {

    angular
        .module('pravla')
        .config(deviceState);

    function deviceState($stateProvider) {
        $stateProvider
             .state('device', {
                url: '/device/:id',
                templateUrl: 'static/device/device.html',
                controller: 'DeviceCtrl',
                controllerAs: 'deviceVm'
            });
    }
})(angular);