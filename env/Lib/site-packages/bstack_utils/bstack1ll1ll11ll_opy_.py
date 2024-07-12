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
from collections import deque
from bstack_utils.constants import *
class bstack1l1l11l11_opy_:
    def __init__(self):
        self._1lllll111ll_opy_ = deque()
        self._1llll1ll1l1_opy_ = {}
        self._1lllll11ll1_opy_ = False
    def bstack1lllll1111l_opy_(self, test_name, bstack1lllll1l111_opy_):
        bstack1lllll11lll_opy_ = self._1llll1ll1l1_opy_.get(test_name, {})
        return bstack1lllll11lll_opy_.get(bstack1lllll1l111_opy_, 0)
    def bstack1lllll11l11_opy_(self, test_name, bstack1lllll1l111_opy_):
        bstack1llll1lll11_opy_ = self.bstack1lllll1111l_opy_(test_name, bstack1lllll1l111_opy_)
        self.bstack1lllll111l1_opy_(test_name, bstack1lllll1l111_opy_)
        return bstack1llll1lll11_opy_
    def bstack1lllll111l1_opy_(self, test_name, bstack1lllll1l111_opy_):
        if test_name not in self._1llll1ll1l1_opy_:
            self._1llll1ll1l1_opy_[test_name] = {}
        bstack1lllll11lll_opy_ = self._1llll1ll1l1_opy_[test_name]
        bstack1llll1lll11_opy_ = bstack1lllll11lll_opy_.get(bstack1lllll1l111_opy_, 0)
        bstack1lllll11lll_opy_[bstack1lllll1l111_opy_] = bstack1llll1lll11_opy_ + 1
    def bstack1l1ll11l1_opy_(self, bstack1llll1lllll_opy_, bstack1llll1lll1l_opy_):
        bstack1llll1ll1ll_opy_ = self.bstack1lllll11l11_opy_(bstack1llll1lllll_opy_, bstack1llll1lll1l_opy_)
        bstack1llll1llll1_opy_ = bstack11l111llll_opy_[bstack1llll1lll1l_opy_]
        bstack1lllll11111_opy_ = bstack1lllll1_opy_ (u"ࠦࢀࢃ࠭ࡼࡿ࠰ࡿࢂࠨᒆ").format(bstack1llll1lllll_opy_, bstack1llll1llll1_opy_, bstack1llll1ll1ll_opy_)
        self._1lllll111ll_opy_.append(bstack1lllll11111_opy_)
    def bstack1lllll1lll_opy_(self):
        return len(self._1lllll111ll_opy_) == 0
    def bstack1ll11l1111_opy_(self):
        bstack1lllll11l1l_opy_ = self._1lllll111ll_opy_.popleft()
        return bstack1lllll11l1l_opy_
    def capturing(self):
        return self._1lllll11ll1_opy_
    def bstack1l1l11lll1_opy_(self):
        self._1lllll11ll1_opy_ = True
    def bstack1111llll1_opy_(self):
        self._1lllll11ll1_opy_ = False