import os
from autotest_lib.client.bin import test, utils

class direct_io_test(test.test):
    version = 1

    def initialize(self):
        self.job.require_gcc()

    def setup(self):
        os.mkdir(self.srcdir)
        os.chdir(self.srcdir)
        utils.system('cp ' + self.bindir+'/direct_io_test.c .')
        cmd = 'gcc -Wall direct_io_test.c -o direct_io_test'
        utils.system(cmd)

    def run_once(self, dir=None):
        if not dir:
            dir = self.tmpdir
        os.chdir(dir)
        direct_io_test = os.path.join(self.srcdir, 'direct_io_test')
        utils.system(direct_io_test)
