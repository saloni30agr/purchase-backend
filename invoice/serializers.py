from rest_framework import serializers

from invoice.models import Company, Product, PurchaseOrder


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'gst')


class ProductSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_cost = serializers.CharField(source='product.cost', read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
