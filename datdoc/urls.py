from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('blog.urls')),
    url(r'^cv$', 'blog.views.cv'),
    url(r'archive$', 'blog.views.archive'),
    url(r'article/(?P<articleid>\d+)$', 'blog.views.article'),
    url(r'kw', 'blog.views.keyword'),
    url(r'^admin/', include(admin.site.urls)),
)
