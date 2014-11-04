angular.module('borg.authentication.controllers')
  .controller('RegisterController', function ($scope, Authentication) {
    $scope.register = function () {
      Authentication.register($scope.username, $scope.password, $scope.email).then(
        function (data, status, headers, config) {
          console.log('Success!');
        },
        function (data, status, headers, config) {
          console.error('Epic failure!');
        }
      );
    };
  });
