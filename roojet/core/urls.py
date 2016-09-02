# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^optimized-price/$',
        view=views.OptimizedPriceResultsView.as_view(),
        name='optimized_price_results'),
    # new one
    url(regex=r'^price-update/$',
        view=views.PriceUpdatesView.as_view(),
        name='updatd_price_results'),    
    url(r'^p/(?P<shopify_variant_id>[-\w]+)/add-cost/$',
        views.AddCostView.as_view(), name='add_cost'),
    url(regex=r'^board/$', view=views.DashboardView.as_view(),
        name='dashboard'),
    url(regex=r'^product-expected-improvement/(?P<product_id>\d+)/$',
        view=views.ProductExpectedImprovementView.as_view(),
        name='product_ei'),
    url(regex=r'^add-shop/$', view=views.AddShopView.as_view(),
        name='add_shop'),
    url(regex=r'^shopify-callback/$', view=views.ShopifyCallbackView.as_view(),
        name='shopify_callback'),
    url(regex=r'^update/$',
        view=views.UpdateProductsView.as_view(),
        name='update'),
    url(regex=r'^pixel/$',
        view=views.TrackingPixelView.as_view(),
        name='pixel'),
    url(regex=r'^create/order/(?P<pk>\d+)/$',
            view=views.CreateOrderPlan.as_view(), name='create_order'),    
]
