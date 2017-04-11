from docutils import nodes
from docutils.parsers.rst import directives, Directive

def setup(app):
    app.add_directive('codesplain', Codesplain)
    app.add_node(CodesplainNode, html=(visit_codesplain_node, depart_codesplain_node))

TEMPLATE = """
<div data-component="codesplain" data-snippet="%(snippet_key)s" />
"""

class CodesplainNode(nodes.General, nodes.Element):
    def __init__(self, content):
        super(CodesplainNode, self).__init__()
        self.codesplain_content = content

def visit_codesplain_node(self, node):
    res = TEMPLATE % node.codesplain_content
    self.body.append(res)
def depart_codesplain_node(self, node):
    pass

class Codesplain(Directive):
    option_spec = {
        'snippet_key': directives.unchanged
    }
    def run(self):
        return [CodesplainNode(self.options)]
