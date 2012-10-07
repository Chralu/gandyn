#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request
import re
import ipretriever

class IfConfig( object ):
  def get_public_ip( self ):
    """Returns the current public IP address. Raises an exception if an issue occurs."""
    try:
      url_page = 'http://ifconfig.me/ip'
      public_ip = None

      f = urllib.request.urlopen(url_page)
      data = f.read().decode("utf8")
      f.close()
      pattern = re.compile('\d+\.\d+\.\d+\.\d+')
      result = pattern.search(data, 0)
      if result == None:
        raise ipretriever.Fault('Service '+url_page+' failed to return the current public IP address')
      else:
        public_ip = result.group(0)
    except urllib.error.URLError as e:
      raise ipretriever.Fault(e)
    return public_ip
