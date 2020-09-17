def leaveRegisterForm(user_id):
    dialog = {
        "title": "Fill the form for Leave",
        "submit_label": "Submit",
        "callback_id": user_id,
        "elements": [
            {
                "label": "Subject",
                "type": "text",
                "name": "subject",
                "placeholder": "Subject for Leave",
            },
            {
                "label": "Description",
                "type": "textarea",
                "name": "body",
                "placeholder": "Reason for Leave",
            },
            {
                "label": "Type of Leave",
                "type": "select",
                "name": "leave_type",
                "options": [
                    {"label": "First Half", "value": "first_half"},
                    {"label": "Second Half", "value": "second_half"},
                    {"label": "Full Day", "value": "full_day"},
                ],
            },
        ],
    }
    return dialog


def leaveRegisterViewForm():
    view = {
        "type": "modal",
        "title": {"type": "plain_text", "text": "Ask for a  Leave"},
        "submit": {"type": "plain_text", "text": "Submit"},
        "blocks": [
            {
                "type": "input",
                "block_id": "a_block_id4",
                "label": {
                    "type": "plain_text",
                    "text": "A simple label",
                },
                "element": {
                    "type": "plain_text_input",
                    "action_id": "an_action_id",
                    "multiline": True,
                },
            },
            {
                "type": "input",
                "block_id": "a_block_id",
                "label": {
                    "type": "plain_text",
                    "text": "A simple label",
                },
                "element": {"type": "plain_text_input", "action_id": "an_action_id"},
            },
            {
                "type": "input",
                "block_id": "a_block_id2",
                "label": {
                    "type": "plain_text",
                    "text": "A simple label type",
                },
                "element": {"type": "plain_text_input", "action_id": "an_action_id"},
            },
            {
                "type": "section",
                "block_id": "section1234",
                "text": {"type": "mrkdwn", "text": "Pick a date for the deadline."},
                "accessory": {
                    "type": "datepicker",
                    "initial_date": "2020-09-17",
                    "action_id": "datepicker123",
                    "placeholder": {"type": "plain_text", "text": "Select a date"},
                },
            },
        ],
    }
    return view
