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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack1lll1llll_opy_ as bstack1lll1111ll_opy_
from browserstack_sdk.bstack1lll111lll_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1l1l1llll1_opy_
class bstack1ll11lllll_opy_:
    def __init__(self, args, logger, bstack11ll11l111_opy_, bstack11ll11ll1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11ll11l111_opy_ = bstack11ll11l111_opy_
        self.bstack11ll11ll1l_opy_ = bstack11ll11ll1l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1l11lllll1_opy_ = []
        self.bstack11ll11ll11_opy_ = None
        self.bstack1l11l1ll1l_opy_ = []
        self.bstack11ll1l1l1l_opy_ = self.bstack1ll111l1_opy_()
        self.bstack1l1lll1ll1_opy_ = -1
    def bstack1ll111ll_opy_(self, bstack11ll1l11l1_opy_):
        self.parse_args()
        self.bstack11ll1l1ll1_opy_()
        self.bstack11ll11lll1_opy_(bstack11ll1l11l1_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack11ll11l1ll_opy_():
        import importlib
        if getattr(importlib, bstack1lllll1_opy_ (u"ࠧࡧ࡫ࡱࡨࡤࡲ࡯ࡢࡦࡨࡶࠬ฿"), False):
            bstack11ll1l1l11_opy_ = importlib.find_loader(bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡵࡨࡰࡪࡴࡩࡶ࡯ࠪเ"))
        else:
            bstack11ll1l1l11_opy_ = importlib.util.find_spec(bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡶࡩࡱ࡫࡮ࡪࡷࡰࠫแ"))
    def bstack11ll1l111l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l1lll1ll1_opy_ = -1
        if self.bstack11ll11ll1l_opy_ and bstack1lllll1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪโ") in self.bstack11ll11l111_opy_:
            self.bstack1l1lll1ll1_opy_ = int(self.bstack11ll11l111_opy_[bstack1lllll1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫใ")])
        try:
            bstack11ll11llll_opy_ = [bstack1lllll1_opy_ (u"ࠬ࠳࠭ࡥࡴ࡬ࡺࡪࡸࠧไ"), bstack1lllll1_opy_ (u"࠭࠭࠮ࡲ࡯ࡹ࡬࡯࡮ࡴࠩๅ"), bstack1lllll1_opy_ (u"ࠧ࠮ࡲࠪๆ")]
            if self.bstack1l1lll1ll1_opy_ >= 0:
                bstack11ll11llll_opy_.extend([bstack1lllll1_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ็"), bstack1lllll1_opy_ (u"ࠩ࠰ࡲ่ࠬ")])
            for arg in bstack11ll11llll_opy_:
                self.bstack11ll1l111l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11ll1l1ll1_opy_(self):
        bstack11ll11ll11_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11ll11ll11_opy_ = bstack11ll11ll11_opy_
        return bstack11ll11ll11_opy_
    def bstack11ll1ll11_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack11ll11l1ll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1l1l1llll1_opy_)
    def bstack11ll11lll1_opy_(self, bstack11ll1l11l1_opy_):
        bstack1111ll1ll_opy_ = Config.bstack1l11llll1_opy_()
        if bstack11ll1l11l1_opy_:
            self.bstack11ll11ll11_opy_.append(bstack1lllll1_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫้ࠧ"))
            self.bstack11ll11ll11_opy_.append(bstack1lllll1_opy_ (u"࡙ࠫࡸࡵࡦ๊ࠩ"))
        if bstack1111ll1ll_opy_.bstack11ll1l1lll_opy_():
            self.bstack11ll11ll11_opy_.append(bstack1lllll1_opy_ (u"ࠬ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶ๋ࠫ"))
            self.bstack11ll11ll11_opy_.append(bstack1lllll1_opy_ (u"࠭ࡔࡳࡷࡨࠫ์"))
        self.bstack11ll11ll11_opy_.append(bstack1lllll1_opy_ (u"ࠧ࠮ࡲࠪํ"))
        self.bstack11ll11ll11_opy_.append(bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡰ࡭ࡷࡪ࡭ࡳ࠭๎"))
        self.bstack11ll11ll11_opy_.append(bstack1lllll1_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫ๏"))
        self.bstack11ll11ll11_opy_.append(bstack1lllll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪ๐"))
        if self.bstack1l1lll1ll1_opy_ > 1:
            self.bstack11ll11ll11_opy_.append(bstack1lllll1_opy_ (u"ࠫ࠲ࡴࠧ๑"))
            self.bstack11ll11ll11_opy_.append(str(self.bstack1l1lll1ll1_opy_))
    def bstack11ll1l11ll_opy_(self):
        bstack1l11l1ll1l_opy_ = []
        for spec in self.bstack1l11lllll1_opy_:
            bstack1111l1l1_opy_ = [spec]
            bstack1111l1l1_opy_ += self.bstack11ll11ll11_opy_
            bstack1l11l1ll1l_opy_.append(bstack1111l1l1_opy_)
        self.bstack1l11l1ll1l_opy_ = bstack1l11l1ll1l_opy_
        return bstack1l11l1ll1l_opy_
    def bstack1ll111l1_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11ll1l1l1l_opy_ = True
            return True
        except Exception as e:
            self.bstack11ll1l1l1l_opy_ = False
        return self.bstack11ll1l1l1l_opy_
    def bstack1ll11l111_opy_(self, bstack11ll11l1l1_opy_, bstack1ll111ll_opy_):
        bstack1ll111ll_opy_[bstack1lllll1_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ๒")] = self.bstack11ll11l111_opy_
        multiprocessing.set_start_method(bstack1lllll1_opy_ (u"࠭ࡳࡱࡣࡺࡲࠬ๓"))
        bstack1lll11111l_opy_ = []
        manager = multiprocessing.Manager()
        bstack1l111l111_opy_ = manager.list()
        if bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ๔") in self.bstack11ll11l111_opy_:
            for index, platform in enumerate(self.bstack11ll11l111_opy_[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ๕")]):
                bstack1lll11111l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11ll11l1l1_opy_,
                                                            args=(self.bstack11ll11ll11_opy_, bstack1ll111ll_opy_, bstack1l111l111_opy_)))
            bstack11ll11l11l_opy_ = len(self.bstack11ll11l111_opy_[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ๖")])
        else:
            bstack1lll11111l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11ll11l1l1_opy_,
                                                        args=(self.bstack11ll11ll11_opy_, bstack1ll111ll_opy_, bstack1l111l111_opy_)))
            bstack11ll11l11l_opy_ = 1
        i = 0
        for t in bstack1lll11111l_opy_:
            os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ๗")] = str(i)
            if bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ๘") in self.bstack11ll11l111_opy_:
                os.environ[bstack1lllll1_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭๙")] = json.dumps(self.bstack11ll11l111_opy_[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ๚")][i % bstack11ll11l11l_opy_])
            i += 1
            t.start()
        for t in bstack1lll11111l_opy_:
            t.join()
        return list(bstack1l111l111_opy_)
    @staticmethod
    def bstack1lll1lll1_opy_(driver, bstack11111111_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ๛"), None)
        if item and getattr(item, bstack1lllll1_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤࡩࡡࡴࡧࠪ๜"), None) and not getattr(item, bstack1lllll1_opy_ (u"ࠩࡢࡥ࠶࠷ࡹࡠࡵࡷࡳࡵࡥࡤࡰࡰࡨࠫ๝"), False):
            logger.info(
                bstack1lllll1_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠤ๞"))
            bstack11ll1l1111_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lll1111ll_opy_.bstack1ll111llll_opy_(driver, bstack11ll1l1111_opy_, item.name, item.module.__name__, item.path, bstack11111111_opy_)
            item._a11y_stop_done = True
            if wait:
                sleep(2)