api.log('use action:sys_assertContains')
# api.log('Assert %s contains %s' % (p1, p2))
api.log('Assert %s contains ' % (p1))
for p in p2:
    api.log('%s ' % (p))
obj = p1 = sys_resolveFromVar(context, p1)
for p3 in p2:
    p3 = sys_resolveFromVar(context, p3)
    if not isinstance(obj, collections.Iterable):
        obj = str(obj)
    if isinstance(p3, basestring):
        if not isinstance(obj, basestring):
            obj = [str(e) if not isinstance(e, basestring) else e for e in obj]
    elif isinstance(obj, basestring):
        p3 = str(p3)
    if p3 in obj:
        api.log('True: %s contains %s',(p,p3))
        sys_assertResult(context, True, 'Assert Success')
        api.exit_on(0)
        # api.log('Assert Failed')
        # sys_assertResult(context, False, 'Assert Fail: %s contains %s' % (p1, p3))
        # api.exit_on(0)
    else:
        api.log('%s not contains %s', (p, p3))

api.log('Assert Failed')
sys_assertResult(context, False, 'Assert Fail: %s contains %s' % (p1, p3))
api.exit_on(0)
