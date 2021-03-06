from django.views import View
from rest_framework import status
from datetime import datetime, timezone
from django.http import JsonResponse
from django.db import connection


class HealthCheckCustom(View):
    """
    Support function for health check
    """

    def get(self, *args, **kwargs):
        utc_time = datetime.now(timezone.utc)
        local_time = utc_time.astimezone()
        offset = local_time.utcoffset().total_seconds()
        if offset == 0.0:
            offset = "None"

        db_name = connection.settings_dict['NAME']

        with connection.cursor() as cursor:
            cursor.execute("select 1")
            one = cursor.fetchone()[0]
            if one != 1:
                raise Exception('The site did not pass the health check')
            return JsonResponse({"status": "Work",
                                 "components": {
                                     "db": {
                                         "status": "Work",
                                         "name": db_name,
                                         "database": "PostgreSQL"
                                     },
                                     "ping": {
                                         "status": "Work"
                                     },
                                     "time": {
                                         "epoch": int(utc_time.timestamp()),
                                         "local": local_time.isoformat(),
                                         "offset": offset
                                     }
                                 }}, status=status.HTTP_200_OK)
