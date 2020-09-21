from leaveapp.models import Leave, Task


def create_leave(payload_obj):
    leave_obj = Leave.objects.create(
        title=payload_obj["submission"]["subject"],
        description=payload_obj["submission"]["body"],
        leave_type=payload_obj["submission"]["leave_type"],
        user_name=payload_obj["user"]["name"],
        leave_date=payload_obj["submission"]["date"],
        response_url=payload_obj["response_url"],
    )
    return leave_obj


def create_task(payload_obj):
    task_obj = Task.objects.create(
        title=payload_obj["submission"]["subject"],
        description=payload_obj["submission"]["body"],
        estimated_hour=payload_obj["submission"]["estimated_hours"],
        user_name=payload_obj["user"]["name"],
        response_url=payload_obj["response_url"],
    )
    return task_obj
