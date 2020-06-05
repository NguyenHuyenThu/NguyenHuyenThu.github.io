from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined','hihih'])

print(Subscriber)

sub = Subscriber("vuong", ['xuan', 'phung'],'vuong')

print(sub)