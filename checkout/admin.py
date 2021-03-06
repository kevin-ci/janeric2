from django.contrib import admin

from .models import Product, Order, OrderLineItem, ProductShippingData,  ShipFromAddress


# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 'shipping_cost', 'ca_sales_tax', 'order_total', 'grand_total', 'original_cart', 'stripe_pid',)

    fields = (
        'order_number', 'order_date', 'ship_full_name', 'email', 'ship_phone_number','ship_street_address1', 'ship_street_address2', 'ship_city', 'ship_state', 'ship_zipcode', 'shipping_cost','ca_sales_tax', 'order_total', 'grand_total', 'original_cart', 'stripe_pid', 'bill_full_name', 'bill_phone_number','bill_street_address1', 'bill_street_address2', 'bill_city', 'bill_state', 'bill_zipcode',)

    list_display = ('order_number', 'order_date', 'email', 'order_total', 'shipping_cost', 'ca_sales_tax', 'grand_total', 'ship_full_name', 'ship_phone_number','ship_street_address1', 'ship_street_address2', 'ship_city', 'ship_state', 'ship_zipcode', 'bill_full_name', 'bill_phone_number','bill_street_address1', 'bill_street_address2', 'bill_city', 'bill_state', 'bill_zipcode',)

    ordering = ('-order_date', )


class ShipFromAddressDataAdmin(admin.ModelAdmin):
    list_display = (
        'shipper_reference_name',
        'shipper_company_name',
        'shipper_phone_number',
        'shipper_streetline1',
        'shipper_streeline2',
        'shipper_city',
        'shipper_state',
        'shipper_postal_code'
    )

    ordering = ('shipper_reference_name', )


class ProductShippingDataAdmin(admin.ModelAdmin):

    list_display = (
        'product',
        'product_pkg_weight_lb',
        'shipper_address'
    )

    ordering = ('product',)


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductShippingData, ProductShippingDataAdmin)
admin.site.register(ShipFromAddress, ShipFromAddressDataAdmin)
