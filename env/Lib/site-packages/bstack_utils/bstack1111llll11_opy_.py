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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack111l11llll_opy_
from browserstack_sdk.bstack1ll1l111ll_opy_ import bstack1ll11lllll_opy_
def _1111ll11ll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack1111ll1111_opy_:
    def __init__(self, handler):
        self._1111lll1l1_opy_ = {}
        self._1111lll111_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1ll11lllll_opy_.version()
        if bstack111l11llll_opy_(pytest_version, bstack1lllll1_opy_ (u"ࠢ࠹࠰࠴࠲࠶ࠨ፿")) >= 0:
            self._1111lll1l1_opy_[bstack1lllll1_opy_ (u"ࠨࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᎀ")] = Module._register_setup_function_fixture
            self._1111lll1l1_opy_[bstack1lllll1_opy_ (u"ࠩࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᎁ")] = Module._register_setup_module_fixture
            self._1111lll1l1_opy_[bstack1lllll1_opy_ (u"ࠪࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᎂ")] = Class._register_setup_class_fixture
            self._1111lll1l1_opy_[bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᎃ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack1111lllll1_opy_(bstack1lllll1_opy_ (u"ࠬ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᎄ"))
            Module._register_setup_module_fixture = self.bstack1111lllll1_opy_(bstack1lllll1_opy_ (u"࠭࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᎅ"))
            Class._register_setup_class_fixture = self.bstack1111lllll1_opy_(bstack1lllll1_opy_ (u"ࠧࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᎆ"))
            Class._register_setup_method_fixture = self.bstack1111lllll1_opy_(bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᎇ"))
        else:
            self._1111lll1l1_opy_[bstack1lllll1_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᎈ")] = Module._inject_setup_function_fixture
            self._1111lll1l1_opy_[bstack1lllll1_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᎉ")] = Module._inject_setup_module_fixture
            self._1111lll1l1_opy_[bstack1lllll1_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᎊ")] = Class._inject_setup_class_fixture
            self._1111lll1l1_opy_[bstack1lllll1_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᎋ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack1111lllll1_opy_(bstack1lllll1_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᎌ"))
            Module._inject_setup_module_fixture = self.bstack1111lllll1_opy_(bstack1lllll1_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᎍ"))
            Class._inject_setup_class_fixture = self.bstack1111lllll1_opy_(bstack1lllll1_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᎎ"))
            Class._inject_setup_method_fixture = self.bstack1111lllll1_opy_(bstack1lllll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᎏ"))
    def bstack1111lll1ll_opy_(self, bstack1111ll111l_opy_, hook_type):
        meth = getattr(bstack1111ll111l_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._1111lll111_opy_[hook_type] = meth
            setattr(bstack1111ll111l_opy_, hook_type, self.bstack1111ll1ll1_opy_(hook_type))
    def bstack1111lll11l_opy_(self, instance, bstack1111llll1l_opy_):
        if bstack1111llll1l_opy_ == bstack1lllll1_opy_ (u"ࠥࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪࠨ᎐"):
            self.bstack1111lll1ll_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧ᎑"))
            self.bstack1111lll1ll_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤ᎒"))
        if bstack1111llll1l_opy_ == bstack1lllll1_opy_ (u"ࠨ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠢ᎓"):
            self.bstack1111lll1ll_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࠨ᎔"))
            self.bstack1111lll1ll_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠥ᎕"))
        if bstack1111llll1l_opy_ == bstack1lllll1_opy_ (u"ࠤࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠤ᎖"):
            self.bstack1111lll1ll_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠣ᎗"))
            self.bstack1111lll1ll_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠧ᎘"))
        if bstack1111llll1l_opy_ == bstack1lllll1_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࠨ᎙"):
            self.bstack1111lll1ll_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠧ᎚"))
            self.bstack1111lll1ll_opy_(instance.obj, bstack1lllll1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠤ᎛"))
    @staticmethod
    def bstack1111ll11l1_opy_(hook_type, func, args):
        if hook_type in [bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧ᎜"), bstack1lllll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫ᎝")]:
            _1111ll11ll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack1111ll1ll1_opy_(self, hook_type):
        def bstack1111ll1l1l_opy_(arg=None):
            self.handler(hook_type, bstack1lllll1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪ᎞"))
            result = None
            exception = None
            try:
                self.bstack1111ll11l1_opy_(hook_type, self._1111lll111_opy_[hook_type], (arg,))
                result = Result(result=bstack1lllll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ᎟"))
            except Exception as e:
                result = Result(result=bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᎠ"), exception=e)
                self.handler(hook_type, bstack1lllll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᎡ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1lllll1_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭Ꭲ"), result)
        def bstack1111ll1lll_opy_(this, arg=None):
            self.handler(hook_type, bstack1lllll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨᎣ"))
            result = None
            exception = None
            try:
                self.bstack1111ll11l1_opy_(hook_type, self._1111lll111_opy_[hook_type], (this, arg))
                result = Result(result=bstack1lllll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᎤ"))
            except Exception as e:
                result = Result(result=bstack1lllll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᎥ"), exception=e)
                self.handler(hook_type, bstack1lllll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪᎦ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1lllll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᎧ"), result)
        if hook_type in [bstack1lllll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬᎨ"), bstack1lllll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᎩ")]:
            return bstack1111ll1lll_opy_
        return bstack1111ll1l1l_opy_
    def bstack1111lllll1_opy_(self, bstack1111llll1l_opy_):
        def bstack1111ll1l11_opy_(this, *args, **kwargs):
            self.bstack1111lll11l_opy_(this, bstack1111llll1l_opy_)
            self._1111lll1l1_opy_[bstack1111llll1l_opy_](this, *args, **kwargs)
        return bstack1111ll1l11_opy_