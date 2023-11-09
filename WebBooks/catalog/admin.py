from django.contrib import admin
from django.utils.html import format_html

from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'photo', 'show_photo')
    fields = ['last_name', 'first_name', ('date_of_birth', 'photo',)]
    readonly_fields = ['show_photo']

    # После этого создаем функцию (метод) с именем show photo (). Этот метод в параметр
    # obj принимает зарегистрированную модель с авторами книг, а затем через функцию
    # format _ html () возвращает ссылку на изображение
    # { obj.photo.url}, а также с помощью стилей задает максимальную высоту изображения в 100 рх. В последней строке
    # создана поясняющая надпись к этому полю-«Фото».
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height: 100px;">'
        )
    show_photo.short_description = 'фото'


class BookInstanceInLine(admin.TabularInline):
    model = BookInstance


@admin.register(Book)  # аналогично этому admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author', 'show_photo')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInLine]
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')
    show_photo.short_description = 'Обложка'




@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    # Тут мы разбиваем на две секции
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'inv_nom')}),
        ('Статус и окончания его действия', {'fields': ('status', 'due_back')})
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Publisher)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Status)


