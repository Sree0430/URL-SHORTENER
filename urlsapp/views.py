import random, string
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ShortURL
from .forms import ShortenForm

ALPHABET = string.ascii_letters + string.digits

def generate_code(n=6):
    return ''.join(random.choice(ALPHABET) for _ in range(n))

def index(request):
    form = ShortenForm()
    recent = ShortURL.objects.order_by('-id')[:10]  # show recent 10 links
    last_short = request.session.get('last_short')
    return render(request, 'urlsapp/index.html', {'form': form, 'recent': recent, 'last_short': last_short})

def shorten(request):
    if request.method != 'POST':
        return redirect('index')

    form = ShortenForm(request.POST)
    if form.is_valid():
        long_url = form.cleaned_data['long_url']
        custom = form.cleaned_data.get('custom')
        if custom:
            code = custom
        else:
            for _ in range(8):
                code = generate_code()
                if not ShortURL.objects.filter(code=code).exists():
                    break

        su = ShortURL.objects.create(long_url=long_url, code=code)
        short_url = request.build_absolute_uri(reverse('follow', args=[su.code]))
        request.session['last_short'] = short_url
        return redirect('index')
    else:
        recent = ShortURL.objects.order_by('-id')[:10]
        return render(request, 'urlsapp/index.html', {'form': form, 'recent': recent})

def follow(request, code):
    try:
        su = ShortURL.objects.get(code=code)
    except ShortURL.DoesNotExist:
        return redirect('index')
    su.clicks += 1
    su.save(update_fields=['clicks'])
    return HttpResponseRedirect(su.long_url)
