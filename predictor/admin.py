from django.contrib import admin
from .models import PredictionHistory

@admin.register(PredictionHistory)
class PredictionHistoryAdmin(admin.ModelAdmin):
    list_display = ('location', 'predicted_price', 'bedrooms', 'bathrooms', 'created_at')
    list_filter = ('location', 'condition', 'created_at')
    search_fields = ('location',)
    readonly_fields = ('created_at',)
