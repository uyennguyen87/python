'''
Created on Jan 29, 2016

@author: ncuyen
'''
class WhatIHave:
    def g(self): pass
    def h(self): pass

class WhatIWant:
    def f(self): pass

class ProxyAdapter(WhatIWant):
    def __init__(self, what_i_have):
            self.what_i_have = what_i_have
    
    def f(self):
        # Implement behavior using
        # method in WhatIHave
        self.g()
        self.h()

class WhatIUse:
    def op(self, what_i_want):
        what_i_want.f()

# Approach 2: build adapter use into op():
class WhatIUse2:
    def op(self, what_i_have):
        ProxyAdapter(what_i_have).f()
    
# Approach 3:  build adapter into WhatIHave
class WhatIHave2(WhatIHave, WhatIWant):
    def f(self):
        self.g()
        self.h()

# Approach 4: use a inner class:
class WhatIHave3(WhatIHave):
    class InnerAdapter(WhatIWant):
        def __init__(self, outer):
            self.outer = outer
        
        def f(self):
            self.outer.g()
            self.outer.h()

    def what_i_want(self):
        return WhatIHave3.InnerAdapter(self)

if __name__ == '__main__':
    what_i_use = WhatIUse()
    what_i_have = WhatIHave()
    adapter = ProxyAdapter(what_i_have)
    what_i_use_2 = WhatIUse2()
    what_i_have_2 = WhatIHave2()
    what_i_have_3 = WhatIHave3()
    
    # Approach 1:
    what_i_use.op(adapter)
    
    # Approach 2:
    what_i_use_2(what_i_have_2)
    
    # Approach 3:
    what_i_use.op(what_i_have_2)
    
    # Approach 4:
    what_i_use.op(what_i_have_3.what_i_want())