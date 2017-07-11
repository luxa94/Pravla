(function(angular) {

    'use strict';

    angular
        .module('pravla')
        .controller('AuthCtrl', AuthCtrl);

    AuthCtrl.$inject = ['storageService', '$window'];

    function AuthCtrl(storageService, $window) {

        var authVm = this;

        authVm.isSessionActive = isSessionActive;
        authVm.terminateSession = terminateSession;

        function isSessionActive() {
            //dummy check
            return storageService.getToken();
        }

        function terminateSession() {
            storageService.removeToken();
            $window.location.replace("/")
        }

    }
})(angular);