from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request, 'home.html')


def contacts(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		print(f'Ваши данные: имя - {name} телефон - {phone} сообщение - {message}')
	return render(request, 'contacts.html')
