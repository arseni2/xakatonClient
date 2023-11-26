from django.db import models


class Document(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    INFO_REQUEST = 'info_request'
    IN_REWORK = 'in_rework'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (NEW, 'Новая'),
        (IN_PROGRESS, 'В работе'),
        (INFO_REQUEST, 'Дозапрос информации'),
        (IN_REWORK, 'На доработке'),
        (COMPLETED, 'Завершена'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NEW,
    )


class AdditionalInfo(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    info_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
