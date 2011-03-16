import os
from autotest_lib.client.bin import test, utils

class blogbench(test.test):
    version = 1

    def initialize(self):
        self.job.require_gcc()

    # http://download.pureftpd.org/pub/blogbench/blogbench-1.1.tar.bz2
    def setup(self, tarball='blogbench-1.1.tar.bz2'):
        self.tarball = utils.unmap_url(self.bindir, tarball, self.tmpdir)
        utils.extract_tarball_to_dir(self.tarball, self.srcdir)

        os.chdir(self.srcdir)
        utils.system('./configure')
        utils.system('make')

    def run_once(self, dir=None):
        if not dir:
            dir = self.tmpdir
        os.chdir(dir)
        utils.run(
            command=os.path.join(self.srcdir, 'src', 'blogbench'),
            args=[
                '-d',
                dir,
                ],
            stdout_tee=utils.TEE_TO_LOGS,
            stderr_tee=utils.TEE_TO_LOGS,
            )
