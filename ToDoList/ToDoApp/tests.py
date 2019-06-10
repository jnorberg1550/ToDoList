from django.test import TestCase
from django.contrib auth.models.User
from django.urls import reverse
from models import ListType
import datetime


class ListTypeTest(TestCase):
   #set up one time sample data
  class ListTypeTest(TestCase):
    def test_string(self):
       type=ListType(listtitle='Shopping')
       self.assertEqual(str(ListType), type.listtitle)

    def test_string(self):
       type=ListType(listcreatedate='6-10-2019')
       self.assertEqual(str(ListType), type.listcreatedate)

    def test_string(self):
       type=ListType(listcreatetime='12:15')
       self.assertEqual(str(ListType), type.listcreatetime)

    def test_string(self):
       type=ListType(listitem='toothpaste')
       self.assertEqual(str(ListType), type.listitem)

    def test_string(self):
       type=ListType(listduedate='6-12-2019')
       self.assertEqual(str(ListType), type.listduedate)

    def test_string(self):
       type=ListType(listduetime='15:00')
       self.assertEqual(str(ListType), type.listduetime)

    def test_string(self):
       type=ListType(listpriority='Urgent')
       self.assertEqual(str(ListType), type.listpriority)

   
   
   
   
        