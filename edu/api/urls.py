from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView,AllCategoriesListView,CategoryDeleteView,CategoryUpdateView
from .views import ProductListCreateView, ProductDetailView,AllProductsListView,ProductDeleteView,ProductUpdateView
# from .views import AccountListCreateView, AccountDetailView,AllAccountsListView


urlpatterns = [
    path('product/', ProductListCreateView.as_view(), name='product'),
    path('create/', CategoryListCreateView.as_view(), name='create'),
    path('<int:pk>/detail', CategoryDetailView.as_view(), name='detail'),
    path('categories', AllCategoriesListView.as_view(), name='all-categories-list'),  
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'), 
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='update'), 


    
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product-detail'),
    path('products/', AllProductsListView.as_view(), name='products'),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'), 
    path('update-product/<int:pk>/', ProductUpdateView.as_view(), name='update-product'), 

]