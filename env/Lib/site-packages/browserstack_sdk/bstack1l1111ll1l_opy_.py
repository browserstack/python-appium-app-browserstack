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
class RobotHandler():
    def __init__(self, args, logger, bstack11ll11l111_opy_, bstack11ll11ll1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11ll11l111_opy_ = bstack11ll11l111_opy_
        self.bstack11ll11ll1l_opy_ = bstack11ll11ll1l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack11ll1lllll_opy_(bstack11ll111l11_opy_):
        bstack11ll111ll1_opy_ = []
        if bstack11ll111l11_opy_:
            tokens = str(os.path.basename(bstack11ll111l11_opy_)).split(bstack1lllll1_opy_ (u"ࠦࡤࠨ๟"))
            camelcase_name = bstack1lllll1_opy_ (u"ࠧࠦࠢ๠").join(t.title() for t in tokens)
            suite_name, bstack11ll111l1l_opy_ = os.path.splitext(camelcase_name)
            bstack11ll111ll1_opy_.append(suite_name)
        return bstack11ll111ll1_opy_
    @staticmethod
    def bstack11ll111lll_opy_(typename):
        if bstack1lllll1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤ๡") in typename:
            return bstack1lllll1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣ๢")
        return bstack1lllll1_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤ๣")