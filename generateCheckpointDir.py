"""
Daniel Walther
creation date: 23.08.2023 (dd.mm.yyyy)
purpose: generate the checkpoint directory string
"""


def get_date_yy_mm_dd():
    date_string_test_dummy = '230823'
    date_string = date_string_test_dummy  # TBD: get today's date, format it to yymmdd
    return date_string


def get_todays_session_id(date):
    session_id = 0
    existing_session_id_test_dummy = 2
    existing_session_id = -1  # This value should not change if there is no (training) session checkpoint dir yet for today.
    existing_session_id = existing_session_id_test_dummy  # TBD: find some way of knowing today's existing checkpoint dir's session id on the cluster (does not have to involve communicating with the cluster)

    while session_id <= existing_session_id:
        session_id += 1

    return session_id
