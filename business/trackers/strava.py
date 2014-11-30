__author__ = 'pdiazv'

from django.core.urlresolvers import reverse
from stravalib.client import Client
from business import conf
from repository import context


class StravaTracker(object):

    auth_view = 'strava_auth'

    def get_auth_url(self):
        client = Client()

        path = reverse('{0}:{1}'.format(conf.auth_namespace, self.auth_view))
        redirect_to = '{0}{1}'.format(conf.auth_domain, path)

        return client.authorization_url(client_id=conf.strava['client_id'], redirect_uri=redirect_to)


    def add_tracker(self, user_id, code):
        client = Client()
        token = client.exchange_code_for_token(
            client_id=conf.strava['client_id'],
            client_secret=conf.strava['secret'],
            code=code)

        client.access_token = token
        athlete = client.get_athlete()

        return context.UserContext().add_tracker(user_id, {
            'name': 'strava',
            'token': token,
            'client_id': str(athlete.id)
        })


