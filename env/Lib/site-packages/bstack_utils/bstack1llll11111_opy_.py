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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11l1l1l_opy_
import tempfile
import json
bstack1111l11l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠪᎪ"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1lllll1_opy_ (u"ࠩ࡟ࡲࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧᎫ"),
      datefmt=bstack1lllll1_opy_ (u"ࠪࠩࡍࡀࠥࡎ࠼ࠨࡗࠬᎬ"),
      stream=sys.stdout
    )
  return logger
def bstack1111l1l11l_opy_():
  global bstack1111l11l1l_opy_
  if os.path.exists(bstack1111l11l1l_opy_):
    os.remove(bstack1111l11l1l_opy_)
def bstack1ll11l1l1_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1l11l11111_opy_(config, log_level):
  bstack1111l1ll1l_opy_ = log_level
  if bstack1lllll1_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭Ꭽ") in config and config[bstack1lllll1_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᎮ")] in bstack11l11l1l1l_opy_:
    bstack1111l1ll1l_opy_ = bstack11l11l1l1l_opy_[config[bstack1lllll1_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᎯ")]]
  if config.get(bstack1lllll1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩᎰ"), False):
    logging.getLogger().setLevel(bstack1111l1ll1l_opy_)
    return bstack1111l1ll1l_opy_
  global bstack1111l11l1l_opy_
  bstack1ll11l1l1_opy_()
  bstack1111l1lll1_opy_ = logging.Formatter(
    fmt=bstack1lllll1_opy_ (u"ࠨ࡞ࡱࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭Ꮁ"),
    datefmt=bstack1lllll1_opy_ (u"ࠩࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫᎲ")
  )
  bstack1111l11l11_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack1111l11l1l_opy_)
  file_handler.setFormatter(bstack1111l1lll1_opy_)
  bstack1111l11l11_opy_.setFormatter(bstack1111l1lll1_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack1111l11l11_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1lllll1_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡴࡨࡱࡴࡺࡥ࠯ࡴࡨࡱࡴࡺࡥࡠࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࠬᎳ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack1111l11l11_opy_.setLevel(bstack1111l1ll1l_opy_)
  logging.getLogger().addHandler(bstack1111l11l11_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack1111l1ll1l_opy_
def bstack1111l111ll_opy_(config):
  try:
    bstack1111l11ll1_opy_ = set([
      bstack1lllll1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭Ꮄ"), bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᎵ"), bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᎶ"), bstack1lllll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᎷ"), bstack1lllll1_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠪᎸ"),
      bstack1lllll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬᎹ"), bstack1lllll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭Ꮊ"), bstack1lllll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡖࡵࡨࡶࠬᎻ"), bstack1lllll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡔࡷࡵࡸࡺࡒࡤࡷࡸ࠭Ꮌ")
    ])
    bstack1111l1l1l1_opy_ = bstack1lllll1_opy_ (u"࠭ࠧᎽ")
    with open(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪᎾ")) as bstack1111l1l111_opy_:
      bstack1111l11lll_opy_ = bstack1111l1l111_opy_.read()
      bstack1111l1l1l1_opy_ = re.sub(bstack1lllll1_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠦ࠲࠯ࠪ࡜࡯ࠩᎿ"), bstack1lllll1_opy_ (u"ࠩࠪᏀ"), bstack1111l11lll_opy_, flags=re.M)
      bstack1111l1l1l1_opy_ = re.sub(
        bstack1lllll1_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃ࠭࠭Ꮑ") + bstack1lllll1_opy_ (u"ࠫࢁ࠭Ꮒ").join(bstack1111l11ll1_opy_) + bstack1lllll1_opy_ (u"ࠬ࠯࠮ࠫࠦࠪᏃ"),
        bstack1lllll1_opy_ (u"ࡸࠧ࡝࠴࠽ࠤࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨᏄ"),
        bstack1111l1l1l1_opy_, flags=re.M | re.I
      )
    def bstack1111l111l1_opy_(dic):
      bstack1111l1ll11_opy_ = {}
      for key, value in dic.items():
        if key in bstack1111l11ll1_opy_:
          bstack1111l1ll11_opy_[key] = bstack1lllll1_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫᏅ")
        else:
          if isinstance(value, dict):
            bstack1111l1ll11_opy_[key] = bstack1111l111l1_opy_(value)
          else:
            bstack1111l1ll11_opy_[key] = value
      return bstack1111l1ll11_opy_
    bstack1111l1ll11_opy_ = bstack1111l111l1_opy_(config)
    return {
      bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫᏆ"): bstack1111l1l1l1_opy_,
      bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡳࡧ࡬ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᏇ"): json.dumps(bstack1111l1ll11_opy_)
    }
  except Exception as e:
    return {}
def bstack1l1l111l1_opy_(config):
  global bstack1111l11l1l_opy_
  try:
    if config.get(bstack1lllll1_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬᏈ"), False):
      return
    uuid = os.getenv(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᏉ"))
    if not uuid or uuid == bstack1lllll1_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᏊ"):
      return
    bstack1111l1llll_opy_ = [bstack1lllll1_opy_ (u"࠭ࡲࡦࡳࡸ࡭ࡷ࡫࡭ࡦࡰࡷࡷ࠳ࡺࡸࡵࠩᏋ"), bstack1lllll1_opy_ (u"ࠧࡑ࡫ࡳࡪ࡮ࡲࡥࠨᏌ"), bstack1lllll1_opy_ (u"ࠨࡲࡼࡴࡷࡵࡪࡦࡥࡷ࠲ࡹࡵ࡭࡭ࠩᏍ"), bstack1111l11l1l_opy_]
    bstack1ll11l1l1_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯࡯ࡳ࡬ࡹ࠭ࠨᏎ") + uuid + bstack1lllll1_opy_ (u"ࠪ࠲ࡹࡧࡲ࠯ࡩࡽࠫᏏ"))
    with tarfile.open(output_file, bstack1lllll1_opy_ (u"ࠦࡼࡀࡧࡻࠤᏐ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack1111l1llll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack1111l111ll_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack1111l1l1ll_opy_ = data.encode()
        tarinfo.size = len(bstack1111l1l1ll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack1111l1l1ll_opy_))
    bstack11l1lll1_opy_ = MultipartEncoder(
      fields= {
        bstack1lllll1_opy_ (u"ࠬࡪࡡࡵࡣࠪᏑ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1lllll1_opy_ (u"࠭ࡲࡣࠩᏒ")), bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡾ࠭ࡨࡼ࡬ࡴࠬᏓ")),
        bstack1lllll1_opy_ (u"ࠨࡥ࡯࡭ࡪࡴࡴࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᏔ"): uuid
      }
    )
    response = requests.post(
      bstack1lllll1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡹࡵࡲ࡯ࡢࡦ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡣ࡭࡫ࡨࡲࡹ࠳࡬ࡰࡩࡶ࠳ࡺࡶ࡬ࡰࡣࡧࠦᏕ"),
      data=bstack11l1lll1_opy_,
      headers={bstack1lllll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᏖ"): bstack11l1lll1_opy_.content_type},
      auth=(config[bstack1lllll1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭Ꮧ")], config[bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᏘ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1lllll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰ࡭ࡱࡤࡨࠥࡲ࡯ࡨࡵ࠽ࠤࠬᏙ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1lllll1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷ࠿࠭Ꮪ") + str(e))
  finally:
    try:
      bstack1111l1l11l_opy_()
    except:
      pass