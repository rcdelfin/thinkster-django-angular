angular.module('borg.authentication.controllers')
  .controller('LoginController', function ($location, $scope, Authentication) {
    // Logged in users should not be on this page.
    if (Authentication.getAuthenticatedUser()) {
      $location.url('/');
    }

    $scope.login = function () {
      Authentication.login($scope.username, $scope.password);
    };
  });
