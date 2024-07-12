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
from urllib.parse import urlparse
from bstack_utils.messages import bstack1111l1111l_opy_
def bstack1llll1ll11l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1llll1ll111_opy_(bstack1llll1l1lll_opy_, bstack1llll1l11ll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1llll1l1lll_opy_):
        with open(bstack1llll1l1lll_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1llll1ll11l_opy_(bstack1llll1l1lll_opy_):
        pac = get_pac(url=bstack1llll1l1lll_opy_)
    else:
        raise Exception(bstack1lllll1_opy_ (u"ࠬࡖࡡࡤࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠻ࠢࡾࢁࠬᒇ").format(bstack1llll1l1lll_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1lllll1_opy_ (u"ࠨ࠸࠯࠺࠱࠼࠳࠾ࠢᒈ"), 80))
        bstack1llll1l1l1l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1llll1l1l1l_opy_ = bstack1lllll1_opy_ (u"ࠧ࠱࠰࠳࠲࠵࠴࠰ࠨᒉ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1llll1l11ll_opy_, bstack1llll1l1l1l_opy_)
    return proxy_url
def bstack1lll11l11_opy_(config):
    return bstack1lllll1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᒊ") in config or bstack1lllll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᒋ") in config
def bstack1ll11lll1_opy_(config):
    if not bstack1lll11l11_opy_(config):
        return
    if config.get(bstack1lllll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᒌ")):
        return config.get(bstack1lllll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᒍ"))
    if config.get(bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᒎ")):
        return config.get(bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᒏ"))
def bstack1l11111ll_opy_(config, bstack1llll1l11ll_opy_):
    proxy = bstack1ll11lll1_opy_(config)
    proxies = {}
    if config.get(bstack1lllll1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᒐ")) or config.get(bstack1lllll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᒑ")):
        if proxy.endswith(bstack1lllll1_opy_ (u"ࠩ࠱ࡴࡦࡩࠧᒒ")):
            proxies = bstack1llllllll_opy_(proxy, bstack1llll1l11ll_opy_)
        else:
            proxies = {
                bstack1lllll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᒓ"): proxy
            }
    return proxies
def bstack1llllllll_opy_(bstack1llll1l1lll_opy_, bstack1llll1l11ll_opy_):
    proxies = {}
    global bstack1llll1l1l11_opy_
    if bstack1lllll1_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧᒔ") in globals():
        return bstack1llll1l1l11_opy_
    try:
        proxy = bstack1llll1ll111_opy_(bstack1llll1l1lll_opy_, bstack1llll1l11ll_opy_)
        if bstack1lllll1_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧᒕ") in proxy:
            proxies = {}
        elif bstack1lllll1_opy_ (u"ࠨࡈࡕࡖࡓࠦᒖ") in proxy or bstack1lllll1_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨᒗ") in proxy or bstack1lllll1_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢᒘ") in proxy:
            bstack1llll1l1ll1_opy_ = proxy.split(bstack1lllll1_opy_ (u"ࠤࠣࠦᒙ"))
            if bstack1lllll1_opy_ (u"ࠥ࠾࠴࠵ࠢᒚ") in bstack1lllll1_opy_ (u"ࠦࠧᒛ").join(bstack1llll1l1ll1_opy_[1:]):
                proxies = {
                    bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᒜ"): bstack1lllll1_opy_ (u"ࠨࠢᒝ").join(bstack1llll1l1ll1_opy_[1:])
                }
            else:
                proxies = {
                    bstack1lllll1_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᒞ"): str(bstack1llll1l1ll1_opy_[0]).lower() + bstack1lllll1_opy_ (u"ࠣ࠼࠲࠳ࠧᒟ") + bstack1lllll1_opy_ (u"ࠤࠥᒠ").join(bstack1llll1l1ll1_opy_[1:])
                }
        elif bstack1lllll1_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤᒡ") in proxy:
            bstack1llll1l1ll1_opy_ = proxy.split(bstack1lllll1_opy_ (u"ࠦࠥࠨᒢ"))
            if bstack1lllll1_opy_ (u"ࠧࡀ࠯࠰ࠤᒣ") in bstack1lllll1_opy_ (u"ࠨࠢᒤ").join(bstack1llll1l1ll1_opy_[1:]):
                proxies = {
                    bstack1lllll1_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᒥ"): bstack1lllll1_opy_ (u"ࠣࠤᒦ").join(bstack1llll1l1ll1_opy_[1:])
                }
            else:
                proxies = {
                    bstack1lllll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᒧ"): bstack1lllll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᒨ") + bstack1lllll1_opy_ (u"ࠦࠧᒩ").join(bstack1llll1l1ll1_opy_[1:])
                }
        else:
            proxies = {
                bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᒪ"): proxy
            }
    except Exception as e:
        print(bstack1lllll1_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥᒫ"), bstack1111l1111l_opy_.format(bstack1llll1l1lll_opy_, str(e)))
    bstack1llll1l1l11_opy_ = proxies
    return proxies