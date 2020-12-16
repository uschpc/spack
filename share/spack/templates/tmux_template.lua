{% extends "modules/modulefile.lua" %}
{% block footer %}

-- Override TMUX_TMPDIR from /tmp to scratch --
local username=os.getenv("USER")
setenv("TMUX_TMPDIR", "/scratch2/" .. username)
{% endblock %}
