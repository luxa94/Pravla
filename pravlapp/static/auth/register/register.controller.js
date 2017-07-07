(function(angular){

    'use strict';

    angular
        .module('pravla')
        .controller('RegisterCtrl', RegisterCtrl);

    RegisterCtrl.$inject = ['registerService'];

    function RegisterCtrl(registerService) {

        var registerVm = this;

        registerVm.user = {};

        registerVm.register = register;

        function register(){
            debugger;
            registerService.register(registerVm.user)
                .then(function(response) {

                }).catch(function(error) {

            });
        }
    }
})(angular);