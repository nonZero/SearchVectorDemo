from django.views.generic import ListView

from stuff.models import Row


class Home(ListView):
    model = Row
    paginate_by = 50

    def term(self):
        return self.request.GET.get('q', '')

    def get_queryset(self):
        return super().get_queryset().filter(sv=self.term())

    def paginate_queryset(self, queryset, page_size):
        return super().paginate_queryset(queryset, page_size)

    # def total(self):
    #     return Row.objects.count()  # too slow!!!
