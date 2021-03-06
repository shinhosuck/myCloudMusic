from django.shortcuts import render, redirect
from users.forms import UserRegisterForm, MessageForm



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
         form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def message(request):
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        if form.is_valid():
            form.save()
            # messages.success(request, f"Thank you very much for the message. I will get back to you as soon as possible.")
            return redirect("music:home")
        else:
            # messages.warning(request, f"Message did not sent. Please try again!")
            return redirect("music:home")