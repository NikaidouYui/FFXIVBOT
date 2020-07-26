from django.http import HttpResponseRedirect

from Otter import settings
from otterbot.oauth_client import OAuthQQ


def qq_login(req):
    oauth_qq = OAuthQQ(settings.QQ_APP_ID, settings.QQ_KEY, settings.QQ_RECALL_URL)
    url = oauth_qq.get_auth_url()
    return HttpResponseRedirect(url)
