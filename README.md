#vitumblr#
###Post to Tumblr using VIM###

vitumblr is a simple script that allows you to write posts using your favourite
editor and publish them to Tumblr.

---
###First configuration###
- vitumblr is written in Python 2.7, thus download and install it.
- You also need [PyTumblr](https://github.com/tumblr/pytumblr) library.
- Now register a new application [here](http://www.tumblr.com/oauth/apps).
- Read your keys [here](https://api.tumblr.com/console) and write them in the *USER CONFIG* section
- Remember to change also the username in the config section with your username.

---
###Post format###

You must write a post using this simple syntax:
- Write the post title in the first line
- Leave the second line empty
- Write the post body starting from the third line
```
POST TITLE

post body
```
If you don't leave the second line empty, the whole file is considered as post body.

---
###License###
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
