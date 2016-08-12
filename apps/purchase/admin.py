import arrow
from django.conf import settings

from django.contrib import admin

from apps.purchase.models import Purchase, Purchase1SDK

@admin.register(Purchase)
class AdminPurchase(admin.ModelAdmin):
    list_display = (
        'id', 'server_id', 'char_id', 'goods_id', 'create_at',
        'platform', 'fee', 'verified',
    )

    ordering = ('-create_at',)
    readonly_fields = list_display

@admin.register(Purchase1SDK)
class AdminPurchase1SDK(admin.ModelAdmin):
    list_display = (
        'id', 'ct_date','pt_date', 'fee', 'sdk', 'ssid',
        'st', 'tcd', 'uid'
    )

    search_fields = ('id', 'tcd',)
    readonly_fields = (
        'id', 'ct', 'fee', 'pt', 'sdk', 'ssid',
        'st', 'tcd', 'uid'
    )

    ordering = ('-ct',)

    def ct_date(self, obj):
        return arrow.get(obj.ct).to(settings.TIME_ZONE).to("YYYY-MM-DD HH:mm:ss")

    def pt_date(self, obj):
        return arrow.get(obj.pt).to(settings.TIME_ZONE).to("YYYY-MM-DD HH:mm:ss")
