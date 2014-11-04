angular.module('borg.authentication.services')
  .service('Authentication', function ($cookies, $http) {
    var Authentication = {
      register: function (username, password, email) {
        return $http.post('/api/v1/users/', {
          username: username,
          password: password,
          email: email
        }).then(function (data, status, headers, config) {
          Authentication.login(username, password);
        }, function(data, status, headers, config) {
          console.error('Epic failure!');
        });
      },

      login: function (username, password) {
        return $http.post('/api/v1/auth/login/', {
          username: username, password: password
        }).then(function (data, status, headers, config) {
          Authentication.setAuthenticatedUser(data.data);

          window.location = '/';
        }, function (data, status, headers, config) {
          console.error('Epic failure!');
        });
      },

      logout: function (username, password) {
        return $http.post('/api/v1/auth/logout/')
          .then(function (data, status, headers, config) {
            Authentication.unauthenticate();
          
            window.location = '/';
          }, function (data, status, headers, config) {
            console.error('Epic failure!');
          });
      },

      getAuthenticatedUser: function () {
        if (!$cookies.authenticatedUser) {
          return;
        }

        return JSON.parse($cookies.authenticatedUser);
      },

      setAuthenticatedUser: function (user) {
        $cookies.authenticatedUser = JSON.stringify(user);
      },

      unauthenticate: function () {
        delete $cookies.authenticatedUser;
      }
    };

    return Authentication;
  });
