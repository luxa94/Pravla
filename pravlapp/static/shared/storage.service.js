(function (angular) {
    'use strict';

    angular
        .module('pravla')
        .service('storageService', storageService);

    storageService.$inject = ['$window'];

    function storageService($window) {
        var LOCAL_STORAGE_KEY = 'pravla_token';
        var LOCAL_STORAGE_INSTANCE = $window.localStorage;

        return {
            getToken: getToken,
            setToken: setToken,
            removeToken: removeToken
        };

        function getToken() {
            if (LOCAL_STORAGE_INSTANCE) {
                var token = LOCAL_STORAGE_INSTANCE.getItem(LOCAL_STORAGE_KEY);
                if (token) {
                    return token;
                }
            }
            return null;
        }

        function setToken(token) {
            if (LOCAL_STORAGE_INSTANCE && token) {
                LOCAL_STORAGE_INSTANCE.setItem(LOCAL_STORAGE_KEY, token);
            }
        }

        function removeToken() {
            LOCAL_STORAGE_INSTANCE && LOCAL_STORAGE_INSTANCE.removeItem(LOCAL_STORAGE_KEY);
        }

    }
})(angular);