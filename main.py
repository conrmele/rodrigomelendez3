#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

html = '''<!DOCTYPE html> 
<html lang="en"> 
<head> 
<meta charset="utf-8" /> 
<title>Smashing HTML5!</title>  
<link rel="stylesheet" href="/stylesheets/style.css" type="text/css" />  
<!--[if IE]> <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
<![endif]--> <!--[if lte IE 7]> <script src="js/IE8.js" type="text/javascript"></script>
<![endif]--> <!--[if lt IE 7]>  <link rel="stylesheet" type="text/css" media="all" href="css/ie6.css"/>
<![endif]--> 
</head>  
<body> 
<h1>HELLO WORLD</h1>
</body> 
</html>
'''

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
