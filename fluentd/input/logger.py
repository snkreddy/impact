from fluent import sender
from fluent import event

sender.setup('debug.test', host='minikube.local.domino.tech', port=31000)
for i in range(1000):
  event.Event('', {
    'from': 'userA',
    'to': 'userB'
  })
