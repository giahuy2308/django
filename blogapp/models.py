from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=250, blank=False)
    avatar = models.ImageField(upload_to='static/images')

    def __str__(self):
        return str(self.username) + " id:" + str(self.id)


class MainPage(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return str(self.title) + " -User:" + str(self.user.username) + " id:" + str(self.id)


class Blog(models.Model):
    mainPage = models.ForeignKey(MainPage, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(max_length=100000, blank=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)+ ' -MainPage:' + str(self.mainPage.title) + " id:" + str(self.id)


class Comment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=None)
    content = models.TextField(max_length=10000, blank=False)

    def __str__(self):
        return str(self.content) + " id:" + str(self.id)