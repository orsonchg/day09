from django.db import models


# Create your models here.


class Continent(models.Model):
	"""洲别"""
	name = models.CharField(verbose_name='洲别名称', max_length=20)
	remark = models.CharField(verbose_name='备注', max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name


class Country(models.Model):
	"""国家地区"""
	code = models.CharField(verbose_name='国家代码', max_length=5, unique=True)
	cn_abbr = models.CharField(verbose_name='国家中文简称', max_length=50)
	en_abbr = models.CharField(verbose_name='国家英文简称', max_length=100)
	cn_name = models.CharField(verbose_name='国家中文名称', max_length=200)
	en_name = models.CharField(verbose_name='国家英文名称', max_length=200)
	domain = models.CharField(verbose_name='域名', max_length=5, unique=True)
	continent = models.ForeignKey(verbose_name='所属洲别', to=Continent, on_delete=models.CASCADE)
	remark = models.CharField(verbose_name='备注', max_length=200, null=True, blank=True)

	def __str__(self):
		return '%s(%s)' % (self.en_abbr, self.cn_abbr)


class TelAreaCode(models.Model):
	"""国际电话区号"""
	code = models.CharField(verbose_name='国际电话区号', max_length=10, unique=True)
	country = models.ForeignKey(verbose_name='所属国家', to=Country, on_delete=models.CASCADE)

	def __str__(self):
		return self.code
