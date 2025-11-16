from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UserCreateForm, UserUpdateForm


def user_list(request):
    """List all users"""
    users = UserProfile.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_detail(request, pk):
    """View user details"""
    user = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})


def user_create(request):
    """Create new user"""
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Store password securely if password field exists
            if 'password' in form.cleaned_data:
                user.password_hash = form.cleaned_data['password']
            user.save()
            messages.success(request, f'User "{user.first_name} {user.last_name}" created successfully!')
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserCreateForm()
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Create User'})


def user_update(request, pk):
    """Update existing user"""
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Edit User'})


def user_delete(request, pk):
    """Delete user"""
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
