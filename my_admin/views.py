from django.shortcuts import render

from users.models import CustomUser


def user_(request):
    user_list = CustomUser.objects.all()
    context = {

        'users': user_list,
    }

    return render(request, 'admin/admin_page.html', context)
