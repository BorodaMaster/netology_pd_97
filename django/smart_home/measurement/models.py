from django.db import models


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, null=False)
    description = models.CharField(max_length=50, null=True)

    def save(self, *args, **kwargs):
        super(Sensor, self).save(*args, **kwargs)


class Measurement(models.Model):
    sensor_id = models.ForeignKey('Sensor', related_name='measurement', on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    created_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Measurement, self).save(*args, **kwargs)
