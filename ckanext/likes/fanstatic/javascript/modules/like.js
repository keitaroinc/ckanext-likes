/*
Copyright (c) 2018 Keitaro AB

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

/* Like buttons
 * Handles calling the API to like the current dataset
 *
 * action - This being the action that the button should perform. Currently: "like" or "dislike"
 * type - The being the type of object the user is trying to support. Currently: "user", "group" or "dataset"
 * id - id of the objec the user is trying to follow
 * loading - State management helper
 *
 * Examples
 *
 *   <a data-module="follow" data-module-action="follow" data-module-type="user" data-module-id="{user_id}">Follow User</a>
 *
 */
this.ckan.module('like', function ($, _) {
  return {
    /* options object can be extended using data-module-* attributes */
    options: {
      action: null,
      type: null,
      id: null,
      loading: false
    },

    /* Initialises the module setting up elements and event listeners.
     *
     * Returns nothing.
     */
    initialize: function () {
      $.proxyAll(this, /_on/);
      this.el.on('click', this._onClick);
    },

    /* Handles the clicking of the like button
     *
     * event - An event object.
     *
     * Returns nothing.
     */
    _onClick: function (event) {
      var options = this.options;
      if (
        options.action &&
        options.type &&
        options.id &&
        !options.loading
      ) {
        event.preventDefault();
        var client = this.sandbox.client;
        var path = 'likes_' + options.action + '_' + options.type;
        options.loading = true;
        this.el.addClass('disabled');
        var data = null
        if (options.type == 'dataset') {
          data = {
            dataset_id: options.id
          }
        } else  if (options.type == 'resource') {
          data = {
            resource_id: options.id
          }
        } else  if (options.type == 'request') {
          data = {
            id: options.id
          }
        } else {
          throw Exception("Unknown type: " + options.type)
        }
        client.call('POST', path, data, this._onClickLoaded, function(resp, message, status){
          if (resp.status == 403 ){
            if (options.login_url){
              window.location = options.login_url;
            }
          }else{
            console.error('Failed to submit like: ', status, message)
          }
        });
      }
    },

    /* Fired after the call to the API to either like or dislike
     *
     * json - The return json from the like / dislike API call
     *
     * Returns nothing.
     */
    _onClickLoaded: function (json) {
      var options = this.options;
      var sandbox = this.sandbox;
      var oldAction = options.action;
      var faLike = 'fa-thumbs-o-up';
      var faDislike = 'fa-thumbs-up';
      var markedClass = 'btn-info';

      options.loading = false;
      this.el.removeClass('disabled');
      if (options.action == 'like') {
        options.action = 'dislike';
        this.el.addClass(markedClass);
        this.el.find('.fa').removeClass(faLike).addClass(faDislike);
      } else {
        options.action = 'like';
        this.el.removeClass(markedClass);
        this.el.find('.fa').removeClass(faDislike).addClass(faLike);
      }
      sandbox.publish('like-' + oldAction + '-' + options.id);
    }
  };
});
