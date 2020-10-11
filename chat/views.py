from django.shortcuts import render


def chat(request, room_name='general'):  # Will be add private room fo UserToUser
    return render(request, 'chat/chat.html', {
        'room_name': room_name
    })
