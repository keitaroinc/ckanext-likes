/* Updates the Followers counter in the UI when the Follow/Unfollow button
* is clicked.
*
* id - id of the object the user is trying to follow/unfollow.
* num_followers - Number of followers the object has.
*
* Example
*
*   <dd data-module="followers-counter"
*       data-module-id="object-id"
*       data-module-num_followers="6">
*     <span>6</span>
*   </dd>
*
*/
this.ckan.module('likes-counter', function($) {
    'use strict';
  
    return {
      options: {
        id: null,
        num_likes: 0
      },
  
      /* Subscribe to events when the Follow/Unfollow button is clicked.
      *
      * Returns nothing.
      */
      initialize: function() {
        $.proxyAll(this, /_on/);
  
        this.counterEl = this.$('span');
        this.objId = this.options.id;
  
        this.sandbox.subscribe('like-like-' + this.objId, this._onLike);
        this.sandbox.subscribe('like-dislike-' + this.objId, this._onDislike);
      },
  
      /* Calls a function to update the counter when the Follow button is clicked.
      *
      * Returns nothing.
      */
      _onLike: function() {
        this._updateCounter({action: 'like'});
      },
  
      /* Calls a function to update the counter when the Unfollow button is clicked.
      *
      * Returns nothing.
      */
      _onDislike: function() {
        this._updateCounter({action: 'dislike'});
      },
  
      /* Handles updating the UI for Followers counter.
      *
      * Returns nothing.
      */
      _updateCounter: function(options) {
        var locale = $('html').attr('lang');
        var action = options.action;
        var incrementedLikes;
  
        if (action === 'like') {
          incrementedLikes = (++this.options.num_likes).toLocaleString(locale);
        } else if (action === 'dislike') {
          incrementedLikes = (--this.options.num_likes).toLocaleString(locale);
        }
  
        // Only update the value if it's less than 1000, because for larger
        // numbers the change won't be noticeable since the value is converted
        // to SI number abbreviated with "k", "m" and so on.
        if (this.options.num_likes < 1000) {
          this.counterEl.text(incrementedLikes);
          this.counterEl.removeAttr('title');
        } else {
          this.counterEl.attr('title', incrementedLikes);
        }
      },
  
      /* Remove any subscriptions to prevent memory leaks. This function is
       * called when a module element is removed from the page.
       *
       * Returns nothing.
       */
      teardown: function() {
        this.sandbox.unsubscribe('like-like-' + this.objId, this._onLike);
        this.sandbox.unsubscribe('like-dislike-' + this.objId, this._onDislike);
      }
    }
  });
  