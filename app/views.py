from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.edit import CreateView

from .models import Profesor

# Create your views here.


class ProfesorCreate(CreateView):
    model = Profesor
    template_name = "app/index.html"
    fields = ('__all__')
    success_url = '.'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesores'] = Profesor.objects.all()
        return context
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            data = list(context['profesores'].values())
            return JsonResponse({'profesores': data})
        else:
            response_kwargs.setdefault('content_type', self.content_type)
            return self.response_class(
                request= self.request,
                template = self.get_template_names(),
                context=context,
                using=self.template_engine,
                **response_kwargs
            )
            
        
