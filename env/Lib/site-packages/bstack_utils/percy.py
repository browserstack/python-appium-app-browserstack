# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11ll1ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1ll1_opy_):
    global bstack111ll11_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack1ll111_opy_ = bstack1ll1_opy_ [:-1]
    bstack11l111l_opy_ = bstack11ll1l_opy_ % len (bstack1ll111_opy_)
    bstack11l1l1l_opy_ = bstack1ll111_opy_ [:bstack11l111l_opy_] + bstack1ll111_opy_ [bstack11l111l_opy_:]
    if bstack1111l11_opy_:
        bstack111l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack1l111l1_opy_ + bstack11ll1l_opy_) % bstack11ll1ll_opy_) for bstack1l111l1_opy_, char in enumerate (bstack11l1l1l_opy_)])
    else:
        bstack111l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack1l111l1_opy_ + bstack11ll1l_opy_) % bstack11ll1ll_opy_) for bstack1l111l1_opy_, char in enumerate (bstack11l1l1l_opy_)])
    return eval (bstack111l1ll_opy_)
import os
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1l111l1l1_opy_, bstack1ll1ll1l1_opy_
class bstack111l1l1l_opy_:
  working_dir = os.getcwd()
  bstack1lll11ll11_opy_ = False
  config = {}
  binary_path = bstack1lllll1_opy_ (u"ࠩࠪᐢ")
  bstack1lllllll1l1_opy_ = bstack1lllll1_opy_ (u"ࠪࠫᐣ")
  bstack111111l1_opy_ = False
  bstack111111l111_opy_ = None
  bstack1lllll1ll1l_opy_ = {}
  bstack1111111lll_opy_ = 300
  bstack1llllllllll_opy_ = False
  logger = None
  bstack1lllll1l11l_opy_ = False
  bstack1llllll1l11_opy_ = bstack1lllll1_opy_ (u"ࠫࠬᐤ")
  bstack1111111ll1_opy_ = {
    bstack1lllll1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬᐥ") : 1,
    bstack1lllll1_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧᐦ") : 2,
    bstack1lllll1_opy_ (u"ࠧࡦࡦࡪࡩࠬᐧ") : 3,
    bstack1lllll1_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨᐨ") : 4
  }
  def __init__(self) -> None: pass
  def bstack111111ll11_opy_(self):
    bstack1lllll1llll_opy_ = bstack1lllll1_opy_ (u"ࠩࠪᐩ")
    bstack1lllllll1ll_opy_ = sys.platform
    bstack11111l1l1l_opy_ = bstack1lllll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᐪ")
    if re.match(bstack1lllll1_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦᐫ"), bstack1lllllll1ll_opy_) != None:
      bstack1lllll1llll_opy_ = bstack11l11ll1l1_opy_ + bstack1lllll1_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨᐬ")
      self.bstack1llllll1l11_opy_ = bstack1lllll1_opy_ (u"࠭࡭ࡢࡥࠪᐭ")
    elif re.match(bstack1lllll1_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧᐮ"), bstack1lllllll1ll_opy_) != None:
      bstack1lllll1llll_opy_ = bstack11l11ll1l1_opy_ + bstack1lllll1_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤᐯ")
      bstack11111l1l1l_opy_ = bstack1lllll1_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧᐰ")
      self.bstack1llllll1l11_opy_ = bstack1lllll1_opy_ (u"ࠪࡻ࡮ࡴࠧᐱ")
    else:
      bstack1lllll1llll_opy_ = bstack11l11ll1l1_opy_ + bstack1lllll1_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢᐲ")
      self.bstack1llllll1l11_opy_ = bstack1lllll1_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫᐳ")
    return bstack1lllll1llll_opy_, bstack11111l1l1l_opy_
  def bstack11111l11l1_opy_(self):
    try:
      bstack1lllllll111_opy_ = [os.path.join(expanduser(bstack1lllll1_opy_ (u"ࠨࡾࠣᐴ")), bstack1lllll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᐵ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1lllllll111_opy_:
        if(self.bstack1llllll11ll_opy_(path)):
          return path
      raise bstack1lllll1_opy_ (u"ࠣࡗࡱࡥࡱࡨࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧᐶ")
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦᐷ").format(e))
  def bstack1llllll11ll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1lllll1l1ll_opy_(self, bstack1lllll1llll_opy_, bstack11111l1l1l_opy_):
    try:
      bstack111111111l_opy_ = self.bstack11111l11l1_opy_()
      bstack1111111l1l_opy_ = os.path.join(bstack111111111l_opy_, bstack1lllll1_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰ࡽ࡭ࡵ࠭ᐸ"))
      bstack1lllll1lll1_opy_ = os.path.join(bstack111111111l_opy_, bstack11111l1l1l_opy_)
      if os.path.exists(bstack1lllll1lll1_opy_):
        self.logger.info(bstack1lllll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡶ࡯࡮ࡶࡰࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨᐹ").format(bstack1lllll1lll1_opy_))
        return bstack1lllll1lll1_opy_
      if os.path.exists(bstack1111111l1l_opy_):
        self.logger.info(bstack1lllll1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡿ࡯ࡰࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡶࡰࡽ࡭ࡵࡶࡩ࡯ࡩࠥᐺ").format(bstack1111111l1l_opy_))
        return self.bstack111111l1l1_opy_(bstack1111111l1l_opy_, bstack11111l1l1l_opy_)
      self.logger.info(bstack1lllll1_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭ࠡࡽࢀࠦᐻ").format(bstack1lllll1llll_opy_))
      response = bstack1ll1ll1l1_opy_(bstack1lllll1_opy_ (u"ࠧࡈࡇࡗࠫᐼ"), bstack1lllll1llll_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack1111111l1l_opy_, bstack1lllll1_opy_ (u"ࠨࡹࡥࠫᐽ")) as file:
          file.write(response.content)
        self.logger.info(bstack1lllll1_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡧ࡮ࡥࠢࡶࡥࡻ࡫ࡤࠡࡣࡷࠤࢀࢃࠢᐾ").format(bstack1111111l1l_opy_))
        return self.bstack111111l1l1_opy_(bstack1111111l1l_opy_, bstack11111l1l1l_opy_)
      else:
        raise(bstack1lllll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧ࠱ࠤࡘࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠼ࠣࡿࢂࠨᐿ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧᑀ").format(e))
  def bstack111111l11l_opy_(self, bstack1lllll1llll_opy_, bstack11111l1l1l_opy_):
    try:
      retry = 2
      bstack1lllll1lll1_opy_ = None
      bstack11111lll11_opy_ = False
      while retry > 0:
        bstack1lllll1lll1_opy_ = self.bstack1lllll1l1ll_opy_(bstack1lllll1llll_opy_, bstack11111l1l1l_opy_)
        bstack11111lll11_opy_ = self.bstack11111111ll_opy_(bstack1lllll1llll_opy_, bstack11111l1l1l_opy_, bstack1lllll1lll1_opy_)
        if bstack11111lll11_opy_:
          break
        retry -= 1
      return bstack1lllll1lll1_opy_, bstack11111lll11_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡸࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡵࡧࡴࡩࠤᑁ").format(e))
    return bstack1lllll1lll1_opy_, False
  def bstack11111111ll_opy_(self, bstack1lllll1llll_opy_, bstack11111l1l1l_opy_, bstack1lllll1lll1_opy_, bstack111111ll1l_opy_ = 0):
    if bstack111111ll1l_opy_ > 1:
      return False
    if bstack1lllll1lll1_opy_ == None or os.path.exists(bstack1lllll1lll1_opy_) == False:
      self.logger.warn(bstack1lllll1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡳࡧࡷࡶࡾ࡯࡮ࡨࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠦᑂ"))
      return False
    bstack1llllllll11_opy_ = bstack1lllll1_opy_ (u"ࠢ࡟࠰࠭ࡄࡵ࡫ࡲࡤࡻ࡟࠳ࡨࡲࡩࠡ࡞ࡧ࠲ࡡࡪࠫ࠯࡞ࡧ࠯ࠧᑃ")
    command = bstack1lllll1_opy_ (u"ࠨࡽࢀࠤ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧᑄ").format(bstack1lllll1lll1_opy_)
    bstack1lllllll11l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1llllllll11_opy_, bstack1lllllll11l_opy_) != None:
      return True
    else:
      self.logger.error(bstack1lllll1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡤ࡭ࡱ࡫ࡤࠣᑅ"))
      return False
  def bstack111111l1l1_opy_(self, bstack1111111l1l_opy_, bstack11111l1l1l_opy_):
    try:
      working_dir = os.path.dirname(bstack1111111l1l_opy_)
      shutil.unpack_archive(bstack1111111l1l_opy_, working_dir)
      bstack1lllll1lll1_opy_ = os.path.join(working_dir, bstack11111l1l1l_opy_)
      os.chmod(bstack1lllll1lll1_opy_, 0o755)
      return bstack1lllll1lll1_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡵ࡯ࡼ࡬ࡴࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᑆ"))
  def bstack11111ll1l1_opy_(self):
    try:
      percy = str(self.config.get(bstack1lllll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᑇ"), bstack1lllll1_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦᑈ"))).lower()
      if percy != bstack1lllll1_opy_ (u"ࠨࡴࡳࡷࡨࠦᑉ"):
        return False
      self.bstack111111l1_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᑊ").format(e))
  def bstack11111l1ll1_opy_(self):
    try:
      bstack11111l1ll1_opy_ = str(self.config.get(bstack1lllll1_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫᑋ"), bstack1lllll1_opy_ (u"ࠤࡤࡹࡹࡵࠢᑌ"))).lower()
      return bstack11111l1ll1_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽࠥࡩࡡࡱࡶࡸࡶࡪࠦ࡭ࡰࡦࡨ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᑍ").format(e))
  def init(self, bstack1lll11ll11_opy_, config, logger):
    self.bstack1lll11ll11_opy_ = bstack1lll11ll11_opy_
    self.config = config
    self.logger = logger
    if not self.bstack11111ll1l1_opy_():
      return
    self.bstack1lllll1ll1l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᑎ"), {})
    self.bstack11111ll1ll_opy_ = config.get(bstack1lllll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨᑏ"), bstack1lllll1_opy_ (u"ࠨࡡࡶࡶࡲࠦᑐ"))
    try:
      bstack1lllll1llll_opy_, bstack11111l1l1l_opy_ = self.bstack111111ll11_opy_()
      bstack1lllll1lll1_opy_, bstack11111lll11_opy_ = self.bstack111111l11l_opy_(bstack1lllll1llll_opy_, bstack11111l1l1l_opy_)
      if bstack11111lll11_opy_:
        self.binary_path = bstack1lllll1lll1_opy_
        thread = Thread(target=self.bstack1lllllllll1_opy_)
        thread.start()
      else:
        self.bstack1lllll1l11l_opy_ = True
        self.logger.error(bstack1lllll1_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡲࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡶࡰࡧࠤ࠲ࠦࡻࡾ࠮࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡖࡥࡳࡥࡼࠦᑑ").format(bstack1lllll1lll1_opy_))
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᑒ").format(e))
  def bstack1llllll1111_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1lllll1_opy_ (u"ࠩ࡯ࡳ࡬࠭ᑓ"), bstack1lllll1_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰࡯ࡳ࡬࠭ᑔ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡕࡻࡳࡩ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࡴࠢࡤࡸࠥࢁࡽࠣᑕ").format(logfile))
      self.bstack1lllllll1l1_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࠡࡲࡤࡸ࡭࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᑖ").format(e))
  def bstack1lllllllll1_opy_(self):
    bstack1llllll111l_opy_ = self.bstack11111l111l_opy_()
    if bstack1llllll111l_opy_ == None:
      self.bstack1lllll1l11l_opy_ = True
      self.logger.error(bstack1lllll1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡺ࡯࡬ࡧࡱࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠤᑗ"))
      return False
    command_args = [bstack1lllll1_opy_ (u"ࠢࡢࡲࡳ࠾ࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠣᑘ") if self.bstack1lll11ll11_opy_ else bstack1lllll1_opy_ (u"ࠨࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠬᑙ")]
    bstack1llllll1l1l_opy_ = self.bstack1llllllll1l_opy_()
    if bstack1llllll1l1l_opy_ != None:
      command_args.append(bstack1lllll1_opy_ (u"ࠤ࠰ࡧࠥࢁࡽࠣᑚ").format(bstack1llllll1l1l_opy_))
    env = os.environ.copy()
    env[bstack1lllll1_opy_ (u"ࠥࡔࡊࡘࡃ࡚ࡡࡗࡓࡐࡋࡎࠣᑛ")] = bstack1llllll111l_opy_
    bstack111111lll1_opy_ = [self.binary_path]
    self.bstack1llllll1111_opy_()
    self.bstack111111l111_opy_ = self.bstack1llllll1lll_opy_(bstack111111lll1_opy_ + command_args, env)
    self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠧᑜ"))
    bstack111111ll1l_opy_ = 0
    while self.bstack111111l111_opy_.poll() == None:
      bstack1111111111_opy_ = self.bstack11111ll11l_opy_()
      if bstack1111111111_opy_:
        self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠣᑝ"))
        self.bstack1llllllllll_opy_ = True
        return True
      bstack111111ll1l_opy_ += 1
      self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡘࡥࡵࡴࡼࠤ࠲ࠦࡻࡾࠤᑞ").format(bstack111111ll1l_opy_))
      time.sleep(2)
    self.logger.error(bstack1lllll1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡼࡿࠣࡥࡹࡺࡥ࡮ࡲࡷࡷࠧᑟ").format(bstack111111ll1l_opy_))
    self.bstack1lllll1l11l_opy_ = True
    return False
  def bstack11111ll11l_opy_(self, bstack111111ll1l_opy_ = 0):
    try:
      if bstack111111ll1l_opy_ > 10:
        return False
      bstack111111llll_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࠨᑠ"), bstack1lllll1_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡯ࡳࡨࡧ࡬ࡩࡱࡶࡸ࠿࠻࠳࠴࠺ࠪᑡ"))
      bstack1lllll1ll11_opy_ = bstack111111llll_opy_ + bstack11l11l11l1_opy_
      response = requests.get(bstack1lllll1ll11_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack11111l111l_opy_(self):
    bstack11111l1lll_opy_ = bstack1lllll1_opy_ (u"ࠪࡥࡵࡶࠧᑢ") if self.bstack1lll11ll11_opy_ else bstack1lllll1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᑣ")
    bstack11l111l111_opy_ = bstack1lllll1_opy_ (u"ࠧࡧࡰࡪ࠱ࡤࡴࡵࡥࡰࡦࡴࡦࡽ࠴࡭ࡥࡵࡡࡳࡶࡴࡰࡥࡤࡶࡢࡸࡴࡱࡥ࡯ࡁࡱࡥࡲ࡫࠽ࡼࡿࠩࡸࡾࡶࡥ࠾ࡽࢀࠦᑤ").format(self.config[bstack1lllll1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᑥ")], bstack11111l1lll_opy_)
    uri = bstack1l111l1l1_opy_(bstack11l111l111_opy_)
    try:
      response = bstack1ll1ll1l1_opy_(bstack1lllll1_opy_ (u"ࠧࡈࡇࡗࠫᑦ"), uri, {}, {bstack1lllll1_opy_ (u"ࠨࡣࡸࡸ࡭࠭ᑧ"): (self.config[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᑨ")], self.config[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᑩ")])})
      if response.status_code == 200:
        bstack1lllll1l1l1_opy_ = response.json()
        if bstack1lllll1_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᑪ") in bstack1lllll1l1l1_opy_:
          return bstack1lllll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᑫ")]
        else:
          raise bstack1lllll1_opy_ (u"࠭ࡔࡰ࡭ࡨࡲࠥࡔ࡯ࡵࠢࡉࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠭ᑬ").format(bstack1lllll1l1l1_opy_)
      else:
        raise bstack1lllll1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡳࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡷࡹࡧࡴࡶࡵࠣ࠱ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡇࡵࡤࡺࠢ࠰ࠤࢀࢃࠢᑭ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡲࡵࡳ࡯࡫ࡣࡵࠤᑮ").format(e))
  def bstack1llllllll1l_opy_(self):
    bstack1llllll11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠤࡳࡩࡷࡩࡹࡄࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠧᑯ"))
    try:
      if bstack1lllll1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᑰ") not in self.bstack1lllll1ll1l_opy_:
        self.bstack1lllll1ll1l_opy_[bstack1lllll1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᑱ")] = 2
      with open(bstack1llllll11l1_opy_, bstack1lllll1_opy_ (u"ࠬࡽࠧᑲ")) as fp:
        json.dump(self.bstack1lllll1ll1l_opy_, fp)
      return bstack1llllll11l1_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡦࡶࡪࡧࡴࡦࠢࡳࡩࡷࡩࡹࠡࡥࡲࡲ࡫࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᑳ").format(e))
  def bstack1llllll1lll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll1l11_opy_ == bstack1lllll1_opy_ (u"ࠧࡸ࡫ࡱࠫᑴ"):
        bstack111111l1ll_opy_ = [bstack1lllll1_opy_ (u"ࠨࡥࡰࡨ࠳࡫ࡸࡦࠩᑵ"), bstack1lllll1_opy_ (u"ࠩ࠲ࡧࠬᑶ")]
        cmd = bstack111111l1ll_opy_ + cmd
      cmd = bstack1lllll1_opy_ (u"ࠪࠤࠬᑷ").join(cmd)
      self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡗࡻ࡮࡯࡫ࡱ࡫ࠥࢁࡽࠣᑸ").format(cmd))
      with open(self.bstack1lllllll1l1_opy_, bstack1lllll1_opy_ (u"ࠧࡧࠢᑹ")) as bstack1llllll1ll1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1llllll1ll1_opy_, text=True, stderr=bstack1llllll1ll1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllll1l11l_opy_ = True
      self.logger.error(bstack1lllll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠠࡸ࡫ࡷ࡬ࠥࡩ࡭ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᑺ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllllllll_opy_:
        self.logger.info(bstack1lllll1_opy_ (u"ࠢࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡓࡩࡷࡩࡹࠣᑻ"))
        cmd = [self.binary_path, bstack1lllll1_opy_ (u"ࠣࡧࡻࡩࡨࡀࡳࡵࡱࡳࠦᑼ")]
        self.bstack1llllll1lll_opy_(cmd)
        self.bstack1llllllllll_opy_ = False
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡰࡲࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡦࡳࡲࡳࡡ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᑽ").format(cmd, e))
  def bstack1l11ll11l1_opy_(self):
    if not self.bstack111111l1_opy_:
      return
    try:
      bstack11111l11ll_opy_ = 0
      while not self.bstack1llllllllll_opy_ and bstack11111l11ll_opy_ < self.bstack1111111lll_opy_:
        if self.bstack1lllll1l11l_opy_:
          self.logger.info(bstack1lllll1_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡨࡤ࡭ࡱ࡫ࡤࠣᑾ"))
          return
        time.sleep(1)
        bstack11111l11ll_opy_ += 1
      os.environ[bstack1lllll1_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡆࡊ࡙ࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࠪᑿ")] = str(self.bstack11111l1l11_opy_())
      self.logger.info(bstack1lllll1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠨᒀ"))
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᒁ").format(e))
  def bstack11111l1l11_opy_(self):
    if self.bstack1lll11ll11_opy_:
      return
    try:
      bstack11111l1111_opy_ = [platform[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᒂ")].lower() for platform in self.config.get(bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᒃ"), [])]
      bstack11111ll111_opy_ = sys.maxsize
      bstack11111111l1_opy_ = bstack1lllll1_opy_ (u"ࠩࠪᒄ")
      for browser in bstack11111l1111_opy_:
        if browser in self.bstack1111111ll1_opy_:
          bstack1111111l11_opy_ = self.bstack1111111ll1_opy_[browser]
        if bstack1111111l11_opy_ < bstack11111ll111_opy_:
          bstack11111ll111_opy_ = bstack1111111l11_opy_
          bstack11111111l1_opy_ = browser
      return bstack11111111l1_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡧ࡫ࡳࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᒅ").format(e))