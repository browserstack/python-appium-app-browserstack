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
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll111l11_opy_ = {}
        bstack1l111ll11l_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪൌ"), bstack1lllll1_opy_ (u"്ࠪࠫ"))
        if not bstack1l111ll11l_opy_:
            return bstack1lll111l11_opy_
        try:
            bstack1l111ll1l1_opy_ = json.loads(bstack1l111ll11l_opy_)
            if bstack1lllll1_opy_ (u"ࠦࡴࡹࠢൎ") in bstack1l111ll1l1_opy_:
                bstack1lll111l11_opy_[bstack1lllll1_opy_ (u"ࠧࡵࡳࠣ൏")] = bstack1l111ll1l1_opy_[bstack1lllll1_opy_ (u"ࠨ࡯ࡴࠤ൐")]
            if bstack1lllll1_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦ൑") in bstack1l111ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ൒") in bstack1l111ll1l1_opy_:
                bstack1lll111l11_opy_[bstack1lllll1_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧ൓")] = bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢൔ"), bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢൕ")))
            if bstack1lllll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨൖ") in bstack1l111ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦൗ") in bstack1l111ll1l1_opy_:
                bstack1lll111l11_opy_[bstack1lllll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧ൘")] = bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤ൙"), bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ൚")))
            if bstack1lllll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ൛") in bstack1l111ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧ൜") in bstack1l111ll1l1_opy_:
                bstack1lll111l11_opy_[bstack1lllll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨ൝")] = bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ൞"), bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣൟ")))
            if bstack1lllll1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣൠ") in bstack1l111ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨൡ") in bstack1l111ll1l1_opy_:
                bstack1lll111l11_opy_[bstack1lllll1_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢൢ")] = bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦൣ"), bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤ൤")))
            if bstack1lllll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣ൥") in bstack1l111ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ൦") in bstack1l111ll1l1_opy_:
                bstack1lll111l11_opy_[bstack1lllll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ൧")] = bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦ൨"), bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ൩")))
            if bstack1lllll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ൪") in bstack1l111ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ൫") in bstack1l111ll1l1_opy_:
                bstack1lll111l11_opy_[bstack1lllll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ൬")] = bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥ൭"), bstack1l111ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ൮")))
            if bstack1lllll1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ൯") in bstack1l111ll1l1_opy_:
                bstack1lll111l11_opy_[bstack1lllll1_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧ൰")] = bstack1l111ll1l1_opy_[bstack1lllll1_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨ൱")]
        except Exception as error:
            logger.error(bstack1lllll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩࡧࡴࡢ࠼ࠣࠦ൲") +  str(error))
        return bstack1lll111l11_opy_