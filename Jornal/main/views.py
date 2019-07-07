from django.shortcuts import render, render_to_response
from django.contrib import auth




def main(request):
    args = {}
    args['username'] = auth.get_user(request).username
    return render_to_response('main.html', args)



