from django.db import modelsclass App(models.Model):    name = models.CharField(max_length=64, default='testname', unique=True)    def __str__(self):        return self.name# 为用户创建一个存储class User(models.Model):    openid = models.CharField(max_length=64, unique=True)    # nickname = models.CharField(max_length=64, db_index=True)    nickname = models.CharField(max_length=64)    # 数据库迁移还没做    # python manage.py makemigrations juheapp    # python manage.py makemigrations   才算添加上    # python manage.py migrate    # 关注的城市    focus_cities = models.TextField(default='[]')    # 星座    focus_constellations = models.TextField(default='[]')    # 股票    focus_stocks = models.TextField(default='[]')    # 加一个外键???????    menu = models.ManyToManyField(App)    # 加完之后记得数据库迁移    def __str__(self):        return self.nickname    """    python manage.py dumpdata juheapp>juheapp.json    setting中的database中的一些设置    python manage.py migrate --run-syncdb --database slave    python manage.py loaddata xxx.json    """    class Meta:        """        元:描绘类名本身的一些属性        """        # db_table='abddddd'        # 默认appname_classname  juheapp_user        indexes = [models.Index(fields=['nickname'], name='nickname66666')]