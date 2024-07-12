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
from browserstack_sdk.bstack1ll1l111ll_opy_ import bstack1ll11lllll_opy_
from browserstack_sdk.bstack1l1111ll1l_opy_ import RobotHandler
def bstack11l1l11l1_opy_(framework):
    if framework.lower() == bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᆽ"):
        return bstack1ll11lllll_opy_.version()
    elif framework.lower() == bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬᆾ"):
        return RobotHandler.version()
    elif framework.lower() == bstack1lllll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧᆿ"):
        import behave
        return behave.__version__
    else:
        return bstack1lllll1_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩᇀ")