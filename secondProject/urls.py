from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
from django.conf import settings # 습관처럼 외우자1 (media)
from django.conf.urls.static import static #습관처럼 외우자2 (media)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    #url패스가 꼭 html문서를 연결하는 것이 아니라 함수파일도 가능!
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

