async def leaveRegisterForm(user_id):
    dialog = {
        "title": "Fill the form for Leave",
        "submit_label": "Submit",
        "callback_id": user_id,
        "state": "leaveform",
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
            {
                "label": "Pick a date for leave.",
                "type": "text",
                "name": "date",
                "placeholder": "2020-02-05",
                "hint": "Date format YYYY-MM-DD, eg: 2020-02-05",
            },
        ],
    }
    return dialog


async def taskAddForm(user_id):
    dialog = {
        "title": "Add your task",
        "submit_label": "Submit",
        "callback_id": user_id,
        "state": "taskadd",
        "elements": [
            {
                "label": "Task Title",
                "type": "text",
                "name": "subject",
                "placeholder": "Title of task",
            },
            {
                "label": "Description",
                "type": "textarea",
                "name": "body",
                "placeholder": "description",
            },
            {
                "label": "Estimated Hours",
                "type": "select",
                "name": "estimated_hours",
                "options": [
                    {"label": "Ten Minutes", "value": "0.166"},
                    {"label": "Thirty Minutes", "value": "0.5"},
                    {"label": "One Houre", "value": "1"},
                    {"label": "Two Houre", "value": "2"},
                    {"label": "Three Houre", "value": "3"},
                    {"label": "Four Houre", "value": "4"},
                    {"label": "Five Houre", "value": "5"},
                    {"label": "Six Houre", "value": "6"},
                    {"label": "Seven Houre", "value": "7"},
                    {"label": "Two Days", "value": "14"},
                    {"label": "One Week", "value": "35"},
                ],
            },
        ],
    }
    return dialog


async def leaveRegisterViewForm(user_id):
    view = {
        "private_metadata": "leaveform",
        "type": "modal",
        "callback_id": user_id,
        "title": {"type": "plain_text", "text": "Ask for a  Leave"},
        "submit": {"type": "plain_text", "text": "Submit"},
        "blocks": [
            {
                "type": "input",
                "block_id": "a_block_id",
                "label": {
                    "type": "plain_text",
                    "text": "Subject",
                },
                "element": {"type": "plain_text_input", "action_id": "an_action_id"},
            },
            {
                "type": "input",
                "block_id": "a_block_id4",
                "label": {
                    "type": "plain_text",
                    "text": "Reason for Leave",
                },
                "element": {
                    "type": "plain_text_input",
                    "action_id": "an_action_id",
                    "multiline": True,
                },
            },
            {
                "type": "section",
                "block_id": "section1234",
                "text": {"type": "mrkdwn", "text": "Pick a date for leave."},
                "accessory": {
                    "type": "datepicker",
                    "initial_date": "2020-09-17",
                    "action_id": "datepicker123",
                    "placeholder": {"type": "plain_text", "text": "Select a date"},
                },
            },
            {
                "type": "section",
                "block_id": "section678",
                "text": {"type": "mrkdwn", "text": "Type of Leave"},
                "accessory": {
                    "action_id": "text1234",
                    "type": "static_select",
                    "placeholder": {"type": "plain_text", "text": "Select an item"},
                    "options": [
                        {
                            "text": {"type": "plain_text", "text": "First Half"},
                            "value": "first_half",
                        },
                        {
                            "text": {"type": "plain_text", "text": "Second Half"},
                            "value": "second_half",
                        },
                        {
                            "text": {"type": "plain_text", "text": "Full Day"},
                            "value": "full_day",
                        },
                    ],
                },
            },
        ],
    }
    return view
