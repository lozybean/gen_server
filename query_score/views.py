#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2018/1/24 0024'

"""

from annoying.functions import get_object_or_None
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

    def try_get_by_name(self, name):
        return get_object_or_None(self.model_name, name=name)

    def try_get_by_id_card(self, id_num):
        return get_object_or_None(self.model_name, id_card=id_num)

    def try_get_by_exam_id(self, exam_id):
        return get_object_or_None(self.model_name, exam_id=exam_id)

    def get_context_data(self, search_key, **kwargs):
        context = super(QueryView, self).get_context_data(**kwargs)
        obj = self.try_get_by_name(search_key)
        if obj is None:
            obj = self.try_get_by_exam_id(search_key)
        if obj is None:
            obj = self.try_get_by_id_card(search_key)
        context.update(obj=obj)
        return context
