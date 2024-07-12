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
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
import tempfile
from packaging import version
from uuid import uuid4
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from bstack_utils.constants import *
from bstack_utils.percy import *
from browserstack_sdk.bstack1111l11l1_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1ll1ll11ll_opy_ import bstack1l1l11l11_opy_
import time
import requests
def bstack111111ll_opy_():
  global CONFIG
  headers = {
        bstack1lllll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩࡶ"): bstack1lllll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧࡷ"),
      }
  proxies = bstack1l11111ll_opy_(CONFIG, bstack1lll1ll11l_opy_)
  try:
    response = requests.get(bstack1lll1ll11l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1ll1l1ll_opy_ = response.json()[bstack1lllll1_opy_ (u"ࠬ࡮ࡵࡣࡵࠪࡸ")]
      logger.debug(bstack1ll1ll1l11_opy_.format(response.json()))
      return bstack1ll1l1ll_opy_
    else:
      logger.debug(bstack1l1l11l111_opy_.format(bstack1lllll1_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧࡹ")))
  except Exception as e:
    logger.debug(bstack1l1l11l111_opy_.format(e))
def bstack1l1l111111_opy_(hub_url):
  global CONFIG
  url = bstack1lllll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤࡺ")+  hub_url + bstack1lllll1_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣࡻ")
  headers = {
        bstack1lllll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡼ"): bstack1lllll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡽ"),
      }
  proxies = bstack1l11111ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1ll11ll1l1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l1ll1ll1_opy_.format(hub_url, e))
def bstack1ll11ll1_opy_():
  try:
    global bstack1l11l1ll11_opy_
    bstack1ll1l1ll_opy_ = bstack111111ll_opy_()
    bstack1l1lll1111_opy_ = []
    results = []
    for bstack1ll1111l11_opy_ in bstack1ll1l1ll_opy_:
      bstack1l1lll1111_opy_.append(bstack1l1lllll11_opy_(target=bstack1l1l111111_opy_,args=(bstack1ll1111l11_opy_,)))
    for t in bstack1l1lll1111_opy_:
      t.start()
    for t in bstack1l1lll1111_opy_:
      results.append(t.join())
    bstack1lll1l1111_opy_ = {}
    for item in results:
      hub_url = item[bstack1lllll1_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬࡾ")]
      latency = item[bstack1lllll1_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ࡿ")]
      bstack1lll1l1111_opy_[hub_url] = latency
    bstack1l11l11l1_opy_ = min(bstack1lll1l1111_opy_, key= lambda x: bstack1lll1l1111_opy_[x])
    bstack1l11l1ll11_opy_ = bstack1l11l11l1_opy_
    logger.debug(bstack1llll11l1_opy_.format(bstack1l11l11l1_opy_))
  except Exception as e:
    logger.debug(bstack1l1l11lll_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils import bstack1llll11111_opy_
from bstack_utils.config import Config
from bstack_utils.helper import bstack1l1111ll1_opy_, bstack1ll1ll1l1_opy_, bstack1l111l1l1_opy_, bstack1111l1l11_opy_, bstack11ll1l111_opy_, \
  Notset, bstack1ll1l1lll1_opy_, \
  bstack1l1lllllll_opy_, bstack1lll1lll11_opy_, bstack11l1111l1_opy_, bstack1111l1111_opy_, bstack11lll1ll1_opy_, bstack111l11l11_opy_, \
  bstack1l1ll1lll_opy_, \
  bstack111lll1l_opy_, bstack1lll111l1_opy_, bstack1lll11l11l_opy_, bstack1l1ll1ll11_opy_, \
  bstack1l1ll1ll1l_opy_, bstack1ll111l1l_opy_, bstack1l11ll1l1_opy_
from bstack_utils.bstack1l1l1lll1_opy_ import bstack11l1l11l1_opy_
from bstack_utils.bstack1llllll1ll_opy_ import bstack1ll1l111l1_opy_
from bstack_utils.bstack1lll1l1l1l_opy_ import bstack1l1l1ll11l_opy_, bstack11lll1lll_opy_
from bstack_utils.bstack1111l111_opy_ import bstack1lllll11_opy_
from bstack_utils.bstack1l1l1l1ll_opy_ import bstack1l1l1l1ll_opy_
from bstack_utils.proxy import bstack1llllllll_opy_, bstack1l11111ll_opy_, bstack1ll11lll1_opy_, bstack1lll11l11_opy_
import bstack_utils.bstack1lll1llll_opy_ as bstack1lll1111ll_opy_
from browserstack_sdk.bstack1ll1l111ll_opy_ import *
from browserstack_sdk.bstack1lll111lll_opy_ import *
from bstack_utils.bstack1ll1lll111_opy_ import bstack1l1l111ll1_opy_
bstack1ll11ll1ll_opy_ = bstack1lllll1_opy_ (u"࠭ࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࠦࠠࡪࡨࠫࡴࡦ࡭ࡥࠡ࠿ࡀࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮ࠦࡻ࡝ࡰࠣࠤࠥࡺࡲࡺࡽ࡟ࡲࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡹࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࡠࠬ࡬ࡳ࡝ࠩࠬ࠿ࡡࡴࠠࠡࠢࠣࠤ࡫ࡹ࠮ࡢࡲࡳࡩࡳࡪࡆࡪ࡮ࡨࡗࡾࡴࡣࠩࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭࠲ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡲࡢ࡭ࡳࡪࡥࡹࠫࠣ࠯ࠥࠨ࠺ࠣࠢ࠮ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࠫࡥࡼࡧࡩࡵࠢࡱࡩࡼࡖࡡࡨࡧ࠵࠲ࡪࡼࡡ࡭ࡷࡤࡸࡪ࠮ࠢࠩࠫࠣࡁࡃࠦࡻࡾࠤ࠯ࠤࡡ࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡧࡦࡶࡖࡩࡸࡹࡩࡰࡰࡇࡩࡹࡧࡩ࡭ࡵࠥࢁࡡ࠭ࠩࠪࠫ࡞ࠦ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠢ࡞ࠫࠣ࠯ࠥࠨࠬ࡝࡞ࡱࠦ࠮ࡢ࡮ࠡࠢࠣࠤࢂࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࢃ࡜࡯ࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴࠭ࢀ")
bstack1ll1lllll1_opy_ = bstack1lllll1_opy_ (u"ࠧ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࡟ࡲࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࡟ࡲࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࡡࡴࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁ࡜࡯࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࡠࡳࡺࡲࡺࠢࡾࡠࡳࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࡝ࡰࠣࠤࢂࠦࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࠢࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼ࡞ࡱࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥࡦࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠥࡽࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩࡾࡢ࠯ࡠࡳࠦࠠࠡࠢ࠱࠲࠳ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷࡡࡴࠠࠡࡿࠬࡠࡳࢃ࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳ࠭ࢁ")
from ._version import __version__
bstack1lll1l1ll_opy_ = None
CONFIG = {}
bstack1llll1lll_opy_ = {}
bstack11l1lll1l_opy_ = {}
bstack1l11ll11_opy_ = None
bstack11l11ll11_opy_ = None
bstack1l11111l_opy_ = None
bstack111ll1ll1_opy_ = -1
bstack111lll1l1_opy_ = 0
bstack1ll111111l_opy_ = bstack1l1l11ll1l_opy_
bstack1l1lll1l1l_opy_ = 1
bstack1ll1ll1l1l_opy_ = False
bstack111l1lll_opy_ = False
bstack1ll11l1l1l_opy_ = bstack1lllll1_opy_ (u"ࠨࠩࢂ")
bstack1l11ll11ll_opy_ = bstack1lllll1_opy_ (u"ࠩࠪࢃ")
bstack1l1l1lllll_opy_ = False
bstack111ll1ll_opy_ = True
bstack1ll1lllll_opy_ = bstack1lllll1_opy_ (u"ࠪࠫࢄ")
bstack1l11l1l11_opy_ = []
bstack1l11l1ll11_opy_ = bstack1lllll1_opy_ (u"ࠫࠬࢅ")
bstack1ll1llll_opy_ = False
bstack1ll11111l_opy_ = None
bstack1l1l11ll_opy_ = None
bstack1l1ll1ll_opy_ = None
bstack1ll1llll1l_opy_ = -1
bstack1l11l1111_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠬࢄࠧࢆ")), bstack1lllll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ࢇ"), bstack1lllll1_opy_ (u"ࠧ࠯ࡴࡲࡦࡴࡺ࠭ࡳࡧࡳࡳࡷࡺ࠭ࡩࡧ࡯ࡴࡪࡸ࠮࡫ࡵࡲࡲࠬ࢈"))
bstack11l1l1l11_opy_ = 0
bstack1ll1l11l1_opy_ = 0
bstack11llll111_opy_ = []
bstack1llll11ll1_opy_ = []
bstack1ll1l11ll1_opy_ = []
bstack111lll11_opy_ = []
bstack1lll1l11_opy_ = bstack1lllll1_opy_ (u"ࠨࠩࢉ")
bstack1l1l1ll1l1_opy_ = bstack1lllll1_opy_ (u"ࠩࠪࢊ")
bstack111l1ll11_opy_ = False
bstack11ll1llll_opy_ = False
bstack1ll111l1ll_opy_ = {}
bstack1l111ll1ll_opy_ = None
bstack11l1llll_opy_ = None
bstack1l1ll1l111_opy_ = None
bstack1l1ll11lll_opy_ = None
bstack111l11l1l_opy_ = None
bstack1ll11111_opy_ = None
bstack11l111111_opy_ = None
bstack11111l11l_opy_ = None
bstack1ll1l1l1_opy_ = None
bstack1llll11l1l_opy_ = None
bstack11llll1ll_opy_ = None
bstack1l1l11111_opy_ = None
bstack1l111111_opy_ = None
bstack1ll1lll1l1_opy_ = None
bstack11l1ll11l_opy_ = None
bstack1l11lll11l_opy_ = None
bstack1ll1l1llll_opy_ = None
bstack1l1lll111_opy_ = None
bstack1ll111111_opy_ = None
bstack11111l11_opy_ = None
bstack1l11l111_opy_ = None
bstack1lll1l11l1_opy_ = None
bstack11l11l1l1_opy_ = False
bstack11l11ll1l_opy_ = bstack1lllll1_opy_ (u"ࠥࠦࢋ")
logger = bstack1llll11111_opy_.get_logger(__name__, bstack1ll111111l_opy_)
bstack1111ll1ll_opy_ = Config.bstack1l11llll1_opy_()
percy = bstack111l1l1l_opy_()
bstack111111l1_opy_ = bstack1l1l11l11_opy_()
def bstack11l11l11_opy_():
  global CONFIG
  global bstack111l1ll11_opy_
  global bstack1111ll1ll_opy_
  bstack1lll111ll1_opy_ = bstack11111lll1_opy_(CONFIG)
  if bstack11ll1l111_opy_(CONFIG):
    if (bstack1lllll1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ࢌ") in bstack1lll111ll1_opy_ and str(bstack1lll111ll1_opy_[bstack1lllll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࢍ")]).lower() == bstack1lllll1_opy_ (u"࠭ࡴࡳࡷࡨࠫࢎ")):
      bstack111l1ll11_opy_ = True
    bstack1111ll1ll_opy_.bstack1l11l11l1l_opy_(bstack1lll111ll1_opy_.get(bstack1lllll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ࢏"), False))
  else:
    bstack111l1ll11_opy_ = True
    bstack1111ll1ll_opy_.bstack1l11l11l1l_opy_(True)
def bstack1ll1l1111l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1ll11lll11_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack111llll1_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1lllll1_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧ࢐") == args[i].lower() or bstack1lllll1_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥ࢑") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1ll1lllll_opy_
      bstack1ll1lllll_opy_ += bstack1lllll1_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨ࢒") + path
      return path
  return None
bstack1l11lll1ll_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡶࠧ࠴ࠪࡀ࡞ࠧࡿ࠭࠴ࠪࡀࠫࢀ࠲࠯ࡅࠢ࢓"))
def bstack1l1l111l1l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l11lll1ll_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1lllll1_opy_ (u"ࠧࠪࡻࠣ࢔") + group + bstack1lllll1_opy_ (u"ࠨࡽࠣ࢕"), os.environ.get(group))
  return value
def bstack1l11l11l_opy_():
  bstack1lllll1l1l_opy_ = bstack111llll1_opy_()
  if bstack1lllll1l1l_opy_ and os.path.exists(os.path.abspath(bstack1lllll1l1l_opy_)):
    fileName = bstack1lllll1l1l_opy_
  if bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ࢖") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬࢗ")])) and not bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫ࢘") in locals():
    fileName = os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋ࢙ࠧ")]
  if bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࢚࠭") in locals():
    bstack11l111_opy_ = os.path.abspath(fileName)
  else:
    bstack11l111_opy_ = bstack1lllll1_opy_ (u"࢛ࠬ࠭")
  bstack1ll11l11l_opy_ = os.getcwd()
  bstack1l1l111l_opy_ = bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩ࢜")
  bstack1l1ll11111_opy_ = bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹࡢ࡯࡯ࠫ࢝")
  while (not os.path.exists(bstack11l111_opy_)) and bstack1ll11l11l_opy_ != bstack1lllll1_opy_ (u"ࠣࠤ࢞"):
    bstack11l111_opy_ = os.path.join(bstack1ll11l11l_opy_, bstack1l1l111l_opy_)
    if not os.path.exists(bstack11l111_opy_):
      bstack11l111_opy_ = os.path.join(bstack1ll11l11l_opy_, bstack1l1ll11111_opy_)
    if bstack1ll11l11l_opy_ != os.path.dirname(bstack1ll11l11l_opy_):
      bstack1ll11l11l_opy_ = os.path.dirname(bstack1ll11l11l_opy_)
    else:
      bstack1ll11l11l_opy_ = bstack1lllll1_opy_ (u"ࠤࠥ࢟")
  if not os.path.exists(bstack11l111_opy_):
    bstack1l11l1l1_opy_(
      bstack1l1lll1lll_opy_.format(os.getcwd()))
  try:
    with open(bstack11l111_opy_, bstack1lllll1_opy_ (u"ࠪࡶࠬࢠ")) as stream:
      yaml.add_implicit_resolver(bstack1lllll1_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧࢡ"), bstack1l11lll1ll_opy_)
      yaml.add_constructor(bstack1lllll1_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨࢢ"), bstack1l1l111l1l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack11l111_opy_, bstack1lllll1_opy_ (u"࠭ࡲࠨࢣ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1l11l1l1_opy_(bstack1ll1l1l11l_opy_.format(str(exc)))
def bstack11l1l1l1l_opy_(config):
  bstack1ll111ll11_opy_ = bstack1l11ll1ll1_opy_(config)
  for option in list(bstack1ll111ll11_opy_):
    if option.lower() in bstack11ll1111l_opy_ and option != bstack11ll1111l_opy_[option.lower()]:
      bstack1ll111ll11_opy_[bstack11ll1111l_opy_[option.lower()]] = bstack1ll111ll11_opy_[option]
      del bstack1ll111ll11_opy_[option]
  return config
def bstack1lll1l11l_opy_():
  global bstack11l1lll1l_opy_
  for key, bstack1l1l1l1l1l_opy_ in bstack11l11lll_opy_.items():
    if isinstance(bstack1l1l1l1l1l_opy_, list):
      for var in bstack1l1l1l1l1l_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack11l1lll1l_opy_[key] = os.environ[var]
          break
    elif bstack1l1l1l1l1l_opy_ in os.environ and os.environ[bstack1l1l1l1l1l_opy_] and str(os.environ[bstack1l1l1l1l1l_opy_]).strip():
      bstack11l1lll1l_opy_[key] = os.environ[bstack1l1l1l1l1l_opy_]
  if bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩࢤ") in os.environ:
    bstack11l1lll1l_opy_[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢥ")] = {}
    bstack11l1lll1l_opy_[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢦ")][bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢧ")] = os.environ[bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ࢨ")]
def bstack1l11l1l1l1_opy_():
  global bstack1llll1lll_opy_
  global bstack1ll1lllll_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack1lllll1_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࢩ").lower() == val.lower():
      bstack1llll1lll_opy_[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢪ")] = {}
      bstack1llll1lll_opy_[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢫ")][bstack1lllll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࢬ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack1l1ll1lll1_opy_ in bstack11l11l1ll_opy_.items():
    if isinstance(bstack1l1ll1lll1_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1l1ll1lll1_opy_:
          if idx < len(sys.argv) and bstack1lllll1_opy_ (u"ࠩ࠰࠱ࠬࢭ") + var.lower() == val.lower() and not key in bstack1llll1lll_opy_:
            bstack1llll1lll_opy_[key] = sys.argv[idx + 1]
            bstack1ll1lllll_opy_ += bstack1lllll1_opy_ (u"ࠪࠤ࠲࠳ࠧࢮ") + var + bstack1lllll1_opy_ (u"ࠫࠥ࠭ࢯ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack1lllll1_opy_ (u"ࠬ࠳࠭ࠨࢰ") + bstack1l1ll1lll1_opy_.lower() == val.lower() and not key in bstack1llll1lll_opy_:
          bstack1llll1lll_opy_[key] = sys.argv[idx + 1]
          bstack1ll1lllll_opy_ += bstack1lllll1_opy_ (u"࠭ࠠ࠮࠯ࠪࢱ") + bstack1l1ll1lll1_opy_ + bstack1lllll1_opy_ (u"ࠧࠡࠩࢲ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack111l11l1_opy_(config):
  bstack1l11l1l11l_opy_ = config.keys()
  for bstack1111lll1l_opy_, bstack11l1llll1_opy_ in bstack1l1ll11l1l_opy_.items():
    if bstack11l1llll1_opy_ in bstack1l11l1l11l_opy_:
      config[bstack1111lll1l_opy_] = config[bstack11l1llll1_opy_]
      del config[bstack11l1llll1_opy_]
  for bstack1111lll1l_opy_, bstack11l1llll1_opy_ in bstack1111111ll_opy_.items():
    if isinstance(bstack11l1llll1_opy_, list):
      for bstack1lllllllll_opy_ in bstack11l1llll1_opy_:
        if bstack1lllllllll_opy_ in bstack1l11l1l11l_opy_:
          config[bstack1111lll1l_opy_] = config[bstack1lllllllll_opy_]
          del config[bstack1lllllllll_opy_]
          break
    elif bstack11l1llll1_opy_ in bstack1l11l1l11l_opy_:
      config[bstack1111lll1l_opy_] = config[bstack11l1llll1_opy_]
      del config[bstack11l1llll1_opy_]
  for bstack1lllllllll_opy_ in list(config):
    for bstack1l1l11ll1_opy_ in bstack1lll11l1l_opy_:
      if bstack1lllllllll_opy_.lower() == bstack1l1l11ll1_opy_.lower() and bstack1lllllllll_opy_ != bstack1l1l11ll1_opy_:
        config[bstack1l1l11ll1_opy_] = config[bstack1lllllllll_opy_]
        del config[bstack1lllllllll_opy_]
  bstack1lllll1111_opy_ = [{}]
  if not config.get(bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫࢳ")):
    config[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࢴ")] = [{}]
  bstack1lllll1111_opy_ = config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࢵ")]
  for platform in bstack1lllll1111_opy_:
    for bstack1lllllllll_opy_ in list(platform):
      for bstack1l1l11ll1_opy_ in bstack1lll11l1l_opy_:
        if bstack1lllllllll_opy_.lower() == bstack1l1l11ll1_opy_.lower() and bstack1lllllllll_opy_ != bstack1l1l11ll1_opy_:
          platform[bstack1l1l11ll1_opy_] = platform[bstack1lllllllll_opy_]
          del platform[bstack1lllllllll_opy_]
  for bstack1111lll1l_opy_, bstack11l1llll1_opy_ in bstack1111111ll_opy_.items():
    for platform in bstack1lllll1111_opy_:
      if isinstance(bstack11l1llll1_opy_, list):
        for bstack1lllllllll_opy_ in bstack11l1llll1_opy_:
          if bstack1lllllllll_opy_ in platform:
            platform[bstack1111lll1l_opy_] = platform[bstack1lllllllll_opy_]
            del platform[bstack1lllllllll_opy_]
            break
      elif bstack11l1llll1_opy_ in platform:
        platform[bstack1111lll1l_opy_] = platform[bstack11l1llll1_opy_]
        del platform[bstack11l1llll1_opy_]
  for bstack1llll1ll1_opy_ in bstack1ll111ll1l_opy_:
    if bstack1llll1ll1_opy_ in config:
      if not bstack1ll111ll1l_opy_[bstack1llll1ll1_opy_] in config:
        config[bstack1ll111ll1l_opy_[bstack1llll1ll1_opy_]] = {}
      config[bstack1ll111ll1l_opy_[bstack1llll1ll1_opy_]].update(config[bstack1llll1ll1_opy_])
      del config[bstack1llll1ll1_opy_]
  for platform in bstack1lllll1111_opy_:
    for bstack1llll1ll1_opy_ in bstack1ll111ll1l_opy_:
      if bstack1llll1ll1_opy_ in list(platform):
        if not bstack1ll111ll1l_opy_[bstack1llll1ll1_opy_] in platform:
          platform[bstack1ll111ll1l_opy_[bstack1llll1ll1_opy_]] = {}
        platform[bstack1ll111ll1l_opy_[bstack1llll1ll1_opy_]].update(platform[bstack1llll1ll1_opy_])
        del platform[bstack1llll1ll1_opy_]
  config = bstack11l1l1l1l_opy_(config)
  return config
def bstack11llll11l_opy_(config):
  global bstack1l11ll11ll_opy_
  if bstack11ll1l111_opy_(config) and bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨࢶ") in config and str(config[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩࢷ")]).lower() != bstack1lllll1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬࢸ"):
    if not bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫࢹ") in config:
      config[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢺ")] = {}
    if not config[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢻ")].get(bstack1lllll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠧࢼ")) and not bstack1lllll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ࢽ") in config[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢾ")]:
      bstack1l1llll1_opy_ = datetime.datetime.now()
      bstack1ll11l1lll_opy_ = bstack1l1llll1_opy_.strftime(bstack1lllll1_opy_ (u"࠭ࠥࡥࡡࠨࡦࡤࠫࡈࠦࡏࠪࢿ"))
      hostname = socket.gethostname()
      bstack1ll1l1ll1_opy_ = bstack1lllll1_opy_ (u"ࠧࠨࣀ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1lllll1_opy_ (u"ࠨࡽࢀࡣࢀࢃ࡟ࡼࡿࠪࣁ").format(bstack1ll11l1lll_opy_, hostname, bstack1ll1l1ll1_opy_)
      config[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࣂ")][bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࣃ")] = identifier
    bstack1l11ll11ll_opy_ = config[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࣄ")].get(bstack1lllll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣅ"))
  return config
def bstack1lll11lll_opy_():
  bstack1ll11ll111_opy_ =  bstack1111l1111_opy_()[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠬࣆ")]
  return bstack1ll11ll111_opy_ if bstack1ll11ll111_opy_ else -1
def bstack111ll11l_opy_(bstack1ll11ll111_opy_):
  global CONFIG
  if not bstack1lllll1_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩࣇ") in CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣈ")]:
    return
  CONFIG[bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣉ")] = CONFIG[bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ࣊")].replace(
    bstack1lllll1_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭࣋"),
    str(bstack1ll11ll111_opy_)
  )
def bstack1111l11l_opy_():
  global CONFIG
  if not bstack1lllll1_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫ࣌") in CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ࣍")]:
    return
  bstack1l1llll1_opy_ = datetime.datetime.now()
  bstack1ll11l1lll_opy_ = bstack1l1llll1_opy_.strftime(bstack1lllll1_opy_ (u"ࠧࠦࡦ࠰ࠩࡧ࠳ࠥࡉ࠼ࠨࡑࠬ࣎"))
  CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴ࣏ࠪ")] = CONFIG[bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ࣐ࠫ")].replace(
    bstack1lllll1_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾ࣑ࠩ"),
    bstack1ll11l1lll_opy_
  )
