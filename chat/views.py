from django.shortcuts import render


def chat(request):
    return render(request, 'chat/chat.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
