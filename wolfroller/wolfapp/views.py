from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Role, Choice, Question, Player
from .forms import PlayerForm


def index(request):
	role_list = Role.objects.all()
	role_types = list(set([i.role_type for i in role_list]))
	role_types.sort()
	form = PlayerForm()
	player_list = Player.objects.all()

	if "Submit" in request.POST:
		if request.method == 'POST':
			form = PlayerForm(request.POST)
			if form.is_valid():
				form.save()

	negative_town_roles = [i for i in role_list if
	                       i.game_score < 0 and i.role_alignment == "Town" or i.role_type == "Minion"]
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
		'form': form,
		'player_list': player_list,

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
	           'role_list': role_list,
	           'role_types': role_types,
	           'wolf_number': wolf_number,
	           'negative_town_roles': negative_town_roles,
	           'positive_town_roles': positive_town_roles,
	           'wolf_roles': wolf_roles,
	           'form': form,
	           'player_list': player_list,
	           }
	return render(request, 'wolfapp/delete_player.html', context)
