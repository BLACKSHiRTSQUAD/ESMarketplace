from django.core.management.base import BaseCommand

from ESMarketplace.esm.models import ExpertSystem, ESQuestion
from django.contrib.auth.models import User


class recreate_database_script(BaseCommand):
    def handle(self, **options):
        try:
            User.objects.get(username='juser')

        except User.DoesNotExist:
            u = User(username='juser', first_name='Jerry', last_name='Wdubs', email='jerry@example.com')

            es = ExpertSystem(owner=u, title="Troubleshoot PC Internet Connectivity", cost=110.00)

            esq1 = ESQuestion(es_id=es, qa_text="Try to access google.com. What's the response?")

            esq2 = ESQuestion(prev_question_id=esq1, prev_choice_text="408 Request Timed Out",
                              qa_text="Can you ping 8.8.8.8?")

            esq3 = ESQuestion(prev_question_id=esq1, prev_choice_text="400 Page Not Found",
                              qa_text="Are you sure you typed the URL correctly?")

            esq4 = ESQuestion(prev_question_id=esq1, prev_choice_text="200 Successful",
                              qa_text="Done. You are connected to the internet.", leaf=True)

            esq5 = ESQuestion(prev_question_id=esq2, prev_choice_text="Timed out.",
                              qa_text="Uh-oh. That's not good.")


