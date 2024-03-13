from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied


class Blacklist(MiddlewareMixin):
       blacklists=[
            #   "127.0.0.1"
             "172.30.95.153"
       ]

       def process_request(self, request):
            print(request.META.get("REMOTE_ADDR"))
            ip=request.META.get("REMOTE_ADDR")
            if ip in self.blacklists:
                  raise PermissionDenied()
                  
                  
                  