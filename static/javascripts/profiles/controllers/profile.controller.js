/**
 * ProfileController
 * @namespace thinkster.profiles.controllers
 */
(function () {
  'use strict';

  angular
    .module('thinkster.profiles.controllers')
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$location', '$routeParams', 'Posts', 'Profile', 'Snackbar'];

  /**
   * @namespace ProfileController
   */
  function ProfileController($location, $routeParams, Posts, Profile, Snackbar) {
    var vm = this;

    vm.profile = undefined;
    vm.promiseResolved = false;
    vm.posts = [];

    activate();

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf thinkster.profiles.controllers.ProfileController
     */
    function activate() {
      var username = $routeParams.username.substr(1);

      Profile.get(username).then(profileSuccessFn, profileErrorFn);


      /**
       * @name profileSuccessProfile
       * @desc Update `profile` and `posts` on view
       */
      function profileSuccessFn(data, status, headers, config) {
        vm.profile = data.data;
        vm.promiseResolved = true;
        vm.posts = vm.profile.thoughts;
      }

      /**
       * @name profileErrorFn
       * @desc Redirect to index and show error Snackbar
       */
      function profileErrorFn(data, status, headers, config) {
        $location.url('/');
        Snackbar.error('That user does not exist.');
      }
    }
  }
})();
