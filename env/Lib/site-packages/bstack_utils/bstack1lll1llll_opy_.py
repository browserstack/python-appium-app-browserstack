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
import json
import requests
import logging
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1lll1ll_opy_ as bstack11l1lll11l_opy_
from bstack_utils.bstack1l1l1l1ll_opy_ import bstack1l1l1l1ll_opy_
from bstack_utils.helper import bstack1l1llll1_opy_, bstack11lllllll1_opy_, bstack11ll1l111_opy_, bstack11l1l11lll_opy_, bstack11l1llll11_opy_, bstack1111l1111_opy_, get_host_info, bstack11l1lll111_opy_, bstack1ll1ll1l1_opy_, bstack1l1111l111_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack1l1111l111_opy_(class_method=False)
def _11l1ll1l1l_opy_(driver, bstack11111111_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1lllll1_opy_ (u"ࠩࡲࡷࡤࡴࡡ࡮ࡧࠪ๤"): caps.get(bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩ๥"), None),
        bstack1lllll1_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ๦"): bstack11111111_opy_.get(bstack1lllll1_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ๧"), None),
        bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ๨"): caps.get(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ๩"), None),
        bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ๪"): caps.get(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ๫"), None)
    }
  except Exception as error:
    logger.debug(bstack1lllll1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧ๬") + str(error))
  return response
def bstack11l1l1ll_opy_(config):
  return config.get(bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ๭"), False) or any([p.get(bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ๮"), False) == True for p in config.get(bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ๯"), [])])
def bstack11111111l_opy_(config, bstack1l1llll11_opy_):
  try:
    if not bstack11ll1l111_opy_(config):
      return False
    bstack11l1l1l11l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ๰"), False)
    if int(bstack1l1llll11_opy_) < len(config.get(bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ๱"), [])) and config[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ๲")][bstack1l1llll11_opy_]:
      bstack11ll11111l_opy_ = config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭๳")][bstack1l1llll11_opy_].get(bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ๴"), None)
    else:
      bstack11ll11111l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ๵"), None)
    if bstack11ll11111l_opy_ != None:
      bstack11l1l1l11l_opy_ = bstack11ll11111l_opy_
    bstack11l1ll1ll1_opy_ = os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ๶")) is not None and len(os.getenv(bstack1lllll1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ๷"))) > 0 and os.getenv(bstack1lllll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭๸")) != bstack1lllll1_opy_ (u"ࠩࡱࡹࡱࡲࠧ๹")
    return bstack11l1l1l11l_opy_ and bstack11l1ll1ll1_opy_
  except Exception as error:
    logger.debug(bstack1lllll1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡩࡷ࡯ࡦࡺ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪ๺") + str(error))
  return False
def bstack1llllllll1_opy_(bstack11l1l1ll1l_opy_, test_tags):
  bstack11l1l1ll1l_opy_ = os.getenv(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ๻"))
  if bstack11l1l1ll1l_opy_ is None:
    return True
  bstack11l1l1ll1l_opy_ = json.loads(bstack11l1l1ll1l_opy_)
  try:
    include_tags = bstack11l1l1ll1l_opy_[bstack1lllll1_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ๼")] if bstack1lllll1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ๽") in bstack11l1l1ll1l_opy_ and isinstance(bstack11l1l1ll1l_opy_[bstack1lllll1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ๾")], list) else []
    exclude_tags = bstack11l1l1ll1l_opy_[bstack1lllll1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭๿")] if bstack1lllll1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ຀") in bstack11l1l1ll1l_opy_ and isinstance(bstack11l1l1ll1l_opy_[bstack1lllll1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨກ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1lllll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦຂ") + str(error))
  return False
def bstack1lll1ll11_opy_(config, bstack11l1l1ll11_opy_, bstack11l1ll111l_opy_, bstack11ll1111l1_opy_):
  bstack11ll1111ll_opy_ = bstack11l1l11lll_opy_(config)
  bstack11l1l1llll_opy_ = bstack11l1llll11_opy_(config)
  if bstack11ll1111ll_opy_ is None or bstack11l1l1llll_opy_ is None:
    logger.error(bstack1lllll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭຃"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧຄ"), bstack1lllll1_opy_ (u"ࠧࡼࡿࠪ຅")))
    data = {
        bstack1lllll1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ຆ"): config[bstack1lllll1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧງ")],
        bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ຈ"): config.get(bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧຉ"), os.path.basename(os.getcwd())),
        bstack1lllll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡘ࡮ࡳࡥࠨຊ"): bstack1l1llll1_opy_(),
        bstack1lllll1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ຋"): config.get(bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪຌ"), bstack1lllll1_opy_ (u"ࠨࠩຍ")),
        bstack1lllll1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩຎ"): {
            bstack1lllll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪຏ"): bstack11l1l1ll11_opy_,
            bstack1lllll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧຐ"): bstack11l1ll111l_opy_,
            bstack1lllll1_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩຑ"): __version__,
            bstack1lllll1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨຒ"): bstack1lllll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧຓ"),
            bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨດ"): bstack1lllll1_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫຕ"),
            bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪຖ"): bstack11ll1111l1_opy_
        },
        bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ທ"): settings,
        bstack1lllll1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡉ࡯࡯ࡶࡵࡳࡱ࠭ຘ"): bstack11l1lll111_opy_(),
        bstack1lllll1_opy_ (u"࠭ࡣࡪࡋࡱࡪࡴ࠭ນ"): bstack1111l1111_opy_(),
        bstack1lllll1_opy_ (u"ࠧࡩࡱࡶࡸࡎࡴࡦࡰࠩບ"): get_host_info(),
        bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪປ"): bstack11ll1l111_opy_(config)
    }
    headers = {
        bstack1lllll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨຜ"): bstack1lllll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ຝ"),
    }
    config = {
        bstack1lllll1_opy_ (u"ࠫࡦࡻࡴࡩࠩພ"): (bstack11ll1111ll_opy_, bstack11l1l1llll_opy_),
        bstack1lllll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ຟ"): headers
    }
    response = bstack1ll1ll1l1_opy_(bstack1lllll1_opy_ (u"࠭ࡐࡐࡕࡗࠫຠ"), bstack11l1lll11l_opy_ + bstack1lllll1_opy_ (u"ࠧ࠰ࡸ࠵࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹࠧມ"), data, config)
    bstack11l1lllll1_opy_ = response.json()
    if bstack11l1lllll1_opy_[bstack1lllll1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩຢ")]:
      parsed = json.loads(os.getenv(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪຣ"), bstack1lllll1_opy_ (u"ࠪࡿࢂ࠭຤")))
      parsed[bstack1lllll1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬລ")] = bstack11l1lllll1_opy_[bstack1lllll1_opy_ (u"ࠬࡪࡡࡵࡣࠪ຦")][bstack1lllll1_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧວ")]
      os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨຨ")] = json.dumps(parsed)
      bstack1l1l1l1ll_opy_.bstack11l1lll1l1_opy_(bstack11l1lllll1_opy_[bstack1lllll1_opy_ (u"ࠨࡦࡤࡸࡦ࠭ຩ")][bstack1lllll1_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪສ")])
      bstack1l1l1l1ll_opy_.bstack11l1l1l111_opy_(bstack11l1lllll1_opy_[bstack1lllll1_opy_ (u"ࠪࡨࡦࡺࡡࠨຫ")][bstack1lllll1_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ຬ")])
      bstack1l1l1l1ll_opy_.store()
      return bstack11l1lllll1_opy_[bstack1lllll1_opy_ (u"ࠬࡪࡡࡵࡣࠪອ")][bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫຮ")], bstack11l1lllll1_opy_[bstack1lllll1_opy_ (u"ࠧࡥࡣࡷࡥࠬຯ")][bstack1lllll1_opy_ (u"ࠨ࡫ࡧࠫະ")]
    else:
      logger.error(bstack1lllll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠪັ") + bstack11l1lllll1_opy_[bstack1lllll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫາ")])
      if bstack11l1lllll1_opy_[bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬຳ")] == bstack1lllll1_opy_ (u"ࠬࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡰࡢࡵࡶࡩࡩ࠴ࠧິ"):
        for bstack11l1llll1l_opy_ in bstack11l1lllll1_opy_[bstack1lllll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭ີ")]:
          logger.error(bstack11l1llll1l_opy_[bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨຶ")])
      return None, None
  except Exception as error:
    logger.error(bstack1lllll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠤື") +  str(error))
    return None, None
def bstack1ll1111l1l_opy_():
  if os.getenv(bstack1lllll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜ຸ࡚ࠧ")) is None:
    return {
        bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵູࠪ"): bstack1lllll1_opy_ (u"ࠫࡪࡸࡲࡰࡴ຺ࠪ"),
        bstack1lllll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ົ"): bstack1lllll1_opy_ (u"࠭ࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡩࡣࡧࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠬຼ")
    }
  data = {bstack1lllll1_opy_ (u"ࠧࡦࡰࡧࡘ࡮ࡳࡥࠨຽ"): bstack1l1llll1_opy_()}
  headers = {
      bstack1lllll1_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ຾"): bstack1lllll1_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࠪ຿") + os.getenv(bstack1lllll1_opy_ (u"ࠥࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠣເ")),
      bstack1lllll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪແ"): bstack1lllll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨໂ")
  }
  response = bstack1ll1ll1l1_opy_(bstack1lllll1_opy_ (u"࠭ࡐࡖࡖࠪໃ"), bstack11l1lll11l_opy_ + bstack1lllll1_opy_ (u"ࠧ࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶ࠳ࡸࡺ࡯ࡱࠩໄ"), data, { bstack1lllll1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ໅"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1lllll1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴࠠ࡮ࡣࡵ࡯ࡪࡪࠠࡢࡵࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠦࡡࡵࠢࠥໆ") + bstack11lllllll1_opy_().isoformat() + bstack1lllll1_opy_ (u"ࠪ࡞ࠬ໇"))
      return {bstack1lllll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶ່ࠫ"): bstack1lllll1_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ້࠭"), bstack1lllll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫໊ࠧ"): bstack1lllll1_opy_ (u"ࠧࠨ໋")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1lllll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡨࡵ࡭ࡱ࡮ࡨࡸ࡮ࡵ࡮ࠡࡱࡩࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯࠼ࠣࠦ໌") + str(error))
    return {
        bstack1lllll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩໍ"): bstack1lllll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ໎"),
        bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ໏"): str(error)
    }
def bstack1l111l1l_opy_(caps, options, desired_capabilities={}):
  try:
    bstack11l1llllll_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭໐"), {}).get(bstack1lllll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ໑"), caps.get(bstack1lllll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ໒"), bstack1lllll1_opy_ (u"ࠨࠩ໓")))
    if bstack11l1llllll_opy_:
      logger.warn(bstack1lllll1_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ໔"))
      return False
    if options:
      bstack11l1ll11l1_opy_ = options.to_capabilities()
    elif desired_capabilities:
      bstack11l1ll11l1_opy_ = desired_capabilities
    else:
      bstack11l1ll11l1_opy_ = {}
    browser = caps.get(bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ໕"), bstack1lllll1_opy_ (u"ࠫࠬ໖")).lower() or bstack11l1ll11l1_opy_.get(bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ໗"), bstack1lllll1_opy_ (u"࠭ࠧ໘")).lower()
    if browser != bstack1lllll1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ໙"):
      logger.warn(bstack1lllll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ໚"))
      return False
    browser_version = caps.get(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ໛")) or caps.get(bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬໜ")) or bstack11l1ll11l1_opy_.get(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬໝ")) or bstack11l1ll11l1_opy_.get(bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ໞ"), {}).get(bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧໟ")) or bstack11l1ll11l1_opy_.get(bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ໠"), {}).get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ໡"))
    if browser_version and browser_version != bstack1lllll1_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩ໢") and int(browser_version.split(bstack1lllll1_opy_ (u"ࠪ࠲ࠬ໣"))[0]) <= 94:
      logger.warn(bstack1lllll1_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥ࠿࠴࠯ࠤ໤"))
      return False
    if not options is None:
      bstack11l1ll1111_opy_ = bstack11l1ll11l1_opy_.get(bstack1lllll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ໥"), {})
      if bstack1lllll1_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪ໦") in bstack11l1ll1111_opy_.get(bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡷࠬ໧"), []):
        logger.warn(bstack1lllll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥ໨"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack1lllll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦ໩") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack11l1ll1lll_opy_ = config.get(bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ໪"), {})
    bstack11l1ll1lll_opy_[bstack1lllll1_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧ໫")] = os.getenv(bstack1lllll1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ໬"))
    bstack11l1l1l1l1_opy_ = json.loads(os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ໭"), bstack1lllll1_opy_ (u"ࠧࡼࡿࠪ໮"))).get(bstack1lllll1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ໯"))
    caps[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ໰")] = True
    if bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ໱") in caps:
      caps[bstack1lllll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ໲")][bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ໳")] = bstack11l1ll1lll_opy_
      caps[bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ໴")][bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ໵")][bstack1lllll1_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ໶")] = bstack11l1l1l1l1_opy_
    else:
      caps[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ໷")] = bstack11l1ll1lll_opy_
      caps[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ໸")][bstack1lllll1_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ໹")] = bstack11l1l1l1l1_opy_
  except Exception as error:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࠨ໺") +  str(error))
def bstack111lllll1_opy_(driver, bstack11l1ll1l11_opy_):
  try:
    setattr(driver, bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭໻"), True)
    session = driver.session_id
    if session:
      bstack11ll111111_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11ll111111_opy_ = False
      bstack11ll111111_opy_ = url.scheme in [bstack1lllll1_opy_ (u"ࠢࡩࡶࡷࡴࠧ໼"), bstack1lllll1_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢ໽")]
      if bstack11ll111111_opy_:
        if bstack11l1ll1l11_opy_:
          logger.info(bstack1lllll1_opy_ (u"ࠤࡖࡩࡹࡻࡰࠡࡨࡲࡶࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡨࡢࡵࠣࡷࡹࡧࡲࡵࡧࡧ࠲ࠥࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡧ࡫ࡧࡪࡰࠣࡱࡴࡳࡥ࡯ࡶࡤࡶ࡮ࡲࡹ࠯ࠤ໾"))
      return bstack11l1ll1l11_opy_
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡦࡸࡴࡪࡰࡪࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ໿") + str(e))
    return False
def bstack1ll111llll_opy_(driver, class_name, name, module_name, path, bstack11111111_opy_):
  try:
    bstack11ll1l1111_opy_ = [class_name] if not class_name is None else []
    bstack11l1l1lll1_opy_ = {
        bstack1lllll1_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤༀ"): True,
        bstack1lllll1_opy_ (u"ࠧࡺࡥࡴࡶࡇࡩࡹࡧࡩ࡭ࡵࠥ༁"): {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦ༂"): name,
            bstack1lllll1_opy_ (u"ࠢࡵࡧࡶࡸࡗࡻ࡮ࡊࡦࠥ༃"): os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡗࡉࡘ࡚࡟ࡓࡗࡑࡣࡎࡊࠧ༄")),
            bstack1lllll1_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡐࡢࡶ࡫ࠦ༅"): str(path),
            bstack1lllll1_opy_ (u"ࠥࡷࡨࡵࡰࡦࡎ࡬ࡷࡹࠨ༆"): [module_name, *bstack11ll1l1111_opy_, name],
        },
        bstack1lllll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨ༇"): _11l1ll1l1l_opy_(driver, bstack11111111_opy_)
    }
    logger.debug(bstack1lllll1_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨ༈"))
    logger.debug(driver.execute_async_script(bstack1l1l1l1ll_opy_.perform_scan, {bstack1lllll1_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨ༉"): name}))
    logger.debug(driver.execute_async_script(bstack1l1l1l1ll_opy_.bstack11l1l1l1ll_opy_, bstack11l1l1lll1_opy_))
    logger.info(bstack1lllll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥ༊"))
  except Exception as bstack11l1ll11ll_opy_:
    logger.error(bstack1lllll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥ་") + str(path) + bstack1lllll1_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦ༌") + str(bstack11l1ll11ll_opy_))