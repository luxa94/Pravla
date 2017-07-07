(function (angular) {

    'use strict';

    angular
        .module('pravla')
        .config(registerState);

    function registerState($stateProvider) {
        $stateProvider
            .state('register', {
                url: '/register',
                templateUrl: 'static/auth/register/register.html',
                controller: 'RegisterCtrl',
                controllerAs: 'registerVm'
            });
    }
})(angular);