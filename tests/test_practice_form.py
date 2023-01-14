from demoqa_tests.model.data.user import obojealexander
from demoqa_tests.model.pages.practice_form import PracticeForm


def test_registration_user():
    practice_form = PracticeForm(obojealexander)
    practice_form.open_page()
    (practice_form.fill_name()
        .fill_contacts()
        .select_gender()
        .select_birthday()
        .input_subject()
        .select_hobbies()
        .send_image()
        .input_address()
        .select_state()
        .select_city()
        .submit())
    practice_form.assert_results_registration()