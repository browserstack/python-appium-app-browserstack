import subprocess, os, time, json,logging
import psutil

from browserstack.local_binary import LocalBinary
from browserstack.bserrors import BrowserStackLocalError

logger = logging.getLogger(__name__)
try:
    from importlib.metadata import version as package_version, PackageNotFoundError
except:
    import pkg_resources

class Local:
  def __init__(self, key=None, binary_path=None, **kwargs):
    self.key = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else key
    self.options = kwargs
    self.local_logfile_path = os.path.join(os.getcwd(), 'local.log')

  def __xstr(self, key, value):
    if key is None:
      return ['']
    if str(value).lower() == "true":
      return ['-' + key]
    elif str(value).lower() == "false":
      return ['']
    else:
      return ['-' + key, value]

  def get_package_version(self):
    name = "browserstack-local"
    version = 'None'
    use_fallback = False
    try:
        temp = package_version
    except NameError: # Only catch if package_version is not defined(and not other errors)
        use_fallback = True

    if use_fallback:
        try:
            version = pkg_resources.get_distribution(name).version
        except pkg_resources.DistributionNotFound:
            version = 'None'
    else:
        try:
            version = package_version(name)
        except PackageNotFoundError:
            version = 'None'

    return version

  def _generate_cmd(self):
    cmd = [self.binary_path, '-d', 'start', '-logFile', self.local_logfile_path, "-k", self.key, '--source', 'python:' + self.get_package_version()]
    for o in self.options.keys():
      if self.options.get(o) is not None:
        cmd = cmd + self.__xstr(o, self.options.get(o))
    return cmd

  def _generate_stop_cmd(self):
    cmd = self._generate_cmd()
    cmd[2] = 'stop'
    return cmd

  def start(self, **kwargs):
    for k, v in kwargs.items():
        self.options[k] = v

    if 'key' in self.options:
      self.key = self.options['key']
      del self.options['key']

    if 'binarypath' in self.options:
      self.binary_path = self.options['binarypath']
      del self.options['binarypath']
    else:
      self.binary_path = LocalBinary().get_binary()

    if 'logfile' in self.options:
      self.local_logfile_path = self.options['logfile']
      del self.options['logfile']

    if "onlyCommand" in kwargs and kwargs["onlyCommand"]:
      return

    if 'source' in self.options:
      del self.options['source']

    self.proc = subprocess.Popen(self._generate_cmd(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = self.proc.communicate()

    os.system('echo "" > "'+ self.local_logfile_path +'"')
    try:
      if out:
        output_string = out.decode()
      else:
        output_string = err.decode()

      data = json.loads(output_string)

      if data['state'] != "connected":
        raise BrowserStackLocalError(data["message"]["message"])
      else:
        self.pid = data['pid']
    except ValueError:
      logger.error("BinaryOutputParseError: Raw String = '{}'".format(output_string) )
      raise BrowserStackLocalError('Error parsing JSON output from daemon. Raw String = "{}"'.format(output_string))

  def isRunning(self):
    return hasattr(self, 'pid') and psutil.pid_exists(self.pid)

  def stop(self):
    try:
      proc = subprocess.Popen(self._generate_stop_cmd(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      (out, err) = proc.communicate()
    except Exception as e:
      return

  def __enter__(self):
    self.start(**self.options)
    return self

  def __exit__(self, *args):
    self.stop()
