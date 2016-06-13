#!/bin/bash

cd /opt/processmaker/

chmod -R 770 shared workflow/public_html gulliver/js gulliver/thirdparty/html2ps_pdf/cache

cd workflow/engine/

chmod -R 770 config content/languages plugins xmlform js/labels

chown -R :www-data /opt/processmaker