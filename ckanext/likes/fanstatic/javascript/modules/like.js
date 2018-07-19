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
        } else {
          data = {
            resource_id: options.id
          }
        }
        client.call('POST', path, data, this._onClickLoaded);
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
