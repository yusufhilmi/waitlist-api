from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    url = models.SlugField()

    def __str__(self):
        return str(self.title)


class Waiter(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project")
    message = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.email)
