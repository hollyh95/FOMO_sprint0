class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.prods = []
        # One-time configuration and initialization.

    def __call__(self, request):
        request.session['lastFive'] = self.prods
        response = self.get_response(request)
        self.prods = request.session.get('lastFive')
        return response
