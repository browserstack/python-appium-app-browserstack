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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack11l1lll111_opy_, bstack1111l1111_opy_, get_host_info, bstack11l1l11lll_opy_, bstack11l1llll11_opy_, bstack111llll11l_opy_, bstack11lllllll1_opy_, \
    bstack11l1111lll_opy_, bstack111l1l111l_opy_, bstack1ll1ll1l1_opy_, bstack111ll11111_opy_, bstack1l11ll1l1_opy_, bstack1l1111l111_opy_, bstack1l1ll1lll_opy_, bstack1l1llll1_opy_
from bstack_utils.bstack1llll111l11_opy_ import bstack1llll11111l_opy_
from bstack_utils.bstack1l1111l1ll_opy_ import bstack11llllllll_opy_
import bstack_utils.bstack1lll1llll_opy_ as bstack1lll1111ll_opy_
from bstack_utils.constants import bstack11l11l1111_opy_
bstack1lll11l111l_opy_ = [
    bstack1lllll1_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪᕓ"), bstack1lllll1_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᕔ"), bstack1lllll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᕕ"), bstack1lllll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪᕖ"),
    bstack1lllll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᕗ"), bstack1lllll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᕘ"), bstack1lllll1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᕙ")
]
bstack1lll11ll111_opy_ = bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡤࡱ࡯ࡰࡪࡩࡴࡰࡴ࠰ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ᕚ")
logger = logging.getLogger(__name__)
class bstack1lllll11_opy_:
    bstack1llll111l11_opy_ = None
    bs_config = None
    @classmethod
    @bstack1l1111l111_opy_(class_method=True)
    def launch(cls, bs_config, bstack1lll11l1l1l_opy_):
        cls.bs_config = bs_config
        cls.bstack1lll11l1ll1_opy_()
        bstack11ll1111ll_opy_ = bstack11l1l11lll_opy_(bs_config)
        bstack11l1l1llll_opy_ = bstack11l1llll11_opy_(bs_config)
        bstack111111l1l_opy_ = False
        bstack1lll1111l_opy_ = False
        if bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࠫᕛ") in bs_config:
            bstack111111l1l_opy_ = True
        else:
            bstack1lll1111l_opy_ = True
        bstack1l1l11l1_opy_ = {
            bstack1lllll1_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨᕜ"): cls.bstack111ll111_opy_(bstack1lll11l1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪᕝ"), bstack1lllll1_opy_ (u"ࠪࠫᕞ"))),
            bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᕟ"): bstack1lll1111ll_opy_.bstack11l1l1ll_opy_(bs_config),
            bstack1lllll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᕠ"): bs_config.get(bstack1lllll1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᕡ"), False),
            bstack1lllll1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩᕢ"): bstack1lll1111l_opy_,
            bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᕣ"): bstack111111l1l_opy_
        }
        data = {
            bstack1lllll1_opy_ (u"ࠩࡩࡳࡷࡳࡡࡵࠩᕤ"): bstack1lllll1_opy_ (u"ࠪ࡮ࡸࡵ࡮ࠨᕥ"),
            bstack1lllll1_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡤࡴࡡ࡮ࡧࠪᕦ"): bs_config.get(bstack1lllll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᕧ"), bstack1lllll1_opy_ (u"࠭ࠧᕨ")),
            bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᕩ"): bs_config.get(bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᕪ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᕫ"): bs_config.get(bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᕬ")),
            bstack1lllll1_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩᕭ"): bs_config.get(bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨᕮ"), bstack1lllll1_opy_ (u"࠭ࠧᕯ")),
            bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡶࡹࡥࡴࡪ࡯ࡨࠫᕰ"): datetime.datetime.now().isoformat(),
            bstack1lllll1_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᕱ"): bstack111llll11l_opy_(bs_config),
            bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡸࡺ࡟ࡪࡰࡩࡳࠬᕲ"): get_host_info(),
            bstack1lllll1_opy_ (u"ࠪࡧ࡮ࡥࡩ࡯ࡨࡲࠫᕳ"): bstack1111l1111_opy_(),
            bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡶࡺࡴ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᕴ"): os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫᕵ")),
            bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࡸࡥࡳࡷࡱࠫᕶ"): os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠬᕷ"), False),
            bstack1lllll1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡡࡦࡳࡳࡺࡲࡰ࡮ࠪᕸ"): bstack11l1lll111_opy_(),
            bstack1lllll1_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧᕹ"): bstack1l1l11l1_opy_,
            bstack1lllll1_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡢࡺࡪࡸࡳࡪࡱࡱࠫᕺ"): {
                bstack1lllll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫᕻ"): bstack1lll11l1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭ᕼ"), bstack1lllll1_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭ᕽ")),
                bstack1lllll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪᕾ"): bstack1lll11l1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᕿ")),
                bstack1lllll1_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᖀ"): bstack1lll11l1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᖁ"))
            }
        }
        config = {
            bstack1lllll1_opy_ (u"ࠫࡦࡻࡴࡩࠩᖂ"): (bstack11ll1111ll_opy_, bstack11l1l1llll_opy_),
            bstack1lllll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᖃ"): cls.default_headers()
        }
        response = bstack1ll1ll1l1_opy_(bstack1lllll1_opy_ (u"࠭ࡐࡐࡕࡗࠫᖄ"), cls.request_url(bstack1lllll1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹࠧᖅ")), data, config)
        if response.status_code != 200:
            os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᖆ")] = bstack1lllll1_opy_ (u"ࠩࡱࡹࡱࡲࠧᖇ")
            os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡃࡐࡏࡓࡐࡊ࡚ࡅࡅࠩᖈ")] = bstack1lllll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪᖉ")
            os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ᖊ")] = bstack1lllll1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᖋ")
            os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ᖌ")] = bstack1lllll1_opy_ (u"ࠣࡰࡸࡰࡱࠨᖍ")
            os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪᖎ")] = bstack1lllll1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᖏ")
            bstack1lll11l1111_opy_ = response.json()
            if bstack1lll11l1111_opy_ and bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᖐ")]:
                error_message = bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᖑ")]
                if bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"࠭ࡥࡳࡴࡲࡶ࡙ࡿࡰࡦࠩᖒ")] == bstack1lllll1_opy_ (u"ࠧࡆࡔࡕࡓࡗࡥࡉࡏࡘࡄࡐࡎࡊ࡟ࡄࡔࡈࡈࡊࡔࡔࡊࡃࡏࡗࠬᖓ"):
                    logger.error(error_message)
                elif bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࡔࡺࡲࡨࠫᖔ")] == bstack1lllll1_opy_ (u"ࠩࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠨᖕ"):
                    logger.info(error_message)
                elif bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡖࡼࡴࡪ࠭ᖖ")] == bstack1lllll1_opy_ (u"ࠫࡊࡘࡒࡐࡔࡢࡗࡉࡑ࡟ࡅࡇࡓࡖࡊࡉࡁࡕࡇࡇࠫᖗ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1lllll1_opy_ (u"ࠧࡊࡡࡵࡣࠣࡹࡵࡲ࡯ࡢࡦࠣࡸࡴࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡚ࠥࡥࡴࡶࠣࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠣࡪࡦ࡯࡬ࡦࡦࠣࡨࡺ࡫ࠠࡵࡱࠣࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢᖘ"))
            return [None, None, None]
        bstack1lll11l1111_opy_ = response.json()
        os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᖙ")] = bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩᖚ")]
        if cls.bstack111ll111_opy_(bstack1lll11l1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩᖛ"), bstack1lllll1_opy_ (u"ࠩࠪᖜ"))) is True:
            logger.debug(bstack1lllll1_opy_ (u"ࠪࡘࡪࡹࡴࠡࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠡࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࠧࠧᖝ"))
            os.environ[bstack1lllll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪᖞ")] = bstack1lllll1_opy_ (u"ࠬࡺࡲࡶࡧࠪᖟ")
            if bstack1lll11l1111_opy_.get(bstack1lllll1_opy_ (u"࠭ࡪࡸࡶࠪᖠ")):
                os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨᖡ")] = bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠨ࡬ࡺࡸࠬᖢ")]
                os.environ[bstack1lllll1_opy_ (u"ࠩࡆࡖࡊࡊࡅࡏࡖࡌࡅࡑ࡙࡟ࡇࡑࡕࡣࡈࡘࡁࡔࡊࡢࡖࡊࡖࡏࡓࡖࡌࡒࡌ࠭ᖣ")] = json.dumps({
                    bstack1lllll1_opy_ (u"ࠪࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬᖤ"): bstack11ll1111ll_opy_,
                    bstack1lllll1_opy_ (u"ࠫࡵࡧࡳࡴࡹࡲࡶࡩ࠭ᖥ"): bstack11l1l1llll_opy_
                })
            if bstack1lll11l1111_opy_.get(bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᖦ")):
                os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᖧ")] = bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩᖨ")]
            if bstack1lll11l1111_opy_.get(bstack1lllll1_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬᖩ")):
                os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪᖪ")] = str(bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᖫ")])
        return [bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠫ࡯ࡽࡴࠨᖬ")], bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧᖭ")], bstack1lll11l1111_opy_[bstack1lllll1_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᖮ")]]
    @classmethod
    @bstack1l1111l111_opy_(class_method=True)
    def stop(cls, bstack1lll111l1l1_opy_ = None):
        if not cls.on():
            return
        if os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨᖯ")] == bstack1lllll1_opy_ (u"ࠣࡰࡸࡰࡱࠨᖰ") or os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨᖱ")] == bstack1lllll1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᖲ"):
            print(bstack1lllll1_opy_ (u"ࠫࡊ࡞ࡃࡆࡒࡗࡍࡔࡔࠠࡊࡐࠣࡷࡹࡵࡰࡃࡷ࡬ࡰࡩ࡛ࡰࡴࡶࡵࡩࡦࡳࠠࡓࡇࡔ࡙ࡊ࡙ࡔࠡࡖࡒࠤ࡙ࡋࡓࡕࠢࡒࡆࡘࡋࡒࡗࡃࡅࡍࡑࡏࡔ࡚ࠢ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬᖳ"))
            return {
                bstack1lllll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᖴ"): bstack1lllll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᖵ"),
                bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᖶ"): bstack1lllll1_opy_ (u"ࠨࡖࡲ࡯ࡪࡴ࠯ࡣࡷ࡬ࡰࡩࡏࡄࠡ࡫ࡶࠤࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠬࠡࡤࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡰ࡭࡬࡮ࡴࠡࡪࡤࡺࡪࠦࡦࡢ࡫࡯ࡩࡩ࠭ᖷ")
            }
        else:
            cls.bstack1llll111l11_opy_.shutdown()
            data = {
                bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᖸ"): bstack1l1llll1_opy_()
            }
            if not bstack1lll111l1l1_opy_ is None:
                data[bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡳࡥࡵࡣࡧࡥࡹࡧࠧᖹ")] = [{
                    bstack1lllll1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᖺ"): bstack1lllll1_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪᖻ"),
                    bstack1lllll1_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭ᖼ"): bstack1lll111l1l1_opy_
                }]
            config = {
                bstack1lllll1_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᖽ"): cls.default_headers()
            }
            bstack11l111l111_opy_ = bstack1lllll1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸࡺ࡯ࡱࠩᖾ").format(os.environ[bstack1lllll1_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠣᖿ")])
            bstack1lll111ll11_opy_ = cls.request_url(bstack11l111l111_opy_)
            response = bstack1ll1ll1l1_opy_(bstack1lllll1_opy_ (u"ࠪࡔ࡚࡚ࠧᗀ"), bstack1lll111ll11_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1lllll1_opy_ (u"ࠦࡘࡺ࡯ࡱࠢࡵࡩࡶࡻࡥࡴࡶࠣࡲࡴࡺࠠࡰ࡭ࠥᗁ"))
    @classmethod
    def bstack11llll11l1_opy_(cls):
        if cls.bstack1llll111l11_opy_ is None:
            return
        cls.bstack1llll111l11_opy_.shutdown()
    @classmethod
    def bstack1l1l11l1l1_opy_(cls):
        if cls.on():
            print(
                bstack1lllll1_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠨᗂ").format(os.environ[bstack1lllll1_opy_ (u"ࠨࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠧᗃ")]))
    @classmethod
    def bstack1lll11l1ll1_opy_(cls):
        if cls.bstack1llll111l11_opy_ is not None:
            return
        cls.bstack1llll111l11_opy_ = bstack1llll11111l_opy_(cls.bstack1lll111ll1l_opy_)
        cls.bstack1llll111l11_opy_.start()
    @classmethod
    def bstack11ll1llll1_opy_(cls, bstack11lll1l11l_opy_, bstack1lll11ll1l1_opy_=bstack1lllll1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭ᗄ")):
        if not cls.on():
            return
        bstack11111ll11_opy_ = bstack11lll1l11l_opy_[bstack1lllll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᗅ")]
        bstack1lll111l1ll_opy_ = {
            bstack1lllll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᗆ"): bstack1lllll1_opy_ (u"ࠪࡘࡪࡹࡴࡠࡕࡷࡥࡷࡺ࡟ࡖࡲ࡯ࡳࡦࡪࠧᗇ"),
            bstack1lllll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᗈ"): bstack1lllll1_opy_ (u"࡚ࠬࡥࡴࡶࡢࡉࡳࡪ࡟ࡖࡲ࡯ࡳࡦࡪࠧᗉ"),
            bstack1lllll1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᗊ"): bstack1lllll1_opy_ (u"ࠧࡕࡧࡶࡸࡤ࡙࡫ࡪࡲࡳࡩࡩࡥࡕࡱ࡮ࡲࡥࡩ࠭ᗋ"),
            bstack1lllll1_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᗌ"): bstack1lllll1_opy_ (u"ࠩࡏࡳ࡬ࡥࡕࡱ࡮ࡲࡥࡩ࠭ᗍ"),
            bstack1lllll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᗎ"): bstack1lllll1_opy_ (u"ࠫࡍࡵ࡯࡬ࡡࡖࡸࡦࡸࡴࡠࡗࡳࡰࡴࡧࡤࠨᗏ"),
            bstack1lllll1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᗐ"): bstack1lllll1_opy_ (u"࠭ࡈࡰࡱ࡮ࡣࡊࡴࡤࡠࡗࡳࡰࡴࡧࡤࠨᗑ"),
            bstack1lllll1_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᗒ"): bstack1lllll1_opy_ (u"ࠨࡅࡅࡘࡤ࡛ࡰ࡭ࡱࡤࡨࠬᗓ")
        }.get(bstack11111ll11_opy_)
        if bstack1lll11ll1l1_opy_ == bstack1lllll1_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨᗔ"):
            cls.bstack1lll11l1ll1_opy_()
            cls.bstack1llll111l11_opy_.add(bstack11lll1l11l_opy_)
        elif bstack1lll11ll1l1_opy_ == bstack1lllll1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᗕ"):
            cls.bstack1lll111ll1l_opy_([bstack11lll1l11l_opy_], bstack1lll11ll1l1_opy_)
    @classmethod
    @bstack1l1111l111_opy_(class_method=True)
    def bstack1lll111ll1l_opy_(cls, bstack11lll1l11l_opy_, bstack1lll11ll1l1_opy_=bstack1lllll1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᗖ")):
        config = {
            bstack1lllll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᗗ"): cls.default_headers()
        }
        response = bstack1ll1ll1l1_opy_(bstack1lllll1_opy_ (u"࠭ࡐࡐࡕࡗࠫᗘ"), cls.request_url(bstack1lll11ll1l1_opy_), bstack11lll1l11l_opy_, config)
        bstack11l1lllll1_opy_ = response.json()
    @classmethod
    @bstack1l1111l111_opy_(class_method=True)
    def bstack1l1l111l1_opy_(cls, bstack11lll1111l_opy_):
        bstack1lll111l11l_opy_ = []
        for log in bstack11lll1111l_opy_:
            bstack1lll11lll11_opy_ = {
                bstack1lllll1_opy_ (u"ࠧ࡬࡫ࡱࡨࠬᗙ"): bstack1lllll1_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡌࡐࡉࠪᗚ"),
                bstack1lllll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᗛ"): log[bstack1lllll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᗜ")],
                bstack1lllll1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᗝ"): log[bstack1lllll1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᗞ")],
                bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡣࡷ࡫ࡳࡱࡱࡱࡷࡪ࠭ᗟ"): {},
                bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᗠ"): log[bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᗡ")],
            }
            if bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᗢ") in log:
                bstack1lll11lll11_opy_[bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᗣ")] = log[bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᗤ")]
            elif bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᗥ") in log:
                bstack1lll11lll11_opy_[bstack1lllll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᗦ")] = log[bstack1lllll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᗧ")]
            bstack1lll111l11l_opy_.append(bstack1lll11lll11_opy_)
        cls.bstack11ll1llll1_opy_({
            bstack1lllll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᗨ"): bstack1lllll1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᗩ"),
            bstack1lllll1_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᗪ"): bstack1lll111l11l_opy_
        })
    @classmethod
    @bstack1l1111l111_opy_(class_method=True)
    def bstack1lll11l1l11_opy_(cls, steps):
        bstack1lll11l11ll_opy_ = []
        for step in steps:
            bstack1lll111lll1_opy_ = {
                bstack1lllll1_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᗫ"): bstack1lllll1_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗ࡙ࡋࡐࠨᗬ"),
                bstack1lllll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᗭ"): step[bstack1lllll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᗮ")],
                bstack1lllll1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᗯ"): step[bstack1lllll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᗰ")],
                bstack1lllll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᗱ"): step[bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᗲ")],
                bstack1lllll1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᗳ"): step[bstack1lllll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨᗴ")]
            }
            if bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᗵ") in step:
                bstack1lll111lll1_opy_[bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᗶ")] = step[bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᗷ")]
            elif bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᗸ") in step:
                bstack1lll111lll1_opy_[bstack1lllll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᗹ")] = step[bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᗺ")]
            bstack1lll11l11ll_opy_.append(bstack1lll111lll1_opy_)
        cls.bstack11ll1llll1_opy_({
            bstack1lllll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᗻ"): bstack1lllll1_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᗼ"),
            bstack1lllll1_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭ᗽ"): bstack1lll11l11ll_opy_
        })
    @classmethod
    @bstack1l1111l111_opy_(class_method=True)
    def bstack1l11ll1l1l_opy_(cls, screenshot):
        cls.bstack11ll1llll1_opy_({
            bstack1lllll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᗾ"): bstack1lllll1_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧᗿ"),
            bstack1lllll1_opy_ (u"ࠫࡱࡵࡧࡴࠩᘀ"): [{
                bstack1lllll1_opy_ (u"ࠬࡱࡩ࡯ࡦࠪᘁ"): bstack1lllll1_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠨᘂ"),
                bstack1lllll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᘃ"): bstack11lllllll1_opy_().isoformat() + bstack1lllll1_opy_ (u"ࠨ࡜ࠪᘄ"),
                bstack1lllll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᘅ"): screenshot[bstack1lllll1_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩᘆ")],
                bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᘇ"): screenshot[bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᘈ")]
            }]
        }, bstack1lll11ll1l1_opy_=bstack1lllll1_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᘉ"))
    @classmethod
    @bstack1l1111l111_opy_(class_method=True)
    def bstack1l111lll_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11ll1llll1_opy_({
            bstack1lllll1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᘊ"): bstack1lllll1_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬᘋ"),
            bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫᘌ"): {
                bstack1lllll1_opy_ (u"ࠥࡹࡺ࡯ࡤࠣᘍ"): cls.current_test_uuid(),
                bstack1lllll1_opy_ (u"ࠦ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠥᘎ"): cls.bstack1l111111l1_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ᘏ"), None) is None or os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᘐ")] == bstack1lllll1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᘑ"):
            return False
        return True
    @classmethod
    def bstack111ll111_opy_(cls, framework=bstack1lllll1_opy_ (u"ࠣࠤᘒ")):
        if framework not in bstack11l11l1111_opy_:
            return False
        bstack1lll111llll_opy_ = not bstack1l1ll1lll_opy_()
        return bstack1l11ll1l1_opy_(cls.bs_config.get(bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ᘓ"), bstack1lll111llll_opy_))
    @staticmethod
    def request_url(url):
        return bstack1lllll1_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩᘔ").format(bstack1lll11ll111_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack1lllll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᘕ"): bstack1lllll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᘖ"),
            bstack1lllll1_opy_ (u"࠭ࡘ࠮ࡄࡖࡘࡆࡉࡋ࠮ࡖࡈࡗ࡙ࡕࡐࡔࠩᘗ"): bstack1lllll1_opy_ (u"ࠧࡵࡴࡸࡩࠬᘘ")
        }
        if os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩᘙ"), None):
            headers[bstack1lllll1_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᘚ")] = bstack1lllll1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᘛ").format(os.environ[bstack1lllll1_opy_ (u"ࠦࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠧᘜ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᘝ"), None)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᘞ"), None)
    @staticmethod
    def bstack1l111l1ll1_opy_():
        if getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᘟ"), None):
            return {
                bstack1lllll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᘠ"): bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺࠧᘡ"),
                bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᘢ"): getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᘣ"), None)
            }
        if getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᘤ"), None):
            return {
                bstack1lllll1_opy_ (u"࠭ࡴࡺࡲࡨࠫᘥ"): bstack1lllll1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᘦ"),
                bstack1lllll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᘧ"): getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᘨ"), None)
            }
        return None
    @staticmethod
    def bstack1l111111l1_opy_(driver):
        return {
            bstack111l1l111l_opy_(): bstack11l1111lll_opy_(driver)
        }
    @staticmethod
    def bstack1lll11l1lll_opy_(exception_info, report):
        return [{bstack1lllll1_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᘩ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11ll111lll_opy_(typename):
        if bstack1lllll1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᘪ") in typename:
            return bstack1lllll1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᘫ")
        return bstack1lllll1_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᘬ")
    @staticmethod
    def bstack1lll11ll1ll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1lllll11_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11ll1lllll_opy_(test, hook_name=None):
        bstack1lll11ll11l_opy_ = test.parent
        if hook_name in [bstack1lllll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᘭ"), bstack1lllll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩᘮ"), bstack1lllll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨᘯ"), bstack1lllll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬᘰ")]:
            bstack1lll11ll11l_opy_ = test
        scope = []
        while bstack1lll11ll11l_opy_ is not None:
            scope.append(bstack1lll11ll11l_opy_.name)
            bstack1lll11ll11l_opy_ = bstack1lll11ll11l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1lll11l11l1_opy_(hook_type):
        if hook_type == bstack1lllll1_opy_ (u"ࠦࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠤᘱ"):
            return bstack1lllll1_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡭ࡵ࡯࡬ࠤᘲ")
        elif hook_type == bstack1lllll1_opy_ (u"ࠨࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠥᘳ"):
            return bstack1lllll1_opy_ (u"ࠢࡕࡧࡤࡶࡩࡵࡷ࡯ࠢ࡫ࡳࡴࡱࠢᘴ")
    @staticmethod
    def bstack1lll11lll1l_opy_(bstack1l11lllll1_opy_):
        try:
            if not bstack1lllll11_opy_.on():
                return bstack1l11lllll1_opy_
            if os.environ.get(bstack1lllll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࠨᘵ"), None) == bstack1lllll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᘶ"):
                tests = os.environ.get(bstack1lllll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠢᘷ"), None)
                if tests is None or tests == bstack1lllll1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᘸ"):
                    return bstack1l11lllll1_opy_
                bstack1l11lllll1_opy_ = tests.split(bstack1lllll1_opy_ (u"ࠬ࠲ࠧᘹ"))
                return bstack1l11lllll1_opy_
        except Exception as exc:
            print(bstack1lllll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡸࡥࡳࡷࡱࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶ࠿ࠦࠢᘺ"), str(exc))
        return bstack1l11lllll1_opy_
    @classmethod
    def bstack1l1111llll_opy_(cls, event: str, bstack11lll1l11l_opy_: bstack11llllllll_opy_):
        bstack11llll111l_opy_ = {
            bstack1lllll1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᘻ"): event,
            bstack11lll1l11l_opy_.bstack11lllll111_opy_(): bstack11lll1l11l_opy_.bstack1l111l1111_opy_(event)
        }
        bstack1lllll11_opy_.bstack11ll1llll1_opy_(bstack11llll111l_opy_)