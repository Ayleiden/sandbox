from django.db import models

# Create your models here.

# Table for storing source information
class Source(models.Model):
    source_name = models.CharField(max_length=255)  # e.g., website, newspaper name
    author = models.CharField(max_length=255)  # Author's name
    date_added = models.DateField(auto_now_add=True)  # Automatically adds the current date

    def __str__(self):
        return f"{self.author} - {self.source_name} ({self.date_added})"

class TextMeta(models.Model):
    text_id = models.AutoField(primary_key=True)
    hsk_level = models.IntegerField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)  # Linking to Source

    def __str__(self):
        return f"Text ID: {self.text_id}, HSK Level: {self.hsk_level}"

class TextFull(models.Model):
    text_id = models.OneToOneField(TextMeta, on_delete=models.CASCADE)
    text_full = models.TextField()

    def __str__(self):
        return f"Text ID: {self.text_id}"

class TextParagraph(models.Model):
    text_id = models.ForeignKey(TextMeta, on_delete=models.CASCADE)
    p_number = models.IntegerField()
    p_text = models.TextField()

    def __str__(self):
        return f"Text ID: {self.text_id}, Paragraph: {self.p_number}"

class TextTitle(models.Model):
    text_id = models.OneToOneField(TextMeta, on_delete=models.CASCADE)
    text_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Text ID: {self.text_id}, Title: {self.text_name}"
