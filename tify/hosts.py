from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'www','tify.urls', name='www'),
    host(r'admin', 'tify.urls_admin', name='admin'),
)