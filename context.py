from main.models import State

print "loading"

def states_menu(request):

    print "loaded"

    states = State.objects.all()[:5]

    return {'states_menu': states}