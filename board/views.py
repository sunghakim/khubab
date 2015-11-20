
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from board.models import Board
from django.utils import timezone
# Create your views here.


def board(request):
	list_final = Board.objects.all().order_by('-pk')
	return render(request, 'free_board.html', {'list_final': list_final})


def view(request, board_id):
	pop = get_object_or_404(Board, pk = board_id)
	next_id = pop.id + 1
	prev_id = pop.id - 1
	last = Board.objects.latest('pk')
	last_id = last.id +1
	return render(request, 'view.html', {'pop': pop, 'next_id':next_id, 'prev_id':prev_id, 'last_id': last_id})

def write(request):
	return render(request, 'write.html')

def write_board(request):
	write_data = Board (writer = request.POST.get('_writer', False),
						title = request.POST.get('_title', False),
						board_contents = request.POST.get('_board_contents', False),
						board_date = timezone.now()
						)
	write_data.save()

	url = '/board/'
	return HttpResponseRedirect(url) 