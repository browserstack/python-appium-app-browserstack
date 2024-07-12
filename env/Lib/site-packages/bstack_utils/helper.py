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
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
import urllib
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack11l11l1ll1_opy_, bstack1ll111lll1_opy_, bstack1lll11ll1_opy_, bstack111ll1l1l_opy_,
                                    bstack11l11l1l11_opy_, bstack11l11l1lll_opy_)
from bstack_utils.messages import bstack1lll1ll111_opy_, bstack1l11lll1l_opy_
from bstack_utils.proxy import bstack1l11111ll_opy_, bstack1ll11lll1_opy_
bstack1111ll1ll_opy_ = Config.bstack1l11llll1_opy_()
logger = logging.getLogger(__name__)
def bstack11l1l11lll_opy_(config):
    return config[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᇁ")]
def bstack11l1llll11_opy_(config):
    return config[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᇂ")]
def bstack1l1ll1lll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack111l1l11l1_opy_(obj):
    values = []
    bstack111ll1111l_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡶࠧࡤࡃࡖࡕࡗࡓࡒࡥࡔࡂࡉࡢࡠࡩ࠱ࠤࠣᇃ"), re.I)
    for key in obj.keys():
        if bstack111ll1111l_opy_.match(key):
            values.append(obj[key])
    return values
def bstack111llll11l_opy_(config):
    tags = []
    tags.extend(bstack111l1l11l1_opy_(os.environ))
    tags.extend(bstack111l1l11l1_opy_(config))
    return tags
def bstack111ll1l1l1_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack111lllllll_opy_(bstack111l11111l_opy_):
    if not bstack111l11111l_opy_:
        return bstack1lllll1_opy_ (u"ࠬ࠭ᇄ")
    return bstack1lllll1_opy_ (u"ࠨࡻࡾࠢࠫࡿࢂ࠯ࠢᇅ").format(bstack111l11111l_opy_.name, bstack111l11111l_opy_.email)
def bstack11l1lll111_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111l1lllll_opy_ = repo.common_dir
        info = {
            bstack1lllll1_opy_ (u"ࠢࡴࡪࡤࠦᇆ"): repo.head.commit.hexsha,
            bstack1lllll1_opy_ (u"ࠣࡵ࡫ࡳࡷࡺ࡟ࡴࡪࡤࠦᇇ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1lllll1_opy_ (u"ࠤࡥࡶࡦࡴࡣࡩࠤᇈ"): repo.active_branch.name,
            bstack1lllll1_opy_ (u"ࠥࡸࡦ࡭ࠢᇉ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1lllll1_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡸࡪࡸࠢᇊ"): bstack111lllllll_opy_(repo.head.commit.committer),
            bstack1lllll1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡹ࡫ࡲࡠࡦࡤࡸࡪࠨᇋ"): repo.head.commit.committed_datetime.isoformat(),
            bstack1lllll1_opy_ (u"ࠨࡡࡶࡶ࡫ࡳࡷࠨᇌ"): bstack111lllllll_opy_(repo.head.commit.author),
            bstack1lllll1_opy_ (u"ࠢࡢࡷࡷ࡬ࡴࡸ࡟ࡥࡣࡷࡩࠧᇍ"): repo.head.commit.authored_datetime.isoformat(),
            bstack1lllll1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡠ࡯ࡨࡷࡸࡧࡧࡦࠤᇎ"): repo.head.commit.message,
            bstack1lllll1_opy_ (u"ࠤࡵࡳࡴࡺࠢᇏ"): repo.git.rev_parse(bstack1lllll1_opy_ (u"ࠥ࠱࠲ࡹࡨࡰࡹ࠰ࡸࡴࡶ࡬ࡦࡸࡨࡰࠧᇐ")),
            bstack1lllll1_opy_ (u"ࠦࡨࡵ࡭࡮ࡱࡱࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧᇑ"): bstack111l1lllll_opy_,
            bstack1lllll1_opy_ (u"ࠧࡽ࡯ࡳ࡭ࡷࡶࡪ࡫࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᇒ"): subprocess.check_output([bstack1lllll1_opy_ (u"ࠨࡧࡪࡶࠥᇓ"), bstack1lllll1_opy_ (u"ࠢࡳࡧࡹ࠱ࡵࡧࡲࡴࡧࠥᇔ"), bstack1lllll1_opy_ (u"ࠣ࠯࠰࡫࡮ࡺ࠭ࡤࡱࡰࡱࡴࡴ࠭ࡥ࡫ࡵࠦᇕ")]).strip().decode(
                bstack1lllll1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᇖ")),
            bstack1lllll1_opy_ (u"ࠥࡰࡦࡹࡴࡠࡶࡤ࡫ࠧᇗ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1lllll1_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡷࡤࡹࡩ࡯ࡥࡨࡣࡱࡧࡳࡵࡡࡷࡥ࡬ࠨᇘ"): repo.git.rev_list(
                bstack1lllll1_opy_ (u"ࠧࢁࡽ࠯࠰ࡾࢁࠧᇙ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack111l1ll1l1_opy_ = []
        for remote in remotes:
            bstack11l111ll11_opy_ = {
                bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᇚ"): remote.name,
                bstack1lllll1_opy_ (u"ࠢࡶࡴ࡯ࠦᇛ"): remote.url,
            }
            bstack111l1ll1l1_opy_.append(bstack11l111ll11_opy_)
        bstack111l11l11l_opy_ = {
            bstack1lllll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᇜ"): bstack1lllll1_opy_ (u"ࠤࡪ࡭ࡹࠨᇝ"),
            **info,
            bstack1lllll1_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡶࠦᇞ"): bstack111l1ll1l1_opy_
        }
        bstack111l11l11l_opy_ = bstack111l1llll1_opy_(bstack111l11l11l_opy_)
        return bstack111l11l11l_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1lllll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡶࡵ࡭ࡣࡷ࡭ࡳ࡭ࠠࡈ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢᇟ").format(err))
        return {}
def bstack111l1llll1_opy_(bstack111l11l11l_opy_):
    bstack111l1111ll_opy_ = bstack111ll111l1_opy_(bstack111l11l11l_opy_)
    if bstack111l1111ll_opy_ and bstack111l1111ll_opy_ > bstack11l11l1l11_opy_:
        bstack111l1ll1ll_opy_ = bstack111l1111ll_opy_ - bstack11l11l1l11_opy_
        bstack11l111ll1l_opy_ = bstack111l1ll111_opy_(bstack111l11l11l_opy_[bstack1lllll1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᇠ")], bstack111l1ll1ll_opy_)
        bstack111l11l11l_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢᇡ")] = bstack11l111ll1l_opy_
        logger.info(bstack1lllll1_opy_ (u"ࠢࡕࡪࡨࠤࡨࡵ࡭࡮࡫ࡷࠤ࡭ࡧࡳࠡࡤࡨࡩࡳࠦࡴࡳࡷࡱࡧࡦࡺࡥࡥ࠰ࠣࡗ࡮ࢀࡥࠡࡱࡩࠤࡨࡵ࡭࡮࡫ࡷࠤࡦ࡬ࡴࡦࡴࠣࡸࡷࡻ࡮ࡤࡣࡷ࡭ࡴࡴࠠࡪࡵࠣࡿࢂࠦࡋࡃࠤᇢ")
                    .format(bstack111ll111l1_opy_(bstack111l11l11l_opy_) / 1024))
    return bstack111l11l11l_opy_
def bstack111ll111l1_opy_(bstack1l1llll1ll_opy_):
    try:
        if bstack1l1llll1ll_opy_:
            bstack111ll11ll1_opy_ = json.dumps(bstack1l1llll1ll_opy_)
            bstack111l11l1l1_opy_ = sys.getsizeof(bstack111ll11ll1_opy_)
            return bstack111l11l1l1_opy_
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠣࡕࡲࡱࡪࡺࡨࡪࡰࡪࠤࡼ࡫࡮ࡵࠢࡺࡶࡴࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡣ࡯ࡧࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡹࡩࡻࡧࠣࡳ࡫ࠦࡊࡔࡑࡑࠤࡴࡨࡪࡦࡥࡷ࠾ࠥࢁࡽࠣᇣ").format(e))
    return -1
def bstack111l1ll111_opy_(field, bstack111l111ll1_opy_):
    try:
        bstack111l111l11_opy_ = len(bytes(bstack11l11l1lll_opy_, bstack1lllll1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᇤ")))
        bstack111lll1ll1_opy_ = bytes(field, bstack1lllll1_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᇥ"))
        bstack111l11ll11_opy_ = len(bstack111lll1ll1_opy_)
        bstack111l1l1l11_opy_ = ceil(bstack111l11ll11_opy_ - bstack111l111ll1_opy_ - bstack111l111l11_opy_)
        if bstack111l1l1l11_opy_ > 0:
            bstack111llllll1_opy_ = bstack111lll1ll1_opy_[:bstack111l1l1l11_opy_].decode(bstack1lllll1_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪᇦ"), errors=bstack1lllll1_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࠬᇧ")) + bstack11l11l1lll_opy_
            return bstack111llllll1_opy_
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡹࡸࡵ࡯ࡥࡤࡸ࡮ࡴࡧࠡࡨ࡬ࡩࡱࡪࠬࠡࡰࡲࡸ࡭࡯࡮ࡨࠢࡺࡥࡸࠦࡴࡳࡷࡱࡧࡦࡺࡥࡥࠢ࡫ࡩࡷ࡫࠺ࠡࡽࢀࠦᇨ").format(e))
    return field
def bstack1111l1111_opy_():
    env = os.environ
    if (bstack1lllll1_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡗࡕࡐࠧᇩ") in env and len(env[bstack1lllll1_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᇪ")]) > 0) or (
            bstack1lllll1_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢࡌࡔࡓࡅࠣᇫ") in env and len(env[bstack1lllll1_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤᇬ")]) > 0):
        return {
            bstack1lllll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇭ"): bstack1lllll1_opy_ (u"ࠧࡐࡥ࡯࡭࡬ࡲࡸࠨᇮ"),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇯ"): env.get(bstack1lllll1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᇰ")),
            bstack1lllll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᇱ"): env.get(bstack1lllll1_opy_ (u"ࠤࡍࡓࡇࡥࡎࡂࡏࡈࠦᇲ")),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᇳ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᇴ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠧࡉࡉࠣᇵ")) == bstack1lllll1_opy_ (u"ࠨࡴࡳࡷࡨࠦᇶ") and bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋࡃࡊࠤᇷ"))):
        return {
            bstack1lllll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᇸ"): bstack1lllll1_opy_ (u"ࠤࡆ࡭ࡷࡩ࡬ࡦࡅࡌࠦᇹ"),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᇺ"): env.get(bstack1lllll1_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᇻ")),
            bstack1lllll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᇼ"): env.get(bstack1lllll1_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡊࡐࡄࠥᇽ")),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᇾ"): env.get(bstack1lllll1_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࠦᇿ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠤࡆࡍࠧሀ")) == bstack1lllll1_opy_ (u"ࠥࡸࡷࡻࡥࠣሁ") and bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࠦሂ"))):
        return {
            bstack1lllll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥሃ"): bstack1lllll1_opy_ (u"ࠨࡔࡳࡣࡹ࡭ࡸࠦࡃࡊࠤሄ"),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥህ"): env.get(bstack1lllll1_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡄࡘࡍࡑࡊ࡟ࡘࡇࡅࡣ࡚ࡘࡌࠣሆ")),
            bstack1lllll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦሇ"): env.get(bstack1lllll1_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧለ")),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥሉ"): env.get(bstack1lllll1_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦሊ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡃࡊࠤላ")) == bstack1lllll1_opy_ (u"ࠢࡵࡴࡸࡩࠧሌ") and env.get(bstack1lllll1_opy_ (u"ࠣࡅࡌࡣࡓࡇࡍࡆࠤል")) == bstack1lllll1_opy_ (u"ࠤࡦࡳࡩ࡫ࡳࡩ࡫ࡳࠦሎ"):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣሏ"): bstack1lllll1_opy_ (u"ࠦࡈࡵࡤࡦࡵ࡫࡭ࡵࠨሐ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣሑ"): None,
            bstack1lllll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣሒ"): None,
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨሓ"): None
        }
    if env.get(bstack1lllll1_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇࡘࡁࡏࡅࡋࠦሔ")) and env.get(bstack1lllll1_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡉࡏࡎࡏࡌࡘࠧሕ")):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣሖ"): bstack1lllll1_opy_ (u"ࠦࡇ࡯ࡴࡣࡷࡦ࡯ࡪࡺࠢሗ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣመ"): env.get(bstack1lllll1_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡊࡍ࡙ࡥࡈࡕࡖࡓࡣࡔࡘࡉࡈࡋࡑࠦሙ")),
            bstack1lllll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤሚ"): None,
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢማ"): env.get(bstack1lllll1_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦሜ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠥࡇࡎࠨም")) == bstack1lllll1_opy_ (u"ࠦࡹࡸࡵࡦࠤሞ") and bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"ࠧࡊࡒࡐࡐࡈࠦሟ"))):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦሠ"): bstack1lllll1_opy_ (u"ࠢࡅࡴࡲࡲࡪࠨሡ"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦሢ"): env.get(bstack1lllll1_opy_ (u"ࠤࡇࡖࡔࡔࡅࡠࡄࡘࡍࡑࡊ࡟ࡍࡋࡑࡏࠧሣ")),
            bstack1lllll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧሤ"): None,
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥሥ"): env.get(bstack1lllll1_opy_ (u"ࠧࡊࡒࡐࡐࡈࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥሦ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡃࡊࠤሧ")) == bstack1lllll1_opy_ (u"ࠢࡵࡴࡸࡩࠧረ") and bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࠦሩ"))):
        return {
            bstack1lllll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢሪ"): bstack1lllll1_opy_ (u"ࠥࡗࡪࡳࡡࡱࡪࡲࡶࡪࠨራ"),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢሬ"): env.get(bstack1lllll1_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡑࡕࡋࡆࡔࡉ࡛ࡃࡗࡍࡔࡔ࡟ࡖࡔࡏࠦር")),
            bstack1lllll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣሮ"): env.get(bstack1lllll1_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧሯ")),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢሰ"): env.get(bstack1lllll1_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡌࡈࠧሱ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠥࡇࡎࠨሲ")) == bstack1lllll1_opy_ (u"ࠦࡹࡸࡵࡦࠤሳ") and bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"ࠧࡍࡉࡕࡎࡄࡆࡤࡉࡉࠣሴ"))):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦስ"): bstack1lllll1_opy_ (u"ࠢࡈ࡫ࡷࡐࡦࡨࠢሶ"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦሷ"): env.get(bstack1lllll1_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡘࡖࡑࠨሸ")),
            bstack1lllll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧሹ"): env.get(bstack1lllll1_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤሺ")),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦሻ"): env.get(bstack1lllll1_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡉࡅࠤሼ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠢࡄࡋࠥሽ")) == bstack1lllll1_opy_ (u"ࠣࡶࡵࡹࡪࠨሾ") and bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࠧሿ"))):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣቀ"): bstack1lllll1_opy_ (u"ࠦࡇࡻࡩ࡭ࡦ࡮࡭ࡹ࡫ࠢቁ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣቂ"): env.get(bstack1lllll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧቃ")),
            bstack1lllll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤቄ"): env.get(bstack1lllll1_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡑࡇࡂࡆࡎࠥቅ")) or env.get(bstack1lllll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡖࡉࡑࡇࡏࡍࡓࡋ࡟ࡏࡃࡐࡉࠧቆ")),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤቇ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨቈ"))
        }
    if bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"࡚ࠧࡆࡠࡄࡘࡍࡑࡊࠢ቉"))):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦቊ"): bstack1lllll1_opy_ (u"ࠢࡗ࡫ࡶࡹࡦࡲࠠࡔࡶࡸࡨ࡮ࡵࠠࡕࡧࡤࡱ࡙ࠥࡥࡳࡸ࡬ࡧࡪࡹࠢቋ"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦቌ"): bstack1lllll1_opy_ (u"ࠤࡾࢁࢀࢃࠢቍ").format(env.get(bstack1lllll1_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡇࡑࡘࡒࡉࡇࡔࡊࡑࡑࡗࡊࡘࡖࡆࡔࡘࡖࡎ࠭቎")), env.get(bstack1lllll1_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡒࡕࡓࡏࡋࡃࡕࡋࡇࠫ቏"))),
            bstack1lllll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢቐ"): env.get(bstack1lllll1_opy_ (u"ࠨࡓ࡚ࡕࡗࡉࡒࡥࡄࡆࡈࡌࡒࡎ࡚ࡉࡐࡐࡌࡈࠧቑ")),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨቒ"): env.get(bstack1lllll1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣቓ"))
        }
    if bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࠦቔ"))):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣቕ"): bstack1lllll1_opy_ (u"ࠦࡆࡶࡰࡷࡧࡼࡳࡷࠨቖ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ቗"): bstack1lllll1_opy_ (u"ࠨࡻࡾ࠱ࡳࡶࡴࡰࡥࡤࡶ࠲ࡿࢂ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁࠧቘ").format(env.get(bstack1lllll1_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡘࡖࡑ࠭቙")), env.get(bstack1lllll1_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡅࡈࡉࡏࡖࡐࡗࡣࡓࡇࡍࡆࠩቚ")), env.get(bstack1lllll1_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡕࡘࡏࡋࡇࡆࡘࡤ࡙ࡌࡖࡉࠪቛ")), env.get(bstack1lllll1_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧቜ"))),
            bstack1lllll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨቝ"): env.get(bstack1lllll1_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤ቞")),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ቟"): env.get(bstack1lllll1_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣበ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠣࡃ࡝࡙ࡗࡋ࡟ࡉࡖࡗࡔࡤ࡛ࡓࡆࡔࡢࡅࡌࡋࡎࡕࠤቡ")) and env.get(bstack1lllll1_opy_ (u"ࠤࡗࡊࡤࡈࡕࡊࡎࡇࠦቢ")):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣባ"): bstack1lllll1_opy_ (u"ࠦࡆࢀࡵࡳࡧࠣࡇࡎࠨቤ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣብ"): bstack1lllll1_opy_ (u"ࠨࡻࡾࡽࢀ࠳ࡤࡨࡵࡪ࡮ࡧ࠳ࡷ࡫ࡳࡶ࡮ࡷࡷࡄࡨࡵࡪ࡮ࡧࡍࡩࡃࡻࡾࠤቦ").format(env.get(bstack1lllll1_opy_ (u"ࠧࡔ࡛ࡖࡘࡊࡓ࡟ࡕࡇࡄࡑࡋࡕࡕࡏࡆࡄࡘࡎࡕࡎࡔࡇࡕ࡚ࡊࡘࡕࡓࡋࠪቧ")), env.get(bstack1lllll1_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡖࡒࡐࡌࡈࡇ࡙࠭ቨ")), env.get(bstack1lllll1_opy_ (u"ࠩࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠩቩ"))),
            bstack1lllll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧቪ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦቫ")),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦቬ"): env.get(bstack1lllll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨቭ"))
        }
    if any([env.get(bstack1lllll1_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧቮ")), env.get(bstack1lllll1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡗࡋࡓࡐࡎ࡙ࡉࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢቯ")), env.get(bstack1lllll1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤ࡙ࡏࡖࡔࡆࡉࡤ࡜ࡅࡓࡕࡌࡓࡓࠨተ"))]):
        return {
            bstack1lllll1_opy_ (u"ࠥࡲࡦࡳࡥࠣቱ"): bstack1lllll1_opy_ (u"ࠦࡆ࡝ࡓࠡࡅࡲࡨࡪࡈࡵࡪ࡮ࡧࠦቲ"),
            bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣታ"): env.get(bstack1lllll1_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡓ࡙ࡇࡒࡉࡄࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧቴ")),
            bstack1lllll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤት"): env.get(bstack1lllll1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨቶ")),
            bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣቷ"): env.get(bstack1lllll1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣቸ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡧࡻࡩ࡭ࡦࡑࡹࡲࡨࡥࡳࠤቹ")):
        return {
            bstack1lllll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥቺ"): bstack1lllll1_opy_ (u"ࠨࡂࡢ࡯ࡥࡳࡴࠨቻ"),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥቼ"): env.get(bstack1lllll1_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡤࡸ࡭ࡱࡪࡒࡦࡵࡸࡰࡹࡹࡕࡳ࡮ࠥች")),
            bstack1lllll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦቾ"): env.get(bstack1lllll1_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡷ࡭ࡵࡲࡵࡌࡲࡦࡓࡧ࡭ࡦࠤቿ")),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥኀ"): env.get(bstack1lllll1_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥኁ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘࠢኂ")) or env.get(bstack1lllll1_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤኃ")):
        return {
            bstack1lllll1_opy_ (u"ࠣࡰࡤࡱࡪࠨኄ"): bstack1lllll1_opy_ (u"ࠤ࡚ࡩࡷࡩ࡫ࡦࡴࠥኅ"),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨኆ"): env.get(bstack1lllll1_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣኇ")),
            bstack1lllll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢኈ"): bstack1lllll1_opy_ (u"ࠨࡍࡢ࡫ࡱࠤࡕ࡯ࡰࡦ࡮࡬ࡲࡪࠨ኉") if env.get(bstack1lllll1_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡏࡄࡍࡓࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡕࡗࡅࡗ࡚ࡅࡅࠤኊ")) else None,
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢኋ"): env.get(bstack1lllll1_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡋࡎ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢኌ"))
        }
    if any([env.get(bstack1lllll1_opy_ (u"ࠥࡋࡈࡖ࡟ࡑࡔࡒࡎࡊࡉࡔࠣኍ")), env.get(bstack1lllll1_opy_ (u"ࠦࡌࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧ኎")), env.get(bstack1lllll1_opy_ (u"ࠧࡍࡏࡐࡉࡏࡉࡤࡉࡌࡐࡗࡇࡣࡕࡘࡏࡋࡇࡆࡘࠧ኏"))]):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦነ"): bstack1lllll1_opy_ (u"ࠢࡈࡱࡲ࡫ࡱ࡫ࠠࡄ࡮ࡲࡹࡩࠨኑ"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦኒ"): None,
            bstack1lllll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦና"): env.get(bstack1lllll1_opy_ (u"ࠥࡔࡗࡕࡊࡆࡅࡗࡣࡎࡊࠢኔ")),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥን"): env.get(bstack1lllll1_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢኖ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡓࡉࡋࡓࡔࡆࡈࡌࡆࠤኗ")):
        return {
            bstack1lllll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧኘ"): bstack1lllll1_opy_ (u"ࠣࡕ࡫࡭ࡵࡶࡡࡣ࡮ࡨࠦኙ"),
            bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧኚ"): env.get(bstack1lllll1_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤኛ")),
            bstack1lllll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨኜ"): bstack1lllll1_opy_ (u"ࠧࡐ࡯ࡣࠢࠦࡿࢂࠨኝ").format(env.get(bstack1lllll1_opy_ (u"࠭ࡓࡉࡋࡓࡔࡆࡈࡌࡆࡡࡍࡓࡇࡥࡉࡅࠩኞ"))) if env.get(bstack1lllll1_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠥኟ")) else None,
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢአ"): env.get(bstack1lllll1_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦኡ"))
        }
    if bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"ࠥࡒࡊ࡚ࡌࡊࡈ࡜ࠦኢ"))):
        return {
            bstack1lllll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤኣ"): bstack1lllll1_opy_ (u"ࠧࡔࡥࡵ࡮࡬ࡪࡾࠨኤ"),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤእ"): env.get(bstack1lllll1_opy_ (u"ࠢࡅࡇࡓࡐࡔ࡟࡟ࡖࡔࡏࠦኦ")),
            bstack1lllll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥኧ"): env.get(bstack1lllll1_opy_ (u"ࠤࡖࡍ࡙ࡋ࡟ࡏࡃࡐࡉࠧከ")),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤኩ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨኪ"))
        }
    if bstack1l11ll1l1_opy_(env.get(bstack1lllll1_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤࡇࡃࡕࡋࡒࡒࡘࠨካ"))):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦኬ"): bstack1lllll1_opy_ (u"ࠢࡈ࡫ࡷࡌࡺࡨࠠࡂࡥࡷ࡭ࡴࡴࡳࠣክ"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦኮ"): bstack1lllll1_opy_ (u"ࠤࡾࢁ࠴ࢁࡽ࠰ࡣࡦࡸ࡮ࡵ࡮ࡴ࠱ࡵࡹࡳࡹ࠯ࡼࡿࠥኯ").format(env.get(bstack1lllll1_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡗࡊࡘࡖࡆࡔࡢ࡙ࡗࡒࠧኰ")), env.get(bstack1lllll1_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡗࡋࡐࡐࡕࡌࡘࡔࡘ࡙ࠨ኱")), env.get(bstack1lllll1_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡕࡏࡡࡌࡈࠬኲ"))),
            bstack1lllll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣኳ"): env.get(bstack1lllll1_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡘࡑࡕࡏࡋࡒࡏࡘࠤኴ")),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢኵ"): env.get(bstack1lllll1_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡࡕ࡙ࡓࡥࡉࡅࠤ኶"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠥࡇࡎࠨ኷")) == bstack1lllll1_opy_ (u"ࠦࡹࡸࡵࡦࠤኸ") and env.get(bstack1lllll1_opy_ (u"ࠧ࡜ࡅࡓࡅࡈࡐࠧኹ")) == bstack1lllll1_opy_ (u"ࠨ࠱ࠣኺ"):
        return {
            bstack1lllll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧኻ"): bstack1lllll1_opy_ (u"ࠣࡘࡨࡶࡨ࡫࡬ࠣኼ"),
            bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧኽ"): bstack1lllll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࡿࢂࠨኾ").format(env.get(bstack1lllll1_opy_ (u"࡛ࠫࡋࡒࡄࡇࡏࡣ࡚ࡘࡌࠨ኿"))),
            bstack1lllll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢዀ"): None,
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ዁"): None,
        }
    if env.get(bstack1lllll1_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡ࡙ࡉࡗ࡙ࡉࡐࡐࠥዂ")):
        return {
            bstack1lllll1_opy_ (u"ࠣࡰࡤࡱࡪࠨዃ"): bstack1lllll1_opy_ (u"ࠤࡗࡩࡦࡳࡣࡪࡶࡼࠦዄ"),
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨዅ"): None,
            bstack1lllll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ዆"): env.get(bstack1lllll1_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡑࡔࡒࡎࡊࡉࡔࡠࡐࡄࡑࡊࠨ዇")),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧወ"): env.get(bstack1lllll1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨዉ"))
        }
    if any([env.get(bstack1lllll1_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࠦዊ")), env.get(bstack1lllll1_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡛ࡒࡍࠤዋ")), env.get(bstack1lllll1_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡔࡇࡕࡒࡆࡓࡅࠣዌ")), env.get(bstack1lllll1_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡕࡇࡄࡑࠧው"))]):
        return {
            bstack1lllll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥዎ"): bstack1lllll1_opy_ (u"ࠨࡃࡰࡰࡦࡳࡺࡸࡳࡦࠤዏ"),
            bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥዐ"): None,
            bstack1lllll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥዑ"): env.get(bstack1lllll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥዒ")) or None,
            bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤዓ"): env.get(bstack1lllll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡍࡉࠨዔ"), 0)
        }
    if env.get(bstack1lllll1_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥዕ")):
        return {
            bstack1lllll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦዖ"): bstack1lllll1_opy_ (u"ࠢࡈࡱࡆࡈࠧ዗"),
            bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦዘ"): None,
            bstack1lllll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦዙ"): env.get(bstack1lllll1_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣዚ")),
            bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥዛ"): env.get(bstack1lllll1_opy_ (u"ࠧࡍࡏࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡇࡔ࡛ࡎࡕࡇࡕࠦዜ"))
        }
    if env.get(bstack1lllll1_opy_ (u"ࠨࡃࡇࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦዝ")):
        return {
            bstack1lllll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧዞ"): bstack1lllll1_opy_ (u"ࠣࡅࡲࡨࡪࡌࡲࡦࡵ࡫ࠦዟ"),
            bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧዠ"): env.get(bstack1lllll1_opy_ (u"ࠥࡇࡋࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤዡ")),
            bstack1lllll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨዢ"): env.get(bstack1lllll1_opy_ (u"ࠧࡉࡆࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡒࡆࡓࡅࠣዣ")),
            bstack1lllll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧዤ"): env.get(bstack1lllll1_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧዥ"))
        }
    return {bstack1lllll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢዦ"): None}
def get_host_info():
    return {
        bstack1lllll1_opy_ (u"ࠤ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠦዧ"): platform.node(),
        bstack1lllll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧየ"): platform.system(),
        bstack1lllll1_opy_ (u"ࠦࡹࡿࡰࡦࠤዩ"): platform.machine(),
        bstack1lllll1_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨዪ"): platform.version(),
        bstack1lllll1_opy_ (u"ࠨࡡࡳࡥ࡫ࠦያ"): platform.architecture()[0]
    }
def bstack111l11l11_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111l1l111l_opy_():
    if bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨዬ")):
        return bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧይ")
    return bstack1lllll1_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠨዮ")
def bstack11l1111lll_opy_(driver):
    info = {
        bstack1lllll1_opy_ (u"ࠪࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩዯ"): driver.capabilities,
        bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠨደ"): driver.session_id,
        bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ዱ"): driver.capabilities.get(bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫዲ"), None),
        bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩዳ"): driver.capabilities.get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩዴ"), None),
        bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࠫድ"): driver.capabilities.get(bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩዶ"), None),
    }
    if bstack111l1l111l_opy_() == bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪዷ"):
        info[bstack1lllll1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ዸ")] = bstack1lllll1_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬዹ") if bstack1lll11ll11_opy_() else bstack1lllll1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩዺ")
    return info
