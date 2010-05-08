from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class add_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"add", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)
            
class choice_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"choice", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class corr_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"corr", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class damage_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"damage", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class del_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"del", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class gap_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"gap", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class handshift_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"handshift", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class orig_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"orig", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class reg_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"reg", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class restore_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"restore", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class sic_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"sic", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class subst_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"subst", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class supplied_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"supplied", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class unclear_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"unclear", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

