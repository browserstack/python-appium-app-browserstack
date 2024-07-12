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
import atexit
import datetime
import inspect
import logging
import os
import signal
import sys
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1ll1l1l1ll_opy_, bstack111l11l1_opy_, update, bstack1lll111111_opy_,
                                       bstack11lll1l1l_opy_, bstack1ll1l11ll_opy_, bstack11ll1l1l1_opy_, bstack1ll1ll11_opy_,
                                       bstack1l11ll1ll_opy_, bstack1l11l1l1l_opy_, bstack1l1111ll_opy_, bstack11l1l111l_opy_,
                                       bstack1l1l1l11_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack11ll1lll_opy_)
from browserstack_sdk.bstack1ll1l111ll_opy_ import bstack1ll11lllll_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1llll11111_opy_
from bstack_utils.capture import bstack11lllll11l_opy_
from bstack_utils.config import Config
from bstack_utils.constants import bstack1l1l11ll1l_opy_, bstack1l1l1l1l11_opy_, bstack1l11llll11_opy_, \
    bstack1l1l11l11l_opy_
from bstack_utils.helper import bstack1111l1l11_opy_, bstack111ll111ll_opy_, bstack11lllllll1_opy_, bstack111l11l11_opy_, bstack111l1l1l1l_opy_, bstack1l1llll1_opy_, \
    bstack111llll1l1_opy_, \
    bstack111ll1l1l1_opy_, bstack1ll11lll11_opy_, bstack1lllll1ll_opy_, bstack111l1l1lll_opy_, bstack11lll1ll1_opy_, Notset, \
    bstack1ll1l1lll1_opy_, bstack11l111111l_opy_, bstack11l1111ll1_opy_, Result, bstack111ll1ll11_opy_, bstack111ll1l11l_opy_, bstack1l1111l111_opy_, \
    bstack1lll11l11l_opy_, bstack1l1ll1ll1l_opy_, bstack1l11ll1l1_opy_, bstack11l11111ll_opy_
from bstack_utils.bstack1111llll11_opy_ import bstack1111ll1111_opy_
from bstack_utils.messages import bstack1l11ll1l_opy_, bstack11ll111l1_opy_, bstack1l1lll1l11_opy_, bstack1111l1l1l_opy_, bstack1l1l1llll1_opy_, \
    bstack1l11lll1l_opy_, bstack1l1111lll_opy_, bstack1ll111ll1_opy_, bstack111llll11_opy_, bstack1111llll_opy_, \
    bstack1lllll11l1_opy_, bstack1ll1ll1ll_opy_
from bstack_utils.proxy import bstack1ll11lll1_opy_, bstack1llllllll_opy_
from bstack_utils.bstack1ll1lll111_opy_ import bstack1llll11ll11_opy_, bstack1llll111ll1_opy_, bstack1llll11l1l1_opy_, bstack1llll1l1111_opy_, \
    bstack1llll1l11l1_opy_, bstack1llll11lll1_opy_, bstack1llll1l111l_opy_, bstack1l1l111ll1_opy_, bstack1llll111l1l_opy_
from bstack_utils.bstack1llllll1ll_opy_ import bstack1ll1l111l1_opy_
from bstack_utils.bstack1lll1l1l1l_opy_ import bstack1l1l1111_opy_, bstack1l11l111ll_opy_, bstack11ll1ll1_opy_, \
    bstack1l1l1ll11l_opy_, bstack11lll1lll_opy_
