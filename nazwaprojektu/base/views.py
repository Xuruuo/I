from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Computer
from .forms import ComputerForm, RoomForm
from django.contrib import messages


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def computer_list(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    computers = room.computers.all()
    return render(request, 'computer_list.html', {'room': room, 'computers': computers})

def computer_detail(request, computer_id):
    computer = get_object_or_404(Computer, id=computer_id)
    return render(request, 'computer_detail.html', {'computer': computer})

def room_add(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'room_add.html', {'form': form})

def computer_edit(request, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            computer = form.save()
            return redirect('computer_detail', pk=computer.pk)
    else:
        form = ComputerForm(instance=computer)
    return render(request, 'computer_management/computer_edit.html', {'form': form, 'computer': computer})

def computer_delete(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    room_pk = computer.room.pk
    computer.delete()
    messages.success(request, 'Komputer został usunięty.')
    return redirect('room_detail', pk=room_pk)

def computer_add(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            computer = form.save()
            return redirect('computer_detail', pk=computer.pk)
    else:
        form = ComputerForm()
    return render(request, 'computer_add.html', {'form': form})