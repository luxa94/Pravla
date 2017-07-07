(function (angular) {

    'use strict';

    angular.module('pravla')
        .service('authInterceptor', authInterceptor);

    authInterceptor.$inject = ['$q', 'storageService'];

    function authInterceptor($q, storageService) {

        return {
            request: request,
            responseError: responseError
        };

        function request(config) {
            var token = storageService.getToken();
            if (token) {
                config.headers["Authorization"] = token;
            }
            return config;
        }

        function responseError(response) {
            return $q.reject(response);
        }
    }
})(angular);