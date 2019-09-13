routers = dict(
    BASE = dict(default_application='locadora',
    default_controller='default'),
)
"""
routes_in = (
    # do not reroute admin unless you want to disable it
    (BASE + '/admin', '/admin/default/index'),
    (BASE + '/admin/$anything', '/admin/$anything'),
    # do not reroute appadmin unless you want to disable it
    (BASE + '/$app/appadmin', '/$app/appadmin/index'),
    (BASE + '/$app/appadmin/$anything', '/$app/appadmin/$anything'),
    # do not reroute static files
    (BASE + '/$app/static/$anything', '/$app/static/$anything'),
    # reroute favicon and robots, use exable for lack of better choice
    ('/favicon.ico', '/examples/static/favicon.ico'),
    ('/robots.txt', '/examples/static/robots.txt'),
    # do other stuff
    ((r'.*http://otherdomain\.com.* (?P<any>.*)', r'/app/ctr\g<any>')),
    # remove the BASE prefix
    (BASE + '/$anything', '/$anything'),
)

# routes_out, like routes_in translates URL paths created with the web2py URL()
# function in the same manner that route_in translates inbound URL paths.
#

routes_out = (
    # do not reroute admin unless you want to disable it
    ('/admin/$anything', BASE + '/admin/$anything'),
    # do not reroute appadmin unless you want to disable it
    ('/$app/appadmin/$anything', BASE + '/$app/appadmin/$anything'),
    # do not reroute static files
    ('/$app/static/$anything', BASE + '/$app/static/$anything'),
    # do other stuff
    (r'.*http://otherdomain\.com.* /app/ctr(?P<any>.*)', r'\g<any>'),
    (r'/app(?P<any>.*)', r'\g<any>'),
    # restore the BASE prefix
    ('/$anything', BASE + '/$anything'),
)"""