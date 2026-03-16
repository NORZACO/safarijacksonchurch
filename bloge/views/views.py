# pylint: disable=unused-argument
from django.shortcuts import redirect, render

import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from ..models import Post, AboutUs, Member, Gallery, MenuOver, EventMission, Album
from django import forms
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, "bloge/index.html")


def NoPage(request):
    return HttpResponse(
        """<a class="btn btn-primary" href="#" role="button">Link</a>
    """
    )


def libraries(request):
    album = Album.objects.all()
    return render(request, 'bloge/libraries.html', {'album': album})


#teachings
def teachings(request):
    #menu_datas = MenuOver.objects.all()
    return render(request, 'bloge/teachings.html')


def news(request):
    return render(request, 'bloge/news.html')


def menu(request):
    menu_datas = MenuOver.objects.all()
    return render(request, 'bloge/menu.html', {'menu_datas': menu_datas})


def events(request):
    events = EventMission.objects.all()
    return render(request, 'bloge/events.html', {'events': events})


def about(request):
    about_data = AboutUs.objects.filter(status='published').first()  #
    context = {'about_data': about_data}
    return render(request, 'bloge/about.html', context)


def service(request):
    return render(request, 'bloge/service.html')


def members(request):
    members = Member.objects.all()
    return render(request, 'bloge/members.html', {'members': members})


def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'bloge/gallery.html', {'images': images})


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name',
        'required': True
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email',
        'required': True
    }))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject',
        'required': True
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 6,
        'placeholder': 'Message',
        'required': True
    }))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print(name, email, subject, message)
            # Send email
            send_mail(
                subject,
                message,
                email,  # From email
                [settings.EMAIL_HOST_USER],  # To email
                fail_silently=False,
            )

            # Render success page or message
            return render(request, 'bloge/success.html')
    else:
        form = ContactForm()

    return render(request, 'bloge/contact.html', {'form': form})


def post_list(request):
    posts = Post.objects.all().order_by('-publish_date')
    return render(request, 'bloge/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'bloge/post_detail.html', {'post': post})


def donations(request):
    return render(request, 'bloge/donation.html')


def success(request):
    return render(request, 'bloge/success.html')


def cancel(request):
    return render(request, 'bloge/cancel.html')


@csrf_exempt
def create_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': settings.STRIPE_PRICE_ID,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.DOMAIN_URL + '/success/',
            cancel_url=settings.DOMAIN_URL + '/cancel/',
        )
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    return redirect(checkout_session.url, code=303) # type: ignore
