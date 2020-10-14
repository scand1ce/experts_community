from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def chat(request, room_name='general'):  # Will be add private room fo UserToUser
    return render(request, 'chat/chat.html', {
        'room_name': room_name
    })
