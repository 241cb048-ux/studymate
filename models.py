from django.db import models
from django.contrib.auth.models import User

class StudyDocument(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="study_documents")
    title = models.CharField(max_length=180)
    pdf_file = models.FileField(upload_to="study_pdfs/")
    extracted_text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class StudyActivity(models.Model):
    ACTIVITY_CHOICES = [
        ("question", "Question"), ("summary", "Summary"),
        ("quiz", "Quiz"), ("flashcards", "Flashcards"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="study_activities")
    document = models.ForeignKey(StudyDocument, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    score = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner.username} - {self.activity_type}"
