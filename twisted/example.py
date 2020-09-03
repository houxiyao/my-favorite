#  noqa: D100
from twisted.internet import defer, reactor


def getDummyData(inputData):  # noqa: D103
    print('getDummyData called')
    deferred = defer.Deferred()
    reactor.callLater(0, deferred.callback, inputData * 3)
    return deferred


def cbPrintData(result):  # noqa: D103
    print(f'Result received: {result}')


deferred = getDummyData(3)
deferred.addCallback(cbPrintData)

reactor.callLater(4, reactor.stop)

print('Starting the reactor')
reactor.run()