def bstack1l1l1llll_opy_():
  global CONFIG
  if bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࣒࠭") in CONFIG and not bool(CONFIG[bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣓ࠧ")]):
    del CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣔ")]
    return
  if not bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣕ") in CONFIG:
    CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣖ")] = bstack1lllll1_opy_ (u"ࠩࠦࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬࣗ")
  if bstack1lllll1_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩࣘ") in CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ࣙ")]:
    bstack1111l11l_opy_()
    os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩࣚ")] = CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣛ")]
  if not bstack1lllll1_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩࣜ") in CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣝ")]:
    return
  bstack1ll11ll111_opy_ = bstack1lllll1_opy_ (u"ࠩࠪࣞ")
  bstack1l1l1l11l1_opy_ = bstack1lll11lll_opy_()
  if bstack1l1l1l11l1_opy_ != -1:
    bstack1ll11ll111_opy_ = bstack1lllll1_opy_ (u"ࠪࡇࡎࠦࠧࣟ") + str(bstack1l1l1l11l1_opy_)
  if bstack1ll11ll111_opy_ == bstack1lllll1_opy_ (u"ࠫࠬ࣠"):
    bstack1l1ll1l1l_opy_ = bstack11llllll_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ࣡")])
    if bstack1l1ll1l1l_opy_ != -1:
      bstack1ll11ll111_opy_ = str(bstack1l1ll1l1l_opy_)
  if bstack1ll11ll111_opy_:
    bstack111ll11l_opy_(bstack1ll11ll111_opy_)
    os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ࣢")] = CONFIG[bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࣣࠩ")]
def bstack1l111llll_opy_(bstack1l11lll111_opy_, bstack1ll11lll1l_opy_, path):
  bstack1l1llll1ll_opy_ = {
    bstack1lllll1_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࣤ"): bstack1ll11lll1l_opy_
  }
  if os.path.exists(path):
    bstack111111111_opy_ = json.load(open(path, bstack1lllll1_opy_ (u"ࠩࡵࡦࠬࣥ")))
  else:
    bstack111111111_opy_ = {}
  bstack111111111_opy_[bstack1l11lll111_opy_] = bstack1l1llll1ll_opy_
  with open(path, bstack1lllll1_opy_ (u"ࠥࡻ࠰ࠨࣦ")) as outfile:
    json.dump(bstack111111111_opy_, outfile)
def bstack11llllll_opy_(bstack1l11lll111_opy_):
  bstack1l11lll111_opy_ = str(bstack1l11lll111_opy_)
  bstack1l111l11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠫࢃ࠭ࣧ")), bstack1lllll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬࣨ"))
  try:
    if not os.path.exists(bstack1l111l11_opy_):
      os.makedirs(bstack1l111l11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"࠭ࡾࠨࣩ")), bstack1lllll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ࣪"), bstack1lllll1_opy_ (u"ࠨ࠰ࡥࡹ࡮ࡲࡤ࠮ࡰࡤࡱࡪ࠳ࡣࡢࡥ࡫ࡩ࠳ࡰࡳࡰࡰࠪ࣫"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1lllll1_opy_ (u"ࠩࡺࠫ࣬")):
        pass
      with open(file_path, bstack1lllll1_opy_ (u"ࠥࡻ࠰ࠨ࣭")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1lllll1_opy_ (u"ࠫࡷ࣮࠭")) as bstack1llllll11_opy_:
      bstack1l11l1ll1_opy_ = json.load(bstack1llllll11_opy_)
    if bstack1l11lll111_opy_ in bstack1l11l1ll1_opy_:
      bstack11lllll11_opy_ = bstack1l11l1ll1_opy_[bstack1l11lll111_opy_][bstack1lllll1_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ࣯ࠩ")]
      bstack1ll11111l1_opy_ = int(bstack11lllll11_opy_) + 1
      bstack1l111llll_opy_(bstack1l11lll111_opy_, bstack1ll11111l1_opy_, file_path)
      return bstack1ll11111l1_opy_
    else:
      bstack1l111llll_opy_(bstack1l11lll111_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1lll1ll111_opy_.format(str(e)))
    return -1
def bstack11l1ll1ll_opy_(config):
  if not config[bstack1lllll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨࣰ")] or not config[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࣱࠪ")]:
    return True
  else:
    return False
