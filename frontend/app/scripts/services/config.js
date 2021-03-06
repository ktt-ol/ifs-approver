'use strict';

/**
 * @ngdoc service
 * @name frontendApp.Config
 * @description
 * # Config
 * Constant in the frontendApp.
 */
angular.module('frontendApp').constant('Config', {
  baseUrl: '@@STATUS' === 'dev' ? 'http://localhost:5000' : ''
});
