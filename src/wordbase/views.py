# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from random import randrange

from .models import Word


def main(request):
    return render(request, 'wordbase/main.html')


def index(request):
    words_list = Word.objects.order_by('-pk')
    context = {'words_list': words_list}
    return render(request, 'wordbase/index.html', context)


def add_word(request):
    return HttpResponse('View: add_word')


def edit_word(request):
    return HttpResponse('View: edit_word')


def run_test(request):
    id_list = Word.objects.values_list('pk', flat=True)
    random_id = id_list[randrange(0, len(id_list))]
    return HttpResponseRedirect(f'{Word.objects.get(pk=random_id).id}/test')


def test(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    # return HttpResponse(f'View: test, word_id: {word_id}')
    return render(request, 'wordbase/test.html', {'word': word})


def reply(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    try:
        answer = request.POST['answer']
    except (KeyError, Word.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'wordbase/test.html', {
            'word': word,
            'error_message': "You didn't write a answer.",
        })
    else:
        word.last_question = timezone.now()
        word.num_answer += 1
        correct_answer = False
        if answer.upper() == word.name.upper():
            correct_answer = True
            word.num_correct += 1
        word.save()
        return render(request, 'wordbase/reply.html', {
            'word': word,
            'correct_answer': correct_answer,
            'answer': answer,
        })
