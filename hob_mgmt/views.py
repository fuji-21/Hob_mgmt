from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Hob_mgmt
from .forms import InputForm, AddForm
from .createqr import createQR

class InputView(View):
    def get(self, request, *args, **kwargs):
        form = InputForm(request.POST or None)

        return render(request, 'hob_mgmt/input.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = InputForm(request.POST or None)
        if form.is_valid():
            serial_no = request.POST.get('serial_no', '')  # 製品番号を取得
            results = Hob_mgmt.objects.filter(serial_no=serial_no)  # 製品番号で検索
        return render(request, 'hob_mgmt/send.html', {
            'results': results
        })


class ListView(View):
    def get(self, request, *args, **kwargs):
        hob_mgmt_data = Hob_mgmt.objects.order_by('blade_thickness')

        return render(request, 'hob_mgmt/list.html', {
            'hob_mgmt_data': hob_mgmt_data,
        })

class AddView(View):
    def get(self, request, *args, **kwargs):
        form = AddForm(request.POST or None)

        return render(request, 'hob_mgmt/add.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = AddForm(request.POST or None)

        if form.is_valid():
            Hob_mgmt_data = Hob_mgmt()
            Hob_mgmt_data.tool = form.cleaned_data['tool']
            Hob_mgmt_data.serial_no = form.cleaned_data['serial_no']
            Hob_mgmt_data.pg_no = form.cleaned_data['pg_no']
            Hob_mgmt_data.blade_thickness = form.cleaned_data['blade_thickness']
            Hob_mgmt_data.axial_rake_angle = form.cleaned_data['axial_rake_angle']
            Hob_mgmt_data.save()
            createQR(Hob_mgmt_data.pg_no)
        return redirect('list')

class SendView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'hob_mgmt/send.html', {
        })

class EditView(View):
    def get(self, request, *args, **kwargs):
        hob_mgmt_data = Hob_mgmt.objects.get(id=self.kwargs['pk'])
        form = AddForm(
            request.POST or None,
            initial={
                'tool': hob_mgmt_data.tool,
                'serial_no': hob_mgmt_data.serial_no,
                'pg_no': hob_mgmt_data.pg_no,
                'blade_thickness': hob_mgmt_data.blade_thickness,
                'axial_rake_angle': hob_mgmt_data.axial_rake_angle,
            }
        )

        return render(request, 'hob_mgmt/edit.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = AddForm(request.POST or None)

        if form.is_valid():
            Hob_mgmt_data = Hob_mgmt.objects.get(id=self.kwargs['pk'])
            Hob_mgmt_data.tool = form.cleaned_data['tool']
            Hob_mgmt_data.serial_no = form.cleaned_data['serial_no']
            Hob_mgmt_data.pg_no = form.cleaned_data['pg_no']
            Hob_mgmt_data.blade_thickness = form.cleaned_data['blade_thickness']
            Hob_mgmt_data.axial_rake_angle = form.cleaned_data['axial_rake_angle']
            Hob_mgmt_data.save()
            createQR(Hob_mgmt_data.pg_no)

            return redirect('list')
        return render('edit', self.kwargs['pk'])

class DeleteView(View):
    def get(self, request, *args, **kwargs):
        hob_mgmt_data = Hob_mgmt.objects.get(id=self.kwargs['pk'])
        hob_mgmt_data.delete()
        return redirect('list')