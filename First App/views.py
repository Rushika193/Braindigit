from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Post

# Create your views here.
from django.utils import timezone
from django.views.generic import View


from django.template import loader
from django.urls import reverse
from .forms import PostForm


def index(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by("pub_date")
    return render(request, "a1/index.html", {"posts": posts})


def p_d(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, "a1/p_d.html", {"post": post})


def post_new(request):
    form = PostForm()
    return render(request, "a1/post_edit.html", {"form": form})


# def index(request):
# latest_question_list = Question.objects.order_by("-pub_date")[:5]
# template = loader.get_template("a1/index.html")
# context = {
#  "latest_question_list": latest_question_list,
# }
# return render(request, "a1/index.html", context)


# def detail(request, question_id):
# try:
#   question = get_object - or_404(Question, pk=question_id)
#  except Question.DoesNotExist:
#     raise Http404("Question does not exist")
# return render(request, "a1/detail.html", {"question": question})

#
# def results(request, question_id):
# question = get_object_or_404(Question, pk=question_id)
# return render(request, "a1/results.html", {"question": question})


# class IndexView(generic.ListView):
# template_name = "a1/index.html"
# context_object_name = "latest_question_list"

# def get_queryset(self):
#  return Question.objects.order_by("-pub_date")[:5]


# class DetailView(generic.DetailView):
#  model = Question
#  template_name = "a1/detail.html"


# class ResultsView(generic.DetailView):
#  model = Question
# template_name = "a1/results.html"


# def vote(result, question_id):
# question = get_object - or_404(Question, pk=question_id)
#  try:
#  selected_choice = question.choice_set.get(pk=request.POST["choice"])
#  except (KeyError, Choice.DoesNotExist):
# Redisplay the question voting form.
#  return render(
#     request,
#    "a1/detail.html",
#    {"question": question, "error_message": "You didn't select a choice.",},
# )
##else:
# selected_choice.votes += 1
# selected_choice.save()
# return HttpResponseRedirect(reverse("a1:results", args=(question.id,)))

