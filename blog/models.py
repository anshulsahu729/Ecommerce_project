from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)   # to hide/show blog
    deleted = models.BooleanField(default=False) # soft delete

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Always generate unique slug from title
        if not self.slug:
            base_slug = slugify(self.title)
        else:
            base_slug = self.slug  

        slug = base_slug
        counter = 1
        while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        self.slug = slug
        super().save(*args, **kwargs)

    # Soft delete instead of removing from DB
    def delete(self, *args, **kwargs):
        self.deleted = True
        super().save(update_fields=["deleted"])
