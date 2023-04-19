from django.shortcuts import render

# Create your views here.
def profile(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'user/profile.html', context=context_dict)
    