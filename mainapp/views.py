from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View, TemplateView
from django.views.generic.edit import CreateView
from .models import Slider, Menu, SubMenu, Context, Question
from .models import Personal, ArticleContext, Gallery, Images
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse


class CommonMixinExample(object):
    initial = {'key': 'value'}

    def get_context_data(self, **kwargs):
        kwargs['main'] = Menu.objects.get(pk=1)
        kwargs['services'] = Menu.objects.get(pk=2)
        kwargs['question'] = Menu.objects.get(pk=3)
        kwargs['gallery'] = Menu.objects.get(pk=4)
        kwargs['articles'] = Menu.objects.get(pk=5)
        kwargs['contact'] = Menu.objects.get(pk=6)
        kwargs['galleryimage'] = Gallery.objects.get(pk=1)
        kwargs['medpersonal'] = SubMenu.objects.get(id=19)
        kwargs['prices'] = SubMenu.objects.get(id=18)
        kwargs['workinghourcontact'] = SubMenu.objects.get(id=17)
        kwargs['contactus'] = SubMenu.objects.get(id=20)
        kwargs['services_subitem'] = kwargs['services'].submenu_set.all()
        kwargs['gallery_subitem '] = kwargs['gallery'].submenu_set.all()
        kwargs['articles_subitem'] = kwargs['articles'].submenu_set.all()
        kwargs['contact_subitem'] = kwargs['contact'].submenu_set.all()
        kwargs['gallery_images'] = kwargs['galleryimage'].images_set.order_by('id').all()
        kwargs['questions'] = Question.objects.all()
        kwargs['persons'] = Personal.objects.all()
        kwargs['slide'] = Slider.objects.all()
        kwargs['main_context'] = Context.objects.get(pk=1)
        kwargs['working_context'] = Context.objects.get(pk=3)
        kwargs['prices_context'] = Context.objects.get(pk=2)
        kwargs['allarticles'] = ArticleContext.objects.all()
        kwargs['forma'] = ContactForm(initial=self.initial)
        return super(CommonMixinExample, self).get_context_data(**kwargs)


class IndexView(CommonMixinExample, generic.ListView):
    template_name = 'mainapp/index.html'
    model = Menu


class QuestionCreate(CommonMixinExample, CreateView):
    model = Question
    template_name = 'mainapp/question_form.html'
    fields = ['name', 'email', 'question']
    success_url = reverse_lazy('mainapp:question-add')


class PersonalView(CommonMixinExample, generic.ListView):
    model = Personal
    template_name = 'mainapp/personal.html'


class DetailView(CommonMixinExample, generic.DetailView):
    model = Personal
    template_name = 'mainapp/detail.html'


class WorkingHours(CommonMixinExample, generic.ListView):
    model = Context
    template_name = 'mainapp/workinghour.html'


class Prices(CommonMixinExample, generic.ListView):
    model = Context
    template_name = 'mainapp/prices.html'


class ContactUs(CommonMixinExample, generic.ListView):
    template_name = 'mainapp/contact.html'
    model = Context

    def post(self, request):
        if request.method == 'POST':
            forma = ContactForm(request.POST)

            if forma.is_valid():
                username = forma.cleaned_data['username']
                message = forma.cleaned_data['message']
                email = forma.cleaned_data['email']
                recipients = ['auroch222@gmail.com']

                send_mail(username, message, email, recipients)
                return HttpResponseRedirect('/contactus/')

class Articles(CommonMixinExample, generic.ListView):
    model = ArticleContext
    template_name = 'mainapp/articles.html'


class ArticleDetail(CommonMixinExample, generic.DetailView):
    model = ArticleContext
    template_name = 'mainapp/articlesdetail.html'


class GalleryView(CommonMixinExample, generic.ListView):
    model = Gallery
    template_name = 'mainapp/gallery.html'


class ServicesView(CommonMixinExample, generic.DetailView):
    model = SubMenu
    template_name = 'mainapp/services.html'
