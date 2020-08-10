from django.shortcuts import render

from users.models import CustomUser


def get_user_list(request):
    user_list = CustomUser.objects.all()
    context = {
        'users': user_list,
    }

    return render(request, 'admin/admin_page.html', context)
