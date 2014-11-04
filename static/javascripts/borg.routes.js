angular.module('borg.routes')
  .config(function ($routeProvider) {
    $routeProvider.when('/register', {
      controller: 'RegisterController',
      templateUrl: '/static/templates/authentication/register.html'
    }).otherwise('/');
  });
