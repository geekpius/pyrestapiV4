from django.db import models

class Quote (models.Model):
    quote_author = models.CharField(max_length=60)
    quote_body = models.TextField()
    context = models.CharField(max_length=100)
    source = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Metadata
    class Meta :
        ordering = ['id']

    #Methods
    def __str__(self):
        return self.quote_author
