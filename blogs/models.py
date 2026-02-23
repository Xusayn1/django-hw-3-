from django.db import models

from shared.models import BaseModel

# Create your models here.

class Author(BaseModel):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/')
    profession = models.CharField(max_length=100)
    about = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Category(BaseModel):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'        

class Tag(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'       


class BlogStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'
    ARCHIVED = 'archived', 'Archived'


class Blog(BaseModel):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    tags = models.ManyToManyField(Tag, related_name='blogs')
    is_active = models.BooleanField(default=True)
    long_description = models.TextField()


    status = models.CharField(max_length=20, choices=BlogStatus.choices, default=BlogStatus.DRAFT)



    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'        