from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField('昵称', max_length=20)
    all_integral = models.IntegerField('总积分', default=0)
    all_bout = models.IntegerField('总局数', default=0)
    login_time = models.DateField('注册时间', auto_now_add=True)
    last_active_time = models.DateField('最后活跃时间', auto_now=True)
    is_active = models.BooleanField('是否活跃', default=1)

    class Meta:
        db_table = "player"
        verbose_name_plural = verbose_name = '玩家'


class Session(models.Model):
    name = models.CharField('场次名称',max_length=30)
    begin_time = models.DateTimeField('开始时间',auto_now_add=True)
    end_time = models.DateTimeField('结束时间',default = 0/0/0/0/0/0)
    player1 = models.ForeignKey(Player,on_delete=models.PROTECT)
    player2 = models.ForeignKey(Player,on_delete=models.PROTECT)
    player3 = models.ForeignKey(Player,on_delete=models.PROTECT)
    player4 = models.ForeignKey(Player,on_delete=models.PROTECT,null=True)
    class Meta:
        db_table = "session"
        verbose_name_plural = verbose_name = '场次'


class Bout(models.Model):
    pass

    class Meta:
        db_table = "bout"
        verbose_name_plural = verbose_name = '对局'
