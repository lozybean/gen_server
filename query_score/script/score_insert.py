#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2018/1/24 0024'

"""

import csv
import os
from collections import namedtuple

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gen_server.settings")
django.setup()

from query_score.models import UserScore


def insert_elementary_score():
    with open('初级班成绩', encoding='utf-8') as fp:
        header = next(fp)
        Row = namedtuple('Row', header)
        csv_reader = csv.reader(fp, delimiter='\t')
        for r in csv_reader:
            row = Row(*r)._asdict()
            score = UserScore(name=row['姓名'], id_card=row['身份证号'].lower(), exam_id=row['准考证号'],
                              score_theory=row['理论成绩'], score_major=row['专业成绩'],
                              score_case='无', score_major_total='无')
            score.save()


def insert_intermediate_score():
    with open('中级班成绩', encoding='utf-8') as fp:
        header = next(fp)
        Row = namedtuple('Row', header)
        csv_reader = csv.reader(fp, delimiter='\t')
        for r in csv_reader:
            row = Row(*r)._asdict()
            score = UserScore(name=row['姓名'], id_card=row['身份证号'].lower(), exam_id=row['准考证号'],
                              score_theory=row['理论成绩'], score_major=row['专业成绩'],
                              score_case=row['案例成绩'], score_major_total=row['专业总成绩'])
            score.save()


if __name__ == '__main__':
    insert_intermediate_score()
