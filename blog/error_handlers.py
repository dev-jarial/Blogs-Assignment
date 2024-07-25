from django.shortcuts import render

def custom_403_error(request, exception):
    return render(request, '403.html', status=403)
