(function (angular) {

    'use strict';

    angular
        .module('pravla', ['ui.router'])
        .config(function ($stateProvider, $urlRouterProvider, $httpProvider) {

            $httpProvider.interceptors.push('authInterceptor');
        });

})(angular);