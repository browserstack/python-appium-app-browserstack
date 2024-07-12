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
class bstack11lllll11l_opy_:
    def __init__(self, handler):
        self._11l11lll1l_opy_ = sys.stdout.write
        self._11l11lllll_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack11l11llll1_opy_
        sys.stdout.error = self.bstack11l1l11111_opy_
    def bstack11l11llll1_opy_(self, _str):
        self._11l11lll1l_opy_(_str)
        if self.handler:
            self.handler({bstack1lllll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ༢"): bstack1lllll1_opy_ (u"ࠫࡎࡔࡆࡐࠩ༣"), bstack1lllll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭༤"): _str})
    def bstack11l1l11111_opy_(self, _str):
        self._11l11lllll_opy_(_str)
        if self.handler:
            self.handler({bstack1lllll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ༥"): bstack1lllll1_opy_ (u"ࠧࡆࡔࡕࡓࡗ࠭༦"), bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ༧"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._11l11lll1l_opy_
        sys.stderr.write = self._11l11lllll_opy_