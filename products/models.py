from django.db import models

from tools.validators import validate_file_size


# Create your models here.

class Category(models.Model):
	"""产品分类"""
	category = models.CharField(verbose_name='产品分类', max_length=32)
	parent_category = models.ForeignKey(verbose_name='父类', to='Category', on_delete=models.CASCADE, null=True, blank=True, related_name='Cate_P', default='无')
	cate_desc = models.CharField(verbose_name='产品分类说明', max_length=200, null=True, blank=True, default='无')

	def __str__(self):
		return self.category

class Products(models.Model):
	"""产品表"""
	name = models.CharField(verbose_name='产品名称', max_length=200)
	category = models.ForeignKey(verbose_name='产品类别', to=Category, on_delete=models.CASCADE)
	product_photo = models.ImageField(verbose_name='产品图片', upload_to='upload/products/', blank=True, validators=[validate_file_size,])

	def __str__(self):
		return self.name
class ProductRelative(models.Model):
	"""产品相关表"""
	pass

