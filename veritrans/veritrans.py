
class VTDirect(object):

    def __init__(self, server_key, sandbox_mode=False):
        self.server_key = server_key
        self.sandbox_mode = sandbox_mode

    @property
    def base_url(self):
        ''' Returns the Veritrans base URL for API requests. '''
        return 'https://api.sandbox.veritrans.co.id/v2' if self.sandbox_mode \
            else 'https://api.veritrans.co.id/v2'

    def _build_payload(self, payment_type,
                       customer_details=None, billing_address=None,
                       shipping_address=None, item_details=[]):
        rv = {}
        rv['payment_type']
        return rv

    def submit_request(self, request):
        pass
