angular.module('borg.authentication.controllers')
  .controller('RegisterController', function ($location, $scope, Authentication) {
    // Logged in users should not be on this page.
    if (Authentication.getAuthenticatedUser()) {
      $location.url('/');
    }

    $scope.register = function () {
      Authentication.register($scope.username, $scope.password, $scope.email);
    };
  });
