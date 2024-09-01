
from django.contrib import admin
from .models import Category,Subcategory,Poll, Choice,Contact,Subscriber,Video,Product, Affiliate,Post, Comment
from .forms import VideoAdminForm,ProductAdminForm,PostAdminForm
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'topic', 'status')
    list_filter = ('topic', 'status')
    search_fields = ('title', 'description', 'keyword')
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug from title

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        # Optionally handle custom save logic
        super().save_model(request, obj, form, change)



class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent_category', 'topic', 'status')
    list_filter = ('topic', 'status', 'parent_category')
    search_fields = ('title', 'description', 'keyword')
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug from title


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1  # Number of empty forms to display

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'slug', 'created_at', 'updated_at')
    search_fields = ('question',)
    prepopulated_fields = {'slug': ('question',)}  # Automatically generate slug from question
    inlines = [ChoiceInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    ordering = ('-subscribed_at',)
    
    
    
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    form =VideoAdminForm
    list_display = ('title', 'slug', 'description', 'thumbnail', 'url', 'keyword', 'category', 'subcategory', 'user', 'created_at', 'updated_at')
    search_fields = ('title', 'keyword', 'description')
    list_filter = ('category', 'subcategory', 'user', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
 
 
 
 
 
class AffiliateInline(admin.TabularInline):  # or use admin.StackedInline for a different layout
    model = Affiliate
    extra = 1  # Number of empty forms to display for new affiliates
    fields = ('name', 'url', 'price')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(topic='product')
            
        if db_field.name == "subcategory":
            kwargs["queryset"] = Subcategory.objects.filter(topic='product')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
   
    form=ProductAdminForm
    list_display = ('title', 'slug', 'price', 'offerprice', 'category', 'subcategory', 'user', 'created_at', 'updated_at')
    search_fields = ('title', 'keyword', 'description')
    list_filter = ('category', 'subcategory', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [AffiliateInline]

@admin.register(Affiliate)
class AffiliateAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'price', 'product')
    search_fields = ('name', 'product__title')
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(topic='post')
            
        if db_field.name == "subcategory":
            kwargs["queryset"] = Subcategory.objects.filter(topic='post')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    form = PostAdminForm
    list_display = ('title', 'slug', 'category', 'subcategory', 'views', 'status', 'created_at')
    search_fields = ('title', 'description', 'content')
    list_filter = ('category', 'subcategory', 'status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('products',)  # Allows selecting multiple products in the admin

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at', 'updated_at')
    search_fields = ('name', 'body')
    list_filter = ('created_at', 'updated_at') 
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Poll, PollAdmin)