from bstack_utils.bstack1l1111l1ll_opy_ import bstack1l11111l11_opy_
from bstack_utils.bstack1111l111_opy_ import bstack1lllll11_opy_
import bstack_utils.bstack1lll1llll_opy_ as bstack1lll1111ll_opy_
from bstack_utils.bstack1l1l1l1ll_opy_ import bstack1l1l1l1ll_opy_
bstack1l111ll1ll_opy_ = None
bstack11l1llll_opy_ = None
bstack11l111111_opy_ = None
bstack11111l11l_opy_ = None
bstack1llll11l1l_opy_ = None
bstack11llll1ll_opy_ = None
bstack1l1l11111_opy_ = None
bstack1l111111_opy_ = None
bstack1ll1lll1l1_opy_ = None
bstack11l1ll11l_opy_ = None
bstack1l11lll11l_opy_ = None
bstack1ll1l1llll_opy_ = None
bstack1ll111111_opy_ = None
bstack1ll11l1l1l_opy_ = bstack1lllll1_opy_ (u"ࠨࠩᘼ")
CONFIG = {}
bstack1l1l1lllll_opy_ = False
bstack1l11l1ll11_opy_ = bstack1lllll1_opy_ (u"ࠩࠪᘽ")
bstack1l11ll11ll_opy_ = bstack1lllll1_opy_ (u"ࠪࠫᘾ")
bstack1ll1ll1l1l_opy_ = False
bstack1l11l1l11_opy_ = []
bstack1ll111111l_opy_ = bstack1l1l11ll1l_opy_
bstack1ll1lll111l_opy_ = bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᘿ")
bstack1ll1lllll11_opy_ = False
bstack1ll111l1ll_opy_ = {}
bstack11l11l1l1_opy_ = False
logger = bstack1llll11111_opy_.get_logger(__name__, bstack1ll111111l_opy_)
store = {
    bstack1lllll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᙀ"): []
}
bstack1ll1ll1ll11_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_11lll111ll_opy_ = {}
current_test_uuid = None
def bstack1l11l11l11_opy_(page, bstack1l1llllll_opy_):
    try:
        page.evaluate(bstack1lllll1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᙁ"),
                      bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫᙂ") + json.dumps(
                          bstack1l1llllll_opy_) + bstack1lllll1_opy_ (u"ࠣࡿࢀࠦᙃ"))
    except Exception as e:
        print(bstack1lllll1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃࠢᙄ"), e)
def bstack1111ll11_opy_(page, message, level):
    try:
        page.evaluate(bstack1lllll1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᙅ"), bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩᙆ") + json.dumps(
            message) + bstack1lllll1_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨᙇ") + json.dumps(level) + bstack1lllll1_opy_ (u"࠭ࡽࡾࠩᙈ"))
    except Exception as e:
        print(bstack1lllll1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿࠥᙉ"), e)
def pytest_configure(config):
    bstack1111ll1ll_opy_ = Config.bstack1l11llll1_opy_()
    config.args = bstack1lllll11_opy_.bstack1lll11lll1l_opy_(config.args)
    bstack1111ll1ll_opy_.bstack1l11l11l1l_opy_(bstack1l11ll1l1_opy_(config.getoption(bstack1lllll1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᙊ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1ll1lll1111_opy_ = item.config.getoption(bstack1lllll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᙋ"))
    plugins = item.config.getoption(bstack1lllll1_opy_ (u"ࠥࡴࡱࡻࡧࡪࡰࡶࠦᙌ"))
    report = outcome.get_result()
    bstack1ll1llll1ll_opy_(item, call, report)
    if bstack1lllll1_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡳࡰࡺ࡭ࡩ࡯ࠤᙍ") not in plugins or bstack11lll1ll1_opy_():
        return
    summary = []
    driver = getattr(item, bstack1lllll1_opy_ (u"ࠧࡥࡤࡳ࡫ࡹࡩࡷࠨᙎ"), None)
    page = getattr(item, bstack1lllll1_opy_ (u"ࠨ࡟ࡱࡣࡪࡩࠧᙏ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1ll1ll1llll_opy_(item, report, summary, bstack1ll1lll1111_opy_)
    if (page is not None):
        bstack1ll1llll1l1_opy_(item, report, summary, bstack1ll1lll1111_opy_)
def bstack1ll1ll1llll_opy_(item, report, summary, bstack1ll1lll1111_opy_):
    if report.when == bstack1lllll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᙐ") and report.skipped:
        bstack1llll111l1l_opy_(report)
    if report.when in [bstack1lllll1_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢᙑ"), bstack1lllll1_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦᙒ")]:
        return
    if not bstack111l1l1l1l_opy_():
        return
    try:
        if (str(bstack1ll1lll1111_opy_).lower() != bstack1lllll1_opy_ (u"ࠪࡸࡷࡻࡥࠨᙓ")):
            item._driver.execute_script(
                bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩᙔ") + json.dumps(
                    report.nodeid) + bstack1lllll1_opy_ (u"ࠬࢃࡽࠨᙕ"))
        os.environ[bstack1lllll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩᙖ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack1lllll1_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦ࠼ࠣࡿ࠵ࢃࠢᙗ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1lllll1_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥᙘ")))
    bstack11ll11ll1_opy_ = bstack1lllll1_opy_ (u"ࠤࠥᙙ")
    bstack1llll111l1l_opy_(report)
    if not passed:
        try:
            bstack11ll11ll1_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack1lllll1_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥᙚ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack11ll11ll1_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack1lllll1_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᙛ")))
        bstack11ll11ll1_opy_ = bstack1lllll1_opy_ (u"ࠧࠨᙜ")
        if not passed:
            try:
                bstack11ll11ll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1lllll1_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨᙝ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack11ll11ll1_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫᙞ")
                    + json.dumps(bstack1lllll1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠢࠤᙟ"))
                    + bstack1lllll1_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧᙠ")
                )
            else:
                item._driver.execute_script(
                    bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨᙡ")
                    + json.dumps(str(bstack11ll11ll1_opy_))
                    + bstack1lllll1_opy_ (u"ࠦࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢᙢ")
                )
        except Exception as e:
            summary.append(bstack1lllll1_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡥࡳࡴ࡯ࡵࡣࡷࡩ࠿ࠦࡻ࠱ࡿࠥᙣ").format(e))
def bstack1lll1111111_opy_(test_name, error_message):
    try:
        bstack1ll1ll1l111_opy_ = []
        bstack1l1llll11_opy_ = os.environ.get(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᙤ"), bstack1lllll1_opy_ (u"ࠧ࠱ࠩᙥ"))
        bstack1l1l1ll111_opy_ = {bstack1lllll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᙦ"): test_name, bstack1lllll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᙧ"): error_message, bstack1lllll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩᙨ"): bstack1l1llll11_opy_}
        bstack1lll1111ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩᙩ"))
        if os.path.exists(bstack1lll1111ll1_opy_):
            with open(bstack1lll1111ll1_opy_) as f:
                bstack1ll1ll1l111_opy_ = json.load(f)
        bstack1ll1ll1l111_opy_.append(bstack1l1l1ll111_opy_)
        with open(bstack1lll1111ll1_opy_, bstack1lllll1_opy_ (u"ࠬࡽࠧᙪ")) as f:
            json.dump(bstack1ll1ll1l111_opy_, f)
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡨࡶࡸ࡯ࡳࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡳࡽࡹ࡫ࡳࡵࠢࡨࡶࡷࡵࡲࡴ࠼ࠣࠫᙫ") + str(e))
def bstack1ll1llll1l1_opy_(item, report, summary, bstack1ll1lll1111_opy_):
    if report.when in [bstack1lllll1_opy_ (u"ࠢࡴࡧࡷࡹࡵࠨᙬ"), bstack1lllll1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࠥ᙭")]:
        return
    if (str(bstack1ll1lll1111_opy_).lower() != bstack1lllll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ᙮")):
        bstack1l11l11l11_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1lllll1_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᙯ")))
    bstack11ll11ll1_opy_ = bstack1lllll1_opy_ (u"ࠦࠧᙰ")
    bstack1llll111l1l_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack11ll11ll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1lllll1_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡪࡺࡥࡳ࡯࡬ࡲࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡳࡧࡤࡷࡴࡴ࠺ࠡࡽ࠳ࢁࠧᙱ").format(e)
                )
        try:
            if passed:
                bstack11lll1lll_opy_(getattr(item, bstack1lllll1_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬᙲ"), None), bstack1lllll1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢᙳ"))
            else:
                error_message = bstack1lllll1_opy_ (u"ࠨࠩᙴ")
                if bstack11ll11ll1_opy_:
                    bstack1111ll11_opy_(item._page, str(bstack11ll11ll1_opy_), bstack1lllll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣᙵ"))
                    bstack11lll1lll_opy_(getattr(item, bstack1lllll1_opy_ (u"ࠪࡣࡵࡧࡧࡦࠩᙶ"), None), bstack1lllll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦᙷ"), str(bstack11ll11ll1_opy_))
                    error_message = str(bstack11ll11ll1_opy_)
                else:
                    bstack11lll1lll_opy_(getattr(item, bstack1lllll1_opy_ (u"ࠬࡥࡰࡢࡩࡨࠫᙸ"), None), bstack1lllll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᙹ"))
                bstack1lll1111111_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack1lllll1_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡻࡰࡥࡣࡷࡩࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼ࠲ࢀࠦᙺ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack1lllll1_opy_ (u"ࠣ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧᙻ"), default=bstack1lllll1_opy_ (u"ࠤࡉࡥࡱࡹࡥࠣᙼ"), help=bstack1lllll1_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡨࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠤᙽ"))
    parser.addoption(bstack1lllll1_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᙾ"), default=bstack1lllll1_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦᙿ"), help=bstack1lllll1_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧ "))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack1lllll1_opy_ (u"ࠢ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠤᚁ"), action=bstack1lllll1_opy_ (u"ࠣࡵࡷࡳࡷ࡫ࠢᚂ"), default=bstack1lllll1_opy_ (u"ࠤࡦ࡬ࡷࡵ࡭ࡦࠤᚃ"),
                         help=bstack1lllll1_opy_ (u"ࠥࡈࡷ࡯ࡶࡦࡴࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴࠤᚄ"))
def bstack1l111ll111_opy_(log):
    if not (log[bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᚅ")] and log[bstack1lllll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᚆ")].strip()):
        return
    active = bstack1l111l1ll1_opy_()
    log = {
        bstack1lllll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᚇ"): log[bstack1lllll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᚈ")],
        bstack1lllll1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᚉ"): bstack11lllllll1_opy_().isoformat() + bstack1lllll1_opy_ (u"ࠩ࡝ࠫᚊ"),
        bstack1lllll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᚋ"): log[bstack1lllll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᚌ")],
    }
    if active:
        if active[bstack1lllll1_opy_ (u"ࠬࡺࡹࡱࡧࠪᚍ")] == bstack1lllll1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᚎ"):
            log[bstack1lllll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᚏ")] = active[bstack1lllll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᚐ")]
        elif active[bstack1lllll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᚑ")] == bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࠨᚒ"):
            log[bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᚓ")] = active[bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᚔ")]
    bstack1lllll11_opy_.bstack1l1l111l1_opy_([log])
def bstack1l111l1ll1_opy_():
    if len(store[bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᚕ")]) > 0 and store[bstack1lllll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᚖ")][-1]:
        return {
            bstack1lllll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᚗ"): bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᚘ"),
            bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᚙ"): store[bstack1lllll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᚚ")][-1]
        }
    if store.get(bstack1lllll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ᚛"), None):
        return {
            bstack1lllll1_opy_ (u"࠭ࡴࡺࡲࡨࠫ᚜"): bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࠬ᚝"),
            bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᚞"): store[bstack1lllll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭᚟")]
        }
    return None
bstack11llll11ll_opy_ = bstack11lllll11l_opy_(bstack1l111ll111_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack1ll1lllll11_opy_
        item._1lll111111l_opy_ = True
        bstack11111l111_opy_ = bstack1lll1111ll_opy_.bstack1llllllll1_opy_(CONFIG, bstack111ll1l1l1_opy_(item.own_markers))
        item._a11y_test_case = bstack11111l111_opy_
        if bstack1ll1lllll11_opy_:
            driver = getattr(item, bstack1lllll1_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫᚠ"), None)
            item._a11y_started = bstack1lll1111ll_opy_.bstack111lllll1_opy_(driver, bstack11111l111_opy_)
        if not bstack1lllll11_opy_.on() or bstack1ll1lll111l_opy_ != bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᚡ"):
            return
        global current_test_uuid, bstack11llll11ll_opy_
        bstack11llll11ll_opy_.start()
        bstack11lll1l1l1_opy_ = {
            bstack1lllll1_opy_ (u"ࠬࡻࡵࡪࡦࠪᚢ"): uuid4().__str__(),
            bstack1lllll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᚣ"): bstack11lllllll1_opy_().isoformat() + bstack1lllll1_opy_ (u"࡛ࠧࠩᚤ")
        }
        current_test_uuid = bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᚥ")]
        store[bstack1lllll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᚦ")] = bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᚧ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _11lll111ll_opy_[item.nodeid] = {**_11lll111ll_opy_[item.nodeid], **bstack11lll1l1l1_opy_}
        bstack1ll1ll11ll1_opy_(item, _11lll111ll_opy_[item.nodeid], bstack1lllll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᚨ"))
    except Exception as err:
        print(bstack1lllll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡩࡡ࡭࡮࠽ࠤࢀࢃࠧᚩ"), str(err))
def pytest_runtest_setup(item):
    global bstack1ll1ll1ll11_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111l1l1lll_opy_():
        atexit.register(bstack11l11l1l_opy_)
        if not bstack1ll1ll1ll11_opy_:
            try:
                bstack1ll1lll11l1_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack11l11111ll_opy_():
                    bstack1ll1lll11l1_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1ll1lll11l1_opy_:
                    signal.signal(s, bstack1ll1ll11lll_opy_)
                bstack1ll1ll1ll11_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack1lllll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨ࡫࡮ࡹࡴࡦࡴࠣࡷ࡮࡭࡮ࡢ࡮ࠣ࡬ࡦࡴࡤ࡭ࡧࡵࡷ࠿ࠦࠢᚪ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1llll11ll11_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack1lllll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᚫ")
    try:
        if not bstack1lllll11_opy_.on():
            return
        bstack11llll11ll_opy_.start()
        uuid = uuid4().__str__()
        bstack11lll1l1l1_opy_ = {
            bstack1lllll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᚬ"): uuid,
            bstack1lllll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᚭ"): bstack11lllllll1_opy_().isoformat() + bstack1lllll1_opy_ (u"ࠪ࡞ࠬᚮ"),
            bstack1lllll1_opy_ (u"ࠫࡹࡿࡰࡦࠩᚯ"): bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᚰ"),
            bstack1lllll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᚱ"): bstack1lllll1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬᚲ"),
            bstack1lllll1_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫᚳ"): bstack1lllll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᚴ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack1lllll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧᚵ")] = item
        store[bstack1lllll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᚶ")] = [uuid]
        if not _11lll111ll_opy_.get(item.nodeid, None):
            _11lll111ll_opy_[item.nodeid] = {bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᚷ"): [], bstack1lllll1_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᚸ"): []}
        _11lll111ll_opy_[item.nodeid][bstack1lllll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᚹ")].append(bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᚺ")])
        _11lll111ll_opy_[item.nodeid + bstack1lllll1_opy_ (u"ࠩ࠰ࡷࡪࡺࡵࡱࠩᚻ")] = bstack11lll1l1l1_opy_
        bstack1ll1ll1l1ll_opy_(item, bstack11lll1l1l1_opy_, bstack1lllll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᚼ"))
    except Exception as err:
        print(bstack1lllll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡸ࡫ࡴࡶࡲ࠽ࠤࢀࢃࠧᚽ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack1ll111l1ll_opy_
        if CONFIG.get(bstack1lllll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᚾ"), False):
            if CONFIG.get(bstack1lllll1_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩᚿ"), bstack1lllll1_opy_ (u"ࠢࡢࡷࡷࡳࠧᛀ")) == bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᛁ"):
                bstack1lll111l111_opy_ = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᛂ"), None)
                bstack111l11lll_opy_ = bstack1lll111l111_opy_ + bstack1lllll1_opy_ (u"ࠥ࠱ࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᛃ")
                driver = getattr(item, bstack1lllll1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᛄ"), None)
                PercySDK.screenshot(driver, bstack111l11lll_opy_)
        if getattr(item, bstack1lllll1_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡸࡺࡡࡳࡶࡨࡨࠬᛅ"), False):
            bstack1ll11lllll_opy_.bstack1lll1lll1_opy_(getattr(item, bstack1lllll1_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᛆ"), None), bstack1ll111l1ll_opy_, logger, item)
        if not bstack1lllll11_opy_.on():
            return
        bstack11lll1l1l1_opy_ = {
            bstack1lllll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᛇ"): uuid4().__str__(),
            bstack1lllll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᛈ"): bstack11lllllll1_opy_().isoformat() + bstack1lllll1_opy_ (u"ࠩ࡝ࠫᛉ"),
            bstack1lllll1_opy_ (u"ࠪࡸࡾࡶࡥࠨᛊ"): bstack1lllll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᛋ"),
            bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᛌ"): bstack1lllll1_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪᛍ"),
            bstack1lllll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪᛎ"): bstack1lllll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪᛏ")
        }
        _11lll111ll_opy_[item.nodeid + bstack1lllll1_opy_ (u"ࠩ࠰ࡸࡪࡧࡲࡥࡱࡺࡲࠬᛐ")] = bstack11lll1l1l1_opy_
        bstack1ll1ll1l1ll_opy_(item, bstack11lll1l1l1_opy_, bstack1lllll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᛑ"))
    except Exception as err:
        print(bstack1lllll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡀࠠࡼࡿࠪᛒ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1lllll11_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1llll1l1111_opy_(fixturedef.argname):
        store[bstack1lllll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥ࡭ࡰࡦࡸࡰࡪࡥࡩࡵࡧࡰࠫᛓ")] = request.node
    elif bstack1llll1l11l1_opy_(fixturedef.argname):
        store[bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡤ࡮ࡤࡷࡸࡥࡩࡵࡧࡰࠫᛔ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᛕ"): fixturedef.argname,
            bstack1lllll1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᛖ"): bstack111llll1l1_opy_(outcome),
            bstack1lllll1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫᛗ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack1lllll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧᛘ")]
        if not _11lll111ll_opy_.get(current_test_item.nodeid, None):
            _11lll111ll_opy_[current_test_item.nodeid] = {bstack1lllll1_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᛙ"): []}
        _11lll111ll_opy_[current_test_item.nodeid][bstack1lllll1_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᛚ")].append(fixture)
    except Exception as err:
        logger.debug(bstack1lllll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡳࡦࡶࡸࡴ࠿ࠦࡻࡾࠩᛛ"), str(err))
if bstack11lll1ll1_opy_() and bstack1lllll11_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _11lll111ll_opy_[request.node.nodeid][bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᛜ")].bstack1lll11llll1_opy_(id(step))
        except Exception as err:
            print(bstack1lllll1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱ࠼ࠣࡿࢂ࠭ᛝ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _11lll111ll_opy_[request.node.nodeid][bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᛞ")].bstack11lll1l1ll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack1lllll1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡳࡵࡧࡳࡣࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠧᛟ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack1l1111l1ll_opy_: bstack1l11111l11_opy_ = _11lll111ll_opy_[request.node.nodeid][bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᛠ")]
            bstack1l1111l1ll_opy_.bstack11lll1l1ll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack1lllll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡵࡷࡩࡵࡥࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠩᛡ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1ll1lll111l_opy_
        try:
            if not bstack1lllll11_opy_.on() or bstack1ll1lll111l_opy_ != bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪᛢ"):
                return
            global bstack11llll11ll_opy_
            bstack11llll11ll_opy_.start()
            driver = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ᛣ"), None)
            if not _11lll111ll_opy_.get(request.node.nodeid, None):
                _11lll111ll_opy_[request.node.nodeid] = {}
            bstack1l1111l1ll_opy_ = bstack1l11111l11_opy_.bstack1lll1l1l1l1_opy_(
                scenario, feature, request.node,
                name=bstack1llll11lll1_opy_(request.node, scenario),
                bstack11llll1111_opy_=bstack1l1llll1_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack1lllll1_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴ࠮ࡥࡸࡧࡺࡳࡢࡦࡴࠪᛤ"),
                tags=bstack1llll1l111l_opy_(feature, scenario),
                bstack1l11111111_opy_=bstack1lllll11_opy_.bstack1l111111l1_opy_(driver) if driver and driver.session_id else {}
            )
            _11lll111ll_opy_[request.node.nodeid][bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᛥ")] = bstack1l1111l1ll_opy_
            bstack1ll1lll1lll_opy_(bstack1l1111l1ll_opy_.uuid)
            bstack1lllll11_opy_.bstack1l1111llll_opy_(bstack1lllll1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᛦ"), bstack1l1111l1ll_opy_)
        except Exception as err:
            print(bstack1lllll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰ࠼ࠣࡿࢂ࠭ᛧ"), str(err))
def bstack1ll1ll1l11l_opy_(bstack1ll1ll1l1l1_opy_):
    if bstack1ll1ll1l1l1_opy_ in store[bstack1lllll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᛨ")]:
        store[bstack1lllll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᛩ")].remove(bstack1ll1ll1l1l1_opy_)
def bstack1ll1lll1lll_opy_(bstack1lll1111l11_opy_):
    store[bstack1lllll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᛪ")] = bstack1lll1111l11_opy_
    threading.current_thread().current_test_uuid = bstack1lll1111l11_opy_
@bstack1lllll11_opy_.bstack1lll11ll1ll_opy_
def bstack1ll1llll1ll_opy_(item, call, report):
    global bstack1ll1lll111l_opy_
    bstack1l1ll1l1_opy_ = bstack1l1llll1_opy_()
    if hasattr(report, bstack1lllll1_opy_ (u"ࠨࡵࡷࡳࡵ࠭᛫")):
        bstack1l1ll1l1_opy_ = bstack111ll1ll11_opy_(report.stop)
    elif hasattr(report, bstack1lllll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࠨ᛬")):
        bstack1l1ll1l1_opy_ = bstack111ll1ll11_opy_(report.start)
    try:
        if getattr(report, bstack1lllll1_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ᛭"), bstack1lllll1_opy_ (u"ࠫࠬᛮ")) == bstack1lllll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᛯ"):
            bstack11llll11ll_opy_.reset()
        if getattr(report, bstack1lllll1_opy_ (u"࠭ࡷࡩࡧࡱࠫᛰ"), bstack1lllll1_opy_ (u"ࠧࠨᛱ")) == bstack1lllll1_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᛲ"):
            if bstack1ll1lll111l_opy_ == bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᛳ"):
                _11lll111ll_opy_[item.nodeid][bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᛴ")] = bstack1l1ll1l1_opy_
                bstack1ll1ll11ll1_opy_(item, _11lll111ll_opy_[item.nodeid], bstack1lllll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᛵ"), report, call)
                store[bstack1lllll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᛶ")] = None
            elif bstack1ll1lll111l_opy_ == bstack1lllll1_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᛷ"):
                bstack1l1111l1ll_opy_ = _11lll111ll_opy_[item.nodeid][bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᛸ")]
                bstack1l1111l1ll_opy_.set(hooks=_11lll111ll_opy_[item.nodeid].get(bstack1lllll1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ᛹"), []))
                exception, bstack11lll1l111_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack11lll1l111_opy_ = [call.excinfo.exconly(), getattr(report, bstack1lllll1_opy_ (u"ࠩ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠨ᛺"), bstack1lllll1_opy_ (u"ࠪࠫ᛻"))]
                bstack1l1111l1ll_opy_.stop(time=bstack1l1ll1l1_opy_, result=Result(result=getattr(report, bstack1lllll1_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬ᛼"), bstack1lllll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ᛽")), exception=exception, bstack11lll1l111_opy_=bstack11lll1l111_opy_))
                bstack1lllll11_opy_.bstack1l1111llll_opy_(bstack1lllll1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ᛾"), _11lll111ll_opy_[item.nodeid][bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ᛿")])
        elif getattr(report, bstack1lllll1_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᜀ"), bstack1lllll1_opy_ (u"ࠩࠪᜁ")) in [bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᜂ"), bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ᜃ")]:
            bstack1l1111lll1_opy_ = item.nodeid + bstack1lllll1_opy_ (u"ࠬ࠳ࠧᜄ") + getattr(report, bstack1lllll1_opy_ (u"࠭ࡷࡩࡧࡱࠫᜅ"), bstack1lllll1_opy_ (u"ࠧࠨᜆ"))
            if getattr(report, bstack1lllll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᜇ"), False):
                hook_type = bstack1lllll1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᜈ") if getattr(report, bstack1lllll1_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᜉ"), bstack1lllll1_opy_ (u"ࠫࠬᜊ")) == bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᜋ") else bstack1lllll1_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪᜌ")
                _11lll111ll_opy_[bstack1l1111lll1_opy_] = {
                    bstack1lllll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᜍ"): uuid4().__str__(),
                    bstack1lllll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᜎ"): bstack1l1ll1l1_opy_,
                    bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᜏ"): hook_type
                }
            _11lll111ll_opy_[bstack1l1111lll1_opy_][bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᜐ")] = bstack1l1ll1l1_opy_
            bstack1ll1ll1l11l_opy_(_11lll111ll_opy_[bstack1l1111lll1_opy_][bstack1lllll1_opy_ (u"ࠫࡺࡻࡩࡥࠩᜑ")])
            bstack1ll1ll1l1ll_opy_(item, _11lll111ll_opy_[bstack1l1111lll1_opy_], bstack1lllll1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᜒ"), report, call)
            if getattr(report, bstack1lllll1_opy_ (u"࠭ࡷࡩࡧࡱࠫᜓ"), bstack1lllll1_opy_ (u"ࠧࠨ᜔")) == bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ᜕ࠧ"):
                if getattr(report, bstack1lllll1_opy_ (u"ࠩࡲࡹࡹࡩ࡯࡮ࡧࠪ᜖"), bstack1lllll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ᜗")) == bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᜘"):
                    bstack11lll1l1l1_opy_ = {
                        bstack1lllll1_opy_ (u"ࠬࡻࡵࡪࡦࠪ᜙"): uuid4().__str__(),
                        bstack1lllll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ᜚"): bstack1l1llll1_opy_(),
                        bstack1lllll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᜛"): bstack1l1llll1_opy_()
                    }
                    _11lll111ll_opy_[item.nodeid] = {**_11lll111ll_opy_[item.nodeid], **bstack11lll1l1l1_opy_}
                    bstack1ll1ll11ll1_opy_(item, _11lll111ll_opy_[item.nodeid], bstack1lllll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ᜜"))
                    bstack1ll1ll11ll1_opy_(item, _11lll111ll_opy_[item.nodeid], bstack1lllll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ᜝"), report, call)
    except Exception as err:
        print(bstack1lllll1_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࢁࡽࠨ᜞"), str(err))
def bstack1ll1lll1ll1_opy_(test, bstack11lll1l1l1_opy_, result=None, call=None, bstack11111ll11_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l1111l1ll_opy_ = {
        bstack1lllll1_opy_ (u"ࠫࡺࡻࡩࡥࠩᜟ"): bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠬࡻࡵࡪࡦࠪᜠ")],
        bstack1lllll1_opy_ (u"࠭ࡴࡺࡲࡨࠫᜡ"): bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࠬᜢ"),
        bstack1lllll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᜣ"): test.name,
        bstack1lllll1_opy_ (u"ࠩࡥࡳࡩࡿࠧᜤ"): {
            bstack1lllll1_opy_ (u"ࠪࡰࡦࡴࡧࠨᜥ"): bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫᜦ"),
            bstack1lllll1_opy_ (u"ࠬࡩ࡯ࡥࡧࠪᜧ"): inspect.getsource(test.obj)
        },
        bstack1lllll1_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᜨ"): test.name,
        bstack1lllll1_opy_ (u"ࠧࡴࡥࡲࡴࡪ࠭ᜩ"): test.name,
        bstack1lllll1_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨᜪ"): bstack1lllll11_opy_.bstack11ll1lllll_opy_(test),
        bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬᜫ"): file_path,
        bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬᜬ"): file_path,
        bstack1lllll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᜭ"): bstack1lllll1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ᜮ"),
        bstack1lllll1_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫᜯ"): file_path,
        bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᜰ"): bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᜱ")],
        bstack1lllll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᜲ"): bstack1lllll1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪᜳ"),
        bstack1lllll1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳ᜴ࠧ"): {
            bstack1lllll1_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩ᜵"): test.nodeid
        },
        bstack1lllll1_opy_ (u"࠭ࡴࡢࡩࡶࠫ᜶"): bstack111ll1l1l1_opy_(test.own_markers)
    }
    if bstack11111ll11_opy_ in [bstack1lllll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨ᜷"), bstack1lllll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ᜸")]:
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠩࡰࡩࡹࡧࠧ᜹")] = {
            bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ᜺"): bstack11lll1l1l1_opy_.get(bstack1lllll1_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭᜻"), [])
        }
    if bstack11111ll11_opy_ == bstack1lllll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭᜼"):
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭᜽")] = bstack1lllll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ᜾")
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ᜿")] = bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᝀ")]
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᝁ")] = bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᝂ")]
    if result:
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᝃ")] = result.outcome
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᝄ")] = result.duration * 1000
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᝅ")] = bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᝆ")]
        if result.failed:
            bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᝇ")] = bstack1lllll11_opy_.bstack11ll111lll_opy_(call.excinfo.typename)
            bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᝈ")] = bstack1lllll11_opy_.bstack1lll11l1lll_opy_(call.excinfo, result)
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᝉ")] = bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᝊ")]
    if outcome:
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᝋ")] = bstack111llll1l1_opy_(outcome)
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᝌ")] = 0
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᝍ")] = bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᝎ")]
        if bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᝏ")] == bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᝐ"):
            bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫᝑ")] = bstack1lllll1_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧᝒ")  # bstack1ll1llll11l_opy_
            bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᝓ")] = [{bstack1lllll1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ᝔"): [bstack1lllll1_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭᝕")]}]
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ᝖")] = bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ᝗")]
    return bstack1l1111l1ll_opy_
def bstack1ll1lllllll_opy_(test, bstack11lll11lll_opy_, bstack11111ll11_opy_, result, call, outcome, bstack1lll11111ll_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ᝘")]
    hook_name = bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ᝙")]
    hook_data = {
        bstack1lllll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ᝚"): bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭᝛")],
        bstack1lllll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ᝜"): bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ᝝"),
        bstack1lllll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ᝞"): bstack1lllll1_opy_ (u"ࠬࢁࡽࠨ᝟").format(bstack1llll111ll1_opy_(hook_name)),
        bstack1lllll1_opy_ (u"࠭ࡢࡰࡦࡼࠫᝠ"): {
            bstack1lllll1_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬᝡ"): bstack1lllll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨᝢ"),
            bstack1lllll1_opy_ (u"ࠩࡦࡳࡩ࡫ࠧᝣ"): None
        },
        bstack1lllll1_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩᝤ"): test.name,
        bstack1lllll1_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫᝥ"): bstack1lllll11_opy_.bstack11ll1lllll_opy_(test, hook_name),
        bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨᝦ"): file_path,
        bstack1lllll1_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨᝧ"): file_path,
        bstack1lllll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᝨ"): bstack1lllll1_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩᝩ"),
        bstack1lllll1_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᝪ"): file_path,
        bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᝫ"): bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᝬ")],
        bstack1lllll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ᝭"): bstack1lllll1_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨᝮ") if bstack1ll1lll111l_opy_ == bstack1lllll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᝯ") else bstack1lllll1_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨᝰ"),
        bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬ᝱"): hook_type
    }
    bstack1lll1111lll_opy_ = bstack1l111l11l1_opy_(_11lll111ll_opy_.get(test.nodeid, None))
    if bstack1lll1111lll_opy_:
        hook_data[bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡯ࡤࠨᝲ")] = bstack1lll1111lll_opy_
    if result:
        hook_data[bstack1lllll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᝳ")] = result.outcome
        hook_data[bstack1lllll1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭᝴")] = result.duration * 1000
        hook_data[bstack1lllll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᝵")] = bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᝶")]
        if result.failed:
            hook_data[bstack1lllll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ᝷")] = bstack1lllll11_opy_.bstack11ll111lll_opy_(call.excinfo.typename)
            hook_data[bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ᝸")] = bstack1lllll11_opy_.bstack1lll11l1lll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack1lllll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ᝹")] = bstack111llll1l1_opy_(outcome)
        hook_data[bstack1lllll1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ᝺")] = 100
        hook_data[bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ᝻")] = bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᝼")]
        if hook_data[bstack1lllll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ᝽")] == bstack1lllll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᝾"):
            hook_data[bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ᝿")] = bstack1lllll1_opy_ (u"࡙ࠪࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠫក")  # bstack1ll1llll11l_opy_
            hook_data[bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬខ")] = [{bstack1lllll1_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨគ"): [bstack1lllll1_opy_ (u"࠭ࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠪឃ")]}]
    if bstack1lll11111ll_opy_:
        hook_data[bstack1lllll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧង")] = bstack1lll11111ll_opy_.result
        hook_data[bstack1lllll1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩច")] = bstack11l111111l_opy_(bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ឆ")], bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨជ")])
        hook_data[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩឈ")] = bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪញ")]
        if hook_data[bstack1lllll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ដ")] == bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧឋ"):
            hook_data[bstack1lllll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧឌ")] = bstack1lllll11_opy_.bstack11ll111lll_opy_(bstack1lll11111ll_opy_.exception_type)
            hook_data[bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪឍ")] = [{bstack1lllll1_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ណ"): bstack11l1111ll1_opy_(bstack1lll11111ll_opy_.exception)}]
    return hook_data
