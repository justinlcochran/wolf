from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Role, Player, RoleAssignment, WolfNumber, RoleType
from .forms import PlayerForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random

@login_required(login_url='/wolfapp/login')
def index(request):
	role_list = Role.objects.all()
	role_types = RoleType.objects.all()
	player_form = PlayerForm()
	player_list = Player.objects.all()
	wolfcount = WolfNumber.objects.all()[0].number
	role_assignments = RoleAssignment.objects.all()
	game_score = 0
	for i in role_assignments:
		game_score += i.role_score
	down = -1
	up = 1

	if "Submit" in request.POST:
		if request.method == 'POST':
			form = PlayerForm(request.POST)
			if form.is_valid():
				form.save()

	context = {
		'role_list': role_list,
		'role_types': role_types,
		'wolfcount': wolfcount,
		'player_form': player_form,
		'player_list': player_list,
		'down': down,
		'up': up,
		'role_assignments': role_assignments,
		'game_score': game_score,

	}

	return render(request, 'wolfapp/index.html', context)


def delete(request, pk):

	player = Player.objects.get(id=pk)
	if request.method == "POST":
		player.delete()
		return redirect('/wolfapp')

	context = {'player': player,

	           }
	return render(request, 'wolfapp/delete_player.html', context)

def roll(request):
	role_types = RoleType.objects.filter(toggle=True)
	role_list = Role.objects.filter(role_type_id__in=role_types)
	player_list = list(Player.objects.all())
	wolfcount = WolfNumber.objects.all()[0].number

	negative_town_roles = [i for i in role_list if i.role_score < 0 and i.role_alignment == "Town"]
	positive_town_roles = [i for i in role_list if i.role_score >= 0]
	wolf_roles = [i for i in role_list if i.role_type_id == "Wolf"]

	RoleAssignment.objects.filter(locked=False).delete()
	locked_game = list(RoleAssignment.objects.all())
	roles_list = []
	locked_roles = []
	for i in locked_game:
		roles_list.append(Role.objects.filter(role_title=i.role_title).get())
		locked_roles.append(Role.objects.filter(role_title=i.role_title).get())

	print(roles_list)

	new_wolfcount = wolfcount - len([i for i in roles_list if i.role_alignment == "Evil"])
	print(new_wolfcount)

	RoleAssignment.objects.all().delete()

	for i in range(new_wolfcount):
		roles_list.append(random.choice(wolf_roles))
	while len(player_list) > len(roles_list):
		game_score = 0
		for i in roles_list:
			game_score += i.role_score
		if game_score > 0:
			roles_list.append(random.choice(negative_town_roles))
		elif game_score <= 0:
			roles_list.append(random.choice(positive_town_roles))

	game_score = 0
	for i in roles_list:
		game_score += i.role_score
	random.shuffle(roles_list)
	random.shuffle(player_list)
	for i in range(len(roles_list)):
		form = RoleAssignment(player_name=player_list[i].name, role_title=roles_list[i].role_title, role_alignment=roles_list[i].role_alignment, role_score=roles_list[i].role_score, role_description=roles_list[i].role_description, locked=True if roles_list[i] in locked_roles else False)
		form.save()
	return redirect('/wolfapp')


def wolfcounter(request, direction):
	wolfcount = WolfNumber.objects.all()[0].number
	WolfNumber.objects.all().delete()
	form = WolfNumber(number=wolfcount+int(direction))
	form.save()
	return redirect('/wolfapp')

def update_toggle(request, pk):
	role_type = RoleType.objects.get(id=pk)
	if role_type.toggle:
		role_type.toggle = False
		role_type.save()
	else:
		role_type.toggle = True
		role_type.save()
	return redirect('/wolfapp')

def update_lock(request, pk):
	role_type = RoleAssignment.objects.get(id=pk)
	if role_type.locked:
		role_type.locked = False
		role_type.save()
	else:
		role_type.locked = True
		role_type.save()
	return redirect('/wolfapp')

def loginPage(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/wolfapp')

		else:
			messages.info(request, "Username or Password is incorrect")


	context = {}
	return render(request, 'wolfapp/login.html', context)

def logoutPage(request):
	logout(request)
	return redirect('/wolfapp/login')

def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, "Account Created: " + user)
			return redirect('/wolfapp/login')

	context = {'form': form,}
	return render(request, 'wolfapp/register.html', context)