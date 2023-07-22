from django.db import models


class Hob_mgmt(models.Model):
    tool = models.CharField("ホブツールNo", max_length=20)
    serial_no = models.CharField("製造番号", max_length=10)
    pg_no = models.CharField("プログラムNo", max_length=20)
    blade_thickness = models.DecimalField("刃厚", max_digits=3, decimal_places=1)
    axial_rake_angle = models.DecimalField("向芯度・すくい角", max_digits=2, decimal_places=1)


    def __str__(self):
        return self.tool