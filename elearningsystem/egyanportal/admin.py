from django.contrib import admin
from .models import login
from .models import registration
from .models import Usm
# from .models import Assessment
from .models import uploadLecture
from .models import complaint
from .models import Feedback
from .models import Enquiry
from .models import noti
# Register your models here.
admin.site.register(login)
admin.site.register(registration)
admin.site.register(Usm)
# admin.site.register(Assessment)
admin.site.register(uploadLecture)
admin.site.register(complaint)
admin.site.register(Feedback)
admin.site.register(Enquiry)
admin.site.register(noti)


