from django.contrib import admin
from juheapp.models import App, User
import random
import time
# admin.site.register(User)
admin.site.register(App)


# admin.site.register(User, UserAdmin)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ['openid']  # 和include相反, 不显示xx属性

    # 可以定义一些规则来控制后台插入模型字段的值
    def save_model(self, request, obj, form, change):
        obj.openid = obj.nickname + str(random.randint(1, 1000))
        return super(UserAdmin, self).save_model(request, obj, form, change)
