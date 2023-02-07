from django.conf import settings

def ioi_settings(request):
    return {'settings': {
        'SITE_TITLE': 'Task Translation System',
        'CONTEST_TITLE': 'Kódkupa -- IIOT Válogatóverseny',
        'TIME_ZONE': settings.TIME_ZONE,
        'IMAGES_URL': '/media/images/',
    }}