def bstack1lll11ll11_opy_():
    if bstack1111ll1ll_opy_.get_property(bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧዻ")):
        return True
    if bstack1l11ll1l1_opy_(os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪዼ"), None)):
        return True
    return False
def bstack1ll1ll1l1_opy_(bstack111l1l11ll_opy_, url, data, config):
    headers = config.get(bstack1lllll1_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫዽ"), None)
    proxies = bstack1l11111ll_opy_(config, url)
    auth = config.get(bstack1lllll1_opy_ (u"ࠫࡦࡻࡴࡩࠩዾ"), None)
    response = requests.request(
            bstack111l1l11ll_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l11l11ll1_opy_(bstack1llll1111_opy_, size):
    bstack111l11ll_opy_ = []
    while len(bstack1llll1111_opy_) > size:
        bstack1l11111l1_opy_ = bstack1llll1111_opy_[:size]
        bstack111l11ll_opy_.append(bstack1l11111l1_opy_)
        bstack1llll1111_opy_ = bstack1llll1111_opy_[size:]
    bstack111l11ll_opy_.append(bstack1llll1111_opy_)
    return bstack111l11ll_opy_
def bstack111ll11111_opy_(message, bstack11l111l1ll_opy_=False):
    os.write(1, bytes(message, bstack1lllll1_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫዿ")))
    os.write(1, bytes(bstack1lllll1_opy_ (u"࠭࡜࡯ࠩጀ"), bstack1lllll1_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ጁ")))
    if bstack11l111l1ll_opy_:
        with open(bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮ࡱ࠴࠵ࡾ࠳ࠧጂ") + os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠨጃ")] + bstack1lllll1_opy_ (u"ࠪ࠲ࡱࡵࡧࠨጄ"), bstack1lllll1_opy_ (u"ࠫࡦ࠭ጅ")) as f:
            f.write(message + bstack1lllll1_opy_ (u"ࠬࡢ࡮ࠨጆ"))
def bstack111l1l1l1l_opy_():
    return os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩጇ")].lower() == bstack1lllll1_opy_ (u"ࠧࡵࡴࡸࡩࠬገ")
def bstack1l111l1l1_opy_(bstack11l111l111_opy_):
    return bstack1lllll1_opy_ (u"ࠨࡽࢀ࠳ࢀࢃࠧጉ").format(bstack11l11l1ll1_opy_, bstack11l111l111_opy_)
def bstack1l1llll1_opy_():
    return bstack11lllllll1_opy_().replace(tzinfo=None).isoformat() + bstack1lllll1_opy_ (u"ࠩ࡝ࠫጊ")
def bstack11l111111l_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1lllll1_opy_ (u"ࠪ࡞ࠬጋ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1lllll1_opy_ (u"ࠫ࡟࠭ጌ")))).total_seconds() * 1000
def bstack111ll1ll11_opy_(timestamp):
    return bstack111ll111ll_opy_(timestamp).isoformat() + bstack1lllll1_opy_ (u"ࠬࡠࠧግ")
def bstack111lll11l1_opy_(bstack111lll1lll_opy_):
    date_format = bstack1lllll1_opy_ (u"࡚࠭ࠥࠧࡰࠩࡩࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠫጎ")
    bstack111l111l1l_opy_ = datetime.datetime.strptime(bstack111lll1lll_opy_, date_format)
    return bstack111l111l1l_opy_.isoformat() + bstack1lllll1_opy_ (u"࡛ࠧࠩጏ")
def bstack111llll1l1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1lllll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨጐ")
    else:
        return bstack1lllll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ጑")
def bstack1l11ll1l1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1lllll1_opy_ (u"ࠪࡸࡷࡻࡥࠨጒ")
def bstack111l111111_opy_(val):
    return val.__str__().lower() == bstack1lllll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪጓ")
def bstack1l1111l111_opy_(bstack111l1lll11_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack111l1lll11_opy_ as e:
                print(bstack1lllll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧጔ").format(func.__name__, bstack111l1lll11_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111lll11ll_opy_(bstack111ll11l1l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111ll11l1l_opy_(cls, *args, **kwargs)
            except bstack111l1lll11_opy_ as e:
                print(bstack1lllll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨጕ").format(bstack111ll11l1l_opy_.__name__, bstack111l1lll11_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111lll11ll_opy_
    else:
        return decorator
def bstack11ll1l111_opy_(bstack11ll11l111_opy_):
    if bstack1lllll1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ጖") in bstack11ll11l111_opy_ and bstack111l111111_opy_(bstack11ll11l111_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ጗")]):
        return False
    if bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫጘ") in bstack11ll11l111_opy_ and bstack111l111111_opy_(bstack11ll11l111_opy_[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬጙ")]):
        return False
    return True
def bstack11lll1ll1_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack1lllll1ll_opy_(hub_url):
    if bstack1ll11lll11_opy_() <= version.parse(bstack1lllll1_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫጚ")):
        if hub_url != bstack1lllll1_opy_ (u"ࠬ࠭ጛ"):
            return bstack1lllll1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢጜ") + hub_url + bstack1lllll1_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦጝ")
        return bstack1lll11ll1_opy_
    if hub_url != bstack1lllll1_opy_ (u"ࠨࠩጞ"):
        return bstack1lllll1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦጟ") + hub_url + bstack1lllll1_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦጠ")
    return bstack111ll1l1l_opy_
def bstack111l1l1lll_opy_():
    return isinstance(os.getenv(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪጡ")), str)
def bstack1llll1l1_opy_(url):
    return urlparse(url).hostname
def bstack1l1l1ll1_opy_(hostname):
    for bstack1ll11l1l_opy_ in bstack1ll111lll1_opy_:
        regex = re.compile(bstack1ll11l1l_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack111l1l1ll1_opy_(bstack111ll1l1ll_opy_, file_name, logger):
    bstack1l111l11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠬࢄࠧጢ")), bstack111ll1l1ll_opy_)
    try:
        if not os.path.exists(bstack1l111l11_opy_):
            os.makedirs(bstack1l111l11_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"࠭ࡾࠨጣ")), bstack111ll1l1ll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1lllll1_opy_ (u"ࠧࡸࠩጤ")):
                pass
            with open(file_path, bstack1lllll1_opy_ (u"ࠣࡹ࠮ࠦጥ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1lll1ll111_opy_.format(str(e)))
def bstack111l1lll1l_opy_(file_name, key, value, logger):
    file_path = bstack111l1l1ll1_opy_(bstack1lllll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩጦ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111111111_opy_ = json.load(open(file_path, bstack1lllll1_opy_ (u"ࠪࡶࡧ࠭ጧ")))
        else:
            bstack111111111_opy_ = {}
        bstack111111111_opy_[key] = value
        with open(file_path, bstack1lllll1_opy_ (u"ࠦࡼ࠱ࠢጨ")) as outfile:
            json.dump(bstack111111111_opy_, outfile)
def bstack1l1lllllll_opy_(file_name, logger):
    file_path = bstack111l1l1ll1_opy_(bstack1lllll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬጩ"), file_name, logger)
    bstack111111111_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1lllll1_opy_ (u"࠭ࡲࠨጪ")) as bstack1llllll11_opy_:
            bstack111111111_opy_ = json.load(bstack1llllll11_opy_)
    return bstack111111111_opy_
def bstack1lll1lll11_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤ࡫࡯࡬ࡦ࠼ࠣࠫጫ") + file_path + bstack1lllll1_opy_ (u"ࠨࠢࠪጬ") + str(e))
def bstack1ll11lll11_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1lllll1_opy_ (u"ࠤ࠿ࡒࡔ࡚ࡓࡆࡖࡁࠦጭ")
def bstack1ll1l1lll1_opy_(config):
    if bstack1lllll1_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩጮ") in config:
        del (config[bstack1lllll1_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪጯ")])
        return False
    if bstack1ll11lll11_opy_() < version.parse(bstack1lllll1_opy_ (u"ࠬ࠹࠮࠵࠰࠳ࠫጰ")):
        return False
    if bstack1ll11lll11_opy_() >= version.parse(bstack1lllll1_opy_ (u"࠭࠴࠯࠳࠱࠹ࠬጱ")):
        return True
    if bstack1lllll1_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧጲ") in config and config[bstack1lllll1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨጳ")] is False:
        return False
    else:
        return True
def bstack11l1111l1_opy_(args_list, bstack111ll1ll1l_opy_):
    index = -1
    for value in bstack111ll1ll1l_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack11lll1l111_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack11lll1l111_opy_ = bstack11lll1l111_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1lllll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩጴ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1lllll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪጵ"), exception=exception)
    def bstack11ll111lll_opy_(self):
        if self.result != bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫጶ"):
            return None
        if bstack1lllll1_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣጷ") in self.exception_type:
            return bstack1lllll1_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢጸ")
        return bstack1lllll1_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣጹ")
    def bstack11l1111l11_opy_(self):
        if self.result != bstack1lllll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨጺ"):
            return None
        if self.bstack11lll1l111_opy_:
            return self.bstack11lll1l111_opy_
        return bstack11l1111ll1_opy_(self.exception)
def bstack11l1111ll1_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111ll1l11l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1111l1l11_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack111lll1l_opy_(config, logger):
    try:
        import playwright
        bstack11l1111111_opy_ = playwright.__file__
        bstack111lll1l11_opy_ = os.path.split(bstack11l1111111_opy_)
        bstack111lll1111_opy_ = bstack111lll1l11_opy_[0] + bstack1lllll1_opy_ (u"ࠩ࠲ࡨࡷ࡯ࡶࡦࡴ࠲ࡴࡦࡩ࡫ࡢࡩࡨ࠳ࡱ࡯ࡢ࠰ࡥ࡯࡭࠴ࡩ࡬ࡪ࠰࡭ࡷࠬጻ")
        os.environ[bstack1lllll1_opy_ (u"ࠪࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠭ጼ")] = bstack1ll11lll1_opy_(config)
        with open(bstack111lll1111_opy_, bstack1lllll1_opy_ (u"ࠫࡷ࠭ጽ")) as f:
            bstack1lllll1ll1_opy_ = f.read()
            bstack111lllll11_opy_ = bstack1lllll1_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫጾ")
            bstack1111llllll_opy_ = bstack1lllll1ll1_opy_.find(bstack111lllll11_opy_)
            if bstack1111llllll_opy_ == -1:
              process = subprocess.Popen(bstack1lllll1_opy_ (u"ࠨ࡮ࡱ࡯ࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠥጿ"), shell=True, cwd=bstack111lll1l11_opy_[0])
              process.wait()
              bstack111l1l1111_opy_ = bstack1lllll1_opy_ (u"ࠧࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࠧࡁࠧፀ")
              bstack111l1111l1_opy_ = bstack1lllll1_opy_ (u"ࠣࠤࠥࠤࡡࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶ࡟ࠦࡀࠦࡣࡰࡰࡶࡸࠥࢁࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠣࢁࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨࠫ࠾ࠤ࡮࡬ࠠࠩࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡨࡲࡻ࠴ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠫࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠮ࠩ࠼ࠢࠥࠦࠧፁ")
              bstack111ll1lll1_opy_ = bstack1lllll1ll1_opy_.replace(bstack111l1l1111_opy_, bstack111l1111l1_opy_)
              with open(bstack111lll1111_opy_, bstack1lllll1_opy_ (u"ࠩࡺࠫፂ")) as f:
                f.write(bstack111ll1lll1_opy_)
    except Exception as e:
        logger.error(bstack1l11lll1l_opy_.format(str(e)))
def bstack1lll111l1_opy_():
  try:
    bstack11l1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪፃ"))
    bstack111ll1llll_opy_ = []
    if os.path.exists(bstack11l1111l1l_opy_):
      with open(bstack11l1111l1l_opy_) as f:
        bstack111ll1llll_opy_ = json.load(f)
      os.remove(bstack11l1111l1l_opy_)
    return bstack111ll1llll_opy_
  except:
    pass
  return []
def bstack1lll11l11l_opy_(bstack1l1l1lll11_opy_):
  try:
    bstack111ll1llll_opy_ = []
    bstack11l1111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫፄ"))
    if os.path.exists(bstack11l1111l1l_opy_):
      with open(bstack11l1111l1l_opy_) as f:
        bstack111ll1llll_opy_ = json.load(f)
    bstack111ll1llll_opy_.append(bstack1l1l1lll11_opy_)
    with open(bstack11l1111l1l_opy_, bstack1lllll1_opy_ (u"ࠬࡽࠧፅ")) as f:
        json.dump(bstack111ll1llll_opy_, f)
  except:
    pass
def bstack1l1ll1ll1l_opy_(logger, bstack111l1ll11l_opy_ = False):
  try:
    test_name = os.environ.get(bstack1lllll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩፆ"), bstack1lllll1_opy_ (u"ࠧࠨፇ"))
    if test_name == bstack1lllll1_opy_ (u"ࠨࠩፈ"):
        test_name = threading.current_thread().__dict__.get(bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡄࡧࡨࡤࡺࡥࡴࡶࡢࡲࡦࡳࡥࠨፉ"), bstack1lllll1_opy_ (u"ࠪࠫፊ"))
    bstack111lll1l1l_opy_ = bstack1lllll1_opy_ (u"ࠫ࠱ࠦࠧፋ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111l1ll11l_opy_:
        bstack1l1llll11_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬፌ"), bstack1lllll1_opy_ (u"࠭࠰ࠨፍ"))
        bstack1l1l1ll111_opy_ = {bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬፎ"): test_name, bstack1lllll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧፏ"): bstack111lll1l1l_opy_, bstack1lllll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨፐ"): bstack1l1llll11_opy_}
        bstack11l111l11l_opy_ = []
        bstack111lll111l_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩፑ"))
        if os.path.exists(bstack111lll111l_opy_):
            with open(bstack111lll111l_opy_) as f:
                bstack11l111l11l_opy_ = json.load(f)
        bstack11l111l11l_opy_.append(bstack1l1l1ll111_opy_)
        with open(bstack111lll111l_opy_, bstack1lllll1_opy_ (u"ࠫࡼ࠭ፒ")) as f:
            json.dump(bstack11l111l11l_opy_, f)
    else:
        bstack1l1l1ll111_opy_ = {bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪፓ"): test_name, bstack1lllll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬፔ"): bstack111lll1l1l_opy_, bstack1lllll1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ፕ"): str(multiprocessing.current_process().name)}
        if bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬፖ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l1l1ll111_opy_)
  except Exception as e:
      logger.warn(bstack1lllll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡵࡿࡴࡦࡵࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨፗ").format(e))
def bstack1ll111l1l_opy_(error_message, test_name, index, logger):
  try:
    bstack111ll11lll_opy_ = []
    bstack1l1l1ll111_opy_ = {bstack1lllll1_opy_ (u"ࠪࡲࡦࡳࡥࠨፘ"): test_name, bstack1lllll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪፙ"): error_message, bstack1lllll1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫፚ"): index}
    bstack111llll111_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ፛"))
    if os.path.exists(bstack111llll111_opy_):
        with open(bstack111llll111_opy_) as f:
            bstack111ll11lll_opy_ = json.load(f)
    bstack111ll11lll_opy_.append(bstack1l1l1ll111_opy_)
    with open(bstack111llll111_opy_, bstack1lllll1_opy_ (u"ࠧࡸࠩ፜")) as f:
        json.dump(bstack111ll11lll_opy_, f)
  except Exception as e:
    logger.warn(bstack1lllll1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡶࡴࡨ࡯ࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦ፝").format(e))
def bstack1l1ll1ll11_opy_(bstack1l1l1ll11_opy_, name, logger):
  try:
    bstack1l1l1ll111_opy_ = {bstack1lllll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ፞"): name, bstack1lllll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ፟"): bstack1l1l1ll11_opy_, bstack1lllll1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ፠"): str(threading.current_thread()._name)}
    return bstack1l1l1ll111_opy_
  except Exception as e:
    logger.warn(bstack1lllll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡧࡷࡱࡲࡪࡲࠠࡥࡣࡷࡥ࠿ࠦࡻࡾࠤ፡").format(e))
  return
def bstack11l11111ll_opy_():
    return platform.system() == bstack1lllll1_opy_ (u"࠭ࡗࡪࡰࡧࡳࡼࡹࠧ።")
def bstack1l1111ll1_opy_(bstack111lllll1l_opy_, config, logger):
    bstack111l11lll1_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack111lllll1l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪ࡮ࡲࡴࡦࡴࠣࡧࡴࡴࡦࡪࡩࠣ࡯ࡪࡿࡳࠡࡤࡼࠤࡷ࡫ࡧࡦࡺࠣࡱࡦࡺࡣࡩ࠼ࠣࡿࢂࠨ፣").format(e))
    return bstack111l11lll1_opy_
def bstack111l11llll_opy_(bstack111llll1ll_opy_, bstack111l11ll1l_opy_):
    bstack111l11l1ll_opy_ = version.parse(bstack111llll1ll_opy_)
    bstack11l11111l1_opy_ = version.parse(bstack111l11ll1l_opy_)
    if bstack111l11l1ll_opy_ > bstack11l11111l1_opy_:
        return 1
    elif bstack111l11l1ll_opy_ < bstack11l11111l1_opy_:
        return -1
    else:
        return 0
def bstack11lllllll1_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack111ll111ll_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111l11l111_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack1ll1l11l11_opy_(options, framework):
    if options is None:
        return
    if getattr(options, bstack1lllll1_opy_ (u"ࠨࡩࡨࡸࠬ፤"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack1llll11ll_opy_ = caps.get(bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ፥"))
    bstack111l111lll_opy_ = True
    if bstack111l111111_opy_(caps.get(bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪ࡝࠳ࡄࠩ፦"))) or bstack111l111111_opy_(caps.get(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫ፧"))):
        bstack111l111lll_opy_ = False
    if bstack1ll1l1lll1_opy_({bstack1lllll1_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧ፨"): bstack111l111lll_opy_}):
        bstack1llll11ll_opy_ = bstack1llll11ll_opy_ or {}
        bstack1llll11ll_opy_[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ፩")] = bstack111l11l111_opy_(framework)
        bstack1llll11ll_opy_[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ፪")] = bstack111l1l1l1l_opy_()
        if getattr(options, bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩ፫"), None):
            options.set_capability(bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ፬"), bstack1llll11ll_opy_)
        else:
            options[bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ፭")] = bstack1llll11ll_opy_
    else:
        if getattr(options, bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬ፮"), None):
            options.set_capability(bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭፯"), bstack111l11l111_opy_(framework))
            options.set_capability(bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧ፰"), bstack111l1l1l1l_opy_())
        else:
            options[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ፱")] = bstack111l11l111_opy_(framework)
            options[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠩ፲")] = bstack111l1l1l1l_opy_()
    return options
def bstack111ll1l111_opy_(bstack11l111l1l1_opy_, framework):
    if bstack11l111l1l1_opy_ and len(bstack11l111l1l1_opy_.split(bstack1lllll1_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨ፳"))) > 1:
        ws_url = bstack11l111l1l1_opy_.split(bstack1lllll1_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩ፴"))[0]
        if bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧ፵") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111ll11l11_opy_ = json.loads(urllib.parse.unquote(bstack11l111l1l1_opy_.split(bstack1lllll1_opy_ (u"ࠬࡩࡡࡱࡵࡀࠫ፶"))[1]))
            bstack111ll11l11_opy_ = bstack111ll11l11_opy_ or {}
            bstack111ll11l11_opy_[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ፷")] = str(framework) + str(__version__)
            bstack111ll11l11_opy_[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ፸")] = bstack111l1l1l1l_opy_()
            bstack11l111l1l1_opy_ = bstack11l111l1l1_opy_.split(bstack1lllll1_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧ፹"))[0] + bstack1lllll1_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨ፺") + urllib.parse.quote(json.dumps(bstack111ll11l11_opy_))
    return bstack11l111l1l1_opy_
def bstack1l1ll11ll_opy_():
    global bstack1lll1l11l1_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1lll1l11l1_opy_ = BrowserType.connect
    return bstack1lll1l11l1_opy_
def bstack11l1l1lll_opy_(framework_name):
    global bstack1ll11l1l1l_opy_
    bstack1ll11l1l1l_opy_ = framework_name
    return framework_name
def bstack11111l1l1_opy_(self, *args, **kwargs):
    global bstack1lll1l11l1_opy_
    try:
        global bstack1ll11l1l1l_opy_
        if bstack1lllll1_opy_ (u"ࠪࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺࠧ፻") in kwargs:
            kwargs[bstack1lllll1_opy_ (u"ࠫࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴࠨ፼")] = bstack111ll1l111_opy_(
                kwargs.get(bstack1lllll1_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩ፽"), None),
                bstack1ll11l1l1l_opy_
            )
    except Exception as e:
        logger.error(bstack1lllll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡨࡧࡰࡴ࠼ࠣࡿࢂࠨ፾").format(str(e)))
    return bstack1lll1l11l1_opy_(self, *args, **kwargs)