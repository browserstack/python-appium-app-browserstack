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
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack1l1111ll1l_opy_ import RobotHandler
from bstack_utils.capture import bstack11lllll11l_opy_
from bstack_utils.bstack1l1111l1ll_opy_ import bstack11llllllll_opy_, bstack1l111l11ll_opy_, bstack1l11111l11_opy_
from bstack_utils.bstack1111l111_opy_ import bstack1lllll11_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1111l1l11_opy_, bstack1l1llll1_opy_, Result, \
    bstack1l1111l111_opy_, bstack11lllllll1_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪ൳"): [],
        bstack1lllll1_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭൴"): [],
        bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬ൵"): []
    }
    bstack1l111l111l_opy_ = []
    bstack11ll1ll1ll_opy_ = []
    @staticmethod
    def bstack1l111ll111_opy_(log):
        if not (log[bstack1lllll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ൶")] and log[bstack1lllll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ൷")].strip()):
            return
        active = bstack1lllll11_opy_.bstack1l111l1ll1_opy_()
        log = {
            bstack1lllll1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ൸"): log[bstack1lllll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ൹")],
            bstack1lllll1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩൺ"): bstack11lllllll1_opy_().isoformat() + bstack1lllll1_opy_ (u"࡛ࠧࠩൻ"),
            bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩർ"): log[bstack1lllll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪൽ")],
        }
        if active:
            if active[bstack1lllll1_opy_ (u"ࠪࡸࡾࡶࡥࠨൾ")] == bstack1lllll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩൿ"):
                log[bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ඀")] = active[bstack1lllll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ඁ")]
            elif active[bstack1lllll1_opy_ (u"ࠧࡵࡻࡳࡩࠬං")] == bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ඃ"):
                log[bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ඄")] = active[bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪඅ")]
        bstack1lllll11_opy_.bstack1l1l111l1_opy_([log])
    def __init__(self):
        self.messages = Messages()
        self._11ll1ll111_opy_ = None
        self._1l111l1lll_opy_ = None
        self._11lll111ll_opy_ = OrderedDict()
        self.bstack11llll11ll_opy_ = bstack11lllll11l_opy_(self.bstack1l111ll111_opy_)
    @bstack1l1111l111_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack11llll1ll1_opy_()
        if not self._11lll111ll_opy_.get(attrs.get(bstack1lllll1_opy_ (u"ࠫ࡮ࡪࠧආ")), None):
            self._11lll111ll_opy_[attrs.get(bstack1lllll1_opy_ (u"ࠬ࡯ࡤࠨඇ"))] = {}
        bstack11ll1lll11_opy_ = bstack1l11111l11_opy_(
                bstack11ll1lll1l_opy_=attrs.get(bstack1lllll1_opy_ (u"࠭ࡩࡥࠩඈ")),
                name=name,
                bstack11llll1111_opy_=bstack1l1llll1_opy_(),
                file_path=os.path.relpath(attrs[bstack1lllll1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧඉ")], start=os.getcwd()) if attrs.get(bstack1lllll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨඊ")) != bstack1lllll1_opy_ (u"ࠩࠪඋ") else bstack1lllll1_opy_ (u"ࠪࠫඌ"),
                framework=bstack1lllll1_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪඍ")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack1lllll1_opy_ (u"ࠬ࡯ࡤࠨඎ"), None)
        self._11lll111ll_opy_[attrs.get(bstack1lllll1_opy_ (u"࠭ࡩࡥࠩඏ"))][bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪඐ")] = bstack11ll1lll11_opy_
    @bstack1l1111l111_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack11lll1llll_opy_()
        self._11lll1ll11_opy_(messages)
        for bstack1l1111l1l1_opy_ in self.bstack1l111l111l_opy_:
            bstack1l1111l1l1_opy_[bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪඑ")][bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨඒ")].extend(self.store[bstack1lllll1_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡢ࡬ࡴࡵ࡫ࡴࠩඓ")])
            bstack1lllll11_opy_.bstack11ll1llll1_opy_(bstack1l1111l1l1_opy_)
        self.bstack1l111l111l_opy_ = []
        self.store[bstack1lllll1_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪඔ")] = []
    @bstack1l1111l111_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack11llll11ll_opy_.start()
        if not self._11lll111ll_opy_.get(attrs.get(bstack1lllll1_opy_ (u"ࠬ࡯ࡤࠨඕ")), None):
            self._11lll111ll_opy_[attrs.get(bstack1lllll1_opy_ (u"࠭ࡩࡥࠩඖ"))] = {}
        driver = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭඗"), None)
        bstack1l1111l1ll_opy_ = bstack1l11111l11_opy_(
            bstack11ll1lll1l_opy_=attrs.get(bstack1lllll1_opy_ (u"ࠨ࡫ࡧࠫ඘")),
            name=name,
            bstack11llll1111_opy_=bstack1l1llll1_opy_(),
            file_path=os.path.relpath(attrs[bstack1lllll1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ඙")], start=os.getcwd()),
            scope=RobotHandler.bstack11ll1lllll_opy_(attrs.get(bstack1lllll1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪක"), None)),
            framework=bstack1lllll1_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪඛ"),
            tags=attrs[bstack1lllll1_opy_ (u"ࠬࡺࡡࡨࡵࠪග")],
            hooks=self.store[bstack1lllll1_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬඝ")],
            bstack1l11111111_opy_=bstack1lllll11_opy_.bstack1l111111l1_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack1lllll1_opy_ (u"ࠢࡼࡿࠣࡠࡳࠦࡻࡾࠤඞ").format(bstack1lllll1_opy_ (u"ࠣࠢࠥඟ").join(attrs[bstack1lllll1_opy_ (u"ࠩࡷࡥ࡬ࡹࠧච")]), name) if attrs[bstack1lllll1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨඡ")] else name
        )
        self._11lll111ll_opy_[attrs.get(bstack1lllll1_opy_ (u"ࠫ࡮ࡪࠧජ"))][bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨඣ")] = bstack1l1111l1ll_opy_
        threading.current_thread().current_test_uuid = bstack1l1111l1ll_opy_.bstack1l11111l1l_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack1lllll1_opy_ (u"࠭ࡩࡥࠩඤ"), None)
        self.bstack1l1111llll_opy_(bstack1lllll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨඥ"), bstack1l1111l1ll_opy_)
    @bstack1l1111l111_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack11llll11ll_opy_.reset()
        bstack1l111l1l1l_opy_ = bstack11lll1ll1l_opy_.get(attrs.get(bstack1lllll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨඦ")), bstack1lllll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪට"))
        self._11lll111ll_opy_[attrs.get(bstack1lllll1_opy_ (u"ࠪ࡭ࡩ࠭ඨ"))][bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧඩ")].stop(time=bstack1l1llll1_opy_(), duration=int(attrs.get(bstack1lllll1_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪඪ"), bstack1lllll1_opy_ (u"࠭࠰ࠨණ"))), result=Result(result=bstack1l111l1l1l_opy_, exception=attrs.get(bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨඬ")), bstack11lll1l111_opy_=[attrs.get(bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩත"))]))
        self.bstack1l1111llll_opy_(bstack1lllll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫථ"), self._11lll111ll_opy_[attrs.get(bstack1lllll1_opy_ (u"ࠪ࡭ࡩ࠭ද"))][bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧධ")], True)
        self.store[bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩන")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack1l1111l111_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack11llll1ll1_opy_()
        current_test_id = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡤࠨ඲"), None)
        bstack11lll111l1_opy_ = current_test_id if bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩඳ"), None) else bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡹ࡮ࡺࡥࡠ࡫ࡧࠫප"), None)
        if attrs.get(bstack1lllll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧඵ"), bstack1lllll1_opy_ (u"ࠪࠫබ")).lower() in [bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪභ"), bstack1lllll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧම")]:
            hook_type = bstack11lll11ll1_opy_(attrs.get(bstack1lllll1_opy_ (u"࠭ࡴࡺࡲࡨࠫඹ")), bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫය"), None))
            hook_name = bstack1lllll1_opy_ (u"ࠨࡽࢀࠫර").format(attrs.get(bstack1lllll1_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩ඼"), bstack1lllll1_opy_ (u"ࠪࠫල")))
            if hook_type in [bstack1lllll1_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨ඾"), bstack1lllll1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨ඿")]:
                hook_name = bstack1lllll1_opy_ (u"࡛࠭ࡼࡿࡠࠤࢀࢃࠧව").format(bstack11ll1ll1l1_opy_.get(hook_type), attrs.get(bstack1lllll1_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧශ"), bstack1lllll1_opy_ (u"ࠨࠩෂ")))
            bstack11lll11lll_opy_ = bstack1l111l11ll_opy_(
                bstack11ll1lll1l_opy_=bstack11lll111l1_opy_ + bstack1lllll1_opy_ (u"ࠩ࠰ࠫස") + attrs.get(bstack1lllll1_opy_ (u"ࠪࡸࡾࡶࡥࠨහ"), bstack1lllll1_opy_ (u"ࠫࠬළ")).lower(),
                name=hook_name,
                bstack11llll1111_opy_=bstack1l1llll1_opy_(),
                file_path=os.path.relpath(attrs.get(bstack1lllll1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬෆ")), start=os.getcwd()),
                framework=bstack1lllll1_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬ෇"),
                tags=attrs[bstack1lllll1_opy_ (u"ࠧࡵࡣࡪࡷࠬ෈")],
                scope=RobotHandler.bstack11ll1lllll_opy_(attrs.get(bstack1lllll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ෉"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack11lll11lll_opy_.bstack1l11111l1l_opy_()
            threading.current_thread().current_hook_id = bstack11lll111l1_opy_ + bstack1lllll1_opy_ (u"ࠩ࠰්ࠫ") + attrs.get(bstack1lllll1_opy_ (u"ࠪࡸࡾࡶࡥࠨ෋"), bstack1lllll1_opy_ (u"ࠫࠬ෌")).lower()
            self.store[bstack1lllll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ෍")] = [bstack11lll11lll_opy_.bstack1l11111l1l_opy_()]
            if bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ෎"), None):
                self.store[bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫා")].append(bstack11lll11lll_opy_.bstack1l11111l1l_opy_())
            else:
                self.store[bstack1lllll1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧැ")].append(bstack11lll11lll_opy_.bstack1l11111l1l_opy_())
            if bstack11lll111l1_opy_:
                self._11lll111ll_opy_[bstack11lll111l1_opy_ + bstack1lllll1_opy_ (u"ࠩ࠰ࠫෑ") + attrs.get(bstack1lllll1_opy_ (u"ࠪࡸࡾࡶࡥࠨි"), bstack1lllll1_opy_ (u"ࠫࠬී")).lower()] = { bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨු"): bstack11lll11lll_opy_ }
            bstack1lllll11_opy_.bstack1l1111llll_opy_(bstack1lllll1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ෕"), bstack11lll11lll_opy_)
        else:
            bstack11lll11l1l_opy_ = {
                bstack1lllll1_opy_ (u"ࠧࡪࡦࠪූ"): uuid4().__str__(),
                bstack1lllll1_opy_ (u"ࠨࡶࡨࡼࡹ࠭෗"): bstack1lllll1_opy_ (u"ࠩࡾࢁࠥࢁࡽࠨෘ").format(attrs.get(bstack1lllll1_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪෙ")), attrs.get(bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡴࠩේ"), bstack1lllll1_opy_ (u"ࠬ࠭ෛ"))) if attrs.get(bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡶࠫො"), []) else attrs.get(bstack1lllll1_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧෝ")),
                bstack1lllll1_opy_ (u"ࠨࡵࡷࡩࡵࡥࡡࡳࡩࡸࡱࡪࡴࡴࠨෞ"): attrs.get(bstack1lllll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧෟ"), []),
                bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ෠"): bstack1l1llll1_opy_(),
                bstack1lllll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ෡"): bstack1lllll1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭෢"),
                bstack1lllll1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ෣"): attrs.get(bstack1lllll1_opy_ (u"ࠧࡥࡱࡦࠫ෤"), bstack1lllll1_opy_ (u"ࠨࠩ෥"))
            }
            if attrs.get(bstack1lllll1_opy_ (u"ࠩ࡯࡭ࡧࡴࡡ࡮ࡧࠪ෦"), bstack1lllll1_opy_ (u"ࠪࠫ෧")) != bstack1lllll1_opy_ (u"ࠫࠬ෨"):
                bstack11lll11l1l_opy_[bstack1lllll1_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭෩")] = attrs.get(bstack1lllll1_opy_ (u"࠭࡬ࡪࡤࡱࡥࡲ࡫ࠧ෪"))
            if not self.bstack11ll1ll1ll_opy_:
                self._11lll111ll_opy_[self._11llllll11_opy_()][bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ෫")].add_step(bstack11lll11l1l_opy_)
                threading.current_thread().current_step_uuid = bstack11lll11l1l_opy_[bstack1lllll1_opy_ (u"ࠨ࡫ࡧࠫ෬")]
            self.bstack11ll1ll1ll_opy_.append(bstack11lll11l1l_opy_)
    @bstack1l1111l111_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack11lll1llll_opy_()
        self._11lll1ll11_opy_(messages)
        current_test_id = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡧࠫ෭"), None)
        bstack11lll111l1_opy_ = current_test_id if current_test_id else bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡻࡩࡵࡧࡢ࡭ࡩ࠭෮"), None)
        bstack11lll11l11_opy_ = bstack11lll1ll1l_opy_.get(attrs.get(bstack1lllll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ෯")), bstack1lllll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭෰"))
        bstack11lllll1l1_opy_ = attrs.get(bstack1lllll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ෱"))
        if bstack11lll11l11_opy_ != bstack1lllll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨෲ") and not attrs.get(bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩෳ")) and self._11ll1ll111_opy_:
            bstack11lllll1l1_opy_ = self._11ll1ll111_opy_
        bstack1l111111ll_opy_ = Result(result=bstack11lll11l11_opy_, exception=bstack11lllll1l1_opy_, bstack11lll1l111_opy_=[bstack11lllll1l1_opy_])
        if attrs.get(bstack1lllll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ෴"), bstack1lllll1_opy_ (u"ࠪࠫ෵")).lower() in [bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ෶"), bstack1lllll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ෷")]:
            bstack11lll111l1_opy_ = current_test_id if current_test_id else bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡷ࡬ࡸࡪࡥࡩࡥࠩ෸"), None)
            if bstack11lll111l1_opy_:
                bstack1l1111lll1_opy_ = bstack11lll111l1_opy_ + bstack1lllll1_opy_ (u"ࠢ࠮ࠤ෹") + attrs.get(bstack1lllll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭෺"), bstack1lllll1_opy_ (u"ࠩࠪ෻")).lower()
                self._11lll111ll_opy_[bstack1l1111lll1_opy_][bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭෼")].stop(time=bstack1l1llll1_opy_(), duration=int(attrs.get(bstack1lllll1_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩ෽"), bstack1lllll1_opy_ (u"ࠬ࠶ࠧ෾"))), result=bstack1l111111ll_opy_)
                bstack1lllll11_opy_.bstack1l1111llll_opy_(bstack1lllll1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ෿"), self._11lll111ll_opy_[bstack1l1111lll1_opy_][bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ฀")])
        else:
            bstack11lll111l1_opy_ = current_test_id if current_test_id else bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡪࡦࠪก"), None)
            if bstack11lll111l1_opy_ and len(self.bstack11ll1ll1ll_opy_) == 1:
                current_step_uuid = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭ข"), None)
                self._11lll111ll_opy_[bstack11lll111l1_opy_][bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ฃ")].bstack11lll1l1ll_opy_(current_step_uuid, duration=int(attrs.get(bstack1lllll1_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩค"), bstack1lllll1_opy_ (u"ࠬ࠶ࠧฅ"))), result=bstack1l111111ll_opy_)
            else:
                self.bstack11lll1lll1_opy_(attrs)
            self.bstack11ll1ll1ll_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack1lllll1_opy_ (u"࠭ࡨࡵ࡯࡯ࠫฆ"), bstack1lllll1_opy_ (u"ࠧ࡯ࡱࠪง")) == bstack1lllll1_opy_ (u"ࠨࡻࡨࡷࠬจ"):
                return
            self.messages.push(message)
            bstack11lll1111l_opy_ = []
            if bstack1lllll11_opy_.bstack1l111l1ll1_opy_():
                bstack11lll1111l_opy_.append({
                    bstack1lllll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬฉ"): bstack1l1llll1_opy_(),
                    bstack1lllll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫช"): message.get(bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬซ")),
                    bstack1lllll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫฌ"): message.get(bstack1lllll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬญ")),
                    **bstack1lllll11_opy_.bstack1l111l1ll1_opy_()
                })
                if len(bstack11lll1111l_opy_) > 0:
                    bstack1lllll11_opy_.bstack1l1l111l1_opy_(bstack11lll1111l_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack1lllll11_opy_.bstack11llll11l1_opy_()
    def bstack11lll1lll1_opy_(self, bstack11llll1l11_opy_):
        if not bstack1lllll11_opy_.bstack1l111l1ll1_opy_():
            return
        kwname = bstack1lllll1_opy_ (u"ࠧࡼࡿࠣࡿࢂ࠭ฎ").format(bstack11llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨฏ")), bstack11llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧฐ"), bstack1lllll1_opy_ (u"ࠪࠫฑ"))) if bstack11llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡴࠩฒ"), []) else bstack11llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬณ"))
        error_message = bstack1lllll1_opy_ (u"ࠨ࡫ࡸࡰࡤࡱࡪࡀࠠ࡝ࠤࡾ࠴ࢂࡢࠢࠡࡾࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࡡࠨࡻ࠲ࡿ࡟ࠦࠥࢂࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࡡࠨࡻ࠳ࡿ࡟ࠦࠧด").format(kwname, bstack11llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧต")), str(bstack11llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩถ"))))
        bstack1l1111l11l_opy_ = bstack1lllll1_opy_ (u"ࠤ࡮ࡻࡳࡧ࡭ࡦ࠼ࠣࡠࠧࢁ࠰ࡾ࡞ࠥࠤࢁࠦࡳࡵࡣࡷࡹࡸࡀࠠ࡝ࠤࡾ࠵ࢂࡢࠢࠣท").format(kwname, bstack11llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪธ")))
        bstack11ll1ll11l_opy_ = error_message if bstack11llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬน")) else bstack1l1111l11l_opy_
        bstack11lll11111_opy_ = {
            bstack1lllll1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨบ"): self.bstack11ll1ll1ll_opy_[-1].get(bstack1lllll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪป"), bstack1l1llll1_opy_()),
            bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨผ"): bstack11ll1ll11l_opy_,
            bstack1lllll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧฝ"): bstack1lllll1_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨพ") if bstack11llll1l11_opy_.get(bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪฟ")) == bstack1lllll1_opy_ (u"ࠫࡋࡇࡉࡍࠩภ") else bstack1lllll1_opy_ (u"ࠬࡏࡎࡇࡑࠪม"),
            **bstack1lllll11_opy_.bstack1l111l1ll1_opy_()
        }
        bstack1lllll11_opy_.bstack1l1l111l1_opy_([bstack11lll11111_opy_])
    def _11llllll11_opy_(self):
        for bstack11ll1lll1l_opy_ in reversed(self._11lll111ll_opy_):
            bstack11llll1l1l_opy_ = bstack11ll1lll1l_opy_
            data = self._11lll111ll_opy_[bstack11ll1lll1l_opy_][bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩย")]
            if isinstance(data, bstack1l111l11ll_opy_):
                if not bstack1lllll1_opy_ (u"ࠧࡆࡃࡆࡌࠬร") in data.bstack11llllll1l_opy_():
                    return bstack11llll1l1l_opy_
            else:
                return bstack11llll1l1l_opy_
    def _11lll1ll11_opy_(self, messages):
        try:
            bstack1l11111ll1_opy_ = BuiltIn().get_variable_value(bstack1lllll1_opy_ (u"ࠣࠦࡾࡐࡔࡍࠠࡍࡇ࡙ࡉࡑࢃࠢฤ")) in (bstack11lllll1ll_opy_.DEBUG, bstack11lllll1ll_opy_.TRACE)
            for message, bstack1l1111111l_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack1lllll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪล"))
                level = message.get(bstack1lllll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩฦ"))
                if level == bstack11lllll1ll_opy_.FAIL:
                    self._11ll1ll111_opy_ = name or self._11ll1ll111_opy_
                    self._1l111l1lll_opy_ = bstack1l1111111l_opy_.get(bstack1lllll1_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧว")) if bstack1l11111ll1_opy_ and bstack1l1111111l_opy_ else self._1l111l1lll_opy_
        except:
            pass
    @classmethod
    def bstack1l1111llll_opy_(self, event: str, bstack11lll1l11l_opy_: bstack11llllllll_opy_, bstack1l111l1l11_opy_=False):
        if event == bstack1lllll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧศ"):
            bstack11lll1l11l_opy_.set(hooks=self.store[bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪษ")])
        if event == bstack1lllll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨส"):
            event = bstack1lllll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪห")
        if bstack1l111l1l11_opy_:
            bstack11llll111l_opy_ = {
                bstack1lllll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ฬ"): event,
                bstack11lll1l11l_opy_.bstack11lllll111_opy_(): bstack11lll1l11l_opy_.bstack1l111l1111_opy_(event)
            }
            self.bstack1l111l111l_opy_.append(bstack11llll111l_opy_)
        else:
            bstack1lllll11_opy_.bstack1l1111llll_opy_(event, bstack11lll1l11l_opy_)
class Messages:
    def __init__(self):
        self._1l1111ll11_opy_ = []
    def bstack11llll1ll1_opy_(self):
        self._1l1111ll11_opy_.append([])
    def bstack11lll1llll_opy_(self):
        return self._1l1111ll11_opy_.pop() if self._1l1111ll11_opy_ else list()
    def push(self, message):
        self._1l1111ll11_opy_[-1].append(message) if self._1l1111ll11_opy_ else self._1l1111ll11_opy_.append([message])
class bstack11lllll1ll_opy_:
    FAIL = bstack1lllll1_opy_ (u"ࠪࡊࡆࡏࡌࠨอ")
    ERROR = bstack1lllll1_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪฮ")
    WARNING = bstack1lllll1_opy_ (u"ࠬ࡝ࡁࡓࡐࠪฯ")
    bstack1l11111lll_opy_ = bstack1lllll1_opy_ (u"࠭ࡉࡏࡈࡒࠫะ")
    DEBUG = bstack1lllll1_opy_ (u"ࠧࡅࡇࡅ࡙ࡌ࠭ั")
    TRACE = bstack1lllll1_opy_ (u"ࠨࡖࡕࡅࡈࡋࠧา")
    bstack11llll1lll_opy_ = [FAIL, ERROR]
def bstack1l111l11l1_opy_(bstack11lll1l1l1_opy_):
    if not bstack11lll1l1l1_opy_:
        return None
    if bstack11lll1l1l1_opy_.get(bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬำ"), None):
        return getattr(bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ิ")], bstack1lllll1_opy_ (u"ࠫࡺࡻࡩࡥࠩี"), None)
    return bstack11lll1l1l1_opy_.get(bstack1lllll1_opy_ (u"ࠬࡻࡵࡪࡦࠪึ"), None)
def bstack11lll11ll1_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack1lllll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬื"), bstack1lllll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ุࠩ")]:
        return
    if hook_type.lower() == bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶูࠧ"):
        if current_test_uuid is None:
            return bstack1lllll1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑฺ࠭")
        else:
            return bstack1lllll1_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨ฻")
    elif hook_type.lower() == bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭฼"):
        if current_test_uuid is None:
            return bstack1lllll1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨ฽")
        else:
            return bstack1lllll1_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ฾")