from django.db import models

# Create your models here.
group_choices = (
            ('МОАИС', 'Мат. обеспечение и администрирование информационных систем'),
            ('ПИ', 'Прикладная информатика'),
            ('ПМ', 'Прикладная математика и инофрматика'),
            ('Пед. обр', 'Педагогическое образование с двумя профилями подготовки'),
            ('Не студенческая группа', 'Не студенческая группа'),
        )
class Group(models.Model):
    group_number = models.CharField('Номер группы', max_length=10, unique=True)
    group_title = models.CharField('Направление', max_length=250, choices=group_choices)

    def __str__(self):
        return self.group_title
    def get_absolute_url(self):
        return f'/groups/{self.id}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Student(models.Model):
    student_surname = models.CharField('Фамилия', max_length=50)
    student_name = models.CharField('Имя', max_length=50)
    group = models.ForeignKey('Group', null=True, on_delete=models.CASCADE)
    account_id = models.IntegerField('id аккаунта', unique=True)
    student_solved_acmp_base = models.TextField(null=True)  # Набор решённых на ACMP из базы

    def get_absolute_url(Self):
        return f'/groups/{Self.group_id}/'

    def __str__(self):
        return self.student_surname +' '+ self.student_name

    def fio(self):
        return self.student_surname +' '+ self.student_name

    def acmp_id(self):
        return str(self.account_id)

    def get_tasks(self):
        result = []
        result = result+[x for x in self.student_solved_acmp_base.split(',')]
        return result

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class TaskAcmp(models.Model):
    # BEGINNER = 'BE'
    # MEDIUM = 'ME'
    # HARD = 'HA'
    level_choices = (
        ('Для начинающих', 'Для начинающих'),
        ('Средний', 'Средний'),
        ('Сложный', 'Сложный')
    )
    theme=models.CharField(max_length=50)
    level=models.CharField(max_length=15, choices=level_choices, default='BEGINNER')
    task_list=models.TextField(null=True)#Список задач

    def get_absolute_url(self):
        return '/groups/task_home'

    def __str__(self):
        return self.theme+' ('+self.level+')'
    #статический метод получения полного списка задач

    def getAllTasks():
        tasks=TaskAcmp.objects.all()
        result=[]
        for task in tasks:
            result=result+[int(x) for x in task.task_list.split(',')]
        return result

    def getTasks(self):
        result=[]
        result=result+[int(x) for x in self.task_list.split(',')]
        return result

