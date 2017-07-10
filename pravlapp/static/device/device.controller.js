(function(angular) {

    angular
        .module('pravla')
        .controller('DeviceCtrl', DeviceCtrl);

    DeviceCtrl.$inject = ['$stateParams', 'deviceService'];

    function DeviceCtrl($stateParams, deviceService) {

        var deviceVm = this;

        deviceVm.device = {};

        deviceVm.edit = edit;

        activate();

        function activate() {
            deviceService.find($stateParams.id)
                .then(function(response) {
                    deviceVm.device = response.data;
                }).catch(function(error) {
               console.log("Server error");
            });
        }

        function edit() {
            deviceService.edit(deviceVm.device)
                .then(function(response) {
                    deviceVm.device = response.data;
                }).catch(function(error) {
                console.log("Server error");
            });
        }

    }
})(angular);