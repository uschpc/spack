{% extends "modules/modulefile.lua" %}
{% block footer %}

-- Not proud of this, had to externally install gmt and --
-- Spack wouldn't add these lines to the module file    --
load("gdal")
load("netcdf-c")
{% endblock %}
