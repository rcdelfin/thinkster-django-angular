/**
 * Posts
 * @namespace thinkster.posts.services
 */
(function () {
  'use strict';

  angular
    .module('thinkster.posts.services')
    .factory('Posts', Posts);

  Posts.$inject = ['$http'];

  /**
   * @namespace Posts
   * @returns {Factory}
   */
  function Posts($http) {
    var Posts = {
      all: all,
      create: create
    };

    return Posts;

    ////////////////////
    
    /**
     * @name all
     * @desc Get all Posts
     * @returns {Promise}
     * @memberOf thinkster.posts.services.Posts
     */
    function all() {
      return $http.get('/api/v1/thoughts/');
    }


    /**
     * @name create
     * @desc Create a new Post
     * @param {string} content The content of the new Post
     * @returns {Promise}
     * @memberOf thinkster.posts.services.Posts
     */
    function create(content) {
      return $http.post('/api/v1/thoughts/', {
        content: content
      });
    }
  }
})();
