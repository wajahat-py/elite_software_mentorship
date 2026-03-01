from django.db import models

class Application(models.Model):
    EXPERIENCE_CHOICES = [
        ('1', 'No experience'),
        ('2', 'Some beginner exposure'),
        ('3', 'Completed a coding course before'),
    ]
    
    CONSIDERATION_CHOICES = [
        ('1', 'Yes'),
        ('2', 'I’d like to discuss further'),
    ]

    parent_name = models.CharField("Parent Full Name", max_length=200)
    parent_email = models.EmailField("Parent Email Address")
    student_age = models.IntegerField("Student Age")
    coding_experience = models.CharField(
        "Has your child had any prior coding experience?",
        max_length=1, 
        choices=EXPERIENCE_CHOICES
    )
    main_goal = models.TextField("What is your main goal for enrolling your child in this program?")
    consideration_range = models.CharField(
        "This is a structured 12-week private mentorship with an investment of $2400 total. Is this within your consideration range if it’s a strong fit?",
        max_length=1, 
        choices=CONSIDERATION_CHOICES
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent_name} - {self.parent_email}"
