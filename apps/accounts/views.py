from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, View, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from apps.erp.models import FinancialReceivableTitles
from .models import CustomerUser, MonitorNetwork
from .forms import CustomerUserForm
import json


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'



class MonitorNetworkDashboardView(LoginRequiredMixin, ListView):
    template_name = 'accounts/monitor_network/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        qs = self.get_queryset()
        try:
            if qs.count() > 1:
                return super().dispatch(request, *args, **kwargs)
            else:
                q = qs.first()
                return HttpResponseRedirect(reverse('accounts:monitor_network_detail', kwargs={'pk': q.pk}))
        except:
            return redirect('accounts:profile')

    def get_queryset(self):
        qs = MonitorNetwork.objects.filter(
            is_excluded = False,
            partner = self.request.user.partneruser.partner.id
        )
        return qs



class MonitorNetworkDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/monitor_network/detail.html'
    model = MonitorNetwork

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().partner == self.request.user.partneruser.partner:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('accounts:profile')



class CustomerUserListView(LoginRequiredMixin, ListView):
    template_name = 'accounts/customer_user/list.html'
    paginate_by = 30

    def get_queryset(self):
        qs = CustomerUser.objects.filter(
            is_excluded = False,
            provided_by = self.request.user.partneruser.partner.id
        )
        return qs
  


class CustomerUserCreateView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/customer_user/form.html'
    form_class = CustomerUserForm
    model = CustomerUser
    success_url = reverse_lazy('accounts:customeruser_list')

    def form_valid(self, form):
        data = form.save(commit=False)
        data.provided_by = self.request.user.partneruser.partner
        data.created_by = self.request.user
        data.save()        
        return super().form_valid(form)



class CustomerUserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/customer_user/form.html'
    form_class = CustomerUserForm
    model = CustomerUser
    success_url = reverse_lazy('accounts:customeruser_list')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().provided_by == self.request.user.partneruser.partner:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('accounts:customeruser_list')



class CustomerUserDeleteView(LoginRequiredMixin, View):

    def get(self, request, pk):
        data = dict()
        customer = CustomerUser.objects.get(id = pk)

        try:
            if customer.provided_by == self.request.user.partneruser.partner:
                customer.is_excluded = True
                customer.save()

                data['error'] = False
            else:
                data['error'] = True
        except:
            data['error'] = True
        return JsonResponse(data)



class CustomerUserChangeStatusView(LoginRequiredMixin, View):

    def get(self, request, pk):
        data = dict()
        customer = CustomerUser.objects.get(id = pk)
        
        try:
            customer = CustomerUser.objects.get(pk = pk)
            
            if customer.provided_by == self.request.user.partneruser.partner:
                if customer.status == '1':
                    customer.status = '2'

                elif customer.status == '2':
                    customer.status = '1'
            
            else:
                data['error'] = True
            
            customer.save()
            data['error'] = False
        except:
            data['error'] = True
        
        return JsonResponse(data)



class CustomerUserUpdatePassword(LoginRequiredMixin, View):

    def post(self, request):
        data = dict()
        
        try:
            body = json.loads(request.body.decode('utf-8'))
            
            customer = CustomerUser.objects.get(pk = body['form_id'])
            customer.password = body['new_password']
            customer.save()
            data['error'] = False
        except:
            data['error'] = True
        
        return JsonResponse(data)



class FinancialDashboardView(LoginRequiredMixin, ListView):
    template_name = 'accounts/financial/dashboard.html'
    paginate_by = 10
    
    def get_queryset(self):
        qs = FinancialReceivableTitles.objects.using('erp').filter(
            p_is_receivable = 1,
            deleted = 0,
            contract__id = self.request.user.partneruser.partner.erp_contract_code
        )
        return qs
