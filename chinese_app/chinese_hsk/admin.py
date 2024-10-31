# admin.py
from django.contrib import admin
from .models import Source, TextMeta, TextFull, TextParagraph, TextTitle

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_name', 'author', 'date_added')  # Ensure these fields exist in the model
    search_fields = ('source_name', 'author')  # Searchable fields

@admin.register(TextMeta)
class TextMetaAdmin(admin.ModelAdmin):
    list_display = ('text_id', 'hsk_level', 'source')  # Display these fields in the list view
    list_filter = ('hsk_level', 'source')  # Filter options on the sidebar
    search_fields = ('text_id__text_name',)  # Searching by title through related fields

@admin.register(TextFull)
class TextFullAdmin(admin.ModelAdmin):
    list_display = ('text_id',)  # Display text ID
    search_fields = ('text_id__text_name',)  # Allow searching by title

@admin.register(TextParagraph)
class TextParagraphAdmin(admin.ModelAdmin):
    list_display = ('text_id', 'p_number')  # Display text ID and paragraph number
    list_filter = ('text_id',)  # Allow filtering by text

@admin.register(TextTitle)
class TextTitleAdmin(admin.ModelAdmin):
    list_display = ('text_id', 'text_name')  # Display text ID and title
    search_fields = ('text_name',)  # Allow searching by title
