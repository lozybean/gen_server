#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2018/1/24 0024'

"""

from django.views import generic
from query_score.forms import UserScoreForm
from query_score.models import UserScore


# Create your views here.

class Home(generic.TemplateView):
    template_name = 'home.html'


class QueryView(generic.FormView):
    model_name = UserScore
    form_class = UserScoreForm
    template_name = 'query_score.html'

    def try_get_by_name(self, name: str):
        return self.model_name.objects.filter(name=name).first()

    def try_get_by_id_card(self, id_num: str):
        return self.model_name.objects.filter(id_card=id_num.lower()).first()

    def try_get_by_exam_id(self, exam_id: str):
        return self.model_name.objects.filter(exam_id=exam_id).first()

    def get_context_data(self, **kwargs):
        search_key = self.request.GET.get('keyword')
        context = super(QueryView, self).get_context_data(**kwargs)
        obj = self.try_get_by_name(search_key)
        if obj is None:
            obj = self.try_get_by_exam_id(search_key)
        if obj is None:
            obj = self.try_get_by_id_card(search_key)
        context.update(obj=obj)
        return context
