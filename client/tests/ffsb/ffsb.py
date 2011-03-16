import os
from autotest_lib.client.bin import test, utils

class ffsb(test.test):
    version = 1

    def initialize(self):
        self.job.require_gcc()

    # http://sourceforge.net/projects/ffsb/files/ffsb/ffsb-6.0-rc2/ffsb-6.0-rc2.tar.bz2
    def setup(self, tarball = 'ffsb-6.0-rc2.tar.bz2'):
        self.tarball = utils.unmap_url(self.bindir, tarball, self.tmpdir)
        utils.extract_tarball_to_dir(self.tarball, self.srcdir)

        os.chdir(self.srcdir)
        utils.system('./configure')
        utils.system('make')

    def get_ffsbs(self):
        for filename in os.listdir(self.bindir):
            (base, ext) = os.path.splitext(filename)
            if ext != '.ffsb':
                continue
            yield filename

    def run_once(self, dir=None, profiles=None):
        if not dir:
            dir = self.tmpdir
        if profiles is None:
            profiles = self.get_ffsbs()
        os.chdir(dir)
        ffsb = os.path.join(self.srcdir, 'ffsb')
        for profile in profiles:
            # profiles can be either relative or absolute paths,
            # either will work
            path = os.path.join(self.bindir, profile)
            utils.system('%s %s' % (ffsb, path))
