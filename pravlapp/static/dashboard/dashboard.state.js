(function (angular) {

    'use strict';

    angular
        .module('pravla')
        .config(dashboardState);

    function dashboardState($stateProvider) {
        $stateProvider
            .state('dashboard', {
                url: '/dashboard',
                templateUrl: 'static/dashboard/dashboard.html',
                controller: 'DashboardCtrl',
                controllerAs: 'dashboardVm'
            });
    }
})(angular);