from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Role, Choice, Question, Player, RoleAssignment, WolfNumber
from .forms import PlayerForm
import random


def index(request):
	role_list = Role.objects.all()
	role_types = list(set([i.role_type for i in role_list]))
	role_types.sort()
	player_form = PlayerForm()
	player_list = Player.objects.all()
	wolfcount = WolfNumber.objects.all()[0].number
	role_assignments = RoleAssignment.objects.all()
	down = -1
	up = 1

	if "Submit" in request.POST:
		if request.method == 'POST':
			form = PlayerForm(request.POST)
			if form.is_valid():
				form.save()

	print(request.body)

	negative_town_roles = [i for i in role_list if i.game_score < 0 and i.role_alignment == "Town"]
	positive_town_roles = [i for i in role_list if 0 <= i.game_score]
	wolf_roles = [i for i in role_list if i.role_type == "Wolf"]
	wolf_number = 0

	context = {
		'role_list': role_list,
		'role_types': role_types,
		'wolf_number': wolf_number,
		'negative_town_roles': negative_town_roles,
		'positive_town_roles': positive_town_roles,
		'wolf_roles': wolf_roles,
		'player_form': player_form,
		'player_list': player_list,
		'wolfcount': wolfcount,
		'down': down,
		'up': up,
		'role_assignments': role_assignments,

	}

	return render(request, 'wolfapp/index.html', context)


def delete(request, pk):
	role_list = Role.objects.all()
	role_types = list(set([i.role_type for i in role_list]))
	role_types.sort()
	form = PlayerForm()
	player_list = Player.objects.all()

	negative_town_roles = [i for i in role_list if
	                       i.game_score < 0 and i.role_alignment == "Town" or i.role_type == "Minion"]
	positive_town_roles = [i for i in role_list if 0 <= i.game_score]
	wolf_roles = [i for i in role_list if i.role_type == "Wolf"]
	wolf_number = 0

	player = Player.objects.get(id=pk)
	if request.method == "POST":
		player.delete()
		return redirect('/wolfapp')

	context = {'player': player,

	           }
	return render(request, 'wolfapp/delete_player.html', context)

def roll(request):
	role_list = Role.objects.all()
	player_list = list(Player.objects.all())
	wolfcount = WolfNumber.objects.all()[0].number

	negative_town_roles = [i for i in role_list if i.game_score < 0 and i.role_alignment == "Town"]
	positive_town_roles = [i for i in role_list if i.game_score >= 0]
	wolf_roles = [i for i in role_list if i.role_type == "Wolf"]

	RoleAssignment.objects.all().delete()
	roles_list = []
	for i in range(wolfcount):
		roles_list.append(random.choice(wolf_roles))
	while len(player_list) > len(roles_list):
		game_score = 0
		for i in roles_list:
			game_score += i.game_score
		if game_score > 0:
			roles_list.append(random.choice(negative_town_roles))
		elif game_score <= 0:
			roles_list.append(random.choice(positive_town_roles))

	game_score = 0
	for i in roles_list:
		game_score += i.game_score
	random.shuffle(roles_list)
	random.shuffle(player_list)
	for i in range(len(roles_list)):
		form = RoleAssignment(player_name=player_list[i].name, role_title=roles_list[i].role_title, role_alignment=roles_list[i].role_alignment, role_score=roles_list[i].game_score)
		form.save()
	print(roles_list, player_list)
	return redirect('/wolfapp')


def wolfcounter(request, direction):
	wolfcount = WolfNumber.objects.all()[0].number
	WolfNumber.objects.all().delete()
	form = WolfNumber(number=wolfcount+int(direction))
	form.save()
	return redirect('/wolfapp')


