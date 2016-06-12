from cspreporter.core.plugins import LogFormat

class Simple(LogFormat):
    title = 'Clean up log'
    desc = 'This plugin cleans up log entries to JSON data only'
    enc = ''

    def setup(self):
        self.enc = self.config.get('plugins.logformats.simple', 'encoding')

    def process(self, s):
        tmp = s.decode(self.enc)
        return tmp[tmp.rfind('{"csp-report"'):]

    def teardown(self):
        pass
