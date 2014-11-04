angular.module('borg', [
    'borg.config',
    'borg.routes',
    'borg.authentication'
]);

angular.module('borg.config', []);
angular.module('borg.routes', ['ngRoute']);
