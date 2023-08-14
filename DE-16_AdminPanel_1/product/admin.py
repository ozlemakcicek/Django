from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *



# ------------------------------
# Category: many_to_many olarak olstrdgmz yeni model
# ------------------------------
admin.site.register(Category)











# ---------------------------------------------------
# Product
# ---------------------------------------------------
# bu yapi inherit etmek demek.bir modeli ayni ile baska bir modelde cagirilabilir olsun demek.ustte import ettik altta da class olarak yazip admin.site icine  yeni classi ekledik.list_display model icindeki field ler


class ReviewInline(admin.TabularInline):    #review deki yorumlari inline yaparak producktlara tasidik
    model=Review  #ForeignKey ModelName
    extra=1   # sadece 1 tane yorum ekleme alani versin diye.defaultu 3
    classes=['collapse']  # gizler
class ProductAdmin(ModelAdmin):

     # Tablo sutunları:ModelAdmin den goruyoruz bunlari
    list_display = ['id', 'name', 'is_in_stock', 'create_date', 'update_date']

    # edit etmek icin bu kod yazilir ve neyi guncelkleyeceksen onu yaz
    list_editable=['is_in_stock']

    # link verme(link verdigin seye editable yapilmaz)
    list_display_links = ['id','name']

    # filter(arama degil). buraya name eklersek butun kayitlari gosterir.mantikli degil arama yapilir name de
    list_filter = ['is_in_stock', 'create_date','update_date']

    #Arama: arama butonu koyar.yanindaki total a basarak cikabiliriz
    search_fields=['id','name']

    #Arama bilgilerini yazsin
    search_help_text='Arama yapmak icin burayi kullaniniz'

    #Default siralama(ordering:ModelAdmin de yok bu ama o da BaseModelAdmin den inherit yapilmis orda var)
    ordering=['id']  # 'id'->ASC(numara sirasina gore), '-id'->DESC( harf sirasina gore.- yazarsan tersten siralar)

    # Sayfa basina kayit sayisi
    list_per_page=20
    
    #tümünü göster yaparken max kayit sayisi
    list_max_show_all=200

    #tarihe gore hiyerarsik siralama
    date_hierarchy='create_date'

      # Otomatik kaıyıt oluştur:ayni anda fields ve fieldsets calismaz
    prepopulated_fields = {'slug' : ['name']}

    # Form liste görüntüleme:  
    fields = (
        ('name', 'is_in_stock'),
        ('slug'),
        ('categories'),
        ('description'),
        
    )

    #filter_vertical=['categories']
    filter_horizontal=['categories']



    '''
    # Detaylı form liste görüntüleme:
    fieldsets = (
        ('General Settings', {
            # "classes": ['wide'],
            "fields": (
                ('name', 'is_in_stock'),
                ('slug'),
            )
        }),
        ('Optional Settings', {
            "classes": ['collapse'],
            "fields": (
                ('description'),
            ),
            'description': "You can use this section for optionals settings"
        }),
    )
    '''


    inlines=[ReviewInline]

    def set_stock_in(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.') 

        # bu methodlari simdi bildirecegiz admin panele
    actions = ('set_stock_in', 'set_stock_out')
    set_stock_in.short_description = 'İşaretli ürünleri stoğa ekle'
    set_stock_out.short_description = 'İşaretli ürünleri stoktan çıkar'  


# field leri models .py den almistik.simdi birde kendimiz yazalim ve sutuna ekleyelim yukaridakini buraya getirip.hem field hem method eklenebiliyor list_displaye.bunu daha kisa yoldan += ile de yapablrz

    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.create_date
        return different.days

    #list_display = ['id', 'name', 'is_in_stock', 'create_date', 'update_date', 'added_days_ago']
    list_display+=['added_days_ago']


    
    # Kaçtane yorum var:
    def how_many_reviews(self, object):
        count = object.reviews.count()
        return count
    
    list_display += ['how_many_reviews']





admin.site.register(Product, ProductAdmin)


# -------------------------------------------
# Review
# -------------------------------------------
class ReviewAdmin(ModelAdmin):
    list_display = ("__str__", "created_date")
    raw_id_fields=['product']
    #raw_id_fields=('product',) sonuna , koyarak tuple yaptik.yoksa string


admin.site.register(Review, ReviewAdmin)