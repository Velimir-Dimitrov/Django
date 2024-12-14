# from django.db import models
# from django.contrib.auth import get_user_model
# from FiTrack.category.models import Category
#
# UserModel = get_user_model()
#
# # Create your models here.
# class Workout(models.Model):
#     account = models.ForeignKey(
#         to=UserModel,
#         on_delete=models.CASCADE,
#         related_name="workouts"
#     )
#
#     category = models.ForeignKey(
#         to=Category,
#         on_delete=models.SET_NULL,
#         null=True, related_name="workouts"
#     )
#
#     duration_minutes = models.PositiveIntegerField()
#
#     calories_burned = models.PositiveIntegerField()
#
#     date = models.DateField()