import os
from autotest_lib.client.bin import test, os_dep, utils

class pjd_fstest(test.test):
    version = 1

    def initialize(self):
        self.job.require_gcc()

    # http://tuxera.com/sw/qa/pjd-fstest-20080816.tgz
    def setup(self, tarball='pjd-fstest-20080816.tgz'):
        self.tarball = utils.unmap_url(self.bindir, tarball, self.tmpdir)
        utils.extract_tarball_to_dir(self.tarball, self.srcdir)

        os.chdir(self.srcdir)
        utils.system('patch -p1 < ../urandom.patch')
        utils.system('make')

        # the TAP test harness runner from Perl
        os_dep.command('prove')

    def run_once(self, dir=None, profiles=None):
        if not dir:
            dir = self.tmpdir
        os.chdir(dir)
        utils.system('prove --failures -r %s' % os.path.join(self.srcdir, 'tests'))
