#!/usr/bin/env python
#
# By Steve Molin
#
# documentation for flickrapi: http://stuvel.eu/media/flickrapi-docs/documentation/ 
# hat tip to https://xinyustudio.wordpress.com/2012/03/27/upload-images-in-flickr-using-python-code/

import os
import sys
import flickrapi

api_key = unicode("dj0yJmk9SUtRNXgzTVBTcm9TJmQ9WVdrOVdXRnVOVEJVTm1zbWNHbzlNVFkwT0RreU9ETTJNZy0tJnM9Y29uc3VtZXJzZWNyZXQmeD03Yg")
api_key = unicode("24c871000e13d8a910ab449c2571ae59")
api_secret = unicode("a64502095ad8d1c9")
flickr = None

def progress(progress, done):
  if done:
    print "Done uploading"
  else:
    print "At %s%%" % progress

def auth():
  flickr = flickrapi.FlickrAPI(api_key, api_secret)
  (token, frob) = flickr.get_token_part_one(perms='write')
  if not token:
      raw_input("Press ENTER after you authorized this program")
  flickr.get_token_part_two((token, frob))
  return flickr

def upload(flickr, filename):
  dir = os.path.dirname(os.path.realpath(filename))
  pathsplit = dir.split(os.path.sep)
  pathprotected = ['"%s"' % s for s in pathsplit]
  pathjoin = ' '.join(pathprotected)
  print 'about to upload %s with tags %s...' % (filename, pathjoin)
  flickr.upload( callback=progress, description=u'', filename=filename, is_public=0, is_family=1, is_friend=1, tags=unicode(pathjoin), title=u'',)

def main():
  flickr = auth()
  if len(sys.argv) == 1:
    raise RuntimeError, 'no filenames specified'
  for fn in sys.argv[1:]:
    upload(flickr, fn)

if __name__ == '__main__':
  main()
