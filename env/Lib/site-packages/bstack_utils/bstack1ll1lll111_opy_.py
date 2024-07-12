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
import re
from bstack_utils.bstack1lll1l1l1l_opy_ import bstack1llll11ll1l_opy_
def bstack1llll11l1ll_opy_(fixture_name):
    if fixture_name.startswith(bstack1lllll1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᒬ")):
        return bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᒭ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᒮ")):
        return bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᒯ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᒰ")):
        return bstack1lllll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᒱ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᒲ")):
        return bstack1lllll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᒳ")
def bstack1llll11l111_opy_(fixture_name):
    return bool(re.match(bstack1lllll1_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᒴ"), fixture_name))
def bstack1llll1l1111_opy_(fixture_name):
    return bool(re.match(bstack1lllll1_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᒵ"), fixture_name))
def bstack1llll1l11l1_opy_(fixture_name):
    return bool(re.match(bstack1lllll1_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᒶ"), fixture_name))
def bstack1llll11llll_opy_(fixture_name):
    if fixture_name.startswith(bstack1lllll1_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᒷ")):
        return bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᒸ"), bstack1lllll1_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᒹ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᒺ")):
        return bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧᒻ"), bstack1lllll1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᒼ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᒽ")):
        return bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᒾ"), bstack1lllll1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᒿ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᓀ")):
        return bstack1lllll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᓁ"), bstack1lllll1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᓂ")
    return None, None
def bstack1llll111ll1_opy_(hook_name):
    if hook_name in [bstack1lllll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᓃ"), bstack1lllll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᓄ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1llll11l1l1_opy_(hook_name):
    if hook_name in [bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᓅ"), bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫᓆ")]:
        return bstack1lllll1_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᓇ")
    elif hook_name in [bstack1lllll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᓈ"), bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᓉ")]:
        return bstack1lllll1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᓊ")
    elif hook_name in [bstack1lllll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᓋ"), bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᓌ")]:
        return bstack1lllll1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᓍ")
    elif hook_name in [bstack1lllll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᓎ"), bstack1lllll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᓏ")]:
        return bstack1lllll1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᓐ")
    return hook_name
def bstack1llll11lll1_opy_(node, scenario):
    if hasattr(node, bstack1lllll1_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫᓑ")):
        parts = node.nodeid.rsplit(bstack1lllll1_opy_ (u"ࠥ࡟ࠧᓒ"))
        params = parts[-1]
        return bstack1lllll1_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦᓓ").format(scenario.name, params)
    return scenario.name
def bstack1llll11l11l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1lllll1_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᓔ")):
            examples = list(node.callspec.params[bstack1lllll1_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬᓕ")].values())
        return examples
    except:
        return []
def bstack1llll1l111l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1llll111l1l_opy_(report):
    try:
        status = bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᓖ")
        if report.passed or (report.failed and hasattr(report, bstack1lllll1_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥᓗ"))):
            status = bstack1lllll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᓘ")
        elif report.skipped:
            status = bstack1lllll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᓙ")
        bstack1llll11ll1l_opy_(status)
    except:
        pass
def bstack1l1l111ll1_opy_(status):
    try:
        bstack1llll111lll_opy_ = bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᓚ")
        if status == bstack1lllll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᓛ"):
            bstack1llll111lll_opy_ = bstack1lllll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᓜ")
        elif status == bstack1lllll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᓝ"):
            bstack1llll111lll_opy_ = bstack1lllll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᓞ")
        bstack1llll11ll1l_opy_(bstack1llll111lll_opy_)
    except:
        pass
def bstack1llll11ll11_opy_(item=None, report=None, summary=None, extra=None):
    return