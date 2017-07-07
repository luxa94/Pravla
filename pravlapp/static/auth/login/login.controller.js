(function(angular){

    angular
        .module('pravla')
        .controller('LoginCtrl', LoginCtrl);

    LoginCtrl.$inject = ['$state', 'loginService', 'storageService'];

    function LoginCtrl($state, loginService, storageService) {

        var loginVm = this;

        loginVm.user = {};

        loginVm.login = login;

        function login() {
            loginService.login(loginVm.user)
                .then(function(response) {
                    var token = response.data.id;
                    storageService.setToken(token);
                    $state.go('dashboard');
                }).catch(function(error) {

            });
        }
    }

})(angular);