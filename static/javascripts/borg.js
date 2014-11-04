angular.module('borg', [
    'borg.config',
    'borg.routes',
    'borg.authentication',
    'borg.static'
]);

angular.module('borg.config', []);
angular.module('borg.routes', ['ngRoute']);

angular.module('borg')
  .run(function ($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  });