def bstack1l1ll1111_opy_(config, index=0):
  global bstack1l1l1lllll_opy_
  bstack1llll11ll_opy_ = {}
  caps = bstack1111l1lll_opy_ + bstack1lll11l1ll_opy_
  if bstack1l1l1lllll_opy_:
    caps += bstack1ll1l1l111_opy_
  for key in config:
    if key in caps + [bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࣲࠫ")]:
      continue
    bstack1llll11ll_opy_[key] = config[key]
  if bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࣳ") in config:
    for bstack11ll111l_opy_ in config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࣴ")][index]:
      if bstack11ll111l_opy_ in caps:
        continue
      bstack1llll11ll_opy_[bstack11ll111l_opy_] = config[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣵ")][index][bstack11ll111l_opy_]
  bstack1llll11ll_opy_[bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࣶࠧ")] = socket.gethostname()
  if bstack1lllll1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧࣷ") in bstack1llll11ll_opy_:
    del (bstack1llll11ll_opy_[bstack1lllll1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨࣸ")])
  return bstack1llll11ll_opy_
def bstack1ll11l1ll1_opy_(config):
  global bstack1l1l1lllll_opy_
  bstack1l111ll11_opy_ = {}
  caps = bstack1lll11l1ll_opy_
  if bstack1l1l1lllll_opy_:
    caps += bstack1ll1l1l111_opy_
  for key in caps:
    if key in config:
      bstack1l111ll11_opy_[key] = config[key]
  return bstack1l111ll11_opy_
def bstack11l111l11_opy_(bstack1llll11ll_opy_, bstack1l111ll11_opy_):
  bstack11l1ll1l1_opy_ = {}
  for key in bstack1llll11ll_opy_.keys():
    if key in bstack1l1ll11l1l_opy_:
      bstack11l1ll1l1_opy_[bstack1l1ll11l1l_opy_[key]] = bstack1llll11ll_opy_[key]
    else:
      bstack11l1ll1l1_opy_[key] = bstack1llll11ll_opy_[key]
  for key in bstack1l111ll11_opy_:
    if key in bstack1l1ll11l1l_opy_:
      bstack11l1ll1l1_opy_[bstack1l1ll11l1l_opy_[key]] = bstack1l111ll11_opy_[key]
    else:
      bstack11l1ll1l1_opy_[key] = bstack1l111ll11_opy_[key]
  return bstack11l1ll1l1_opy_
def bstack1ll1l1l1ll_opy_(config, index=0):
  global bstack1l1l1lllll_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1lllll1l11_opy_ = bstack1l1111ll1_opy_(bstack1lll1l1l1_opy_, config, logger)
  bstack1l111ll11_opy_ = bstack1ll11l1ll1_opy_(config)
  bstack11ll1l1l_opy_ = bstack1lll11l1ll_opy_
  bstack11ll1l1l_opy_ += bstack1l1ll111l_opy_
  bstack1l111ll11_opy_ = update(bstack1l111ll11_opy_, bstack1lllll1l11_opy_)
  if bstack1l1l1lllll_opy_:
    bstack11ll1l1l_opy_ += bstack1ll1l1l111_opy_
  if bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࣹࠫ") in config:
    if bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࣺࠧ") in config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࣻ")][index]:
      caps[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩࣼ")] = config[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨࣽ")][index][bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫࣾ")]
    if bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨࣿ") in config[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫऀ")][index]:
      caps[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪँ")] = str(config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ं")][index][bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬः")])
    bstack11lll111_opy_ = bstack1l1111ll1_opy_(bstack1lll1l1l1_opy_, config[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨऄ")][index], logger)
    bstack11ll1l1l_opy_ += list(bstack11lll111_opy_.keys())
    for bstack1ll11ll1l_opy_ in bstack11ll1l1l_opy_:
      if bstack1ll11ll1l_opy_ in config[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩअ")][index]:
        if bstack1ll11ll1l_opy_ == bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩआ"):
          try:
            bstack11lll111_opy_[bstack1ll11ll1l_opy_] = str(config[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫइ")][index][bstack1ll11ll1l_opy_] * 1.0)
          except:
            bstack11lll111_opy_[bstack1ll11ll1l_opy_] = str(config[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬई")][index][bstack1ll11ll1l_opy_])
        else:
          bstack11lll111_opy_[bstack1ll11ll1l_opy_] = config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭उ")][index][bstack1ll11ll1l_opy_]
        del (config[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧऊ")][index][bstack1ll11ll1l_opy_])
    bstack1l111ll11_opy_ = update(bstack1l111ll11_opy_, bstack11lll111_opy_)
  bstack1llll11ll_opy_ = bstack1l1ll1111_opy_(config, index)
  for bstack1lllllllll_opy_ in bstack1lll11l1ll_opy_ + list(bstack1lllll1l11_opy_.keys()):
    if bstack1lllllllll_opy_ in bstack1llll11ll_opy_:
      bstack1l111ll11_opy_[bstack1lllllllll_opy_] = bstack1llll11ll_opy_[bstack1lllllllll_opy_]
      del (bstack1llll11ll_opy_[bstack1lllllllll_opy_])
  if bstack1ll1l1lll1_opy_(config):
    bstack1llll11ll_opy_[bstack1lllll1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬऋ")] = True
    caps.update(bstack1l111ll11_opy_)
    caps[bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧऌ")] = bstack1llll11ll_opy_
  else:
    bstack1llll11ll_opy_[bstack1lllll1_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧऍ")] = False
    caps.update(bstack11l111l11_opy_(bstack1llll11ll_opy_, bstack1l111ll11_opy_))
    if bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ऎ") in caps:
      caps[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪए")] = caps[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨऐ")]
      del (caps[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩऑ")])
    if bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ऒ") in caps:
      caps[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨओ")] = caps[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨऔ")]
      del (caps[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩक")])
  return caps
def bstack1lllll1ll_opy_():
  global bstack1l11l1ll11_opy_
  if bstack1ll11lll11_opy_() <= version.parse(bstack1lllll1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩख")):
    if bstack1l11l1ll11_opy_ != bstack1lllll1_opy_ (u"ࠪࠫग"):
      return bstack1lllll1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧघ") + bstack1l11l1ll11_opy_ + bstack1lllll1_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤङ")
    return bstack1lll11ll1_opy_
  if bstack1l11l1ll11_opy_ != bstack1lllll1_opy_ (u"࠭ࠧच"):
    return bstack1lllll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤछ") + bstack1l11l1ll11_opy_ + bstack1lllll1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤज")
  return bstack111ll1l1l_opy_
def bstack1llll111l_opy_(options):
  return hasattr(options, bstack1lllll1_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪझ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1111l1ll1_opy_(options, bstack11lll11l1_opy_):
  for bstack1ll1l11l1l_opy_ in bstack11lll11l1_opy_:
    if bstack1ll1l11l1l_opy_ in [bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨञ"), bstack1lllll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨट")]:
      continue
    if bstack1ll1l11l1l_opy_ in options._experimental_options:
      options._experimental_options[bstack1ll1l11l1l_opy_] = update(options._experimental_options[bstack1ll1l11l1l_opy_],
                                                         bstack11lll11l1_opy_[bstack1ll1l11l1l_opy_])
    else:
      options.add_experimental_option(bstack1ll1l11l1l_opy_, bstack11lll11l1_opy_[bstack1ll1l11l1l_opy_])
  if bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡵࠪठ") in bstack11lll11l1_opy_:
    for arg in bstack11lll11l1_opy_[bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡶࠫड")]:
      options.add_argument(arg)
    del (bstack11lll11l1_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡷࠬढ")])
  if bstack1lllll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬण") in bstack11lll11l1_opy_:
    for ext in bstack11lll11l1_opy_[bstack1lllll1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭त")]:
      options.add_extension(ext)
    del (bstack11lll11l1_opy_[bstack1lllll1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧथ")])
def bstack1l111111l_opy_(options, bstack1lll1ll1_opy_):
  if bstack1lllll1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪद") in bstack1lll1ll1_opy_:
    for bstack1111ll111_opy_ in bstack1lll1ll1_opy_[bstack1lllll1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫध")]:
      if bstack1111ll111_opy_ in options._preferences:
        options._preferences[bstack1111ll111_opy_] = update(options._preferences[bstack1111ll111_opy_], bstack1lll1ll1_opy_[bstack1lllll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬन")][bstack1111ll111_opy_])
      else:
        options.set_preference(bstack1111ll111_opy_, bstack1lll1ll1_opy_[bstack1lllll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ऩ")][bstack1111ll111_opy_])
  if bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭प") in bstack1lll1ll1_opy_:
    for arg in bstack1lll1ll1_opy_[bstack1lllll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧफ")]:
      options.add_argument(arg)
def bstack11l111l1_opy_(options, bstack1l111l11l_opy_):
  if bstack1lllll1_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫब") in bstack1l111l11l_opy_:
    options.use_webview(bool(bstack1l111l11l_opy_[bstack1lllll1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬभ")]))
  bstack1111l1ll1_opy_(options, bstack1l111l11l_opy_)
def bstack1llll1ll_opy_(options, bstack1lll11ll_opy_):
  for bstack1ll11l11_opy_ in bstack1lll11ll_opy_:
    if bstack1ll11l11_opy_ in [bstack1lllll1_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩम"), bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡶࠫय")]:
      continue
    options.set_capability(bstack1ll11l11_opy_, bstack1lll11ll_opy_[bstack1ll11l11_opy_])
  if bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡷࠬर") in bstack1lll11ll_opy_:
    for arg in bstack1lll11ll_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ऱ")]:
      options.add_argument(arg)
  if bstack1lllll1_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ल") in bstack1lll11ll_opy_:
    options.bstack1l11lll1_opy_(bool(bstack1lll11ll_opy_[bstack1lllll1_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧळ")]))
def bstack1l1ll1llll_opy_(options, bstack11111ll1l_opy_):
  for bstack1l11lll11_opy_ in bstack11111ll1l_opy_:
    if bstack1l11lll11_opy_ in [bstack1lllll1_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨऴ"), bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡵࠪव")]:
      continue
    options._options[bstack1l11lll11_opy_] = bstack11111ll1l_opy_[bstack1l11lll11_opy_]
  if bstack1lllll1_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪश") in bstack11111ll1l_opy_:
    for bstack1l1lll11l1_opy_ in bstack11111ll1l_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫष")]:
      options.bstack1llll1l111_opy_(
        bstack1l1lll11l1_opy_, bstack11111ll1l_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬस")][bstack1l1lll11l1_opy_])
  if bstack1lllll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧह") in bstack11111ll1l_opy_:
    for arg in bstack11111ll1l_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨऺ")]:
      options.add_argument(arg)
def bstack11111llll_opy_(options, caps):
  if not hasattr(options, bstack1lllll1_opy_ (u"ࠫࡐࡋ࡙ࠨऻ")):
    return
  if options.KEY == bstack1lllll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵ़ࠪ") and options.KEY in caps:
    bstack1111l1ll1_opy_(options, caps[bstack1lllll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫऽ")])
  elif options.KEY == bstack1lllll1_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬा") and options.KEY in caps:
    bstack1l111111l_opy_(options, caps[bstack1lllll1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ि")])
  elif options.KEY == bstack1lllll1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪी") and options.KEY in caps:
    bstack1llll1ll_opy_(options, caps[bstack1lllll1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫु")])
  elif options.KEY == bstack1lllll1_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬू") and options.KEY in caps:
    bstack11l111l1_opy_(options, caps[bstack1lllll1_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ृ")])
  elif options.KEY == bstack1lllll1_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬॄ") and options.KEY in caps:
    bstack1l1ll1llll_opy_(options, caps[bstack1lllll1_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ॅ")])
def bstack1lll111111_opy_(caps):
  global bstack1l1l1lllll_opy_
  if isinstance(os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩॆ")), str):
    bstack1l1l1lllll_opy_ = eval(os.getenv(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪे")))
  if bstack1l1l1lllll_opy_:
    if bstack1ll1l1111l_opy_() < version.parse(bstack1lllll1_opy_ (u"ࠪ࠶࠳࠹࠮࠱ࠩै")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1lllll1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫॉ")
    if bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪॊ") in caps:
      browser = caps[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫो")]
    elif bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨौ") in caps:
      browser = caps[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳ्ࠩ")]
    browser = str(browser).lower()
    if browser == bstack1lllll1_opy_ (u"ࠩ࡬ࡴ࡭ࡵ࡮ࡦࠩॎ") or browser == bstack1lllll1_opy_ (u"ࠪ࡭ࡵࡧࡤࠨॏ"):
      browser = bstack1lllll1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫॐ")
    if browser == bstack1lllll1_opy_ (u"ࠬࡹࡡ࡮ࡵࡸࡲ࡬࠭॑"):
      browser = bstack1lllll1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ॒࠭")
    if browser not in [bstack1lllll1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ॓"), bstack1lllll1_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭॔"), bstack1lllll1_opy_ (u"ࠩ࡬ࡩࠬॕ"), bstack1lllll1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪॖ"), bstack1lllll1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬॗ")]:
      return None
    try:
      package = bstack1lllll1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࢂ࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧक़").format(browser)
      name = bstack1lllll1_opy_ (u"࠭ࡏࡱࡶ࡬ࡳࡳࡹࠧख़")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1llll111l_opy_(options):
        return None
      for bstack1lllllllll_opy_ in caps.keys():
        options.set_capability(bstack1lllllllll_opy_, caps[bstack1lllllllll_opy_])
      bstack11111llll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l11l1l1l_opy_(options, bstack111ll1l1_opy_):
  if not bstack1llll111l_opy_(options):
    return
  for bstack1lllllllll_opy_ in bstack111ll1l1_opy_.keys():
    if bstack1lllllllll_opy_ in bstack1l1ll111l_opy_:
      continue
    if bstack1lllllllll_opy_ in options._caps and type(options._caps[bstack1lllllllll_opy_]) in [dict, list]:
      options._caps[bstack1lllllllll_opy_] = update(options._caps[bstack1lllllllll_opy_], bstack111ll1l1_opy_[bstack1lllllllll_opy_])
    else:
      options.set_capability(bstack1lllllllll_opy_, bstack111ll1l1_opy_[bstack1lllllllll_opy_])
  bstack11111llll_opy_(options, bstack111ll1l1_opy_)
  if bstack1lllll1_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ग़") in options._caps:
    if options._caps[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ज़")] and options._caps[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧड़")].lower() != bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫढ़"):
      del options._caps[bstack1lllll1_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪफ़")]
def bstack1l1lll1l1_opy_(proxy_config):
  if bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩय़") in proxy_config:
    proxy_config[bstack1lllll1_opy_ (u"࠭ࡳࡴ࡮ࡓࡶࡴࡾࡹࠨॠ")] = proxy_config[bstack1lllll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫॡ")]
    del (proxy_config[bstack1lllll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬॢ")])
  if bstack1lllll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬॣ") in proxy_config and proxy_config[bstack1lllll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭।")].lower() != bstack1lllll1_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࠫ॥"):
    proxy_config[bstack1lllll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ०")] = bstack1lllll1_opy_ (u"࠭࡭ࡢࡰࡸࡥࡱ࠭१")
  if bstack1lllll1_opy_ (u"ࠧࡱࡴࡲࡼࡾࡇࡵࡵࡱࡦࡳࡳ࡬ࡩࡨࡗࡵࡰࠬ२") in proxy_config:
    proxy_config[bstack1lllll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ३")] = bstack1lllll1_opy_ (u"ࠩࡳࡥࡨ࠭४")
  return proxy_config
def bstack1l1l1l11_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1lllll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ५") in config:
    return proxy
  config[bstack1lllll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ६")] = bstack1l1lll1l1_opy_(config[bstack1lllll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ७")])
  if proxy == None:
    proxy = Proxy(config[bstack1lllll1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ८")])
  return proxy
def bstack11l111lll_opy_(self):
  global CONFIG
  global bstack1l1l11111_opy_
  try:
    proxy = bstack1ll11lll1_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1lllll1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ९")):
        proxies = bstack1llllllll_opy_(proxy, bstack1lllll1ll_opy_())
        if len(proxies) > 0:
          protocol, bstack1l111ll1l_opy_ = proxies.popitem()
          if bstack1lllll1_opy_ (u"ࠣ࠼࠲࠳ࠧ॰") in bstack1l111ll1l_opy_:
            return bstack1l111ll1l_opy_
          else:
            return bstack1lllll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥॱ") + bstack1l111ll1l_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢॲ").format(str(e)))
  return bstack1l1l11111_opy_(self)
def bstack1llll1ll1l_opy_():
  global CONFIG
  return bstack1lll11l11_opy_(CONFIG) and bstack111l11l11_opy_() and bstack1ll11lll11_opy_() >= version.parse(bstack1l1l1l1l11_opy_)
def bstack1111ll1l1_opy_():
  global CONFIG
  return (bstack1lllll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧॳ") in CONFIG or bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩॴ") in CONFIG) and bstack1l1ll1lll_opy_()
def bstack1l11ll1ll1_opy_(config):
  bstack1ll111ll11_opy_ = {}
  if bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪॵ") in config:
    bstack1ll111ll11_opy_ = config[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫॶ")]
  if bstack1lllll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧॷ") in config:
    bstack1ll111ll11_opy_ = config[bstack1lllll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨॸ")]
  proxy = bstack1ll11lll1_opy_(config)
  if proxy:
    if proxy.endswith(bstack1lllll1_opy_ (u"ࠪ࠲ࡵࡧࡣࠨॹ")) and os.path.isfile(proxy):
      bstack1ll111ll11_opy_[bstack1lllll1_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧॺ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1lllll1_opy_ (u"ࠬ࠴ࡰࡢࡥࠪॻ")):
        proxies = bstack1l11111ll_opy_(config, bstack1lllll1ll_opy_())
        if len(proxies) > 0:
          protocol, bstack1l111ll1l_opy_ = proxies.popitem()
          if bstack1lllll1_opy_ (u"ࠨ࠺࠰࠱ࠥॼ") in bstack1l111ll1l_opy_:
            parsed_url = urlparse(bstack1l111ll1l_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1lllll1_opy_ (u"ࠢ࠻࠱࠲ࠦॽ") + bstack1l111ll1l_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1ll111ll11_opy_[bstack1lllll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫॾ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1ll111ll11_opy_[bstack1lllll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬॿ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1ll111ll11_opy_[bstack1lllll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ঀ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1ll111ll11_opy_[bstack1lllll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧঁ")] = str(parsed_url.password)
  return bstack1ll111ll11_opy_
def bstack11111lll1_opy_(config):
  if bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪং") in config:
    return config[bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫঃ")]
  return {}
def bstack11ll1ll1_opy_(caps):
  global bstack1l11ll11ll_opy_
  if bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ঄") in caps:
    caps[bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩঅ")][bstack1lllll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨআ")] = True
    if bstack1l11ll11ll_opy_:
      caps[bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫই")][bstack1lllll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ঈ")] = bstack1l11ll11ll_opy_
  else:
    caps[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪউ")] = True
    if bstack1l11ll11ll_opy_:
      caps[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧঊ")] = bstack1l11ll11ll_opy_
def bstack1l1l111l11_opy_():
  global CONFIG
  if not bstack11ll1l111_opy_(CONFIG):
    return
  if bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫঋ") in CONFIG and bstack1l11ll1l1_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬঌ")]):
    if (
      bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭঍") in CONFIG
      and bstack1l11ll1l1_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ঎")].get(bstack1lllll1_opy_ (u"ࠫࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠨএ")))
    ):
      logger.debug(bstack1lllll1_opy_ (u"ࠧࡒ࡯ࡤࡣ࡯ࠤࡧ࡯࡮ࡢࡴࡼࠤࡳࡵࡴࠡࡵࡷࡥࡷࡺࡥࡥࠢࡤࡷࠥࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨঐ"))
      return
    bstack1ll111ll11_opy_ = bstack1l11ll1ll1_opy_(CONFIG)
    bstack1l1l1l111_opy_(CONFIG[bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ঑")], bstack1ll111ll11_opy_)
def bstack1l1l1l111_opy_(key, bstack1ll111ll11_opy_):
  global bstack1lll1l1ll_opy_
  logger.info(bstack11111l1l_opy_)
  try:
    bstack1lll1l1ll_opy_ = Local()
    bstack11l1ll111_opy_ = {bstack1lllll1_opy_ (u"ࠧ࡬ࡧࡼࠫ঒"): key}
    bstack11l1ll111_opy_.update(bstack1ll111ll11_opy_)
    logger.debug(bstack1lllllll11_opy_.format(str(bstack11l1ll111_opy_)))
    bstack1lll1l1ll_opy_.start(**bstack11l1ll111_opy_)
    if bstack1lll1l1ll_opy_.isRunning():
      logger.info(bstack1lll1ll1l1_opy_)
  except Exception as e:
    bstack1l11l1l1_opy_(bstack1l11llllll_opy_.format(str(e)))
def bstack1ll1l1l1l1_opy_():
  global bstack1lll1l1ll_opy_
  if bstack1lll1l1ll_opy_.isRunning():
    logger.info(bstack1lll11l1l1_opy_)
    bstack1lll1l1ll_opy_.stop()
  bstack1lll1l1ll_opy_ = None
def bstack1l1l1l11ll_opy_(bstack1ll11l1l11_opy_=[]):
  global CONFIG
  bstack1lll111l1l_opy_ = []
  bstack111lll111_opy_ = [bstack1lllll1_opy_ (u"ࠨࡱࡶࠫও"), bstack1lllll1_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬঔ"), bstack1lllll1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧক"), bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭খ"), bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪগ"), bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧঘ")]
  try:
    for err in bstack1ll11l1l11_opy_:
      bstack1ll1lll1l_opy_ = {}
      for k in bstack111lll111_opy_:
        val = CONFIG[bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪঙ")][int(err[bstack1lllll1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧচ")])].get(k)
        if val:
          bstack1ll1lll1l_opy_[k] = val
      if(err[bstack1lllll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨছ")] != bstack1lllll1_opy_ (u"ࠪࠫজ")):
        bstack1ll1lll1l_opy_[bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡵࠪঝ")] = {
          err[bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪঞ")]: err[bstack1lllll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬট")]
        }
        bstack1lll111l1l_opy_.append(bstack1ll1lll1l_opy_)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡳࡷࡳࡡࡵࡶ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺ࠺ࠡࠩঠ") + str(e))
  finally:
    return bstack1lll111l1l_opy_
def bstack1lll111ll_opy_(file_name):
  bstack1ll1llllll_opy_ = []
  try:
    bstack1lll1llll1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1lll1llll1_opy_):
      with open(bstack1lll1llll1_opy_) as f:
        bstack1111l111l_opy_ = json.load(f)
        bstack1ll1llllll_opy_ = bstack1111l111l_opy_
      os.remove(bstack1lll1llll1_opy_)
    return bstack1ll1llllll_opy_
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪ࡮ࡴࡤࡪࡰࡪࠤࡪࡸࡲࡰࡴࠣࡰ࡮ࡹࡴ࠻ࠢࠪড") + str(e))
    return bstack1ll1llllll_opy_
def bstack11l11l1l_opy_():
  global bstack11l11ll1l_opy_
  global bstack1l11l1l11_opy_
  global bstack11llll111_opy_
  global bstack1llll11ll1_opy_
  global bstack1ll1l11ll1_opy_
  global bstack1l1l1ll1l1_opy_
  global CONFIG
  bstack1ll11l111l_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪঢ"))
  if bstack1ll11l111l_opy_ in [bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩণ"), bstack1lllll1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪত")]:
    bstack1ll1lll1_opy_()
  percy.shutdown()
  if bstack11l11ll1l_opy_:
    logger.warning(bstack1ll111l111_opy_.format(str(bstack11l11ll1l_opy_)))
  else:
    try:
      bstack111111111_opy_ = bstack1l1lllllll_opy_(bstack1lllll1_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫথ"), logger)
      if bstack111111111_opy_.get(bstack1lllll1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫদ")) and bstack111111111_opy_.get(bstack1lllll1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬধ")).get(bstack1lllll1_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪন")):
        logger.warning(bstack1ll111l111_opy_.format(str(bstack111111111_opy_[bstack1lllll1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ঩")][bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬপ")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1lll11l1_opy_)
  global bstack1lll1l1ll_opy_
  if bstack1lll1l1ll_opy_:
    bstack1ll1l1l1l1_opy_()
  try:
    for driver in bstack1l11l1l11_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1ll1llll1_opy_)
  if bstack1l1l1ll1l1_opy_ == bstack1lllll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪফ"):
    bstack1ll1l11ll1_opy_ = bstack1lll111ll_opy_(bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ব"))
  if bstack1l1l1ll1l1_opy_ == bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ভ") and len(bstack1llll11ll1_opy_) == 0:
    bstack1llll11ll1_opy_ = bstack1lll111ll_opy_(bstack1lllll1_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬম"))
    if len(bstack1llll11ll1_opy_) == 0:
      bstack1llll11ll1_opy_ = bstack1lll111ll_opy_(bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧয"))
  bstack11l1lll11_opy_ = bstack1lllll1_opy_ (u"ࠩࠪর")
  if len(bstack11llll111_opy_) > 0:
    bstack11l1lll11_opy_ = bstack1l1l1l11ll_opy_(bstack11llll111_opy_)
  elif len(bstack1llll11ll1_opy_) > 0:
    bstack11l1lll11_opy_ = bstack1l1l1l11ll_opy_(bstack1llll11ll1_opy_)
  elif len(bstack1ll1l11ll1_opy_) > 0:
    bstack11l1lll11_opy_ = bstack1l1l1l11ll_opy_(bstack1ll1l11ll1_opy_)
  elif len(bstack111lll11_opy_) > 0:
    bstack11l1lll11_opy_ = bstack1l1l1l11ll_opy_(bstack111lll11_opy_)
  if bool(bstack11l1lll11_opy_):
    bstack1ll1ll1lll_opy_(bstack11l1lll11_opy_)
  else:
    bstack1ll1ll1lll_opy_()
  bstack1lll1lll11_opy_(bstack11ll1lll1_opy_, logger)
  bstack1llll11111_opy_.bstack1l1l111l1_opy_(CONFIG)
  if len(bstack1ll1l11ll1_opy_) > 0:
    sys.exit(len(bstack1ll1l11ll1_opy_))
def bstack1ll1l1lll_opy_(bstack1llll1ll11_opy_, frame):
  global bstack1111ll1ll_opy_
  logger.error(bstack1l1ll11ll1_opy_)
  bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭঱"), bstack1llll1ll11_opy_)
  if hasattr(signal, bstack1lllll1_opy_ (u"ࠫࡘ࡯ࡧ࡯ࡣ࡯ࡷࠬল")):
    bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ঳"), signal.Signals(bstack1llll1ll11_opy_).name)
  else:
    bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭঴"), bstack1lllll1_opy_ (u"ࠧࡔࡋࡊ࡙ࡓࡑࡎࡐ࡙ࡑࠫ঵"))
  bstack1ll11l111l_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩশ"))
  if bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩষ"):
    bstack1lllll11_opy_.stop(bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪস")))
  bstack11l11l1l_opy_()
  sys.exit(1)
def bstack1l11l1l1_opy_(err):
  logger.critical(bstack1lll1lllll_opy_.format(str(err)))
  bstack1ll1ll1lll_opy_(bstack1lll1lllll_opy_.format(str(err)), True)
  atexit.unregister(bstack11l11l1l_opy_)
  bstack1ll1lll1_opy_()
  sys.exit(1)
def bstack1l1111ll_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1ll1ll1lll_opy_(message, True)
  atexit.unregister(bstack11l11l1l_opy_)
  bstack1ll1lll1_opy_()
  sys.exit(1)
def bstack1111l1ll_opy_():
  global CONFIG
  global bstack1llll1lll_opy_
  global bstack11l1lll1l_opy_
  global bstack111ll1ll_opy_
  CONFIG = bstack1l11l11l_opy_()
  load_dotenv(CONFIG.get(bstack1lllll1_opy_ (u"ࠫࡪࡴࡶࡇ࡫࡯ࡩࠬহ")))
  bstack1lll1l11l_opy_()
  bstack1l11l1l1l1_opy_()
  CONFIG = bstack111l11l1_opy_(CONFIG)
  update(CONFIG, bstack11l1lll1l_opy_)
  update(CONFIG, bstack1llll1lll_opy_)
  CONFIG = bstack11llll11l_opy_(CONFIG)
  bstack111ll1ll_opy_ = bstack11ll1l111_opy_(CONFIG)
  os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ঺")] = bstack111ll1ll_opy_.__str__()
  bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ঻"), bstack111ll1ll_opy_)
  if (bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧ়ࠪ") in CONFIG and bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫঽ") in bstack1llll1lll_opy_) or (
          bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬা") in CONFIG and bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ি") not in bstack11l1lll1l_opy_):
    if os.getenv(bstack1lllll1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨী")):
      CONFIG[bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧু")] = os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪূ"))
    else:
      bstack1l1l1llll_opy_()
  elif (bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪৃ") not in CONFIG and bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪৄ") in CONFIG) or (
          bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ৅") in bstack11l1lll1l_opy_ and bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭৆") not in bstack1llll1lll_opy_):
    del (CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ে")])
  if bstack11l1ll1ll_opy_(CONFIG):
    bstack1l11l1l1_opy_(bstack11l1l1ll1_opy_)
  bstack1lllllll1l_opy_()
  bstack111l1111_opy_()
  if bstack1l1l1lllll_opy_:
    CONFIG[bstack1lllll1_opy_ (u"ࠬࡧࡰࡱࠩৈ")] = bstack11111ll1_opy_(CONFIG)
    logger.info(bstack11111l1ll_opy_.format(CONFIG[bstack1lllll1_opy_ (u"࠭ࡡࡱࡲࠪ৉")]))
  if not bstack111ll1ll_opy_:
    CONFIG[bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ৊")] = [{}]
def bstack11l1l111l_opy_(config, bstack1lll11ll11_opy_):
  global CONFIG
  global bstack1l1l1lllll_opy_
  CONFIG = config
  bstack1l1l1lllll_opy_ = bstack1lll11ll11_opy_
def bstack111l1111_opy_():
  global CONFIG
  global bstack1l1l1lllll_opy_
  if bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࠬো") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l1111ll_opy_(e, bstack1llll11l_opy_)
    bstack1l1l1lllll_opy_ = True
    bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨৌ"), True)
def bstack11111ll1_opy_(config):
  bstack111llll1l_opy_ = bstack1lllll1_opy_ (u"্ࠪࠫ")
  app = config[bstack1lllll1_opy_ (u"ࠫࡦࡶࡰࠨৎ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack11llll1l1_opy_:
      if os.path.exists(app):
        bstack111llll1l_opy_ = bstack11ll11111_opy_(config, app)
      elif bstack1ll1l1ll1l_opy_(app):
        bstack111llll1l_opy_ = app
      else:
        bstack1l11l1l1_opy_(bstack1l1l11l1l_opy_.format(app))
    else:
      if bstack1ll1l1ll1l_opy_(app):
        bstack111llll1l_opy_ = app
      elif os.path.exists(app):
        bstack111llll1l_opy_ = bstack11ll11111_opy_(app)
      else:
        bstack1l11l1l1_opy_(bstack11llll1l_opy_)
  else:
    if len(app) > 2:
      bstack1l11l1l1_opy_(bstack1l1ll111l1_opy_)
    elif len(app) == 2:
      if bstack1lllll1_opy_ (u"ࠬࡶࡡࡵࡪࠪ৏") in app and bstack1lllll1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ৐") in app:
        if os.path.exists(app[bstack1lllll1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ৑")]):
          bstack111llll1l_opy_ = bstack11ll11111_opy_(config, app[bstack1lllll1_opy_ (u"ࠨࡲࡤࡸ࡭࠭৒")], app[bstack1lllll1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ৓")])
        else:
          bstack1l11l1l1_opy_(bstack1l1l11l1l_opy_.format(app))
      else:
        bstack1l11l1l1_opy_(bstack1l1ll111l1_opy_)
    else:
      for key in app:
        if key in bstack11ll11ll_opy_:
          if key == bstack1lllll1_opy_ (u"ࠪࡴࡦࡺࡨࠨ৔"):
            if os.path.exists(app[key]):
              bstack111llll1l_opy_ = bstack11ll11111_opy_(config, app[key])
            else:
              bstack1l11l1l1_opy_(bstack1l1l11l1l_opy_.format(app))
          else:
            bstack111llll1l_opy_ = app[key]
        else:
          bstack1l11l1l1_opy_(bstack1l1lll11ll_opy_)
  return bstack111llll1l_opy_
def bstack1ll1l1ll1l_opy_(bstack111llll1l_opy_):
  import re
  bstack11lllll1_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦ৕"))
  bstack1ll111l11_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭࠳ࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ৖"))
  if bstack1lllll1_opy_ (u"࠭ࡢࡴ࠼࠲࠳ࠬৗ") in bstack111llll1l_opy_ or re.fullmatch(bstack11lllll1_opy_, bstack111llll1l_opy_) or re.fullmatch(bstack1ll111l11_opy_, bstack111llll1l_opy_):
    return True
  else:
    return False
def bstack11ll11111_opy_(config, path, bstack11l11l111_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1lllll1_opy_ (u"ࠧࡳࡤࠪ৘")).read()).hexdigest()
  bstack1l11l1lll1_opy_ = bstack11lll1l1_opy_(md5_hash)
  bstack111llll1l_opy_ = None
  if bstack1l11l1lll1_opy_:
    logger.info(bstack1ll11l11ll_opy_.format(bstack1l11l1lll1_opy_, md5_hash))
    return bstack1l11l1lll1_opy_
  bstack11l1lll1_opy_ = MultipartEncoder(
    fields={
      bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭৙"): (os.path.basename(path), open(os.path.abspath(path), bstack1lllll1_opy_ (u"ࠩࡵࡦࠬ৚")), bstack1lllll1_opy_ (u"ࠪࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴࠧ৛")),
      bstack1lllll1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧড়"): bstack11l11l111_opy_
    }
  )
  response = requests.post(bstack1l11l1l111_opy_, data=bstack11l1lll1_opy_,
                           headers={bstack1lllll1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫঢ়"): bstack11l1lll1_opy_.content_type},
                           auth=(config[bstack1lllll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ৞")], config[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪয়")]))
  try:
    res = json.loads(response.text)
    bstack111llll1l_opy_ = res[bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡤࡻࡲ࡭ࠩৠ")]
    logger.info(bstack1llll111l1_opy_.format(bstack111llll1l_opy_))
    bstack11l11llll_opy_(md5_hash, bstack111llll1l_opy_)
  except ValueError as err:
    bstack1l11l1l1_opy_(bstack11l1ll1l_opy_.format(str(err)))
  return bstack111llll1l_opy_
def bstack1lllllll1l_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l1lll1l1l_opy_
  bstack1lll111l11_opy_ = 1
  bstack111l1llll_opy_ = 1
  if bstack1lllll1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩৡ") in CONFIG:
    bstack111l1llll_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪৢ")]
  else:
    bstack111l1llll_opy_ = bstack111111l11_opy_(framework_name, args) or 1
  if bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧৣ") in CONFIG:
    bstack1lll111l11_opy_ = len(CONFIG[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৤")])
  bstack1l1lll1l1l_opy_ = int(bstack111l1llll_opy_) * int(bstack1lll111l11_opy_)
def bstack111111l11_opy_(framework_name, args):
  if framework_name == bstack1l1ll111ll_opy_ and args and bstack1lllll1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ৥") in args:
      bstack1ll11llll_opy_ = args.index(bstack1lllll1_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ০"))
      return int(args[bstack1ll11llll_opy_ + 1]) or 1
  return 1
def bstack11lll1l1_opy_(md5_hash):
  bstack11l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠨࢀࠪ১")), bstack1lllll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ২"), bstack1lllll1_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫ৩"))
  if os.path.exists(bstack11l1l1l1_opy_):
    bstack1ll1ll111l_opy_ = json.load(open(bstack11l1l1l1_opy_, bstack1lllll1_opy_ (u"ࠫࡷࡨࠧ৪")))
    if md5_hash in bstack1ll1ll111l_opy_:
      bstack1ll1ll1ll1_opy_ = bstack1ll1ll111l_opy_[md5_hash]
      bstack1l1ll1l1_opy_ = datetime.datetime.now()
      bstack1ll111lll_opy_ = datetime.datetime.strptime(bstack1ll1ll1ll1_opy_[bstack1lllll1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ৫")], bstack1lllll1_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪ৬"))
      if (bstack1l1ll1l1_opy_ - bstack1ll111lll_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1ll1ll1ll1_opy_[bstack1lllll1_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ৭")]):
        return None
      return bstack1ll1ll1ll1_opy_[bstack1lllll1_opy_ (u"ࠨ࡫ࡧࠫ৮")]
  else:
    return None
def bstack11l11llll_opy_(md5_hash, bstack111llll1l_opy_):
  bstack1l111l11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠩࢁࠫ৯")), bstack1lllll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪৰ"))
  if not os.path.exists(bstack1l111l11_opy_):
    os.makedirs(bstack1l111l11_opy_)
  bstack11l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠫࢃ࠭ৱ")), bstack1lllll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ৲"), bstack1lllll1_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧ৳"))
  bstack1lllll111_opy_ = {
    bstack1lllll1_opy_ (u"ࠧࡪࡦࠪ৴"): bstack111llll1l_opy_,
    bstack1lllll1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ৵"): datetime.datetime.strftime(datetime.datetime.now(), bstack1lllll1_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭৶")),
    bstack1lllll1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ৷"): str(__version__)
  }
  if os.path.exists(bstack11l1l1l1_opy_):
    bstack1ll1ll111l_opy_ = json.load(open(bstack11l1l1l1_opy_, bstack1lllll1_opy_ (u"ࠫࡷࡨࠧ৸")))
  else:
    bstack1ll1ll111l_opy_ = {}
  bstack1ll1ll111l_opy_[md5_hash] = bstack1lllll111_opy_
  with open(bstack11l1l1l1_opy_, bstack1lllll1_opy_ (u"ࠧࡽࠫࠣ৹")) as outfile:
    json.dump(bstack1ll1ll111l_opy_, outfile)
def bstack11ll1l1l1_opy_(self):
  return
def bstack1ll1ll11_opy_(self):
  return
def bstack1l11ll1ll_opy_(self):
  global bstack1l111111_opy_
  bstack1l111111_opy_(self)
def bstack1llll1lll1_opy_():
  global bstack1l1ll1ll_opy_
  bstack1l1ll1ll_opy_ = True
def bstack1ll1l11lll_opy_(self):
  global bstack1ll11l1l1l_opy_
  global bstack1l11ll11_opy_
  global bstack11l1llll_opy_
  try:
    if bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭৺") in bstack1ll11l1l1l_opy_ and self.session_id != None and bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫ৻"), bstack1lllll1_opy_ (u"ࠨࠩৼ")) != bstack1lllll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ৽"):
      bstack1l1l1l1l1_opy_ = bstack1lllll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ৾") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ৿")
      if bstack1l1l1l1l1_opy_ == bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ਀"):
        bstack1l1ll1ll1l_opy_(logger)
      if self != None:
        bstack1l1l1ll11l_opy_(self, bstack1l1l1l1l1_opy_, bstack1lllll1_opy_ (u"࠭ࠬࠡࠩਁ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1lllll1_opy_ (u"ࠧࠨਂ")
    if bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨਃ") in bstack1ll11l1l1l_opy_ and getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ਄"), None):
      bstack1ll11lllll_opy_.bstack1lll1lll1_opy_(self, bstack1ll111l1ll_opy_, logger, wait=True)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠦਅ") + str(e))
  bstack11l1llll_opy_(self)
  self.session_id = None
def bstack1lll1lll_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1ll1l11l11_opy_
    global bstack1ll11l1l1l_opy_
    command_executor = kwargs.get(bstack1lllll1_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠧਆ"), bstack1lllll1_opy_ (u"ࠬ࠭ਇ"))
    bstack11l1l11l_opy_ = False
    if type(command_executor) == str and bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩਈ") in command_executor:
      bstack11l1l11l_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪਉ") in str(getattr(command_executor, bstack1lllll1_opy_ (u"ࠨࡡࡸࡶࡱ࠭ਊ"), bstack1lllll1_opy_ (u"ࠩࠪ਋"))):
      bstack11l1l11l_opy_ = True
    else:
      return bstack1l111ll1ll_opy_(self, *args, **kwargs)
    if bstack11l1l11l_opy_:
      if kwargs.get(bstack1lllll1_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ਌")):
        kwargs[bstack1lllll1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ਍")] = bstack1ll1l11l11_opy_(kwargs[bstack1lllll1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭਎")], bstack1ll11l1l1l_opy_)
      elif kwargs.get(bstack1lllll1_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ਏ")):
        kwargs[bstack1lllll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧਐ")] = bstack1ll1l11l11_opy_(kwargs[bstack1lllll1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ਑")], bstack1ll11l1l1l_opy_)
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡗࡉࡑࠠࡤࡣࡳࡷ࠿ࠦࡻࡾࠤ਒").format(str(e)))
  return bstack1l111ll1ll_opy_(self, *args, **kwargs)
def bstack1l1l1111ll_opy_(self, command_executor=bstack1lllll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲࠵࠷࠽࠮࠱࠰࠳࠲࠶ࡀ࠴࠵࠶࠷ࠦਓ"), *args, **kwargs):
  bstack1l1l1l1111_opy_ = bstack1lll1lll_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1lllll11_opy_.on():
    return bstack1l1l1l1111_opy_
  try:
    logger.debug(bstack1lllll1_opy_ (u"ࠫࡈࡵ࡭࡮ࡣࡱࡨࠥࡋࡸࡦࡥࡸࡸࡴࡸࠠࡸࡪࡨࡲࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤ࡫ࡧ࡬ࡴࡧࠣ࠱ࠥࢁࡽࠨਔ").format(str(command_executor)))
    logger.debug(bstack1lllll1_opy_ (u"ࠬࡎࡵࡣࠢࡘࡖࡑࠦࡩࡴࠢ࠰ࠤࢀࢃࠧਕ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩਖ") in command_executor._url:
      bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨਗ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫਘ") in command_executor):
    bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪਙ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1lllll11_opy_.bstack1l111lll_opy_(self)
  return bstack1l1l1l1111_opy_
def bstack11ll1lll_opy_(args):
  return bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠫਚ") in str(args)
def bstack1lll1ll1l_opy_(self, driver_command, *args, **kwargs):
  global bstack11111l11_opy_
  global bstack11l11l1l1_opy_
  bstack11lllllll_opy_ = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨਛ"), None) and bstack1111l1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫਜ"), None)
  bstack1ll1llll11_opy_ = getattr(self, bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ਝ"), None) != None and getattr(self, bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧਞ"), None) == True
  if not bstack11l11l1l1_opy_ and bstack111ll1ll_opy_ and bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨਟ") in CONFIG and CONFIG[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩਠ")] == True and bstack1l1l1l1ll_opy_.bstack1l1lll111l_opy_(driver_command) and (bstack1ll1llll11_opy_ or bstack11lllllll_opy_) and not bstack11ll1lll_opy_(args):
    try:
      bstack11l11l1l1_opy_ = True
      logger.debug(bstack1lllll1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡾࢁࠬਡ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1lllll1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡧࡵࡪࡴࡸ࡭ࠡࡵࡦࡥࡳࠦࡻࡾࠩਢ").format(str(err)))
    bstack11l11l1l1_opy_ = False
  response = bstack11111l11_opy_(self, driver_command, *args, **kwargs)
  if bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫਣ") in str(bstack1ll11l1l1l_opy_).lower() and bstack1lllll11_opy_.on():
    try:
      if driver_command == bstack1lllll1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪਤ"):
        bstack1lllll11_opy_.bstack1l11ll1l1l_opy_({
            bstack1lllll1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ਥ"): response[bstack1lllll1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧਦ")],
            bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩਧ"): bstack1lllll11_opy_.current_test_uuid() if bstack1lllll11_opy_.current_test_uuid() else bstack1lllll11_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
def bstack11ll1l1ll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1l11ll11_opy_
  global bstack111ll1ll1_opy_
  global bstack1l11111l_opy_
  global bstack1ll1ll1l1l_opy_
  global bstack111l1lll_opy_
  global bstack1ll11l1l1l_opy_
  global bstack1l111ll1ll_opy_
  global bstack1l11l1l11_opy_
  global bstack1ll1llll1l_opy_
  global bstack1ll111l1ll_opy_
  CONFIG[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬਨ")] = str(bstack1ll11l1l1l_opy_) + str(__version__)
  command_executor = bstack1lllll1ll_opy_()
  logger.debug(bstack1111l1l1l_opy_.format(command_executor))
  proxy = bstack1l1l1l11_opy_(CONFIG, proxy)
  bstack1l1llll11_opy_ = 0 if bstack111ll1ll1_opy_ < 0 else bstack111ll1ll1_opy_
  try:
    if bstack1ll1ll1l1l_opy_ is True:
      bstack1l1llll11_opy_ = int(multiprocessing.current_process().name)
    elif bstack111l1lll_opy_ is True:
      bstack1l1llll11_opy_ = int(threading.current_thread().name)
  except:
    bstack1l1llll11_opy_ = 0
  bstack111ll1l1_opy_ = bstack1ll1l1l1ll_opy_(CONFIG, bstack1l1llll11_opy_)
  logger.debug(bstack1ll111ll1_opy_.format(str(bstack111ll1l1_opy_)))
  if bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ਩") in CONFIG and bstack1l11ll1l1_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩਪ")]):
    bstack11ll1ll1_opy_(bstack111ll1l1_opy_)
  if bstack1lll1111ll_opy_.bstack11111111l_opy_(CONFIG, bstack1l1llll11_opy_) and bstack1lll1111ll_opy_.bstack1l111l1l_opy_(bstack111ll1l1_opy_, options, desired_capabilities):
    threading.current_thread().a11yPlatform = True
    bstack1lll1111ll_opy_.set_capabilities(bstack111ll1l1_opy_, CONFIG)
  if desired_capabilities:
    bstack1lll11ll1l_opy_ = bstack111l11l1_opy_(desired_capabilities)
    bstack1lll11ll1l_opy_[bstack1lllll1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ਫ")] = bstack1ll1l1lll1_opy_(CONFIG)
    bstack1l1llll1l_opy_ = bstack1ll1l1l1ll_opy_(bstack1lll11ll1l_opy_)
    if bstack1l1llll1l_opy_:
      bstack111ll1l1_opy_ = update(bstack1l1llll1l_opy_, bstack111ll1l1_opy_)
    desired_capabilities = None
  if options:
    bstack1l11l1l1l_opy_(options, bstack111ll1l1_opy_)
  if not options:
    options = bstack1lll111111_opy_(bstack111ll1l1_opy_)
  bstack1ll111l1ll_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਬ"))[bstack1l1llll11_opy_]
  if proxy and bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨਭ")):
    options.proxy(proxy)
  if options and bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨਮ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1ll11lll11_opy_() < version.parse(bstack1lllll1_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩਯ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack111ll1l1_opy_)
  logger.info(bstack1l1lll1l11_opy_)
  if bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫਰ")):
    bstack1l111ll1ll_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ਱")):
    bstack1l111ll1ll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ਲ")):
    bstack1l111ll1ll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack1l111ll1ll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack1l1l1lll11_opy_ = bstack1lllll1_opy_ (u"ࠧࠨਲ਼")
    if bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࡢ࠲ࠩ਴")):
      bstack1l1l1lll11_opy_ = self.caps.get(bstack1lllll1_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤਵ"))
    else:
      bstack1l1l1lll11_opy_ = self.capabilities.get(bstack1lllll1_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥਸ਼"))
    if bstack1l1l1lll11_opy_:
      bstack1lll11l11l_opy_(bstack1l1l1lll11_opy_)
      if bstack1ll11lll11_opy_() <= version.parse(bstack1lllll1_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫ਷")):
        self.command_executor._url = bstack1lllll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨਸ") + bstack1l11l1ll11_opy_ + bstack1lllll1_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥਹ")
      else:
        self.command_executor._url = bstack1lllll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤ਺") + bstack1l1l1lll11_opy_ + bstack1lllll1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤ਻")
      logger.debug(bstack11ll111l1_opy_.format(bstack1l1l1lll11_opy_))
    else:
      logger.debug(bstack1l11ll1l_opy_.format(bstack1lllll1_opy_ (u"ࠤࡒࡴࡹ࡯࡭ࡢ࡮ࠣࡌࡺࡨࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ਼ࠥ")))
  except Exception as e:
    logger.debug(bstack1l11ll1l_opy_.format(e))
  if bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ਽") in bstack1ll11l1l1l_opy_:
    bstack111lllll_opy_(bstack111ll1ll1_opy_, bstack1ll1llll1l_opy_)
  bstack1l11ll11_opy_ = self.session_id
  if bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫਾ") in bstack1ll11l1l1l_opy_ or bstack1lllll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬਿ") in bstack1ll11l1l1l_opy_ or bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬੀ") in bstack1ll11l1l1l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack1lllll11_opy_.bstack1l111lll_opy_(self)
  bstack1l11l1l11_opy_.append(self)
  if bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪੁ") in CONFIG and bstack1lllll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ੂ") in CONFIG[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ੃")][bstack1l1llll11_opy_]:
    bstack1l11111l_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭੄")][bstack1l1llll11_opy_][bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ੅")]
  logger.debug(bstack1111llll_opy_.format(bstack1l11ll11_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1l1lllll1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1ll1llll_opy_
      if(bstack1lllll1_opy_ (u"ࠧ࡯࡮ࡥࡧࡻ࠲࡯ࡹࠢ੆") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"࠭ࡾࠨੇ")), bstack1lllll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧੈ"), bstack1lllll1_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪ੉")), bstack1lllll1_opy_ (u"ࠩࡺࠫ੊")) as fp:
          fp.write(bstack1lllll1_opy_ (u"ࠥࠦੋ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1lllll1_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨੌ")))):
          with open(args[1], bstack1lllll1_opy_ (u"ࠬࡸ੍ࠧ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1lllll1_opy_ (u"࠭ࡡࡴࡻࡱࡧࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡠࡰࡨࡻࡕࡧࡧࡦࠪࡦࡳࡳࡺࡥࡹࡶ࠯ࠤࡵࡧࡧࡦࠢࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠬ੎") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1ll11ll1ll_opy_)
            lines.insert(1, bstack1ll1lllll1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1lllll1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤ੏")), bstack1lllll1_opy_ (u"ࠨࡹࠪ੐")) as bstack11ll11l1l_opy_:
              bstack11ll11l1l_opy_.writelines(lines)
        CONFIG[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫੑ")] = str(bstack1ll11l1l1l_opy_) + str(__version__)
        bstack1l1llll11_opy_ = 0 if bstack111ll1ll1_opy_ < 0 else bstack111ll1ll1_opy_
        try:
          if bstack1ll1ll1l1l_opy_ is True:
            bstack1l1llll11_opy_ = int(multiprocessing.current_process().name)
          elif bstack111l1lll_opy_ is True:
            bstack1l1llll11_opy_ = int(threading.current_thread().name)
        except:
          bstack1l1llll11_opy_ = 0
        CONFIG[bstack1lllll1_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥ੒")] = False
        CONFIG[bstack1lllll1_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ੓")] = True
        bstack111ll1l1_opy_ = bstack1ll1l1l1ll_opy_(CONFIG, bstack1l1llll11_opy_)
        logger.debug(bstack1ll111ll1_opy_.format(str(bstack111ll1l1_opy_)))
        if CONFIG.get(bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ੔")):
          bstack11ll1ll1_opy_(bstack111ll1l1_opy_)
        if bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ੕") in CONFIG and bstack1lllll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ੖") in CONFIG[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ੗")][bstack1l1llll11_opy_]:
          bstack1l11111l_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ੘")][bstack1l1llll11_opy_][bstack1lllll1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨਖ਼")]
        args.append(os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠫࢃ࠭ਗ਼")), bstack1lllll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬਜ਼"), bstack1lllll1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨੜ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack111ll1l1_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1lllll1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤ੝"))
      bstack1ll1llll_opy_ = True
      return bstack11l1ll11l_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack11ll111ll_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack111ll1ll1_opy_
    global bstack1l11111l_opy_
    global bstack1ll1ll1l1l_opy_
    global bstack111l1lll_opy_
    global bstack1ll11l1l1l_opy_
    CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪਫ਼")] = str(bstack1ll11l1l1l_opy_) + str(__version__)
    bstack1l1llll11_opy_ = 0 if bstack111ll1ll1_opy_ < 0 else bstack111ll1ll1_opy_
    try:
      if bstack1ll1ll1l1l_opy_ is True:
        bstack1l1llll11_opy_ = int(multiprocessing.current_process().name)
      elif bstack111l1lll_opy_ is True:
        bstack1l1llll11_opy_ = int(threading.current_thread().name)
    except:
      bstack1l1llll11_opy_ = 0
    CONFIG[bstack1lllll1_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ੟")] = True
    bstack111ll1l1_opy_ = bstack1ll1l1l1ll_opy_(CONFIG, bstack1l1llll11_opy_)
    logger.debug(bstack1ll111ll1_opy_.format(str(bstack111ll1l1_opy_)))
    if CONFIG.get(bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ੠")):
      bstack11ll1ll1_opy_(bstack111ll1l1_opy_)
    if bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ੡") in CONFIG and bstack1lllll1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੢") in CONFIG[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ੣")][bstack1l1llll11_opy_]:
      bstack1l11111l_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ੤")][bstack1l1llll11_opy_][bstack1lllll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭੥")]
    import urllib
    import json
    bstack111111ll1_opy_ = bstack1lllll1_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫ੦") + urllib.parse.quote(json.dumps(bstack111ll1l1_opy_))
    browser = self.connect(bstack111111ll1_opy_)
    return browser
except Exception as e:
    pass
def bstack111llllll_opy_():
    global bstack1ll1llll_opy_
    global bstack1ll11l1l1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11111l1l1_opy_
        if not bstack111ll1ll_opy_:
          global bstack1lll1l11l1_opy_
          if not bstack1lll1l11l1_opy_:
            from bstack_utils.helper import bstack1l1ll11ll_opy_, bstack11l1l1lll_opy_
            bstack1lll1l11l1_opy_ = bstack1l1ll11ll_opy_()
            bstack11l1l1lll_opy_(bstack1ll11l1l1l_opy_)
          BrowserType.connect = bstack11111l1l1_opy_
          return
        BrowserType.launch = bstack11ll111ll_opy_
        bstack1ll1llll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1l1lllll1_opy_
      bstack1ll1llll_opy_ = True
    except Exception as e:
      pass
def bstack1l11l11l11_opy_(context, bstack1l1llllll_opy_):
  try:
    context.page.evaluate(bstack1lllll1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ੧"), bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨ੨")+ json.dumps(bstack1l1llllll_opy_) + bstack1lllll1_opy_ (u"ࠧࢃࡽࠣ੩"))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦ੪"), e)
def bstack1111ll11_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1lllll1_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ੫"), bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭੬") + json.dumps(message) + bstack1lllll1_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬ੭") + json.dumps(level) + bstack1lllll1_opy_ (u"ࠪࢁࢂ࠭੮"))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃࠢ੯"), e)
def bstack111111lll_opy_(self, url):
  global bstack1ll1lll1l1_opy_
  try:
    bstack1l11l111ll_opy_(url)
  except Exception as err:
    logger.debug(bstack111llll11_opy_.format(str(err)))
  try:
    bstack1ll1lll1l1_opy_(self, url)
  except Exception as e:
    try:
      bstack1ll1l111_opy_ = str(e)
      if any(err_msg in bstack1ll1l111_opy_ for err_msg in bstack1l11llll11_opy_):
        bstack1l11l111ll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack111llll11_opy_.format(str(err)))
    raise e
def bstack1l11l1111l_opy_(self):
  global bstack1l1l11ll_opy_
  bstack1l1l11ll_opy_ = self
  return
def bstack1llll1l1l1_opy_(self):
  global bstack1ll11111l_opy_
  bstack1ll11111l_opy_ = self
  return
def bstack1llllll1l1_opy_(test_name, bstack1111ll1l_opy_):
  global CONFIG
  if CONFIG.get(bstack1lllll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫੰ"), False):
    bstack111l1l1ll_opy_ = os.path.relpath(bstack1111ll1l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack111l1l1ll_opy_)
    bstack1ll1111l_opy_ = suite_name + bstack1lllll1_opy_ (u"ࠨ࠭ࠣੱ") + test_name
    threading.current_thread().percySessionName = bstack1ll1111l_opy_
def bstack1lllll1l1_opy_(self, test, *args, **kwargs):
  global bstack1l1ll1l111_opy_
  test_name = None
  bstack1111ll1l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1111ll1l_opy_ = str(test.source)
  bstack1llllll1l1_opy_(test_name, bstack1111ll1l_opy_)
  bstack1l1ll1l111_opy_(self, test, *args, **kwargs)
def bstack1l1lll11l_opy_(driver, bstack1ll1111l_opy_):
  if not bstack111l1ll11_opy_ and bstack1ll1111l_opy_:
      bstack1lllll11l_opy_ = {
          bstack1lllll1_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧੲ"): bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩੳ"),
          bstack1lllll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬੴ"): {
              bstack1lllll1_opy_ (u"ࠪࡲࡦࡳࡥࠨੵ"): bstack1ll1111l_opy_
          }
      }
      bstack1ll1ll11l1_opy_ = bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ੶").format(json.dumps(bstack1lllll11l_opy_))
      driver.execute_script(bstack1ll1ll11l1_opy_)
  if bstack11l11ll11_opy_:
      bstack1l111lll1l_opy_ = {
          bstack1lllll1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ੷"): bstack1lllll1_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ੸"),
          bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ੹"): {
              bstack1lllll1_opy_ (u"ࠨࡦࡤࡸࡦ࠭੺"): bstack1ll1111l_opy_ + bstack1lllll1_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫ੻"),
              bstack1lllll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ੼"): bstack1lllll1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ੽")
          }
      }
      if bstack11l11ll11_opy_.status == bstack1lllll1_opy_ (u"ࠬࡖࡁࡔࡕࠪ੾"):
          bstack1l11ll11l_opy_ = bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ੿").format(json.dumps(bstack1l111lll1l_opy_))
          driver.execute_script(bstack1l11ll11l_opy_)
          bstack1l1l1ll11l_opy_(driver, bstack1lllll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ઀"))
      elif bstack11l11ll11_opy_.status == bstack1lllll1_opy_ (u"ࠨࡈࡄࡍࡑ࠭ઁ"):
          reason = bstack1lllll1_opy_ (u"ࠤࠥં")
          bstack111ll11ll_opy_ = bstack1ll1111l_opy_ + bstack1lllll1_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠫઃ")
          if bstack11l11ll11_opy_.message:
              reason = str(bstack11l11ll11_opy_.message)
              bstack111ll11ll_opy_ = bstack111ll11ll_opy_ + bstack1lllll1_opy_ (u"ࠫࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠫ઄") + reason
          bstack1l111lll1l_opy_[bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨઅ")] = {
              bstack1lllll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬઆ"): bstack1lllll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ઇ"),
              bstack1lllll1_opy_ (u"ࠨࡦࡤࡸࡦ࠭ઈ"): bstack111ll11ll_opy_
          }
          bstack1l11ll11l_opy_ = bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧઉ").format(json.dumps(bstack1l111lll1l_opy_))
          driver.execute_script(bstack1l11ll11l_opy_)
          bstack1l1l1ll11l_opy_(driver, bstack1lllll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪઊ"), reason)
          bstack1ll111l1l_opy_(reason, str(bstack11l11ll11_opy_), str(bstack111ll1ll1_opy_), logger)
def bstack1l111lll11_opy_(driver, test):
  if CONFIG.get(bstack1lllll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪઋ"), False) and CONFIG.get(bstack1lllll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨઌ"), bstack1lllll1_opy_ (u"ࠨࡡࡶࡶࡲࠦઍ")) == bstack1lllll1_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤ઎"):
      bstack111l11lll_opy_ = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫએ"), None)
      bstack1l1ll1l1ll_opy_(driver, bstack111l11lll_opy_)
  if bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ઐ"), None) and bstack1111l1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩઑ"), None):
      logger.info(bstack1lllll1_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠣࠦ઒"))
      bstack1lll1111ll_opy_.bstack1ll111llll_opy_(driver, class_name=test.parent.name, name=test.name, module_name=None,
                              path=test.source, bstack11111111_opy_=bstack1ll111l1ll_opy_)
def bstack1llll1111l_opy_(test, bstack1ll1111l_opy_):
    try:
      data = {}
      if test:
        data[bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪઓ")] = bstack1ll1111l_opy_
      if bstack11l11ll11_opy_:
        if bstack11l11ll11_opy_.status == bstack1lllll1_opy_ (u"࠭ࡐࡂࡕࡖࠫઔ"):
          data[bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧક")] = bstack1lllll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨખ")
        elif bstack11l11ll11_opy_.status == bstack1lllll1_opy_ (u"ࠩࡉࡅࡎࡒࠧગ"):
          data[bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪઘ")] = bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫઙ")
          if bstack11l11ll11_opy_.message:
            data[bstack1lllll1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬચ")] = str(bstack11l11ll11_opy_.message)
      user = CONFIG[bstack1lllll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨછ")]
      key = CONFIG[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪજ")]
      url = bstack1lllll1_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠴ࢁࡽ࠯࡬ࡶࡳࡳ࠭ઝ").format(user, key, bstack1l11ll11_opy_)
      headers = {
        bstack1lllll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨઞ"): bstack1lllll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ટ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1l1ll1l11_opy_.format(str(e)))
def bstack1ll1111l1_opy_(test, bstack1ll1111l_opy_):
  global CONFIG
  global bstack1ll11111l_opy_
  global bstack1l1l11ll_opy_
  global bstack1l11ll11_opy_
  global bstack11l11ll11_opy_
  global bstack1l11111l_opy_
  global bstack1l1ll11lll_opy_
  global bstack111l11l1l_opy_
  global bstack1ll11111_opy_
  global bstack1l11l111_opy_
  global bstack1l11l1l11_opy_
  global bstack1ll111l1ll_opy_
  try:
    if not bstack1l11ll11_opy_:
      with open(os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠫࢃ࠭ઠ")), bstack1lllll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬડ"), bstack1lllll1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨઢ"))) as f:
        bstack111ll1111_opy_ = json.loads(bstack1lllll1_opy_ (u"ࠢࡼࠤણ") + f.read().strip() + bstack1lllll1_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪત") + bstack1lllll1_opy_ (u"ࠤࢀࠦથ"))
        bstack1l11ll11_opy_ = bstack111ll1111_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1l11l1l11_opy_:
    for driver in bstack1l11l1l11_opy_:
      if bstack1l11ll11_opy_ == driver.session_id:
        if test:
          bstack1l111lll11_opy_(driver, test)
        bstack1l1lll11l_opy_(driver, bstack1ll1111l_opy_)
  elif bstack1l11ll11_opy_:
    bstack1llll1111l_opy_(test, bstack1ll1111l_opy_)
  if bstack1ll11111l_opy_:
    bstack111l11l1l_opy_(bstack1ll11111l_opy_)
  if bstack1l1l11ll_opy_:
    bstack1ll11111_opy_(bstack1l1l11ll_opy_)
  if bstack1l1ll1ll_opy_:
    bstack1l11l111_opy_()
def bstack1llll11lll_opy_(self, test, *args, **kwargs):
  bstack1ll1111l_opy_ = None
  if test:
    bstack1ll1111l_opy_ = str(test.name)
  bstack1ll1111l1_opy_(test, bstack1ll1111l_opy_)
  bstack1l1ll11lll_opy_(self, test, *args, **kwargs)
def bstack11lllll1l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l111111_opy_
  global CONFIG
  global bstack1l11l1l11_opy_
  global bstack1l11ll11_opy_
  bstack1ll1l111l_opy_ = None
  try:
    if bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩદ"), None):
      try:
        if not bstack1l11ll11_opy_:
          with open(os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠫࢃ࠭ધ")), bstack1lllll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬન"), bstack1lllll1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨ઩"))) as f:
            bstack111ll1111_opy_ = json.loads(bstack1lllll1_opy_ (u"ࠢࡼࠤપ") + f.read().strip() + bstack1lllll1_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪફ") + bstack1lllll1_opy_ (u"ࠤࢀࠦબ"))
            bstack1l11ll11_opy_ = bstack111ll1111_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack1l11l1l11_opy_:
        for driver in bstack1l11l1l11_opy_:
          if bstack1l11ll11_opy_ == driver.session_id:
            bstack1ll1l111l_opy_ = driver
    bstack11111l111_opy_ = bstack1lll1111ll_opy_.bstack1llllllll1_opy_(CONFIG, test.tags)
    if bstack1ll1l111l_opy_:
      threading.current_thread().isA11yTest = bstack1lll1111ll_opy_.bstack111lllll1_opy_(bstack1ll1l111l_opy_, bstack11111l111_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11111l111_opy_
  except:
    pass
  bstack11l111111_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11l11ll11_opy_
  bstack11l11ll11_opy_ = self._test
def bstack1l1111l1l_opy_():
  global bstack1l11l1111_opy_
  try:
    if os.path.exists(bstack1l11l1111_opy_):
      os.remove(bstack1l11l1111_opy_)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ભ") + str(e))
def bstack11llllll1_opy_():
  global bstack1l11l1111_opy_
  bstack111111111_opy_ = {}
  try:
    if not os.path.isfile(bstack1l11l1111_opy_):
      with open(bstack1l11l1111_opy_, bstack1lllll1_opy_ (u"ࠫࡼ࠭મ")):
        pass
      with open(bstack1l11l1111_opy_, bstack1lllll1_opy_ (u"ࠧࡽࠫࠣય")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1l11l1111_opy_):
      bstack111111111_opy_ = json.load(open(bstack1l11l1111_opy_, bstack1lllll1_opy_ (u"࠭ࡲࡣࠩર")))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩ઱") + str(e))
  finally:
    return bstack111111111_opy_
def bstack111lllll_opy_(platform_index, item_index):
  global bstack1l11l1111_opy_
  try:
    bstack111111111_opy_ = bstack11llllll1_opy_()
    bstack111111111_opy_[item_index] = platform_index
    with open(bstack1l11l1111_opy_, bstack1lllll1_opy_ (u"ࠣࡹ࠮ࠦલ")) as outfile:
      json.dump(bstack111111111_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧળ") + str(e))
def bstack111l1l111_opy_(bstack1ll1111111_opy_):
  global CONFIG
  bstack11lll1ll_opy_ = bstack1lllll1_opy_ (u"ࠪࠫ઴")
  if not bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧવ") in CONFIG:
    logger.info(bstack1lllll1_opy_ (u"ࠬࡔ࡯ࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠤࡵࡧࡳࡴࡧࡧࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡵࡩࡵࡵࡲࡵࠢࡩࡳࡷࠦࡒࡰࡤࡲࡸࠥࡸࡵ࡯ࠩશ"))
  try:
    platform = CONFIG[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩષ")][bstack1ll1111111_opy_]
    if bstack1lllll1_opy_ (u"ࠧࡰࡵࠪસ") in platform:
      bstack11lll1ll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠨࡱࡶࠫહ")]) + bstack1lllll1_opy_ (u"ࠩ࠯ࠤࠬ઺")
    if bstack1lllll1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭઻") in platform:
      bstack11lll1ll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴ઼ࠧ")]) + bstack1lllll1_opy_ (u"ࠬ࠲ࠠࠨઽ")
    if bstack1lllll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪા") in platform:
      bstack11lll1ll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫિ")]) + bstack1lllll1_opy_ (u"ࠨ࠮ࠣࠫી")
    if bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫુ") in platform:
      bstack11lll1ll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬૂ")]) + bstack1lllll1_opy_ (u"ࠫ࠱ࠦࠧૃ")
    if bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪૄ") in platform:
      bstack11lll1ll_opy_ += str(platform[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫૅ")]) + bstack1lllll1_opy_ (u"ࠧ࠭ࠢࠪ૆")
    if bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩે") in platform:
      bstack11lll1ll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪૈ")]) + bstack1lllll1_opy_ (u"ࠪ࠰ࠥ࠭ૉ")
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠫࡘࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡹࡸࡩ࡯ࡩࠣࡪࡴࡸࠠࡳࡧࡳࡳࡷࡺࠠࡨࡧࡱࡩࡷࡧࡴࡪࡱࡱࠫ૊") + str(e))
  finally:
    if bstack11lll1ll_opy_[len(bstack11lll1ll_opy_) - 2:] == bstack1lllll1_opy_ (u"ࠬ࠲ࠠࠨો"):
      bstack11lll1ll_opy_ = bstack11lll1ll_opy_[:-2]
    return bstack11lll1ll_opy_
def bstack1l1l11ll11_opy_(path, bstack11lll1ll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11l111l1l_opy_ = ET.parse(path)
    bstack111l1lll1_opy_ = bstack11l111l1l_opy_.getroot()
    bstack1l11l11ll_opy_ = None
    for suite in bstack111l1lll1_opy_.iter(bstack1lllll1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬૌ")):
      if bstack1lllll1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫્ࠧ") in suite.attrib:
        suite.attrib[bstack1lllll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭૎")] += bstack1lllll1_opy_ (u"ࠩࠣࠫ૏") + bstack11lll1ll_opy_
        bstack1l11l11ll_opy_ = suite
    bstack1l1l1ll1ll_opy_ = None
    for robot in bstack111l1lll1_opy_.iter(bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩૐ")):
      bstack1l1l1ll1ll_opy_ = robot
    bstack1l11l111l1_opy_ = len(bstack1l1l1ll1ll_opy_.findall(bstack1lllll1_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪ૑")))
    if bstack1l11l111l1_opy_ == 1:
      bstack1l1l1ll1ll_opy_.remove(bstack1l1l1ll1ll_opy_.findall(bstack1lllll1_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ૒"))[0])
      bstack1l1lll1l_opy_ = ET.Element(bstack1lllll1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ૓"), attrib={bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ૔"): bstack1lllll1_opy_ (u"ࠨࡕࡸ࡭ࡹ࡫ࡳࠨ૕"), bstack1lllll1_opy_ (u"ࠩ࡬ࡨࠬ૖"): bstack1lllll1_opy_ (u"ࠪࡷ࠵࠭૗")})
      bstack1l1l1ll1ll_opy_.insert(1, bstack1l1lll1l_opy_)
      bstack1l1llllll1_opy_ = None
      for suite in bstack1l1l1ll1ll_opy_.iter(bstack1lllll1_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪ૘")):
        bstack1l1llllll1_opy_ = suite
      bstack1l1llllll1_opy_.append(bstack1l11l11ll_opy_)
      bstack1l11lllll_opy_ = None
      for status in bstack1l11l11ll_opy_.iter(bstack1lllll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ૙")):
        bstack1l11lllll_opy_ = status
      bstack1l1llllll1_opy_.append(bstack1l11lllll_opy_)
    bstack11l111l1l_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠫ૚") + str(e))
def bstack1l1ll11l11_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l1lll111_opy_
  global CONFIG
  if bstack1lllll1_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡰࡢࡶ࡫ࠦ૛") in options:
    del options[bstack1lllll1_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧ૜")]
  bstack1l1llll1ll_opy_ = bstack11llllll1_opy_()
  for bstack111l11ll1_opy_ in bstack1l1llll1ll_opy_.keys():
    path = os.path.join(os.getcwd(), bstack1lllll1_opy_ (u"ࠩࡳࡥࡧࡵࡴࡠࡴࡨࡷࡺࡲࡴࡴࠩ૝"), str(bstack111l11ll1_opy_), bstack1lllll1_opy_ (u"ࠪࡳࡺࡺࡰࡶࡶ࠱ࡼࡲࡲࠧ૞"))
    bstack1l1l11ll11_opy_(path, bstack111l1l111_opy_(bstack1l1llll1ll_opy_[bstack111l11ll1_opy_]))
  bstack1l1111l1l_opy_()
  return bstack1l1lll111_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1l11lll1l1_opy_(self, ff_profile_dir):
  global bstack11111l11l_opy_
  if not ff_profile_dir:
    return None
  return bstack11111l11l_opy_(self, ff_profile_dir)
def bstack1ll1lll1ll_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l11ll11ll_opy_
  bstack1l1l11llll_opy_ = []
  if bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૟") in CONFIG:
    bstack1l1l11llll_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૠ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1lllll1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࠢૡ")],
      pabot_args[bstack1lllll1_opy_ (u"ࠢࡷࡧࡵࡦࡴࡹࡥࠣૢ")],
      argfile,
      pabot_args.get(bstack1lllll1_opy_ (u"ࠣࡪ࡬ࡺࡪࠨૣ")),
      pabot_args[bstack1lllll1_opy_ (u"ࠤࡳࡶࡴࡩࡥࡴࡵࡨࡷࠧ૤")],
      platform[0],
      bstack1l11ll11ll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1lllll1_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࡫࡯࡬ࡦࡵࠥ૥")] or [(bstack1lllll1_opy_ (u"ࠦࠧ૦"), None)]
    for platform in enumerate(bstack1l1l11llll_opy_)
  ]
def bstack111ll1l11_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l111lllll_opy_=bstack1lllll1_opy_ (u"ࠬ࠭૧")):
  global bstack1llll11l1l_opy_
  self.platform_index = platform_index
  self.bstack1ll111l11l_opy_ = bstack1l111lllll_opy_
  bstack1llll11l1l_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11l1ll11_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack11llll1ll_opy_
  global bstack1ll1lllll_opy_
  bstack1ll1111ll1_opy_ = copy.deepcopy(item)
  if not bstack1lllll1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ૨") in item.options:
    bstack1ll1111ll1_opy_.options[bstack1lllll1_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ૩")] = []
  bstack1lllllll1_opy_ = bstack1ll1111ll1_opy_.options[bstack1lllll1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ૪")].copy()
  for v in bstack1ll1111ll1_opy_.options[bstack1lllll1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ૫")]:
    if bstack1lllll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩ૬") in v:
      bstack1lllllll1_opy_.remove(v)
    if bstack1lllll1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫ૭") in v:
      bstack1lllllll1_opy_.remove(v)
    if bstack1lllll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩ૮") in v:
      bstack1lllllll1_opy_.remove(v)
  bstack1lllllll1_opy_.insert(0, bstack1lllll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜࠿ࢁࡽࠨ૯").format(bstack1ll1111ll1_opy_.platform_index))
  bstack1lllllll1_opy_.insert(0, bstack1lllll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ࠾ࢀࢃࠧ૰").format(bstack1ll1111ll1_opy_.bstack1ll111l11l_opy_))
  bstack1ll1111ll1_opy_.options[bstack1lllll1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ૱")] = bstack1lllllll1_opy_
  if bstack1ll1lllll_opy_:
    bstack1ll1111ll1_opy_.options[bstack1lllll1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ૲")].insert(0, bstack1lllll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕ࠽ࡿࢂ࠭૳").format(bstack1ll1lllll_opy_))
  return bstack11llll1ll_opy_(caller_id, datasources, is_last, bstack1ll1111ll1_opy_, outs_dir)
def bstack11lll11l_opy_(command, item_index):
  if bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ૴")):
    os.environ[bstack1lllll1_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭૵")] = json.dumps(CONFIG[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૶")][item_index % bstack111lll1l1_opy_])
  global bstack1ll1lllll_opy_
  if bstack1ll1lllll_opy_:
    command[0] = command[0].replace(bstack1lllll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭૷"), bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠤࠬ૸") + str(
      item_index) + bstack1lllll1_opy_ (u"ࠩࠣࠫૹ") + bstack1ll1lllll_opy_, 1)
  else:
    command[0] = command[0].replace(bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩૺ"),
                                    bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨૻ") + str(item_index), 1)
def bstack1ll1ll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1ll1l1l1_opy_
  bstack11lll11l_opy_(command, item_index)
  return bstack1ll1l1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1llll1l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1ll1l1l1_opy_
  bstack11lll11l_opy_(command, item_index)
  return bstack1ll1l1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1lll1l11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1ll1l1l1_opy_
  bstack11lll11l_opy_(command, item_index)
  return bstack1ll1l1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1llll1llll_opy_(self, runner, quiet=False, capture=True):
  global bstack1l11ll1lll_opy_
  bstack1ll1ll111_opy_ = bstack1l11ll1lll_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1lllll1_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬૼ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1lllll1_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪ૽")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1ll1ll111_opy_
def bstack1lll1l1l_opy_(self, name, context, *args):
  os.environ[bstack1lllll1_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ૾")] = json.dumps(CONFIG[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૿")][int(threading.current_thread()._name) % bstack111lll1l1_opy_])
  global bstack1llll1l11l_opy_
  if name == bstack1lllll1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠪ଀"):
    bstack1llll1l11l_opy_(self, name, context, *args)
    try:
      if not bstack111l1ll11_opy_:
        bstack1ll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll1_opy_(bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩଁ")) else context.browser
        bstack1l1llllll_opy_ = str(self.feature.name)
        bstack1l11l11l11_opy_(context, bstack1l1llllll_opy_)
        bstack1ll1l111l_opy_.execute_script(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩଂ") + json.dumps(bstack1l1llllll_opy_) + bstack1lllll1_opy_ (u"ࠬࢃࡽࠨଃ"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭଄").format(str(e)))
  elif name == bstack1lllll1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩଅ"):
    bstack1llll1l11l_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack1lllll1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪଆ")):
        self.driver_before_scenario = True
      if (not bstack111l1ll11_opy_):
        scenario_name = args[0].name
        feature_name = bstack1l1llllll_opy_ = str(self.feature.name)
        bstack1l1llllll_opy_ = feature_name + bstack1lllll1_opy_ (u"ࠩࠣ࠱ࠥ࠭ଇ") + scenario_name
        bstack1ll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll1_opy_(bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩଈ")) else context.browser
        if self.driver_before_scenario:
          bstack1l11l11l11_opy_(context, bstack1l1llllll_opy_)
          bstack1ll1l111l_opy_.execute_script(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩଉ") + json.dumps(bstack1l1llllll_opy_) + bstack1lllll1_opy_ (u"ࠬࢃࡽࠨଊ"))
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧଋ").format(str(e)))
  elif name == bstack1lllll1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨଌ"):
    try:
      bstack1l1l111lll_opy_ = args[0].status.name
      bstack1ll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ଍") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack1l1l111lll_opy_).lower() == bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ଎"):
        bstack11ll11ll1_opy_ = bstack1lllll1_opy_ (u"ࠪࠫଏ")
        bstack11111lll_opy_ = bstack1lllll1_opy_ (u"ࠫࠬଐ")
        bstack1llll11l11_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭଑")
        try:
          import traceback
          bstack11ll11ll1_opy_ = self.exception.__class__.__name__
          bstack1l1l11111l_opy_ = traceback.format_tb(self.exc_traceback)
          bstack11111lll_opy_ = bstack1lllll1_opy_ (u"࠭ࠠࠨ଒").join(bstack1l1l11111l_opy_)
          bstack1llll11l11_opy_ = bstack1l1l11111l_opy_[-1]
        except Exception as e:
          logger.debug(bstack1111l11ll_opy_.format(str(e)))
        bstack11ll11ll1_opy_ += bstack1llll11l11_opy_
        bstack1111ll11_opy_(context, json.dumps(str(args[0].name) + bstack1lllll1_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨଓ") + str(bstack11111lll_opy_)),
                            bstack1lllll1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢଔ"))
        if self.driver_before_scenario:
          bstack11lll1lll_opy_(getattr(context, bstack1lllll1_opy_ (u"ࠩࡳࡥ࡬࡫ࠧକ"), None), bstack1lllll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥଖ"), bstack11ll11ll1_opy_)
          bstack1ll1l111l_opy_.execute_script(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩଗ") + json.dumps(str(args[0].name) + bstack1lllll1_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦଘ") + str(bstack11111lll_opy_)) + bstack1lllll1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭ଙ"))
        if self.driver_before_scenario:
          bstack1l1l1ll11l_opy_(bstack1ll1l111l_opy_, bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧଚ"), bstack1lllll1_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧଛ") + str(bstack11ll11ll1_opy_))
      else:
        bstack1111ll11_opy_(context, bstack1lllll1_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥଜ"), bstack1lllll1_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣଝ"))
        if self.driver_before_scenario:
          bstack11lll1lll_opy_(getattr(context, bstack1lllll1_opy_ (u"ࠫࡵࡧࡧࡦࠩଞ"), None), bstack1lllll1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧଟ"))
        bstack1ll1l111l_opy_.execute_script(bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫଠ") + json.dumps(str(args[0].name) + bstack1lllll1_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦଡ")) + bstack1lllll1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧଢ"))
        if self.driver_before_scenario:
          bstack1l1l1ll11l_opy_(bstack1ll1l111l_opy_, bstack1lllll1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤଣ"))
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬତ").format(str(e)))
  elif name == bstack1lllll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫଥ"):
    try:
      bstack1ll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll1_opy_(bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫଦ")) else context.browser
      if context.failed is True:
        bstack1l1l1l1ll1_opy_ = []
        bstack11ll1l11l_opy_ = []
        bstack11ll11l1_opy_ = []
        bstack1l1l1ll11_opy_ = bstack1lllll1_opy_ (u"࠭ࠧଧ")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack1l1l1l1ll1_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1l1l11111l_opy_ = traceback.format_tb(exc_tb)
            bstack1l1ll1l1l1_opy_ = bstack1lllll1_opy_ (u"ࠧࠡࠩନ").join(bstack1l1l11111l_opy_)
            bstack11ll1l11l_opy_.append(bstack1l1ll1l1l1_opy_)
            bstack11ll11l1_opy_.append(bstack1l1l11111l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1111l11ll_opy_.format(str(e)))
        bstack11ll11ll1_opy_ = bstack1lllll1_opy_ (u"ࠨࠩ଩")
        for i in range(len(bstack1l1l1l1ll1_opy_)):
          bstack11ll11ll1_opy_ += bstack1l1l1l1ll1_opy_[i] + bstack11ll11l1_opy_[i] + bstack1lllll1_opy_ (u"ࠩ࡟ࡲࠬପ")
        bstack1l1l1ll11_opy_ = bstack1lllll1_opy_ (u"ࠪࠤࠬଫ").join(bstack11ll1l11l_opy_)
        if not self.driver_before_scenario:
          bstack1111ll11_opy_(context, bstack1l1l1ll11_opy_, bstack1lllll1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥବ"))
          bstack11lll1lll_opy_(getattr(context, bstack1lllll1_opy_ (u"ࠬࡶࡡࡨࡧࠪଭ"), None), bstack1lllll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨମ"), bstack11ll11ll1_opy_)
          bstack1ll1l111l_opy_.execute_script(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬଯ") + json.dumps(bstack1l1l1ll11_opy_) + bstack1lllll1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨର"))
          bstack1l1l1ll11l_opy_(bstack1ll1l111l_opy_, bstack1lllll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ଱"), bstack1lllll1_opy_ (u"ࠥࡗࡴࡳࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࡢ࡮ࠣଲ") + str(bstack11ll11ll1_opy_))
          bstack1l1l1ll111_opy_ = bstack1l1ll1ll11_opy_(bstack1l1l1ll11_opy_, self.feature.name, logger)
          if (bstack1l1l1ll111_opy_ != None):
            bstack111lll11_opy_.append(bstack1l1l1ll111_opy_)
      else:
        if not self.driver_before_scenario:
          bstack1111ll11_opy_(context, bstack1lllll1_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢଳ") + str(self.feature.name) + bstack1lllll1_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢ଴"), bstack1lllll1_opy_ (u"ࠨࡩ࡯ࡨࡲࠦଵ"))
          bstack11lll1lll_opy_(getattr(context, bstack1lllll1_opy_ (u"ࠧࡱࡣࡪࡩࠬଶ"), None), bstack1lllll1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣଷ"))
          bstack1ll1l111l_opy_.execute_script(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧସ") + json.dumps(bstack1lllll1_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨହ") + str(self.feature.name) + bstack1lllll1_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨ଺")) + bstack1lllll1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫ଻"))
          bstack1l1l1ll11l_opy_(bstack1ll1l111l_opy_, bstack1lllll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ଼࠭"))
          bstack1l1l1ll111_opy_ = bstack1l1ll1ll11_opy_(bstack1l1l1ll11_opy_, self.feature.name, logger)
          if (bstack1l1l1ll111_opy_ != None):
            bstack111lll11_opy_.append(bstack1l1l1ll111_opy_)
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩଽ").format(str(e)))
  else:
    bstack1llll1l11l_opy_(self, name, context, *args)
  if name in [bstack1lllll1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨା"), bstack1lllll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪି")]:
    bstack1llll1l11l_opy_(self, name, context, *args)
    if (name == bstack1lllll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫୀ") and self.driver_before_scenario) or (
            name == bstack1lllll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫୁ") and not self.driver_before_scenario):
      try:
        bstack1ll1l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll1_opy_(bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫୂ")) else context.browser
        bstack1ll1l111l_opy_.quit()
      except Exception:
        pass
def bstack11lll1l1l_opy_(config, startdir):
  return bstack1lllll1_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦୃ").format(bstack1lllll1_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨୄ"))
notset = Notset()
def bstack11lll111l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l11lll11l_opy_
  if str(name).lower() == bstack1lllll1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨ୅"):
    return bstack1lllll1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣ୆")
  else:
    return bstack1l11lll11l_opy_(self, name, default, skip)
def bstack11l1lllll_opy_(item, when):
  global bstack1ll1l1llll_opy_
  try:
    bstack1ll1l1llll_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll1l11ll_opy_():
  return
def bstack1l1l1111_opy_(type, name, status, reason, bstack11l11111l_opy_, bstack111ll111l_opy_):
  bstack1lllll11l_opy_ = {
    bstack1lllll1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪେ"): type,
    bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧୈ"): {}
  }
  if type == bstack1lllll1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ୉"):
    bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ୊")][bstack1lllll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ୋ")] = bstack11l11111l_opy_
    bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫୌ")][bstack1lllll1_opy_ (u"ࠩࡧࡥࡹࡧ୍ࠧ")] = json.dumps(str(bstack111ll111l_opy_))
  if type == bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ୎"):
    bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ୏")][bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ୐")] = name
  if type == bstack1lllll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ୑"):
    bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ୒")][bstack1lllll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ୓")] = status
    if status == bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ୔"):
      bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭୕")][bstack1lllll1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫୖ")] = json.dumps(str(reason))
  bstack1ll1ll11l1_opy_ = bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪୗ").format(json.dumps(bstack1lllll11l_opy_))
  return bstack1ll1ll11l1_opy_
def bstack1l111l1ll_opy_(driver_command, response):
    if driver_command == bstack1lllll1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪ୘"):
        bstack1lllll11_opy_.bstack1l11ll1l1l_opy_({
            bstack1lllll1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭୙"): response[bstack1lllll1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧ୚")],
            bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ୛"): bstack1lllll11_opy_.current_test_uuid()
        })
def bstack11l1l111_opy_(item, call, rep):
  global bstack1ll111111_opy_
  global bstack1l11l1l11_opy_
  global bstack111l1ll11_opy_
  name = bstack1lllll1_opy_ (u"ࠪࠫଡ଼")
  try:
    if rep.when == bstack1lllll1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩଢ଼"):
      bstack1l11ll11_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111l1ll11_opy_:
          name = str(rep.nodeid)
          bstack1ll1l1111_opy_ = bstack1l1l1111_opy_(bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭୞"), name, bstack1lllll1_opy_ (u"࠭ࠧୟ"), bstack1lllll1_opy_ (u"ࠧࠨୠ"), bstack1lllll1_opy_ (u"ࠨࠩୡ"), bstack1lllll1_opy_ (u"ࠩࠪୢ"))
          threading.current_thread().bstack1lll1lll1l_opy_ = name
          for driver in bstack1l11l1l11_opy_:
            if bstack1l11ll11_opy_ == driver.session_id:
              driver.execute_script(bstack1ll1l1111_opy_)
      except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪୣ").format(str(e)))
      try:
        bstack1l1l111ll1_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1lllll1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ୤"):
          status = bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ୥") if rep.outcome.lower() == bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭୦") else bstack1lllll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ୧")
          reason = bstack1lllll1_opy_ (u"ࠨࠩ୨")
          if status == bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ୩"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1lllll1_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ୪") if status == bstack1lllll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ୫") else bstack1lllll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ୬")
          data = name + bstack1lllll1_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ୭") if status == bstack1lllll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ୮") else name + bstack1lllll1_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫ୯") + reason
          bstack111l1l1l1_opy_ = bstack1l1l1111_opy_(bstack1lllll1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ୰"), bstack1lllll1_opy_ (u"ࠪࠫୱ"), bstack1lllll1_opy_ (u"ࠫࠬ୲"), bstack1lllll1_opy_ (u"ࠬ࠭୳"), level, data)
          for driver in bstack1l11l1l11_opy_:
            if bstack1l11ll11_opy_ == driver.session_id:
              driver.execute_script(bstack111l1l1l1_opy_)
      except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ୴").format(str(e)))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫ୵").format(str(e)))
  bstack1ll111111_opy_(item, call, rep)
def bstack1l1ll1l1ll_opy_(driver, bstack111l1l11l_opy_):
  PercySDK.screenshot(driver, bstack111l1l11l_opy_)
def bstack1ll1lll11l_opy_(driver):
  if bstack111111l1_opy_.bstack1lllll1lll_opy_() is True or bstack111111l1_opy_.capturing() is True:
    return
  bstack111111l1_opy_.bstack1l1l11lll1_opy_()
  while not bstack111111l1_opy_.bstack1lllll1lll_opy_():
    bstack1l11ll111_opy_ = bstack111111l1_opy_.bstack1ll11l1111_opy_()
    bstack1l1ll1l1ll_opy_(driver, bstack1l11ll111_opy_)
  bstack111111l1_opy_.bstack1111llll1_opy_()
def bstack1l1111111_opy_(sequence, driver_command, response = None, bstack1l1111l11_opy_ = None, args = None):
    try:
      if sequence != bstack1lllll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ୶"):
        return
      if not CONFIG.get(bstack1lllll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ୷"), False):
        return
      bstack1l11ll111_opy_ = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭୸"), None)
      for command in bstack11l11ll1_opy_:
        if command == driver_command:
          for driver in bstack1l11l1l11_opy_:
            bstack1ll1lll11l_opy_(driver)
      bstack1l1l1l11l_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧ୹"), bstack1lllll1_opy_ (u"ࠧࡧࡵࡵࡱࠥ୺"))
      if driver_command in bstack1llll1l1l_opy_[bstack1l1l1l11l_opy_]:
        bstack111111l1_opy_.bstack1l1ll11l1_opy_(bstack1l11ll111_opy_, driver_command)
    except Exception as e:
      pass
def bstack111l111l1_opy_(framework_name):
  global bstack1ll11l1l1l_opy_
  global bstack1ll1llll_opy_
  global bstack11ll1llll_opy_
  bstack1ll11l1l1l_opy_ = framework_name
  logger.info(bstack1ll1ll1ll_opy_.format(bstack1ll11l1l1l_opy_.split(bstack1lllll1_opy_ (u"࠭࠭ࠨ୻"))[0]))
  bstack11l11l11_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack111ll1ll_opy_:
      Service.start = bstack11ll1l1l1_opy_
      Service.stop = bstack1ll1ll11_opy_
      webdriver.Remote.get = bstack111111lll_opy_
      WebDriver.close = bstack1l11ll1ll_opy_
      WebDriver.quit = bstack1ll1l11lll_opy_
      webdriver.Remote.__init__ = bstack11ll1l1ll_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.get_accessibility_results = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
      WebDriver.performScan = perform_scan
      WebDriver.perform_scan = perform_scan
    if not bstack111ll1ll_opy_:
        webdriver.Remote.__init__ = bstack1l1l1111ll_opy_
    WebDriver.execute = bstack1lll1ll1l_opy_
    bstack1ll1llll_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack111ll1ll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1llll1lll1_opy_
  except Exception as e:
    pass
  bstack111llllll_opy_()
  if not bstack1ll1llll_opy_:
    bstack1l1111ll_opy_(bstack1lllll1_opy_ (u"ࠢࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠢࡱࡳࡹࠦࡩ࡯ࡵࡷࡥࡱࡲࡥࡥࠤ୼"), bstack1lllll11l1_opy_)
  if bstack1llll1ll1l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack11l111lll_opy_
    except Exception as e:
      logger.error(bstack1l11lll1l_opy_.format(str(e)))
  if bstack1111ll1l1_opy_():
    bstack111lll1l_opy_(CONFIG, logger)
  if (bstack1lllll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ୽") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if CONFIG.get(bstack1lllll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ୾"), False):
          bstack1ll1l111l1_opy_(bstack1l1111111_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1l11lll1l1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1llll1l1l1_opy_
      except Exception as e:
        logger.warn(bstack1l11ll111l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1l11l1111l_opy_
      except Exception as e:
        logger.debug(bstack1ll11l1ll_opy_ + str(e))
    except Exception as e:
      bstack1l1111ll_opy_(e, bstack1l11ll111l_opy_)
    Output.start_test = bstack1lllll1l1_opy_
    Output.end_test = bstack1llll11lll_opy_
    TestStatus.__init__ = bstack11lllll1l_opy_
    QueueItem.__init__ = bstack111ll1l11_opy_
    pabot._create_items = bstack1ll1lll1ll_opy_
    try:
      from pabot import __version__ as bstack11l1l1111_opy_
      if version.parse(bstack11l1l1111_opy_) >= version.parse(bstack1lllll1_opy_ (u"ࠪ࠶࠳࠷࠵࠯࠲ࠪ୿")):
        pabot._run = bstack1lll1l11ll_opy_
      elif version.parse(bstack11l1l1111_opy_) >= version.parse(bstack1lllll1_opy_ (u"ࠫ࠷࠴࠱࠴࠰࠳ࠫ஀")):
        pabot._run = bstack1llll1l11_opy_
      else:
        pabot._run = bstack1ll1ll1l_opy_
    except Exception as e:
      pabot._run = bstack1ll1ll1l_opy_
    pabot._create_command_for_execution = bstack11l1ll11_opy_
    pabot._report_results = bstack1l1ll11l11_opy_
  if bstack1lllll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ஁") in str(framework_name).lower():
    if not bstack111ll1ll_opy_:
      return
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1111ll_opy_(e, bstack111l1ll1_opy_)
    Runner.run_hook = bstack1lll1l1l_opy_
    Step.run = bstack1llll1llll_opy_
  if bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ஂ") in str(framework_name).lower():
    if not bstack111ll1ll_opy_:
      return
    try:
      if CONFIG.get(bstack1lllll1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ஃ"), False):
          bstack1ll1l111l1_opy_(bstack1l1111111_opy_)
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11lll1l1l_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1ll1l11ll_opy_
      Config.getoption = bstack11lll111l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11l1l111_opy_
    except Exception as e:
      pass
def bstack1ll1111ll_opy_():
  global CONFIG
  if bstack1lllll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ஄") in CONFIG and int(CONFIG[bstack1lllll1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩஅ")]) > 1:
    logger.warn(bstack1111lll11_opy_)
def bstack1l1l1111l1_opy_(arg, bstack1ll111ll_opy_, bstack1ll1llllll_opy_=None):
  global CONFIG
  global bstack1l11l1ll11_opy_
  global bstack1l1l1lllll_opy_
  global bstack111ll1ll_opy_
  global bstack1111ll1ll_opy_
  bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪஆ")
  if bstack1ll111ll_opy_ and isinstance(bstack1ll111ll_opy_, str):
    bstack1ll111ll_opy_ = eval(bstack1ll111ll_opy_)
  CONFIG = bstack1ll111ll_opy_[bstack1lllll1_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫஇ")]
  bstack1l11l1ll11_opy_ = bstack1ll111ll_opy_[bstack1lllll1_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭ஈ")]
  bstack1l1l1lllll_opy_ = bstack1ll111ll_opy_[bstack1lllll1_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨஉ")]
  bstack111ll1ll_opy_ = bstack1ll111ll_opy_[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪஊ")]
  bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ஋"), bstack111ll1ll_opy_)
  os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ஌")] = bstack1ll11l111l_opy_
  os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩ஍")] = json.dumps(CONFIG)
  os.environ[bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫஎ")] = bstack1l11l1ll11_opy_
  os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ஏ")] = str(bstack1l1l1lllll_opy_)
  os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬஐ")] = str(True)
  if bstack11l1111l1_opy_(arg, [bstack1lllll1_opy_ (u"ࠧ࠮ࡰࠪ஑"), bstack1lllll1_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩஒ")]) != -1:
    os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪஓ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1l1l1l1lll_opy_)
    return
  bstack1lll11l111_opy_()
  global bstack1l1lll1l1l_opy_
  global bstack111ll1ll1_opy_
  global bstack1l11ll11ll_opy_
  global bstack1ll1lllll_opy_
  global bstack1llll11ll1_opy_
  global bstack11ll1llll_opy_
  global bstack1ll1ll1l1l_opy_
  arg.append(bstack1lllll1_opy_ (u"ࠥ࠱࡜ࠨஔ"))
  arg.append(bstack1lllll1_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾ࡒࡵࡤࡶ࡮ࡨࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡯࡭ࡱࡱࡵࡸࡪࡪ࠺ࡱࡻࡷࡩࡸࡺ࠮ࡑࡻࡷࡩࡸࡺࡗࡢࡴࡱ࡭ࡳ࡭ࠢக"))
  arg.append(bstack1lllll1_opy_ (u"ࠧ࠳ࡗࠣ஖"))
  arg.append(bstack1lllll1_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡔࡩࡧࠣ࡬ࡴࡵ࡫ࡪ࡯ࡳࡰࠧ஗"))
  global bstack1l111ll1ll_opy_
  global bstack11l1llll_opy_
  global bstack11111l11_opy_
  global bstack11l111111_opy_
  global bstack11111l11l_opy_
  global bstack1llll11l1l_opy_
  global bstack11llll1ll_opy_
  global bstack1l111111_opy_
  global bstack1ll1lll1l1_opy_
  global bstack1l1l11111_opy_
  global bstack1l11lll11l_opy_
  global bstack1ll1l1llll_opy_
  global bstack1ll111111_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l111ll1ll_opy_ = webdriver.Remote.__init__
    bstack11l1llll_opy_ = WebDriver.quit
    bstack1l111111_opy_ = WebDriver.close
    bstack1ll1lll1l1_opy_ = WebDriver.get
    bstack11111l11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1lll11l11_opy_(CONFIG) and bstack111l11l11_opy_():
    if bstack1ll11lll11_opy_() < version.parse(bstack1l1l1l1l11_opy_):
      logger.error(bstack1l1111lll_opy_.format(bstack1ll11lll11_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1l1l11111_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1l11lll1l_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1l11lll11l_opy_ = Config.getoption
    from _pytest import runner
    bstack1ll1l1llll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1l1l1llll1_opy_)
  try:
    from pytest_bdd import reporting
    bstack1ll111111_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨ஘"))
  bstack1l11ll11ll_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬங"), {}).get(bstack1lllll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫச"))
  bstack1ll1ll1l1l_opy_ = True
  bstack111l111l1_opy_(bstack1l1l11l11l_opy_)
  os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫ஛")] = CONFIG[bstack1lllll1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ஜ")]
  os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨ஝")] = CONFIG[bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩஞ")]
  os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪட")] = bstack111ll1ll_opy_.__str__()
  from _pytest.config import main as bstack1llllll11l_opy_
  bstack1l111ll1_opy_ = []
  try:
    bstack1l11l111l_opy_ = bstack1llllll11l_opy_(arg)
    if bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬ஠") in multiprocessing.current_process().__dict__.keys():
      for bstack1ll11l11l1_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l111ll1_opy_.append(bstack1ll11l11l1_opy_)
    try:
      bstack1ll11llll1_opy_ = (bstack1l111ll1_opy_, int(bstack1l11l111l_opy_))
      bstack1ll1llllll_opy_.append(bstack1ll11llll1_opy_)
    except:
      bstack1ll1llllll_opy_.append((bstack1l111ll1_opy_, bstack1l11l111l_opy_))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1l111ll1_opy_.append({bstack1lllll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ஡"): bstack1lllll1_opy_ (u"ࠪࡔࡷࡵࡣࡦࡵࡶࠤࠬ஢") + os.environ.get(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫண")), bstack1lllll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫத"): traceback.format_exc(), bstack1lllll1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ஥"): int(os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ஦")))})
    bstack1ll1llllll_opy_.append((bstack1l111ll1_opy_, 1))
def bstack1l1l1ll1l_opy_(arg):
  global bstack1ll1l11l1_opy_
  bstack111l111l1_opy_(bstack11l11111_opy_)
  os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ஧")] = str(bstack1l1l1lllll_opy_)
  from behave.__main__ import main as bstack1l1l1l111l_opy_
  status_code = bstack1l1l1l111l_opy_(arg)
  if status_code != 0:
    bstack1ll1l11l1_opy_ = status_code
def bstack1lll11lll1_opy_():
  logger.info(bstack1l1ll111_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1lllll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨந"), help=bstack1lllll1_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࠫன"))
  parser.add_argument(bstack1lllll1_opy_ (u"ࠫ࠲ࡻࠧப"), bstack1lllll1_opy_ (u"ࠬ࠳࠭ࡶࡵࡨࡶࡳࡧ࡭ࡦࠩ஫"), help=bstack1lllll1_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ஬"))
  parser.add_argument(bstack1lllll1_opy_ (u"ࠧ࠮࡭ࠪ஭"), bstack1lllll1_opy_ (u"ࠨ࠯࠰࡯ࡪࡿࠧம"), help=bstack1lllll1_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡡࡤࡥࡨࡷࡸࠦ࡫ࡦࡻࠪய"))
  parser.add_argument(bstack1lllll1_opy_ (u"ࠪ࠱࡫࠭ர"), bstack1lllll1_opy_ (u"ࠫ࠲࠳ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩற"), help=bstack1lllll1_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡸࡪࡹࡴࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫல"))
  bstack1l11llll1l_opy_ = parser.parse_args()
  try:
    bstack1l11l1l1ll_opy_ = bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡭ࡥ࡯ࡧࡵ࡭ࡨ࠴ࡹ࡮࡮࠱ࡷࡦࡳࡰ࡭ࡧࠪள")
    if bstack1l11llll1l_opy_.framework and bstack1l11llll1l_opy_.framework not in (bstack1lllll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧழ"), bstack1lllll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩவ")):
      bstack1l11l1l1ll_opy_ = bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨஶ")
    bstack1l1llll11l_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l11l1l1ll_opy_)
    bstack1lll111l_opy_ = open(bstack1l1llll11l_opy_, bstack1lllll1_opy_ (u"ࠪࡶࠬஷ"))
    bstack1l1l1lll_opy_ = bstack1lll111l_opy_.read()
    bstack1lll111l_opy_.close()
    if bstack1l11llll1l_opy_.username:
      bstack1l1l1lll_opy_ = bstack1l1l1lll_opy_.replace(bstack1lllll1_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫஸ"), bstack1l11llll1l_opy_.username)
    if bstack1l11llll1l_opy_.key:
      bstack1l1l1lll_opy_ = bstack1l1l1lll_opy_.replace(bstack1lllll1_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧஹ"), bstack1l11llll1l_opy_.key)
    if bstack1l11llll1l_opy_.framework:
      bstack1l1l1lll_opy_ = bstack1l1l1lll_opy_.replace(bstack1lllll1_opy_ (u"࡙࠭ࡐࡗࡕࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ஺"), bstack1l11llll1l_opy_.framework)
    file_name = bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪ஻")
    file_path = os.path.abspath(file_name)
    bstack1lll1111l1_opy_ = open(file_path, bstack1lllll1_opy_ (u"ࠨࡹࠪ஼"))
    bstack1lll1111l1_opy_.write(bstack1l1l1lll_opy_)
    bstack1lll1111l1_opy_.close()
    logger.info(bstack111l111l_opy_)
    try:
      os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ஽")] = bstack1l11llll1l_opy_.framework if bstack1l11llll1l_opy_.framework != None else bstack1lllll1_opy_ (u"ࠥࠦா")
      config = yaml.safe_load(bstack1l1l1lll_opy_)
      config[bstack1lllll1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫி")] = bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠲ࡹࡥࡵࡷࡳࠫீ")
      bstack1ll1ll1111_opy_(bstack1ll1ll11l_opy_, config)
    except Exception as e:
      logger.debug(bstack111lll1ll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1llll111ll_opy_.format(str(e)))
def bstack1ll1ll1111_opy_(bstack11111ll11_opy_, config, bstack1lll1l111l_opy_={}):
  global bstack111ll1ll_opy_
  global bstack1l1l1ll1l1_opy_
  global bstack1111ll1ll_opy_
  if not config:
    return
  bstack1l1l1111l_opy_ = bstack1l1lllll1l_opy_ if not bstack111ll1ll_opy_ else (
    bstack111l11111_opy_ if bstack1lllll1_opy_ (u"࠭ࡡࡱࡲࠪு") in config else bstack1l11l1ll_opy_)
  bstack111111l1l_opy_ = False
  bstack1lll1111l_opy_ = False
  if bstack111ll1ll_opy_ is True:
      if bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࠫூ") in config:
          bstack111111l1l_opy_ = True
      else:
          bstack1lll1111l_opy_ = True
  bstack1l1l11l1_opy_ = {
      bstack1lllll1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ௃"): bstack1lllll11_opy_.bstack111ll111_opy_(bstack1l1l1ll1l1_opy_),
      bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ௄"): bstack1lll1111ll_opy_.bstack11l1l1ll_opy_(config),
      bstack1lllll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ௅"): config.get(bstack1lllll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪெ"), False),
      bstack1lllll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧே"): bstack1lll1111l_opy_,
      bstack1lllll1_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬை"): bstack111111l1l_opy_
  }
  data = {
    bstack1lllll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ௉"): config[bstack1lllll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪொ")],
    bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬோ"): config[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ௌ")],
    bstack1lllll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ்"): bstack11111ll11_opy_,
    bstack1lllll1_opy_ (u"ࠬࡪࡥࡵࡧࡦࡸࡪࡪࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ௎"): os.environ.get(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ௏"), bstack1l1l1ll1l1_opy_),
    bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩௐ"): bstack1lll1l11_opy_,
    bstack1lllll1_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮ࠪ௑"): bstack1lll111l1_opy_(),
    bstack1lllll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ௒"): {
      bstack1lllll1_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ௓"): str(config[bstack1lllll1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ௔")]) if bstack1lllll1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ௕") in config else bstack1lllll1_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ௖"),
      bstack1lllll1_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡘࡨࡶࡸ࡯࡯࡯ࠩௗ"): sys.version,
      bstack1lllll1_opy_ (u"ࠨࡴࡨࡪࡪࡸࡲࡦࡴࠪ௘"): bstack1l11ll1111_opy_(os.getenv(bstack1lllll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠦ௙"), bstack1lllll1_opy_ (u"ࠥࠦ௚"))),
      bstack1lllll1_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭௛"): bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ௜"),
      bstack1lllll1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧ௝"): bstack1l1l1111l_opy_,
      bstack1lllll1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ௞"): bstack1l1l11l1_opy_,
      bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡡࡸࡹ࡮ࡪࠧ௟"): os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ௠")],
      bstack1lllll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭௡"): bstack11l1l11l1_opy_(os.environ.get(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭௢"), bstack1l1l1ll1l1_opy_)),
      bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௣"): config[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௤")] if config[bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௥")] else bstack1lllll1_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤ௦"),
      bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ௧"): str(config[bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ௨")]) if bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௩") in config else bstack1lllll1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ௪"),
      bstack1lllll1_opy_ (u"࠭࡯ࡴࠩ௫"): sys.platform,
      bstack1lllll1_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ௬"): socket.gethostname(),
      bstack1lllll1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ௭"): bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ௮"))
    }
  }
  if not bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪ௯")) is None:
    data[bstack1lllll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ௰")][bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࡍࡦࡶࡤࡨࡦࡺࡡࠨ௱")] = {
      bstack1lllll1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭௲"): bstack1lllll1_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨࠬ௳"),
      bstack1lllll1_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨ௴"): bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ௵")),
      bstack1lllll1_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࡑࡹࡲࡨࡥࡳࠩ௶"): bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵࠧ௷"))
    }
  update(data[bstack1lllll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ௸")], bstack1lll1l111l_opy_)
  try:
    response = bstack1ll1ll1l1_opy_(bstack1lllll1_opy_ (u"࠭ࡐࡐࡕࡗࠫ௹"), bstack1l111l1l1_opy_(bstack11ll1l11_opy_), data, {
      bstack1lllll1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ௺"): (config[bstack1lllll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ௻")], config[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ௼")])
    })
    if response:
      logger.debug(bstack1ll11ll11l_opy_.format(bstack11111ll11_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11llll11_opy_.format(str(e)))
def bstack1l11ll1111_opy_(framework):
  return bstack1lllll1_opy_ (u"ࠥࡿࢂ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢ௽").format(str(framework), __version__) if framework else bstack1lllll1_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ௾").format(
    __version__)
def bstack1lll11l111_opy_():
  global CONFIG
  global bstack1ll111111l_opy_
  if bool(CONFIG):
    return
  try:
    bstack1111l1ll_opy_()
    logger.debug(bstack11l1l11ll_opy_.format(str(CONFIG)))
    bstack1ll111111l_opy_ = bstack1llll11111_opy_.bstack1l11l11111_opy_(CONFIG, bstack1ll111111l_opy_)
    bstack11l11l11_opy_()
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࠤ௿") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l11l1llll_opy_
  atexit.register(bstack11l11l1l_opy_)
  signal.signal(signal.SIGINT, bstack1ll1l1lll_opy_)
  signal.signal(signal.SIGTERM, bstack1ll1l1lll_opy_)
def bstack1l11l1llll_opy_(exctype, value, traceback):
  global bstack1l11l1l11_opy_
  try:
    for driver in bstack1l11l1l11_opy_:
      bstack1l1l1ll11l_opy_(driver, bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ఀ"), bstack1lllll1_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥఁ") + str(value))
  except Exception:
    pass
  bstack1ll1ll1lll_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1ll1ll1lll_opy_(message=bstack1lllll1_opy_ (u"ࠨࠩం"), bstack1l11llll_opy_ = False):
  global CONFIG
  bstack1ll1l1l1l_opy_ = bstack1lllll1_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡇࡻࡧࡪࡶࡴࡪࡱࡱࠫః") if bstack1l11llll_opy_ else bstack1lllll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩఄ")
  try:
    if message:
      bstack1lll1l111l_opy_ = {
        bstack1ll1l1l1l_opy_ : str(message)
      }
      bstack1ll1ll1111_opy_(bstack1llllll1l_opy_, CONFIG, bstack1lll1l111l_opy_)
    else:
      bstack1ll1ll1111_opy_(bstack1llllll1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1lll1l1lll_opy_.format(str(e)))
def bstack1l11l11ll1_opy_(bstack1llll1111_opy_, size):
  bstack111l11ll_opy_ = []
  while len(bstack1llll1111_opy_) > size:
    bstack1l11111l1_opy_ = bstack1llll1111_opy_[:size]
    bstack111l11ll_opy_.append(bstack1l11111l1_opy_)
    bstack1llll1111_opy_ = bstack1llll1111_opy_[size:]
  bstack111l11ll_opy_.append(bstack1llll1111_opy_)
  return bstack111l11ll_opy_
def bstack1l1llll1l1_opy_(args):
  if bstack1lllll1_opy_ (u"ࠫ࠲ࡳࠧఅ") in args and bstack1lllll1_opy_ (u"ࠬࡶࡤࡣࠩఆ") in args:
    return True
  return False
def run_on_browserstack(bstack1ll1l11111_opy_=None, bstack1ll1llllll_opy_=None, bstack1lll11llll_opy_=False):
  global CONFIG
  global bstack1l11l1ll11_opy_
  global bstack1l1l1lllll_opy_
  global bstack1l1l1ll1l1_opy_
  global bstack1111ll1ll_opy_
  bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"࠭ࠧఇ")
  bstack1lll1lll11_opy_(bstack11ll1lll1_opy_, logger)
  if bstack1ll1l11111_opy_ and isinstance(bstack1ll1l11111_opy_, str):
    bstack1ll1l11111_opy_ = eval(bstack1ll1l11111_opy_)
  if bstack1ll1l11111_opy_:
    CONFIG = bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧఈ")]
    bstack1l11l1ll11_opy_ = bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩఉ")]
    bstack1l1l1lllll_opy_ = bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫఊ")]
    bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬఋ"), bstack1l1l1lllll_opy_)
    bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫఌ")
  bstack1111ll1ll_opy_.bstack1ll11111ll_opy_(bstack1lllll1_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ఍"), uuid4().__str__())
  logger.debug(bstack1lllll1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤ࠾ࠩఎ") + bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩఏ")))
  if not bstack1lll11llll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1l1l1l1lll_opy_)
      return
    if sys.argv[1] == bstack1lllll1_opy_ (u"ࠨ࠯࠰ࡺࡪࡸࡳࡪࡱࡱࠫఐ") or sys.argv[1] == bstack1lllll1_opy_ (u"ࠩ࠰ࡺࠬ఑"):
      logger.info(bstack1lllll1_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡓࡽࡹ࡮࡯࡯ࠢࡖࡈࡐࠦࡶࡼࡿࠪఒ").format(__version__))
      return
    if sys.argv[1] == bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪఓ"):
      bstack1lll11lll1_opy_()
      return
  args = sys.argv
  bstack1lll11l111_opy_()
  global bstack1l1lll1l1l_opy_
  global bstack111lll1l1_opy_
  global bstack1ll1ll1l1l_opy_
  global bstack111l1lll_opy_
  global bstack111ll1ll1_opy_
  global bstack1l11ll11ll_opy_
  global bstack1ll1lllll_opy_
  global bstack11llll111_opy_
  global bstack1llll11ll1_opy_
  global bstack11ll1llll_opy_
  global bstack11l1l1l11_opy_
  bstack111lll1l1_opy_ = len(CONFIG.get(bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఔ"), []))
  if not bstack1ll11l111l_opy_:
    if args[1] == bstack1lllll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭క") or args[1] == bstack1lllll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨఖ"):
      bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨగ")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨఘ"):
      bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩఙ")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪచ"):
      bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫఛ")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧజ"):
      bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨఝ")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨఞ"):
      bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩట")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪఠ"):
      bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫడ")
      args = args[2:]
    else:
      if not bstack1lllll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨఢ") in CONFIG or str(CONFIG[bstack1lllll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩణ")]).lower() in [bstack1lllll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧత"), bstack1lllll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩథ")]:
        bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩద")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ధ")]).lower() == bstack1lllll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪన"):
        bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ఩")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩప")]).lower() == bstack1lllll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ఫ"):
        bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧబ")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬభ")]).lower() == bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪమ"):
        bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫయ")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨర")]).lower() == bstack1lllll1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ఱ"):
        bstack1ll11l111l_opy_ = bstack1lllll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧల")
        args = args[1:]
      else:
        os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪళ")] = bstack1ll11l111l_opy_
        bstack1l11l1l1_opy_(bstack1lll1l1l11_opy_)
  os.environ[bstack1lllll1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪఴ")] = bstack1ll11l111l_opy_
  bstack1l1l1ll1l1_opy_ = bstack1ll11l111l_opy_
  global bstack11l1ll11l_opy_
  global bstack1lll1l11l1_opy_
  if bstack1ll1l11111_opy_:
    try:
      os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬవ")] = bstack1ll11l111l_opy_
      bstack1ll1ll1111_opy_(bstack1llllll111_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack111ll1lll_opy_.format(str(e)))
  global bstack1l111ll1ll_opy_
  global bstack11l1llll_opy_
  global bstack1l1ll1l111_opy_
  global bstack1l1ll11lll_opy_
  global bstack1ll11111_opy_
  global bstack111l11l1l_opy_
  global bstack11l111111_opy_
  global bstack11111l11l_opy_
  global bstack1ll1l1l1_opy_
  global bstack1llll11l1l_opy_
  global bstack11llll1ll_opy_
  global bstack1l111111_opy_
  global bstack1llll1l11l_opy_
  global bstack1l11ll1lll_opy_
  global bstack1ll1lll1l1_opy_
  global bstack1l1l11111_opy_
  global bstack1l11lll11l_opy_
  global bstack1ll1l1llll_opy_
  global bstack1l1lll111_opy_
  global bstack1ll111111_opy_
  global bstack11111l11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l111ll1ll_opy_ = webdriver.Remote.__init__
    bstack11l1llll_opy_ = WebDriver.quit
    bstack1l111111_opy_ = WebDriver.close
    bstack1ll1lll1l1_opy_ = WebDriver.get
    bstack11111l11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11l1ll11l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1l1ll11ll_opy_
    bstack1lll1l11l1_opy_ = bstack1l1ll11ll_opy_()
  except Exception as e:
    pass
  try:
    global bstack1l11l111_opy_
    from QWeb.keywords import browser
    bstack1l11l111_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1lll11l11_opy_(CONFIG) and bstack111l11l11_opy_():
    if bstack1ll11lll11_opy_() < version.parse(bstack1l1l1l1l11_opy_):
      logger.error(bstack1l1111lll_opy_.format(bstack1ll11lll11_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1l1l11111_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1l11lll1l_opy_.format(str(e)))
  if not CONFIG.get(bstack1lllll1_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭శ"), False) and not bstack1ll1l11111_opy_:
    logger.info(bstack1ll11lll_opy_)
  if bstack1ll11l111l_opy_ != bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬష") or (bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭స") and not bstack1ll1l11111_opy_):
    bstack1ll11ll1_opy_()
  if (bstack1ll11l111l_opy_ in [bstack1lllll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭హ"), bstack1lllll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ఺"), bstack1lllll1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ఻")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1l11lll1l1_opy_
        bstack111l11l1l_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l11ll111l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1ll11111_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll11l1ll_opy_ + str(e))
    except Exception as e:
      bstack1l1111ll_opy_(e, bstack1l11ll111l_opy_)
    if bstack1ll11l111l_opy_ != bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯఼ࠫ"):
      bstack1l1111l1l_opy_()
    bstack1l1ll1l111_opy_ = Output.start_test
    bstack1l1ll11lll_opy_ = Output.end_test
    bstack11l111111_opy_ = TestStatus.__init__
    bstack1ll1l1l1_opy_ = pabot._run
    bstack1llll11l1l_opy_ = QueueItem.__init__
    bstack11llll1ll_opy_ = pabot._create_command_for_execution
    bstack1l1lll111_opy_ = pabot._report_results
  if bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫఽ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1111ll_opy_(e, bstack111l1ll1_opy_)
    bstack1llll1l11l_opy_ = Runner.run_hook
    bstack1l11ll1lll_opy_ = Step.run
  if bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬా"):
    try:
      from _pytest.config import Config
      bstack1l11lll11l_opy_ = Config.getoption
      from _pytest import runner
      bstack1ll1l1llll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1l1l1llll1_opy_)
    try:
      from pytest_bdd import reporting
      bstack1ll111111_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧి"))
  try:
    framework_name = bstack1lllll1_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭ీ") if bstack1ll11l111l_opy_ in [bstack1lllll1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧు"), bstack1lllll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨూ"), bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫృ")] else bstack1ll1l1ll11_opy_(bstack1ll11l111l_opy_)
    bstack1lllll11_opy_.launch(CONFIG, {
      bstack1lllll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠬౄ"): bstack1lllll1_opy_ (u"ࠬࢁ࠰ࡾ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫ౅").format(framework_name) if bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ె") and bstack11lll1ll1_opy_() else framework_name,
      bstack1lllll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫే"): bstack11l1l11l1_opy_(framework_name),
      bstack1lllll1_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ై"): __version__,
      bstack1lllll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪ౉"): bstack1ll11l111l_opy_
    })
  except Exception as e:
    logger.debug(bstack1l1llll111_opy_.format(bstack1lllll1_opy_ (u"ࠪࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪొ"), str(e)))
  if bstack1ll11l111l_opy_ in bstack11ll1111_opy_:
    try:
      framework_name = bstack1lllll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪో") if bstack1ll11l111l_opy_ in [bstack1lllll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫౌ"), bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸ్ࠬ")] else bstack1ll11l111l_opy_
      if bstack111ll1ll_opy_ and bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ౎") in CONFIG and CONFIG[bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ౏")] == True:
        if bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ౐") in CONFIG:
          os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ౑")] = os.getenv(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ౒"), json.dumps(CONFIG[bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ౓")]))
          CONFIG[bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭౔")].pop(bstack1lllll1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩౕࠬ"), None)
          CONFIG[bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨౖ")].pop(bstack1lllll1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ౗"), None)
        bstack1l1l11l1ll_opy_, bstack1l1ll11l_opy_ = bstack1lll1111ll_opy_.bstack1lll1ll11_opy_(CONFIG, bstack1ll11l111l_opy_, bstack11l1l11l1_opy_(framework_name), str(bstack1ll11lll11_opy_()))
        if not bstack1l1l11l1ll_opy_ is None:
          os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨౘ")] = bstack1l1l11l1ll_opy_
          os.environ[bstack1lllll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤ࡚ࡅࡔࡖࡢࡖ࡚ࡔ࡟ࡊࡆࠪౙ")] = str(bstack1l1ll11l_opy_)
    except Exception as e:
      logger.debug(bstack1l1llll111_opy_.format(bstack1lllll1_opy_ (u"ࠬࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬౚ"), str(e)))
  if bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭౛"):
    bstack1ll1ll1l1l_opy_ = True
    if bstack1ll1l11111_opy_ and bstack1lll11llll_opy_:
      bstack1l11ll11ll_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ౜"), {}).get(bstack1lllll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪౝ"))
      bstack111l111l1_opy_(bstack111l111ll_opy_)
    elif bstack1ll1l11111_opy_:
      bstack1l11ll11ll_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭౞"), {}).get(bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ౟"))
      global bstack1l11l1l11_opy_
      try:
        if bstack1l1llll1l1_opy_(bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧౠ")]) and multiprocessing.current_process().name == bstack1lllll1_opy_ (u"ࠬ࠶ࠧౡ"):
          bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩౢ")].remove(bstack1lllll1_opy_ (u"ࠧ࠮࡯ࠪౣ"))
          bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ౤")].remove(bstack1lllll1_opy_ (u"ࠩࡳࡨࡧ࠭౥"))
          bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭౦")] = bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ౧")][0]
          with open(bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ౨")], bstack1lllll1_opy_ (u"࠭ࡲࠨ౩")) as f:
            bstack1lllll1ll1_opy_ = f.read()
          bstack11ll11l11_opy_ = bstack1lllll1_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࡧࡩ࡫ࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠪࡶࡩࡱ࡬ࠬࠡࡣࡵ࡫࠱ࠦࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠢࡀࠤ࠵࠯࠺ࠋࠢࠣࡸࡷࡿ࠺ࠋࠢࠣࠤࠥࡧࡲࡨࠢࡀࠤࡸࡺࡲࠩ࡫ࡱࡸ࠭ࡧࡲࡨࠫ࠮࠵࠵࠯ࠊࠡࠢࡨࡼࡨ࡫ࡰࡵࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡧࡳࠡࡧ࠽ࠎࠥࠦࠠࠡࡲࡤࡷࡸࠐࠠࠡࡱࡪࡣࡩࡨࠨࡴࡧ࡯ࡪ࠱ࡧࡲࡨ࠮ࡷࡩࡲࡶ࡯ࡳࡣࡵࡽ࠮ࠐࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࡐࡥࡤ࠱ࡨࡴࡥࡢࡳࡧࡤ࡯ࠥࡃࠠ࡮ࡱࡧࡣࡧࡸࡥࡢ࡭ࠍࡔࡩࡨࠨࠪ࠰ࡶࡩࡹࡥࡴࡳࡣࡦࡩ࠭࠯࡜࡯ࠤࠥࠦ౪").format(str(bstack1ll1l11111_opy_))
          bstack1ll1111lll_opy_ = bstack11ll11l11_opy_ + bstack1lllll1ll1_opy_
          bstack1lllll111l_opy_ = bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ౫")] + bstack1lllll1_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼࠫ౬")
          with open(bstack1lllll111l_opy_, bstack1lllll1_opy_ (u"ࠪࡻࠬ౭")):
            pass
          with open(bstack1lllll111l_opy_, bstack1lllll1_opy_ (u"ࠦࡼ࠱ࠢ౮")) as f:
            f.write(bstack1ll1111lll_opy_)
          import subprocess
          bstack111l1111l_opy_ = subprocess.run([bstack1lllll1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧ౯"), bstack1lllll111l_opy_])
          if os.path.exists(bstack1lllll111l_opy_):
            os.unlink(bstack1lllll111l_opy_)
          os._exit(bstack111l1111l_opy_.returncode)
        else:
          if bstack1l1llll1l1_opy_(bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ౰")]):
            bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ౱")].remove(bstack1lllll1_opy_ (u"ࠨ࠯ࡰࠫ౲"))
            bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౳")].remove(bstack1lllll1_opy_ (u"ࠪࡴࡩࡨࠧ౴"))
            bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ౵")] = bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ౶")][0]
          bstack111l111l1_opy_(bstack111l111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ౷")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1lllll1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩ౸")] = bstack1lllll1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ౹")
          mod_globals[bstack1lllll1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ౺")] = os.path.abspath(bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭౻")])
          exec(open(bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ౼")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1lllll1_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬ౽").format(str(e)))
          for driver in bstack1l11l1l11_opy_:
            bstack1ll1llllll_opy_.append({
              bstack1lllll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ౾"): bstack1ll1l11111_opy_[bstack1lllll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ౿")],
              bstack1lllll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧಀ"): str(e),
              bstack1lllll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨಁ"): multiprocessing.current_process().name
            })
            bstack1l1l1ll11l_opy_(driver, bstack1lllll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪಂ"), bstack1lllll1_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢಃ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l11l1l11_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1l1l1lllll_opy_, CONFIG, logger)
      bstack1l1l111l11_opy_()
      bstack1ll1111ll_opy_()
      bstack1ll111ll_opy_ = {
        bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ಄"): args[0],
        bstack1lllll1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ಅ"): CONFIG,
        bstack1lllll1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨಆ"): bstack1l11l1ll11_opy_,
        bstack1lllll1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪಇ"): bstack1l1l1lllll_opy_
      }
      percy.bstack1l11ll11l1_opy_()
      if bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಈ") in CONFIG:
        bstack1lll11111l_opy_ = []
        manager = multiprocessing.Manager()
        bstack1l111l111_opy_ = manager.list()
        if bstack1l1llll1l1_opy_(args):
          for index, platform in enumerate(CONFIG[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಉ")]):
            if index == 0:
              bstack1ll111ll_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧಊ")] = args
            bstack1lll11111l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1ll111ll_opy_, bstack1l111l111_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಋ")]):
            bstack1lll11111l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1ll111ll_opy_, bstack1l111l111_opy_)))
        for t in bstack1lll11111l_opy_:
          t.start()
        for t in bstack1lll11111l_opy_:
          t.join()
        bstack11llll111_opy_ = list(bstack1l111l111_opy_)
      else:
        if bstack1l1llll1l1_opy_(args):
          bstack1ll111ll_opy_[bstack1lllll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩಌ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1ll111ll_opy_,))
          test.start()
          test.join()
        else:
          bstack111l111l1_opy_(bstack111l111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1lllll1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩ಍")] = bstack1lllll1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪಎ")
          mod_globals[bstack1lllll1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫಏ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩಐ") or bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ಑"):
    percy.init(bstack1l1l1lllll_opy_, CONFIG, logger)
    percy.bstack1l11ll11l1_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l1111ll_opy_(e, bstack1l11ll111l_opy_)
    bstack1l1l111l11_opy_()
    bstack111l111l1_opy_(bstack1l1ll111ll_opy_)
    if bstack111ll1ll_opy_:
      bstack1lllllll1l_opy_(bstack1l1ll111ll_opy_, args)
      if bstack1lllll1_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪಒ") in args:
        i = args.index(bstack1lllll1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫಓ"))
        args.pop(i)
        args.pop(i)
      if bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಔ") not in CONFIG:
        CONFIG[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಕ")] = [{}]
        bstack111lll1l1_opy_ = 1
      if bstack1l1lll1l1l_opy_ == 0:
        bstack1l1lll1l1l_opy_ = 1
      args.insert(0, str(bstack1l1lll1l1l_opy_))
      args.insert(0, str(bstack1lllll1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧಖ")))
    if bstack1lllll11_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1111ll11l_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1l1ll1111l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1lllll1_opy_ (u"ࠥࡖࡔࡈࡏࡕࡡࡒࡔ࡙ࡏࡏࡏࡕࠥಗ"),
        ).parse_args(bstack1111ll11l_opy_)
        bstack11lll11ll_opy_ = args.index(bstack1111ll11l_opy_[0]) if len(bstack1111ll11l_opy_) > 0 else len(args)
        args.insert(bstack11lll11ll_opy_, str(bstack1lllll1_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨಘ")))
        args.insert(bstack11lll11ll_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡸ࡯ࡣࡱࡷࡣࡱ࡯ࡳࡵࡧࡱࡩࡷ࠴ࡰࡺࠩಙ"))))
        if bstack1l11ll1l1_opy_(os.environ.get(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫಚ"))) and str(os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫಛ"), bstack1lllll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ಜ"))) != bstack1lllll1_opy_ (u"ࠩࡱࡹࡱࡲࠧಝ"):
          for bstack1l1l111ll_opy_ in bstack1l1ll1111l_opy_:
            args.remove(bstack1l1l111ll_opy_)
          bstack1l111llll1_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧಞ")).split(bstack1lllll1_opy_ (u"ࠫ࠱࠭ಟ"))
          for bstack1llll1l1ll_opy_ in bstack1l111llll1_opy_:
            args.append(bstack1llll1l1ll_opy_)
      except Exception as e:
        logger.error(bstack1lllll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࠦࡅࡳࡴࡲࡶࠥ࠳ࠠࠣಠ").format(e))
    pabot.main(args)
  elif bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧಡ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l1111ll_opy_(e, bstack1l11ll111l_opy_)
    for a in args:
      if bstack1lllll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭ಢ") in a:
        bstack111ll1ll1_opy_ = int(a.split(bstack1lllll1_opy_ (u"ࠨ࠼ࠪಣ"))[1])
      if bstack1lllll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ತ") in a:
        bstack1l11ll11ll_opy_ = str(a.split(bstack1lllll1_opy_ (u"ࠪ࠾ࠬಥ"))[1])
      if bstack1lllll1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫದ") in a:
        bstack1ll1lllll_opy_ = str(a.split(bstack1lllll1_opy_ (u"ࠬࡀࠧಧ"))[1])
    bstack1lll1ll1ll_opy_ = None
    if bstack1lllll1_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬನ") in args:
      i = args.index(bstack1lllll1_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭಩"))
      args.pop(i)
      bstack1lll1ll1ll_opy_ = args.pop(i)
    if bstack1lll1ll1ll_opy_ is not None:
      global bstack1ll1llll1l_opy_
      bstack1ll1llll1l_opy_ = bstack1lll1ll1ll_opy_
    bstack111l111l1_opy_(bstack1l1ll111ll_opy_)
    run_cli(args)
    if bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬಪ") in multiprocessing.current_process().__dict__.keys():
      for bstack1ll11l11l1_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1ll1llllll_opy_.append(bstack1ll11l11l1_opy_)
  elif bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩಫ"):
    percy.init(bstack1l1l1lllll_opy_, CONFIG, logger)
    percy.bstack1l11ll11l1_opy_()
    bstack1l1l1lll1l_opy_ = bstack1ll11lllll_opy_(args, logger, CONFIG, bstack111ll1ll_opy_)
    bstack1l1l1lll1l_opy_.bstack11ll1ll11_opy_()
    bstack1l1l111l11_opy_()
    bstack111l1lll_opy_ = True
    bstack11ll1llll_opy_ = bstack1l1l1lll1l_opy_.bstack1ll111l1_opy_()
    bstack1l1l1lll1l_opy_.bstack1ll111ll_opy_(bstack111l1ll11_opy_)
    bstack1ll1l1l11_opy_ = bstack1l1l1lll1l_opy_.bstack1ll11l111_opy_(bstack1l1l1111l1_opy_, {
      bstack1lllll1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫಬ"): bstack1l11l1ll11_opy_,
      bstack1lllll1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ಭ"): bstack1l1l1lllll_opy_,
      bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨಮ"): bstack111ll1ll_opy_
    })
    try:
      bstack1l111ll1_opy_, bstack11lll1l11_opy_ = map(list, zip(*bstack1ll1l1l11_opy_))
      bstack1llll11ll1_opy_ = bstack1l111ll1_opy_[0]
      for status_code in bstack11lll1l11_opy_:
        if status_code != 0:
          bstack11l1l1l11_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡦࡴࡵࡳࡷࡹࠠࡢࡰࡧࠤࡸࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠰ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠺ࠡࡽࢀࠦಯ").format(str(e)))
  elif bstack1ll11l111l_opy_ == bstack1lllll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧರ"):
    try:
      from behave.__main__ import main as bstack1l1l1l111l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l1111ll_opy_(e, bstack111l1ll1_opy_)
    bstack1l1l111l11_opy_()
    bstack111l1lll_opy_ = True
    bstack1l1lll1ll1_opy_ = 1
    if bstack1lllll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨಱ") in CONFIG:
      bstack1l1lll1ll1_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩಲ")]
    if bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಳ") in CONFIG:
      bstack1l1lllll_opy_ = int(bstack1l1lll1ll1_opy_) * int(len(CONFIG[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಴")]))
    else:
      bstack1l1lllll_opy_ = int(bstack1l1lll1ll1_opy_)
    config = Configuration(args)
    bstack1llll111_opy_ = config.paths
    if len(bstack1llll111_opy_) == 0:
      import glob
      pattern = bstack1lllll1_opy_ (u"ࠬ࠰ࠪ࠰ࠬ࠱ࡪࡪࡧࡴࡶࡴࡨࠫವ")
      bstack11lll1111_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11lll1111_opy_)
      config = Configuration(args)
      bstack1llll111_opy_ = config.paths
    bstack1l11lllll1_opy_ = [os.path.normpath(item) for item in bstack1llll111_opy_]
    bstack1ll11ll11_opy_ = [os.path.normpath(item) for item in args]
    bstack11l1111ll_opy_ = [item for item in bstack1ll11ll11_opy_ if item not in bstack1l11lllll1_opy_]
    import platform as pf
    if pf.system().lower() == bstack1lllll1_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧಶ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1l11lllll1_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1lll11111_opy_)))
                    for bstack1lll11111_opy_ in bstack1l11lllll1_opy_]
    bstack1l11l1ll1l_opy_ = []
    for spec in bstack1l11lllll1_opy_:
      bstack1111l1l1_opy_ = []
      bstack1111l1l1_opy_ += bstack11l1111ll_opy_
      bstack1111l1l1_opy_.append(spec)
      bstack1l11l1ll1l_opy_.append(bstack1111l1l1_opy_)
    execution_items = []
    for bstack1111l1l1_opy_ in bstack1l11l1ll1l_opy_:
      if bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಷ") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಸ")]):
          item = {}
          item[bstack1lllll1_opy_ (u"ࠩࡤࡶ࡬࠭ಹ")] = bstack1lllll1_opy_ (u"ࠪࠤࠬ಺").join(bstack1111l1l1_opy_)
          item[bstack1lllll1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ಻")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1lllll1_opy_ (u"ࠬࡧࡲࡨ಼ࠩ")] = bstack1lllll1_opy_ (u"࠭ࠠࠨಽ").join(bstack1111l1l1_opy_)
        item[bstack1lllll1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ಾ")] = 0
        execution_items.append(item)
    bstack1l1l1l1l_opy_ = bstack1l11l11ll1_opy_(execution_items, bstack1l1lllll_opy_)
    for execution_item in bstack1l1l1l1l_opy_:
      bstack1lll11111l_opy_ = []
      for item in execution_item:
        bstack1lll11111l_opy_.append(bstack1l1lllll11_opy_(name=str(item[bstack1lllll1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧಿ")]),
                                             target=bstack1l1l1ll1l_opy_,
                                             args=(item[bstack1lllll1_opy_ (u"ࠩࡤࡶ࡬࠭ೀ")],)))
      for t in bstack1lll11111l_opy_:
        t.start()
      for t in bstack1lll11111l_opy_:
        t.join()
  else:
    bstack1l11l1l1_opy_(bstack1lll1l1l11_opy_)
  if not bstack1ll1l11111_opy_:
    bstack1ll1lll1_opy_()
  bstack1llll11111_opy_.bstack1ll11l1l1_opy_()
def browserstack_initialize(bstack1l1lll11_opy_=None):
  run_on_browserstack(bstack1l1lll11_opy_, None, True)
def bstack1ll1lll1_opy_():
  global CONFIG
  global bstack1l1l1ll1l1_opy_
  global bstack11l1l1l11_opy_
  global bstack1ll1l11l1_opy_
  global bstack1111ll1ll_opy_
  bstack1lllll11_opy_.stop(bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪು")))
  bstack1lllll11_opy_.bstack1l1l11l1l1_opy_()
  if bstack1lll1111ll_opy_.bstack11l1l1ll_opy_(CONFIG):
    bstack1lll1111ll_opy_.bstack1ll1111l1l_opy_()
  [bstack111lll11l_opy_, bstack1111lllll_opy_] = get_build_link()
  if bstack111lll11l_opy_ is not None and bstack1lll11lll_opy_() != -1:
    sessions = bstack11ll1ll1l_opy_(bstack111lll11l_opy_)
    bstack1111111l_opy_(sessions, bstack1111lllll_opy_)
  if bstack1l1l1ll1l1_opy_ == bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫೂ") and bstack11l1l1l11_opy_ != 0:
    sys.exit(bstack11l1l1l11_opy_)
  if bstack1l1l1ll1l1_opy_ == bstack1lllll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬೃ") and bstack1ll1l11l1_opy_ != 0:
    sys.exit(bstack1ll1l11l1_opy_)
def bstack1ll1l1ll11_opy_(bstack1l11l11lll_opy_):
  if bstack1l11l11lll_opy_:
    return bstack1l11l11lll_opy_.capitalize()
  else:
    return bstack1lllll1_opy_ (u"࠭ࠧೄ")
def bstack1l1ll1l11l_opy_(bstack1l11ll1l11_opy_):
  if bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೅") in bstack1l11ll1l11_opy_ and bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ೆ")] != bstack1lllll1_opy_ (u"ࠩࠪೇ"):
    return bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"ࠪࡲࡦࡳࡥࠨೈ")]
  else:
    bstack1ll1111l_opy_ = bstack1lllll1_opy_ (u"ࠦࠧ೉")
    if bstack1lllll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬೊ") in bstack1l11ll1l11_opy_ and bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ೋ")] != None:
      bstack1ll1111l_opy_ += bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧೌ")] + bstack1lllll1_opy_ (u"ࠣ࠮್ࠣࠦ")
      if bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"ࠩࡲࡷࠬ೎")] == bstack1lllll1_opy_ (u"ࠥ࡭ࡴࡹࠢ೏"):
        bstack1ll1111l_opy_ += bstack1lllll1_opy_ (u"ࠦ࡮ࡕࡓࠡࠤ೐")
      bstack1ll1111l_opy_ += (bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ೑")] or bstack1lllll1_opy_ (u"࠭ࠧ೒"))
      return bstack1ll1111l_opy_
    else:
      bstack1ll1111l_opy_ += bstack1ll1l1ll11_opy_(bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ೓")]) + bstack1lllll1_opy_ (u"ࠣࠢࠥ೔") + (
              bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫೕ")] or bstack1lllll1_opy_ (u"ࠪࠫೖ")) + bstack1lllll1_opy_ (u"ࠦ࠱ࠦࠢ೗")
      if bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"ࠬࡵࡳࠨ೘")] == bstack1lllll1_opy_ (u"ࠨࡗࡪࡰࡧࡳࡼࡹࠢ೙"):
        bstack1ll1111l_opy_ += bstack1lllll1_opy_ (u"ࠢࡘ࡫ࡱࠤࠧ೚")
      bstack1ll1111l_opy_ += bstack1l11ll1l11_opy_[bstack1lllll1_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ೛")] or bstack1lllll1_opy_ (u"ࠩࠪ೜")
      return bstack1ll1111l_opy_
def bstack1lll1l111_opy_(bstack1lll1l1ll1_opy_):
  if bstack1lll1l1ll1_opy_ == bstack1lllll1_opy_ (u"ࠥࡨࡴࡴࡥࠣೝ"):
    return bstack1lllll1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡃࡰ࡯ࡳࡰࡪࡺࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧೞ")
  elif bstack1lll1l1ll1_opy_ == bstack1lllll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ೟"):
    return bstack1lllll1_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡋࡧࡩ࡭ࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩೠ")
  elif bstack1lll1l1ll1_opy_ == bstack1lllll1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢೡ"):
    return bstack1lllll1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡔࡦࡹࡳࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨೢ")
  elif bstack1lll1l1ll1_opy_ == bstack1lllll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣೣ"):
    return bstack1lllll1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡇࡵࡶࡴࡸ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ೤")
  elif bstack1lll1l1ll1_opy_ == bstack1lllll1_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧ೥"):
    return bstack1lllll1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࠤࡧࡨࡥ࠸࠸࠶࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࠦࡩࡪࡧ࠳࠳࠸ࠥࡂ࡙࡯࡭ࡦࡱࡸࡸࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ೦")
  elif bstack1lll1l1ll1_opy_ == bstack1lllll1_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠢ೧"):
    return bstack1lllll1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࡕࡹࡳࡴࡩ࡯ࡩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ೨")
  else:
    return bstack1lllll1_opy_ (u"ࠨ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࠬ೩") + bstack1ll1l1ll11_opy_(
      bstack1lll1l1ll1_opy_) + bstack1lllll1_opy_ (u"ࠩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ೪")
def bstack11l11lll1_opy_(session):
  return bstack1lllll1_opy_ (u"ࠪࡀࡹࡸࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡳࡱࡺࠦࡃࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡰࡤࡱࡪࠨ࠾࠽ࡣࠣ࡬ࡷ࡫ࡦ࠾ࠤࡾࢁࠧࠦࡴࡢࡴࡪࡩࡹࡃࠢࡠࡤ࡯ࡥࡳࡱࠢ࠿ࡽࢀࡀ࠴ࡧ࠾࠽࠱ࡷࡨࡃࢁࡽࡼࡿ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁ࠵ࡴࡳࡀࠪ೫").format(
    session[bstack1lllll1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨ೬")], bstack1l1ll1l11l_opy_(session), bstack1lll1l111_opy_(session[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠫ೭")]),
    bstack1lll1l111_opy_(session[bstack1lllll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭೮")]),
    bstack1ll1l1ll11_opy_(session[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ೯")] or session[bstack1lllll1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ೰")] or bstack1lllll1_opy_ (u"ࠩࠪೱ")) + bstack1lllll1_opy_ (u"ࠥࠤࠧೲ") + (session[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ೳ")] or bstack1lllll1_opy_ (u"ࠬ࠭೴")),
    session[bstack1lllll1_opy_ (u"࠭࡯ࡴࠩ೵")] + bstack1lllll1_opy_ (u"ࠢࠡࠤ೶") + session[bstack1lllll1_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ೷")], session[bstack1lllll1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ೸")] or bstack1lllll1_opy_ (u"ࠪࠫ೹"),
    session[bstack1lllll1_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨ೺")] if session[bstack1lllll1_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩ೻")] else bstack1lllll1_opy_ (u"࠭ࠧ೼"))
def bstack1111111l_opy_(sessions, bstack1111lllll_opy_):
  try:
    bstack1l1111l1_opy_ = bstack1lllll1_opy_ (u"ࠢࠣ೽")
    if not os.path.exists(bstack1ll1lll11_opy_):
      os.mkdir(bstack1ll1lll11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lllll1_opy_ (u"ࠨࡣࡶࡷࡪࡺࡳ࠰ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭೾")), bstack1lllll1_opy_ (u"ࠩࡵࠫ೿")) as f:
      bstack1l1111l1_opy_ = f.read()
    bstack1l1111l1_opy_ = bstack1l1111l1_opy_.replace(bstack1lllll1_opy_ (u"ࠪࡿࠪࡘࡅࡔࡗࡏࡘࡘࡥࡃࡐࡗࡑࡘࠪࢃࠧഀ"), str(len(sessions)))
    bstack1l1111l1_opy_ = bstack1l1111l1_opy_.replace(bstack1lllll1_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠧࢀࠫഁ"), bstack1111lllll_opy_)
    bstack1l1111l1_opy_ = bstack1l1111l1_opy_.replace(bstack1lllll1_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠩࢂ࠭ം"),
                                              sessions[0].get(bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡡ࡮ࡧࠪഃ")) if sessions[0] else bstack1lllll1_opy_ (u"ࠧࠨഄ"))
    with open(os.path.join(bstack1ll1lll11_opy_, bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬഅ")), bstack1lllll1_opy_ (u"ࠩࡺࠫആ")) as stream:
      stream.write(bstack1l1111l1_opy_.split(bstack1lllll1_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧഇ"))[0])
      for session in sessions:
        stream.write(bstack11l11lll1_opy_(session))
      stream.write(bstack1l1111l1_opy_.split(bstack1lllll1_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨഈ"))[1])
    logger.info(bstack1lllll1_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠢࡤࡸࠥࢁࡽࠨഉ").format(bstack1ll1lll11_opy_));
  except Exception as e:
    logger.debug(bstack111l1ll1l_opy_.format(str(e)))
def bstack11ll1ll1l_opy_(bstack111lll11l_opy_):
  global CONFIG
  try:
    host = bstack1lllll1_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩഊ") if bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࠫഋ") in CONFIG else bstack1lllll1_opy_ (u"ࠨࡣࡳ࡭ࠬഌ")
    user = CONFIG[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ഍")]
    key = CONFIG[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭എ")]
    bstack11ll11lll_opy_ = bstack1lllll1_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪഏ") if bstack1lllll1_opy_ (u"ࠬࡧࡰࡱࠩഐ") in CONFIG else bstack1lllll1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ഑")
    url = bstack1lllll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠮࡫ࡵࡲࡲࠬഒ").format(user, key, host, bstack11ll11lll_opy_,
                                                                                bstack111lll11l_opy_)
    headers = {
      bstack1lllll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧഓ"): bstack1lllll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬഔ"),
    }
    proxies = bstack1l11111ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack1lllll1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨക")], response.json()))
  except Exception as e:
    logger.debug(bstack11l111ll_opy_.format(str(e)))
def get_build_link():
  global CONFIG
  global bstack1lll1l11_opy_
  try:
    if bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧഖ") in CONFIG:
      host = bstack1lllll1_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨഗ") if bstack1lllll1_opy_ (u"࠭ࡡࡱࡲࠪഘ") in CONFIG else bstack1lllll1_opy_ (u"ࠧࡢࡲ࡬ࠫങ")
      user = CONFIG[bstack1lllll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪച")]
      key = CONFIG[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬഛ")]
      bstack11ll11lll_opy_ = bstack1lllll1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩജ") if bstack1lllll1_opy_ (u"ࠫࡦࡶࡰࠨഝ") in CONFIG else bstack1lllll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧഞ")
      url = bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳ࠭ട").format(user, key, host, bstack11ll11lll_opy_)
      headers = {
        bstack1lllll1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ഠ"): bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫഡ"),
      }
      if bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫഢ") in CONFIG:
        params = {bstack1lllll1_opy_ (u"ࠪࡲࡦࡳࡥࠨണ"): CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧത")], bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨഥ"): CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨദ")]}
      else:
        params = {bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬധ"): CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫന")]}
      proxies = bstack1l11111ll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1l1lll1ll_opy_ = response.json()[0][bstack1lllll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡢࡶ࡫࡯ࡨࠬഩ")]
        if bstack1l1lll1ll_opy_:
          bstack1111lllll_opy_ = bstack1l1lll1ll_opy_[bstack1lllll1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧപ")].split(bstack1lllll1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦ࠱ࡧࡻࡩ࡭ࡦࠪഫ"))[0] + bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷ࠴࠭ബ") + bstack1l1lll1ll_opy_[
            bstack1lllll1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩഭ")]
          logger.info(bstack111l1l11_opy_.format(bstack1111lllll_opy_))
          bstack1lll1l11_opy_ = bstack1l1lll1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪമ")]
          bstack1ll1l11l_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫയ")]
          if bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫര") in CONFIG:
            bstack1ll1l11l_opy_ += bstack1lllll1_opy_ (u"ࠪࠤࠬറ") + CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ല")]
          if bstack1ll1l11l_opy_ != bstack1l1lll1ll_opy_[bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪള")]:
            logger.debug(bstack111ll11l1_opy_.format(bstack1l1lll1ll_opy_[bstack1lllll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫഴ")], bstack1ll1l11l_opy_))
          return [bstack1l1lll1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪവ")], bstack1111lllll_opy_]
    else:
      logger.warn(bstack1lll1111_opy_)
  except Exception as e:
    logger.debug(bstack1111lll1_opy_.format(str(e)))
  return [None, None]
def bstack1l11l111ll_opy_(url, bstack1ll111l1l1_opy_=False):
  global CONFIG
  global bstack11l11ll1l_opy_
  if not bstack11l11ll1l_opy_:
    hostname = bstack1llll1l1_opy_(url)
    is_private = bstack1l1l1ll1_opy_(hostname)
    if (bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬശ") in CONFIG and not bstack1l11ll1l1_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ഷ")])) and (is_private or bstack1ll111l1l1_opy_):
      bstack11l11ll1l_opy_ = hostname
def bstack1llll1l1_opy_(url):
  return urlparse(url).hostname
def bstack1l1l1ll1_opy_(hostname):
  for bstack1ll11l1l_opy_ in bstack1ll111lll1_opy_:
    regex = re.compile(bstack1ll11l1l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l111lll1_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack111ll1ll1_opy_
  bstack1l11l1lll_opy_ = not (bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧസ"), None) and bstack1111l1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪഹ"), None))
  bstack11l1111l_opy_ = getattr(driver, bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬഺ"), None) != True
  if not bstack1lll1111ll_opy_.bstack11111111l_opy_(CONFIG, bstack111ll1ll1_opy_) or (bstack11l1111l_opy_ and bstack1l11l1lll_opy_):
    logger.warning(bstack1lllll1_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤ഻"))
    return {}
  try:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶ഼ࠫ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1l1l1l1ll_opy_.bstack1lllll11ll_opy_)
    return results
  except Exception:
    logger.error(bstack1lllll1_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ࠥഽ"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack111ll1ll1_opy_
  bstack1l11l1lll_opy_ = not (bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ാ"), None) and bstack1111l1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩി"), None))
  bstack11l1111l_opy_ = getattr(driver, bstack1lllll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫീ"), None) != True
  if not bstack1lll1111ll_opy_.bstack11111111l_opy_(CONFIG, bstack111ll1ll1_opy_) or (bstack11l1111l_opy_ and bstack1l11l1lll_opy_):
    logger.warning(bstack1lllll1_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤു"))
    return {}
  try:
    logger.debug(bstack1lllll1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼࠫൂ"))
    logger.debug(perform_scan(driver))
    bstack11l11l11l_opy_ = driver.execute_async_script(bstack1l1l1l1ll_opy_.bstack11l111ll1_opy_)
    return bstack11l11l11l_opy_
  except Exception:
    logger.error(bstack1lllll1_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ࠣൃ"))
    return {}
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack111ll1ll1_opy_
  bstack1l11l1lll_opy_ = not (bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬൄ"), None) and bstack1111l1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ൅"), None))
  bstack11l1111l_opy_ = getattr(driver, bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪെ"), None) != True
  if not bstack1lll1111ll_opy_.bstack11111111l_opy_(CONFIG, bstack111ll1ll1_opy_) or (bstack11l1111l_opy_ and bstack1l11l1lll_opy_):
    logger.warning(bstack1lllll1_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡺࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲ࠳ࠨേ"))
    return {}
  try:
    bstack1111111l1_opy_ = driver.execute_async_script(bstack1l1l1l1ll_opy_.perform_scan, {bstack1lllll1_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬൈ"): kwargs.get(bstack1lllll1_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡣࡰ࡯ࡰࡥࡳࡪࠧ൉"), None) or bstack1lllll1_opy_ (u"ࠧࠨൊ")})
    return bstack1111111l1_opy_
  except Exception:
    logger.error(bstack1lllll1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡷࡻ࡮ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠢോ"))
    return {}