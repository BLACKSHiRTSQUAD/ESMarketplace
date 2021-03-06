import os, sys
sys.path.append('/home/rewazi/PycharmProjects/ESMarketplace/ESMarketplace')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ESMarketplace.ESMarketplace.settings")
import django
django.setup()

from esm.models import ExpertSystem, ESQuestion, ESCategoryTwo, ESCategoryThree, Company
from django.contrib.auth.models import User


try:
    User.objects.get(username='juser')
    print("TRY")

except User.DoesNotExist:
    print("EXCEPT")

    company = Company(name="GLOBAL")
    company.save()

    company2 = Company(name="Jerry's Test Global")
    company2.save()

    u = User.objects.create_user(username='juser', first_name='Jerry', last_name='Wdubs', email='jerry@example.com',
                                 password='password', is_superuser=True, is_staff=True)
    u.profile.company = company
    u.save()



    u2 = User.objects.create_user(username='customer', first_name='customer', last_name='customer',
                                  email='customer@customer.com',
                                  password='password')
    u2.profile.company = company2
    u2.save()
    ##########################################################
    esc3 = ESCategoryTwo(category_title="Numbers", category_one_id=company)
    esc3.save()
    esc4 = ESCategoryTwo(category_title="PC", category_one_id=company)
    esc4.save()
    esc5 = ESCategoryTwo(category_title="Networking", category_one_id=company)
    esc5.save()

    esc6 = ESCategoryThree(category_title="Other", category_two_id=esc3)
    esc6.save()
    esc7 = ESCategoryThree(category_title="Networking", category_two_id=esc4)
    esc7.save()
    esc8 = ESCategoryThree(category_title="Systems", category_two_id=esc5)
    esc8.save()
    esc9 = ESCategoryThree(category_title="Programming", category_two_id=esc5)
    esc9.save()

    ##########################################################


    es = ExpertSystem(owner=u, company=company, title="Troubleshoot PC Internet Connectivity", category_id=esc7)
    es.save()

    es2 = ExpertSystem(owner=u, company=company, title="Guess Your Number, 1 to 100", category_id=esc6)
    es2.save()

    ##########################################################
    # es
    esq1 = ESQuestion(es_id=es, qa_text="Try to access google.com. What's the response?")
    esq1.save()

    esq2 = ESQuestion(prev_question_id=esq1, prev_choice_text="408 Request Timed Out",
                      qa_text="Can you ping 8.8.8.8?")
    esq2.save()

    esq3 = ESQuestion(prev_question_id=esq1, prev_choice_text="400 Page Not Found",
                      qa_text="Are you sure you typed the URL correctly?")
    esq3.save()

    esq4 = ESQuestion(prev_question_id=esq1, prev_choice_text="200 Successful",
                      qa_text="Done. You are connected to the internet.", leaf=True)
    esq4.save()

    esq5 = ESQuestion(prev_question_id=esq2, prev_choice_text="Timed out.",
                      qa_text="Uh-oh. That's not good.")
    esq5.save()

    ##########################################################
    # es2
    esq2_1 = ESQuestion(es_id=es2, qa_text="Choose first correct choice.")
    esq2_1.save()
    esq2_2 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 10. Only this option is done!")
    esq2_2.save()
    esq2_3 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 20")
    esq2_3.save()
    esq2_4 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 30")
    esq2_4.save()
    esq2_5 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 40")
    esq2_5.save()
    esq2_6 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 50")
    esq2_6.save()
    esq2_7 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 60")
    esq2_7.save()
    esq2_8 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 70")
    esq2_8.save()
    esq2_9 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 80")
    esq2_9.save()
    esq2_10 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 90")
    esq2_10.save()
    esq2_11 = ESQuestion(prev_question_id=esq2_1, prev_choice_text="Less than 100. It better be. That's the point!")
    esq2_11.save()
    esq2_31 = ESQuestion(prev_question_id=esq2_2, prev_choice_text="Below or equal to 5. Only this one, sorry.")
    esq2_31.save()
    esq2_32 = ESQuestion(prev_question_id=esq2_2, prev_choice_text="Greater than 5.")
    esq2_32.save()
    esq2_33 = ESQuestion(prev_question_id=esq2_31, prev_choice_text="1, 2, or 3.")
    esq2_33.save()
    esq2_34 = ESQuestion(prev_question_id=esq2_31, prev_choice_text="4 or 5.")
    esq2_34.save()
    esq2_35 = ESQuestion(prev_question_id=esq2_34, prev_choice_text="4?")
    esq2_35.save()
    esq2_36 = ESQuestion(prev_question_id=esq2_34, prev_choice_text="Ok. Then 5.")
    esq2_36.save()
    esq2_37 = ESQuestion(prev_question_id=esq2_33, prev_choice_text="3.")
    esq2_37.save()
    esq2_38 = ESQuestion(prev_question_id=esq2_33, prev_choice_text="2.")
    esq2_38.save()
    esq2_39 = ESQuestion(prev_question_id=esq2_33, prev_choice_text="1.")
    esq2_39.save()
    esq2_40 = ESQuestion(prev_question_id=esq2_33, prev_choice_text="BOOM!!!")
    esq2_40.save()
    esq2_41 = ESQuestion(prev_question_id=esq2_40, prev_choice_text="Just kidding. You're a hero. You saved the day. Go you!")
    esq2_41.save()



