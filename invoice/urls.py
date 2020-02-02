from rest_framework.routers import DefaultRouter

from invoice.views import CompanyView, ProductView, PurchaseOrderView

urlpatterns = []

router = DefaultRouter()
router.register(r'company', CompanyView, basename='company')
router.register(r'product', ProductView, basename='product')
router.register(r'purchase_order', PurchaseOrderView, basename='purchase_order')

urlpatterns += router.urls
