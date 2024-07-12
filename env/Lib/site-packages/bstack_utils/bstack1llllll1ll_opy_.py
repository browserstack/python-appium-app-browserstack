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
class bstack1ll1l111l1_opy_:
    def __init__(self, handler):
        self._1lll1ll1l1l_opy_ = None
        self.handler = handler
        self._1lll1lll111_opy_ = self.bstack1lll1ll1lll_opy_()
        self.patch()
    def patch(self):
        self._1lll1ll1l1l_opy_ = self._1lll1lll111_opy_.execute
        self._1lll1lll111_opy_.execute = self.bstack1lll1ll1ll1_opy_()
    def bstack1lll1ll1ll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1lllll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤᓟ"), driver_command, None, this, args)
            response = self._1lll1ll1l1l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1lllll1_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤᓠ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1lll1lll111_opy_.execute = self._1lll1ll1l1l_opy_
    @staticmethod
    def bstack1lll1ll1lll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver