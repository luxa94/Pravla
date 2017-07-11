(function(angular) {

    angular
        .module('pravla')
        .controller('DeviceCtrl', DeviceCtrl);

    DeviceCtrl.$inject = ['$stateParams', 'deviceService'];

    function DeviceCtrl($stateParams, deviceService) {

        var deviceVm = this;

        deviceVm.device = {};
        deviceVm.selectedReading = {};

        deviceVm.editDevice = editDevice;
        deviceVm.editSelectedReading = editSelectedReading;
        deviceVm.selectReading = selectReading;

        activate();

        function activate() {
            deviceService.find($stateParams.id)
                .then(function(response) {
                    deviceVm.device = response.data;
                }).catch(function(error) {
               console.log("Server error");
            });
        }

        function editDevice() {
            deviceService.edit(deviceVm.device)
                .then(function(response) {
                    deviceVm.device = response.data;
                }).catch(function(error) {
                console.log("Server error");
            });
        }

        function editSelectedReading() {
            idx = deviceVm.device.readings.findIndex(reading => deviceVm.selectedReading.id == reading.id)
            deviceVm.device.readings.splice(idx);
            deviceVm.device.readings.push(deviceVm.selectedReading);
        }

        function selectReading(reading) {
            deviceVm.selectedReading = angular.copy(reading);
        }

    }
})(angular);