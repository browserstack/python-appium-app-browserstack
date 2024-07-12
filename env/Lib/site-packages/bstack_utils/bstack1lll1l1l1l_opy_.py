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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack111l1l1ll1_opy_, bstack1llll1l1_opy_, bstack1111l1l11_opy_, bstack1l1l1ll1_opy_, \
    bstack111l1lll1l_opy_
def bstack11l11l1l_opy_(bstack1lll1ll111l_opy_):
    for driver in bstack1lll1ll111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1l1ll11l_opy_(driver, status, reason=bstack1lllll1_opy_ (u"ࠫࠬᓡ")):
    bstack1111ll1ll_opy_ = Config.bstack1l11llll1_opy_()
    if bstack1111ll1ll_opy_.bstack11ll1l1lll_opy_():
        return
    bstack1ll1l1111_opy_ = bstack1l1l1111_opy_(bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᓢ"), bstack1lllll1_opy_ (u"࠭ࠧᓣ"), status, reason, bstack1lllll1_opy_ (u"ࠧࠨᓤ"), bstack1lllll1_opy_ (u"ࠨࠩᓥ"))
    driver.execute_script(bstack1ll1l1111_opy_)
def bstack11lll1lll_opy_(page, status, reason=bstack1lllll1_opy_ (u"ࠩࠪᓦ")):
    try:
        if page is None:
            return
        bstack1111ll1ll_opy_ = Config.bstack1l11llll1_opy_()
        if bstack1111ll1ll_opy_.bstack11ll1l1lll_opy_():
            return
        bstack1ll1l1111_opy_ = bstack1l1l1111_opy_(bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᓧ"), bstack1lllll1_opy_ (u"ࠫࠬᓨ"), status, reason, bstack1lllll1_opy_ (u"ࠬ࠭ᓩ"), bstack1lllll1_opy_ (u"࠭ࠧᓪ"))
        page.evaluate(bstack1lllll1_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᓫ"), bstack1ll1l1111_opy_)
    except Exception as e:
        print(bstack1lllll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨᓬ"), e)
def bstack1l1l1111_opy_(type, name, status, reason, bstack11l11111l_opy_, bstack111ll111l_opy_):
    bstack1lllll11l_opy_ = {
        bstack1lllll1_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩᓭ"): type,
        bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᓮ"): {}
    }
    if type == bstack1lllll1_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ᓯ"):
        bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᓰ")][bstack1lllll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᓱ")] = bstack11l11111l_opy_
        bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᓲ")][bstack1lllll1_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᓳ")] = json.dumps(str(bstack111ll111l_opy_))
    if type == bstack1lllll1_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᓴ"):
        bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᓵ")][bstack1lllll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᓶ")] = name
    if type == bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᓷ"):
        bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᓸ")][bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᓹ")] = status
        if status == bstack1lllll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᓺ") and str(reason) != bstack1lllll1_opy_ (u"ࠤࠥᓻ"):
            bstack1lllll11l_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᓼ")][bstack1lllll1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᓽ")] = json.dumps(str(reason))
    bstack1ll1ll11l1_opy_ = bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᓾ").format(json.dumps(bstack1lllll11l_opy_))
    return bstack1ll1ll11l1_opy_
def bstack1l11l111ll_opy_(url, config, logger, bstack1ll111l1l1_opy_=False):
    hostname = bstack1llll1l1_opy_(url)
    is_private = bstack1l1l1ll1_opy_(hostname)
    try:
        if is_private or bstack1ll111l1l1_opy_:
            file_path = bstack111l1l1ll1_opy_(bstack1lllll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᓿ"), bstack1lllll1_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᔀ"), logger)
            if os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᔁ")) and eval(
                    os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧᔂ"))):
                return
            if (bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᔃ") in config and not config[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨᔄ")]):
                os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪᔅ")] = str(True)
                bstack1lll1ll11l1_opy_ = {bstack1lllll1_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨᔆ"): hostname}
                bstack111l1lll1l_opy_(bstack1lllll1_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᔇ"), bstack1lllll1_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ᔈ"), bstack1lll1ll11l1_opy_, logger)
    except Exception as e:
        pass
def bstack11ll1ll1_opy_(caps, bstack1lll1ll1l11_opy_):
    if bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᔉ") in caps:
        caps[bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᔊ")][bstack1lllll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪᔋ")] = True
        if bstack1lll1ll1l11_opy_:
            caps[bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᔌ")][bstack1lllll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᔍ")] = bstack1lll1ll1l11_opy_
    else:
        caps[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᔎ")] = True
        if bstack1lll1ll1l11_opy_:
            caps[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᔏ")] = bstack1lll1ll1l11_opy_
def bstack1llll11ll1l_opy_(bstack1l111l1l1l_opy_):
    bstack1lll1ll11ll_opy_ = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᔐ"), bstack1lllll1_opy_ (u"ࠪࠫᔑ"))
    if bstack1lll1ll11ll_opy_ == bstack1lllll1_opy_ (u"ࠫࠬᔒ") or bstack1lll1ll11ll_opy_ == bstack1lllll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᔓ"):
        threading.current_thread().testStatus = bstack1l111l1l1l_opy_
    else:
        if bstack1l111l1l1l_opy_ == bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᔔ"):
            threading.current_thread().testStatus = bstack1l111l1l1l_opy_