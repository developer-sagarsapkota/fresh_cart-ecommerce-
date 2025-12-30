from django.urls import path
from .import views
from users import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from products import views as ProductViews
from carts import views as CartViews
from orders import views as OrderViews

# write your urls here

urlpatterns = [
    path("register/", UserViews.RegisterView.as_view()),
    # API for users
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("profile/", UserViews.ProfileView.as_view()),
    # API for products
    # product list
    path("products/", ProductViews.ProductListView.as_view()),
    # product details
    path("products/<int:pk>/", ProductViews.ProductDetailView.as_view()),
    # API for Carts
    path("cart/", CartViews.CartView.as_view()),
    # Add to cart
    path('cart/add/', CartViews.AddToCartView.as_view()),
    # Manage Cart
    path('cart/items/<int:item_id>/', CartViews.ManageCartItemView.as_view()),
    # Orders
    path("orders/place/", OrderViews.PlaceOrderView.as_view()),
    path("orders/", OrderViews.MyOrdersView.as_view()),
    path("orders/<int:pk>/", OrderViews.OrderDetailView.as_view()),
]

