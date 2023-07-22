from django import forms

class InputForm(forms.Form):
    serial_no = forms.CharField(max_length=10, label='serial_no')

class AddForm(forms.Form):
    tool = forms.CharField(max_length=20, label="ホブツールNo")
    serial_no = forms.CharField(max_length=10, label="製造番号")
    pg_no = forms.CharField(max_length=20, label="プログラムNo")
    blade_thickness = forms.DecimalField(max_digits=3, decimal_places=1, label="刃厚")
    axial_rake_angle = forms.DecimalField(max_digits=2, decimal_places=1, label="向芯度・すくい角")