def bstack1ll1ll11ll1_opy_(test, bstack11lll1l1l1_opy_, bstack11111ll11_opy_, result=None, call=None, outcome=None):
    bstack1l1111l1ll_opy_ = bstack1ll1lll1ll1_opy_(test, bstack11lll1l1l1_opy_, result, call, bstack11111ll11_opy_, outcome)
    driver = getattr(test, bstack1lllll1_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬត"), None)
    if bstack11111ll11_opy_ == bstack1lllll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ថ") and driver:
        bstack1l1111l1ll_opy_[bstack1lllll1_opy_ (u"࠭ࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠬទ")] = bstack1lllll11_opy_.bstack1l111111l1_opy_(driver)
    if bstack11111ll11_opy_ == bstack1lllll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨធ"):
        bstack11111ll11_opy_ = bstack1lllll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪន")
    bstack11llll111l_opy_ = {
        bstack1lllll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ប"): bstack11111ll11_opy_,
        bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬផ"): bstack1l1111l1ll_opy_
    }
    bstack1lllll11_opy_.bstack11ll1llll1_opy_(bstack11llll111l_opy_)
def bstack1ll1ll1l1ll_opy_(test, bstack11lll1l1l1_opy_, bstack11111ll11_opy_, result=None, call=None, outcome=None, bstack1lll11111ll_opy_=None):
    hook_data = bstack1ll1lllllll_opy_(test, bstack11lll1l1l1_opy_, bstack11111ll11_opy_, result, call, outcome, bstack1lll11111ll_opy_)
    bstack11llll111l_opy_ = {
        bstack1lllll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨព"): bstack11111ll11_opy_,
        bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧភ"): hook_data
    }
    bstack1lllll11_opy_.bstack11ll1llll1_opy_(bstack11llll111l_opy_)
def bstack1l111l11l1_opy_(bstack11lll1l1l1_opy_):
    if not bstack11lll1l1l1_opy_:
        return None
    if bstack11lll1l1l1_opy_.get(bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩម"), None):
        return getattr(bstack11lll1l1l1_opy_[bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪយ")], bstack1lllll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭រ"), None)
    return bstack11lll1l1l1_opy_.get(bstack1lllll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧល"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1lllll11_opy_.on():
            return
        places = [bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩវ"), bstack1lllll1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩឝ"), bstack1lllll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧឞ")]
        bstack11lll1111l_opy_ = []
        for bstack1ll1lll11ll_opy_ in places:
            records = caplog.get_records(bstack1ll1lll11ll_opy_)
            bstack1ll1lll1l1l_opy_ = bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ស") if bstack1ll1lll11ll_opy_ == bstack1lllll1_opy_ (u"ࠧࡤࡣ࡯ࡰࠬហ") else bstack1lllll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨឡ")
            bstack1ll1ll1lll1_opy_ = request.node.nodeid + (bstack1lllll1_opy_ (u"ࠩࠪអ") if bstack1ll1lll11ll_opy_ == bstack1lllll1_opy_ (u"ࠪࡧࡦࡲ࡬ࠨឣ") else bstack1lllll1_opy_ (u"ࠫ࠲࠭ឤ") + bstack1ll1lll11ll_opy_)
            bstack1lll1111l11_opy_ = bstack1l111l11l1_opy_(_11lll111ll_opy_.get(bstack1ll1ll1lll1_opy_, None))
            if not bstack1lll1111l11_opy_:
                continue
            for record in records:
                if bstack111ll1l11l_opy_(record.message):
                    continue
                bstack11lll1111l_opy_.append({
                    bstack1lllll1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨឥ"): bstack111ll111ll_opy_(record.created).isoformat() + bstack1lllll1_opy_ (u"࡚࠭ࠨឦ"),
                    bstack1lllll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ឧ"): record.levelname,
                    bstack1lllll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩឨ"): record.message,
                    bstack1ll1lll1l1l_opy_: bstack1lll1111l11_opy_
                })
        if len(bstack11lll1111l_opy_) > 0:
            bstack1lllll11_opy_.bstack1l1l111l1_opy_(bstack11lll1111l_opy_)
    except Exception as err:
        print(bstack1lllll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡧࡴࡴࡤࡠࡨ࡬ࡼࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ឩ"), str(err))
def bstack1l111l1ll_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack11l11l1l1_opy_
    bstack11lllllll_opy_ = bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧឪ"), None) and bstack1111l1l11_opy_(
            threading.current_thread(), bstack1lllll1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪឫ"), None)
    bstack1ll1llll11_opy_ = getattr(driver, bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬឬ"), None) != None and getattr(driver, bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ឭ"), None) == True
    if sequence == bstack1lllll1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧឮ") and driver != None:
      if not bstack11l11l1l1_opy_ and bstack111l1l1l1l_opy_() and bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨឯ") in CONFIG and CONFIG[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩឰ")] == True and bstack1l1l1l1ll_opy_.bstack1l1lll111l_opy_(driver_command) and (bstack1ll1llll11_opy_ or bstack11lllllll_opy_) and not bstack11ll1lll_opy_(args):
        try:
          bstack11l11l1l1_opy_ = True
          logger.debug(bstack1lllll1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡾࢁࠬឱ").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack1lllll1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡧࡵࡪࡴࡸ࡭ࠡࡵࡦࡥࡳࠦࡻࡾࠩឲ").format(str(err)))
        bstack11l11l1l1_opy_ = False
    if sequence == bstack1lllll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫឳ"):
        if driver_command == bstack1lllll1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪ឴"):
            bstack1lllll11_opy_.bstack1l11ll1l1l_opy_({
                bstack1lllll1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭឵"): response[bstack1lllll1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧា")],
                bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩិ"): store[bstack1lllll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧី")]
            })
