angular.module('borg.static.controllers')
  .controller('NavbarController', function ($scope, Authentication) {
    $scope.logout = function () {
      Authentication.logout();
    };
  });
