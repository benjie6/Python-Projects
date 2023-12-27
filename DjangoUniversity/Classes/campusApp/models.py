from django.db import models


# Creates model of university campus
class UniversityCampus(models.Model):
    Campus_name = models.CharField(max_length=50, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)

    # Create object Manager
    object = models.Manager()

    def __str__(self):
        display_class = '{0.Campus_name}: {0.state}'
        return display_class.format(self)

    # removes added 's'
    class Meta:
        verbose_name_plural = "University Campus"



