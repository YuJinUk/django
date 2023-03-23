from django.db import models

# Create your models here.

class Todo(models.Model):
    
    '''
    task = charfield pick
    isCompleted = False pick
    created_at = datefield # 생성시각
    completed_at = datefield # 완료 시각
    
    ->
    not : 부정 연산자
    '''
    
    task = models.CharField(max_length=300) # todo 항목
    isCompleted = models.BooleanField(default = False) # 완료 여부
    created_at = models.DateField(auto_now_add = True) # 생성 시각
    completed_at = models.DateField(auto_now = True) # 완료 시각