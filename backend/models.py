from django.db import models

class Staff(models.Model):
    email = models.EmailField('メールアドレス', unique=True)
    first_name = models.CharField(('姓'), max_length=30)
    last_name = models.CharField(('名'), max_length=30)
    tel = models.CharField(('電話番号'), max_length=30, blank=True) # 追加
    mobile = models.CharField(('携帯電話番号'), max_length=30, blank=True) # 追加
    department = models.CharField(('所属'), max_length=30, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
