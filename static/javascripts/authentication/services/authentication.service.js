angular.module('borg.authentication.services')
  .service('Authentication', function ($http) {
    var Authentication = {
      register: function (username, password, email) {
        return $http.post('/api/v1/users/', {
          username: username,
          password: password,
          email: email
        });
      }
    };

    return Authentication;
  });
