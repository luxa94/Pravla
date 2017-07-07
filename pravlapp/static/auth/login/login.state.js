(function (angular) {

    'use strict';

    angular
        .module('pravla')
        .config(loginState);

    function loginState($stateProvider) {
        $stateProvider
            .state('login', {
                url: '/login',
                templateUrl: 'static/auth/login/login.html',
                controller: 'LoginCtrl',
                controllerAs: 'loginVm'
            })
    }
})(angular);