def bstack11l11l1l_opy_():
    global bstack1l11l1l11_opy_
    bstack1llll11111_opy_.bstack1ll11l1l1_opy_()
    logging.shutdown()
    bstack1lllll11_opy_.bstack11llll11l1_opy_()
    for driver in bstack1l11l1l11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1ll1ll11lll_opy_(*args):
    global bstack1l11l1l11_opy_
    bstack1lllll11_opy_.bstack11llll11l1_opy_()
    for driver in bstack1l11l1l11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1l1111ll_opy_(self, *args, **kwargs):
    bstack1l1l1l1111_opy_ = bstack1l111ll1ll_opy_(self, *args, **kwargs)
    if not bstack1lllll11_opy_.on():
        return bstack1l1l1l1111_opy_
    bstack1lllll11_opy_.bstack1l111lll_opy_(self)
    return bstack1l1l1l1111_opy_
def bstack111l111l1_opy_(framework_name):
    global bstack1ll11l1l1l_opy_
    global bstack1ll1llll_opy_
    bstack1ll11l1l1l_opy_ = framework_name
    logger.info(bstack1ll1ll1ll_opy_.format(bstack1ll11l1l1l_opy_.split(bstack1lllll1_opy_ (u"ࠫ࠲࠭ឹ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack111l1l1l1l_opy_():
            Service.start = bstack11ll1l1l1_opy_
            Service.stop = bstack1ll1ll11_opy_
            webdriver.Remote.__init__ = bstack11ll1l1ll_opy_
            webdriver.Remote.get = bstack111111lll_opy_
            if not isinstance(os.getenv(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭ឺ")), str):
                return
            WebDriver.close = bstack1l11ll1ll_opy_
            WebDriver.quit = bstack1ll1l11lll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack111l1l1l1l_opy_():
            webdriver.Remote.__init__ = bstack1l1l1111ll_opy_
        bstack1ll1llll_opy_ = True
    except Exception as e:
        pass
    bstack111llllll_opy_()
    if os.environ.get(bstack1lllll1_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫុ")):
        bstack1ll1llll_opy_ = eval(os.environ.get(bstack1lllll1_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬូ")))
    if not bstack1ll1llll_opy_:
        bstack1l1111ll_opy_(bstack1lllll1_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥួ"), bstack1lllll11l1_opy_)
    if bstack1llll1ll1l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack11l111lll_opy_
        except Exception as e:
            logger.error(bstack1l11lll1l_opy_.format(str(e)))
    if bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩើ") in str(framework_name).lower():
        if not bstack111l1l1l1l_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack11lll1l1l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1ll1l11ll_opy_
            Config.getoption = bstack11lll111l_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack11l1l111_opy_
        except Exception as e:
            pass
def bstack1ll1l11lll_opy_(self):
    global bstack1ll11l1l1l_opy_
    global bstack1l11ll11_opy_
    global bstack11l1llll_opy_
    try:
        if bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪឿ") in bstack1ll11l1l1l_opy_ and self.session_id != None and bstack1111l1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨៀ"), bstack1lllll1_opy_ (u"ࠬ࠭េ")) != bstack1lllll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧែ"):
            bstack1l1l1l1l1_opy_ = bstack1lllll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧៃ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1lllll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨោ")
            bstack1l1ll1ll1l_opy_(logger, True)
            if self != None:
                bstack1l1l1ll11l_opy_(self, bstack1l1l1l1l1_opy_, bstack1lllll1_opy_ (u"ࠩ࠯ࠤࠬៅ").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack1lllll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧំ"), None)
        if item is not None and bstack1ll1lllll11_opy_:
            bstack1ll11lllll_opy_.bstack1lll1lll1_opy_(self, bstack1ll111l1ll_opy_, logger, item)
        threading.current_thread().testStatus = bstack1lllll1_opy_ (u"ࠫࠬះ")
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨៈ") + str(e))
    bstack11l1llll_opy_(self)
    self.session_id = None
def bstack11ll1l1ll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1l11ll11_opy_
    global bstack1l11111l_opy_
    global bstack1ll1ll1l1l_opy_
    global bstack1ll11l1l1l_opy_
    global bstack1l111ll1ll_opy_
    global bstack1l11l1l11_opy_
    global bstack1l11l1ll11_opy_
    global bstack1l11ll11ll_opy_
    global bstack1ll1lllll11_opy_
    global bstack1ll111l1ll_opy_
    CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ៉")] = str(bstack1ll11l1l1l_opy_) + str(__version__)
    command_executor = bstack1lllll1ll_opy_(bstack1l11l1ll11_opy_)
    logger.debug(bstack1111l1l1l_opy_.format(command_executor))
    proxy = bstack1l1l1l11_opy_(CONFIG, proxy)
    bstack1l1llll11_opy_ = 0
    try:
        if bstack1ll1ll1l1l_opy_ is True:
            bstack1l1llll11_opy_ = int(os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ៊")))
    except:
        bstack1l1llll11_opy_ = 0
    bstack111ll1l1_opy_ = bstack1ll1l1l1ll_opy_(CONFIG, bstack1l1llll11_opy_)
    logger.debug(bstack1ll111ll1_opy_.format(str(bstack111ll1l1_opy_)))
    bstack1ll111l1ll_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ់"))[bstack1l1llll11_opy_]
    if bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭៌") in CONFIG and CONFIG[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ៍")]:
        bstack11ll1ll1_opy_(bstack111ll1l1_opy_, bstack1l11ll11ll_opy_)
    if bstack1lll1111ll_opy_.bstack11111111l_opy_(CONFIG, bstack1l1llll11_opy_) and bstack1lll1111ll_opy_.bstack1l111l1l_opy_(bstack111ll1l1_opy_, options, desired_capabilities):
        bstack1ll1lllll11_opy_ = True
        bstack1lll1111ll_opy_.set_capabilities(bstack111ll1l1_opy_, CONFIG)
    if desired_capabilities:
        bstack1lll11ll1l_opy_ = bstack111l11l1_opy_(desired_capabilities)
        bstack1lll11ll1l_opy_[bstack1lllll1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ៎")] = bstack1ll1l1lll1_opy_(CONFIG)
        bstack1l1llll1l_opy_ = bstack1ll1l1l1ll_opy_(bstack1lll11ll1l_opy_)
        if bstack1l1llll1l_opy_:
            bstack111ll1l1_opy_ = update(bstack1l1llll1l_opy_, bstack111ll1l1_opy_)
        desired_capabilities = None
    if options:
        bstack1l11l1l1l_opy_(options, bstack111ll1l1_opy_)
    if not options:
        options = bstack1lll111111_opy_(bstack111ll1l1_opy_)
    if proxy and bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ៏")):
        options.proxy(proxy)
    if options and bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ័")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1ll11lll11_opy_() < version.parse(bstack1lllll1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭៑")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack111ll1l1_opy_)
    logger.info(bstack1l1lll1l11_opy_)
    if bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨ្")):
        bstack1l111ll1ll_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ៓")):
        bstack1l111ll1ll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪ។")):
        bstack1l111ll1ll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack1l111ll1ll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1l1l1lll11_opy_ = bstack1lllll1_opy_ (u"ࠫࠬ៕")
        if bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭៖")):
            bstack1l1l1lll11_opy_ = self.caps.get(bstack1lllll1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨៗ"))
        else:
            bstack1l1l1lll11_opy_ = self.capabilities.get(bstack1lllll1_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ៘"))
        if bstack1l1l1lll11_opy_:
            bstack1lll11l11l_opy_(bstack1l1l1lll11_opy_)
            if bstack1ll11lll11_opy_() <= version.parse(bstack1lllll1_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨ៙")):
                self.command_executor._url = bstack1lllll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ៚") + bstack1l11l1ll11_opy_ + bstack1lllll1_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢ៛")
            else:
                self.command_executor._url = bstack1lllll1_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨៜ") + bstack1l1l1lll11_opy_ + bstack1lllll1_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨ៝")
            logger.debug(bstack11ll111l1_opy_.format(bstack1l1l1lll11_opy_))
        else:
            logger.debug(bstack1l11ll1l_opy_.format(bstack1lllll1_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢ៞")))
    except Exception as e:
        logger.debug(bstack1l11ll1l_opy_.format(e))
    bstack1l11ll11_opy_ = self.session_id
    if bstack1lllll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ៟") in bstack1ll11l1l1l_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack1lllll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬ០"), None)
        if item:
            bstack1lll1111l1l_opy_ = getattr(item, bstack1lllll1_opy_ (u"ࠩࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪࡥࡳࡵࡣࡵࡸࡪࡪࠧ១"), False)
            if not getattr(item, bstack1lllll1_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫ២"), None) and bstack1lll1111l1l_opy_:
                setattr(store[bstack1lllll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ៣")], bstack1lllll1_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭៤"), self)
        bstack1lllll11_opy_.bstack1l111lll_opy_(self)
    bstack1l11l1l11_opy_.append(self)
    if bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ៥") in CONFIG and bstack1lllll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ៦") in CONFIG[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ៧")][bstack1l1llll11_opy_]:
        bstack1l11111l_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ៨")][bstack1l1llll11_opy_][bstack1lllll1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ៩")]
    logger.debug(bstack1111llll_opy_.format(bstack1l11ll11_opy_))
def bstack111111lll_opy_(self, url):
    global bstack1ll1lll1l1_opy_
    global CONFIG
    try:
        bstack1l11l111ll_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack111llll11_opy_.format(str(err)))
    try:
        bstack1ll1lll1l1_opy_(self, url)
    except Exception as e:
        try:
            bstack1ll1l111_opy_ = str(e)
            if any(err_msg in bstack1ll1l111_opy_ for err_msg in bstack1l11llll11_opy_):
                bstack1l11l111ll_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack111llll11_opy_.format(str(err)))
        raise e
def bstack11l1lllll_opy_(item, when):
    global bstack1ll1l1llll_opy_
    try:
        bstack1ll1l1llll_opy_(item, when)
    except Exception as e:
        pass
def bstack11l1l111_opy_(item, call, rep):
    global bstack1ll111111_opy_
    global bstack1l11l1l11_opy_
    name = bstack1lllll1_opy_ (u"ࠫࠬ៪")
    try:
        if rep.when == bstack1lllll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ៫"):
            bstack1l11ll11_opy_ = threading.current_thread().bstackSessionId
            bstack1ll1lll1111_opy_ = item.config.getoption(bstack1lllll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ៬"))
            try:
                if (str(bstack1ll1lll1111_opy_).lower() != bstack1lllll1_opy_ (u"ࠧࡵࡴࡸࡩࠬ៭")):
                    name = str(rep.nodeid)
                    bstack1ll1l1111_opy_ = bstack1l1l1111_opy_(bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ៮"), name, bstack1lllll1_opy_ (u"ࠩࠪ៯"), bstack1lllll1_opy_ (u"ࠪࠫ៰"), bstack1lllll1_opy_ (u"ࠫࠬ៱"), bstack1lllll1_opy_ (u"ࠬ࠭៲"))
                    os.environ[bstack1lllll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ៳")] = name
                    for driver in bstack1l11l1l11_opy_:
                        if bstack1l11ll11_opy_ == driver.session_id:
                            driver.execute_script(bstack1ll1l1111_opy_)
            except Exception as e:
                logger.debug(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ៴").format(str(e)))
            try:
                bstack1l1l111ll1_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack1lllll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ៵"):
                    status = bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ៶") if rep.outcome.lower() == bstack1lllll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ៷") else bstack1lllll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ៸")
                    reason = bstack1lllll1_opy_ (u"ࠬ࠭៹")
                    if status == bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭៺"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack1lllll1_opy_ (u"ࠧࡪࡰࡩࡳࠬ៻") if status == bstack1lllll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ៼") else bstack1lllll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ៽")
                    data = name + bstack1lllll1_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬ៾") if status == bstack1lllll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ៿") else name + bstack1lllll1_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩࠧࠠࠨ᠀") + reason
                    bstack111l1l1l1_opy_ = bstack1l1l1111_opy_(bstack1lllll1_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ᠁"), bstack1lllll1_opy_ (u"ࠧࠨ᠂"), bstack1lllll1_opy_ (u"ࠨࠩ᠃"), bstack1lllll1_opy_ (u"ࠩࠪ᠄"), level, data)
                    for driver in bstack1l11l1l11_opy_:
                        if bstack1l11ll11_opy_ == driver.session_id:
                            driver.execute_script(bstack111l1l1l1_opy_)
            except Exception as e:
                logger.debug(bstack1lllll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤࡱࡱࡸࡪࡾࡴࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ᠅").format(str(e)))
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡤࡸࡪࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁࡽࠨ᠆").format(str(e)))
    bstack1ll111111_opy_(item, call, rep)
notset = Notset()
def bstack11lll111l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l11lll11l_opy_
    if str(name).lower() == bstack1lllll1_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬ᠇"):
        return bstack1lllll1_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧ᠈")
    else:
        return bstack1l11lll11l_opy_(self, name, default, skip)
def bstack11l111lll_opy_(self):
    global CONFIG
    global bstack1l1l11111_opy_
    try:
        proxy = bstack1ll11lll1_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack1lllll1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ᠉")):
                proxies = bstack1llllllll_opy_(proxy, bstack1lllll1ll_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l111ll1l_opy_ = proxies.popitem()
                    if bstack1lllll1_opy_ (u"ࠣ࠼࠲࠳ࠧ᠊") in bstack1l111ll1l_opy_:
                        return bstack1l111ll1l_opy_
                    else:
                        return bstack1lllll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ᠋") + bstack1l111ll1l_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack1lllll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢ᠌").format(str(e)))
    return bstack1l1l11111_opy_(self)
def bstack1llll1ll1l_opy_():
    return (bstack1lllll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ᠍") in CONFIG or bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ᠎") in CONFIG) and bstack111l11l11_opy_() and bstack1ll11lll11_opy_() >= version.parse(
        bstack1l1l1l1l11_opy_)
def bstack11ll111ll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l11111l_opy_
    global bstack1ll1ll1l1l_opy_
    global bstack1ll11l1l1l_opy_
    CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ᠏")] = str(bstack1ll11l1l1l_opy_) + str(__version__)
    bstack1l1llll11_opy_ = 0
    try:
        if bstack1ll1ll1l1l_opy_ is True:
            bstack1l1llll11_opy_ = int(os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ᠐")))
    except:
        bstack1l1llll11_opy_ = 0
    CONFIG[bstack1lllll1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ᠑")] = True
    bstack111ll1l1_opy_ = bstack1ll1l1l1ll_opy_(CONFIG, bstack1l1llll11_opy_)
    logger.debug(bstack1ll111ll1_opy_.format(str(bstack111ll1l1_opy_)))
    if CONFIG.get(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭᠒")):
        bstack11ll1ll1_opy_(bstack111ll1l1_opy_, bstack1l11ll11ll_opy_)
    if bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭᠓") in CONFIG and bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ᠔") in CONFIG[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ᠕")][bstack1l1llll11_opy_]:
        bstack1l11111l_opy_ = CONFIG[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ᠖")][bstack1l1llll11_opy_][bstack1lllll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ᠗")]
    import urllib
    import json
    bstack111111ll1_opy_ = bstack1lllll1_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪ᠘") + urllib.parse.quote(json.dumps(bstack111ll1l1_opy_))
    browser = self.connect(bstack111111ll1_opy_)
    return browser
def bstack111llllll_opy_():
    global bstack1ll1llll_opy_
    global bstack1ll11l1l1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11111l1l1_opy_
        if not bstack111l1l1l1l_opy_():
            global bstack1lll1l11l1_opy_
            if not bstack1lll1l11l1_opy_:
                from bstack_utils.helper import bstack1l1ll11ll_opy_, bstack11l1l1lll_opy_
                bstack1lll1l11l1_opy_ = bstack1l1ll11ll_opy_()
                bstack11l1l1lll_opy_(bstack1ll11l1l1l_opy_)
            BrowserType.connect = bstack11111l1l1_opy_
            return
        BrowserType.launch = bstack11ll111ll_opy_
        bstack1ll1llll_opy_ = True
    except Exception as e:
        pass
def bstack1ll1lllll1l_opy_():
    global CONFIG
    global bstack1l1l1lllll_opy_
    global bstack1l11l1ll11_opy_
    global bstack1l11ll11ll_opy_
    global bstack1ll1ll1l1l_opy_
    global bstack1ll111111l_opy_
    CONFIG = json.loads(os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨ᠙")))
    bstack1l1l1lllll_opy_ = eval(os.environ.get(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ᠚")))
    bstack1l11l1ll11_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫ᠛"))
    bstack11l1l111l_opy_(CONFIG, bstack1l1l1lllll_opy_)
    bstack1ll111111l_opy_ = bstack1llll11111_opy_.bstack1l11l11111_opy_(CONFIG, bstack1ll111111l_opy_)
    global bstack1l111ll1ll_opy_
    global bstack11l1llll_opy_
    global bstack11l111111_opy_
    global bstack11111l11l_opy_
    global bstack1llll11l1l_opy_
    global bstack11llll1ll_opy_
    global bstack1l111111_opy_
    global bstack1ll1lll1l1_opy_
    global bstack1l1l11111_opy_
    global bstack1l11lll11l_opy_
    global bstack1ll1l1llll_opy_
    global bstack1ll111111_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1l111ll1ll_opy_ = webdriver.Remote.__init__
        bstack11l1llll_opy_ = WebDriver.quit
        bstack1l111111_opy_ = WebDriver.close
        bstack1ll1lll1l1_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ᠜") in CONFIG or bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ᠝") in CONFIG) and bstack111l11l11_opy_():
        if bstack1ll11lll11_opy_() < version.parse(bstack1l1l1l1l11_opy_):
            logger.error(bstack1l1111lll_opy_.format(bstack1ll11lll11_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1l1l11111_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack1l11lll1l_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1l11lll11l_opy_ = Config.getoption
        from _pytest import runner
        bstack1ll1l1llll_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1l1l1llll1_opy_)
    try:
        from pytest_bdd import reporting
        bstack1ll111111_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨ᠞"))
    bstack1l11ll11ll_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ᠟"), {}).get(bstack1lllll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᠠ"))
    bstack1ll1ll1l1l_opy_ = True
    bstack111l111l1_opy_(bstack1l1l11l11l_opy_)
if (bstack111l1l1lll_opy_()):
    bstack1ll1lllll1l_opy_()
@bstack1l1111l111_opy_(class_method=False)
def bstack1ll1llll111_opy_(hook_name, event, bstack1ll1ll1ll1l_opy_=None):
    if hook_name not in [bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᠡ"), bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᠢ"), bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᠣ"), bstack1lllll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᠤ"), bstack1lllll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᠥ"), bstack1lllll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩᠦ"), bstack1lllll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᠧ"), bstack1lllll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᠨ")]:
        return
    node = store[bstack1lllll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᠩ")]
    if hook_name in [bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᠪ"), bstack1lllll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᠫ")]:
        node = store[bstack1lllll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭ᠬ")]
    elif hook_name in [bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᠭ"), bstack1lllll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᠮ")]:
        node = store[bstack1lllll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡨࡲࡡࡴࡵࡢ࡭ࡹ࡫࡭ࠨᠯ")]
    if event == bstack1lllll1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫᠰ"):
        hook_type = bstack1llll11l1l1_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack11lll11lll_opy_ = {
            bstack1lllll1_opy_ (u"ࠬࡻࡵࡪࡦࠪᠱ"): uuid,
            bstack1lllll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᠲ"): bstack1l1llll1_opy_(),
            bstack1lllll1_opy_ (u"ࠧࡵࡻࡳࡩࠬᠳ"): bstack1lllll1_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᠴ"),
            bstack1lllll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᠵ"): hook_type,
            bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭ᠶ"): hook_name
        }
        store[bstack1lllll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᠷ")].append(uuid)
        bstack1lll11111l1_opy_ = node.nodeid
        if hook_type == bstack1lllll1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᠸ"):
            if not _11lll111ll_opy_.get(bstack1lll11111l1_opy_, None):
                _11lll111ll_opy_[bstack1lll11111l1_opy_] = {bstack1lllll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᠹ"): []}
            _11lll111ll_opy_[bstack1lll11111l1_opy_][bstack1lllll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᠺ")].append(bstack11lll11lll_opy_[bstack1lllll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᠻ")])
        _11lll111ll_opy_[bstack1lll11111l1_opy_ + bstack1lllll1_opy_ (u"ࠩ࠰ࠫᠼ") + hook_name] = bstack11lll11lll_opy_
        bstack1ll1ll1l1ll_opy_(node, bstack11lll11lll_opy_, bstack1lllll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᠽ"))
    elif event == bstack1lllll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪᠾ"):
        bstack1l1111lll1_opy_ = node.nodeid + bstack1lllll1_opy_ (u"ࠬ࠳ࠧᠿ") + hook_name
        _11lll111ll_opy_[bstack1l1111lll1_opy_][bstack1lllll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᡀ")] = bstack1l1llll1_opy_()
        bstack1ll1ll1l11l_opy_(_11lll111ll_opy_[bstack1l1111lll1_opy_][bstack1lllll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᡁ")])
        bstack1ll1ll1l1ll_opy_(node, _11lll111ll_opy_[bstack1l1111lll1_opy_], bstack1lllll1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᡂ"), bstack1lll11111ll_opy_=bstack1ll1ll1ll1l_opy_)
def bstack1ll1lll1l11_opy_():
    global bstack1ll1lll111l_opy_
    if bstack11lll1ll1_opy_():
        bstack1ll1lll111l_opy_ = bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᡃ")
    else:
        bstack1ll1lll111l_opy_ = bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᡄ")
@bstack1lllll11_opy_.bstack1lll11ll1ll_opy_
def bstack1ll1llllll1_opy_():
    bstack1ll1lll1l11_opy_()
    if bstack111l11l11_opy_():
        bstack1ll1l111l1_opy_(bstack1l111l1ll_opy_)
    try:
        bstack1111ll1111_opy_(bstack1ll1llll111_opy_)
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡴࠢࡳࡥࡹࡩࡨ࠻ࠢࡾࢁࠧᡅ").format(e))
bstack1ll1llllll1_opy_()