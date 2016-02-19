# inspiration

netease music box is the best one I used compare to kugou, kuwo and other
music box. I like it very much. But there no linux version of them. the only
way is to use the web browser to listen to music.

thanks to the project [musicbox]['musicbox'], I know how to get my own work.

# usage

this python script need the dependency:

- requests
- BeautifulSoup4
- python 2.7
- pycrypto

first install this in a virtual env.

# description

this script can get the recommend music list every 6 hours, you can customise
it as you need.

before use the script, you also need to set your username and password.

you can set your username as raw string, but you need to take care of your
password.

before you set your password:

``` python

import hashlib

password = hashlib.md5('your password').hexdigest()

```

fill the password above.

my website [Coder Life](http://smileboywtu.github.io) just use this script.


['musicbox']: https://github.com/darknessomi/musicbox
