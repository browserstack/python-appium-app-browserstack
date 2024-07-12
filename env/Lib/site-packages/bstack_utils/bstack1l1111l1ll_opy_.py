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
from uuid import uuid4
from bstack_utils.helper import bstack1l1llll1_opy_, bstack11l111111l_opy_
from bstack_utils.bstack1ll1lll111_opy_ import bstack1llll11l11l_opy_
class bstack11llllllll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack11llll1111_opy_=None, framework=None, tags=[], scope=[], bstack1lll1l11l11_opy_=None, bstack1lll1l1l111_opy_=True, bstack1lll1l1l11l_opy_=None, bstack11111ll11_opy_=None, result=None, duration=None, bstack11ll1lll1l_opy_=None, meta={}):
        self.bstack11ll1lll1l_opy_ = bstack11ll1lll1l_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1lll1l1l111_opy_:
            self.uuid = uuid4().__str__()
        self.bstack11llll1111_opy_ = bstack11llll1111_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1lll1l11l11_opy_ = bstack1lll1l11l11_opy_
        self.bstack1lll1l1l11l_opy_ = bstack1lll1l1l11l_opy_
        self.bstack11111ll11_opy_ = bstack11111ll11_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack1l11111l1l_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack1lll1l111l1_opy_(self):
        bstack1lll1ll1111_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1lllll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᔕ"): bstack1lll1ll1111_opy_,
            bstack1lllll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᔖ"): bstack1lll1ll1111_opy_,
            bstack1lllll1_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᔗ"): bstack1lll1ll1111_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1lllll1_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦᔘ") + key)
            setattr(self, key, val)
    def bstack1lll1l1ll1l_opy_(self):
        return {
            bstack1lllll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᔙ"): self.name,
            bstack1lllll1_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᔚ"): {
                bstack1lllll1_opy_ (u"࠭࡬ࡢࡰࡪࠫᔛ"): bstack1lllll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᔜ"),
                bstack1lllll1_opy_ (u"ࠨࡥࡲࡨࡪ࠭ᔝ"): self.code
            },
            bstack1lllll1_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᔞ"): self.scope,
            bstack1lllll1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᔟ"): self.tags,
            bstack1lllll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᔠ"): self.framework,
            bstack1lllll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᔡ"): self.bstack11llll1111_opy_
        }
    def bstack1lll1l111ll_opy_(self):
        return {
         bstack1lllll1_opy_ (u"࠭࡭ࡦࡶࡤࠫᔢ"): self.meta
        }
    def bstack1lll1l1l1ll_opy_(self):
        return {
            bstack1lllll1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪᔣ"): {
                bstack1lllll1_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬᔤ"): self.bstack1lll1l11l11_opy_
            }
        }
    def bstack1lll1l1llll_opy_(self, bstack1lll1l11111_opy_, details):
        step = next(filter(lambda st: st[bstack1lllll1_opy_ (u"ࠩ࡬ࡨࠬᔥ")] == bstack1lll1l11111_opy_, self.meta[bstack1lllll1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᔦ")]), None)
        step.update(details)
    def bstack1lll11llll1_opy_(self, bstack1lll1l11111_opy_):
        step = next(filter(lambda st: st[bstack1lllll1_opy_ (u"ࠫ࡮ࡪࠧᔧ")] == bstack1lll1l11111_opy_, self.meta[bstack1lllll1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᔨ")]), None)
        step.update({
            bstack1lllll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᔩ"): bstack1l1llll1_opy_()
        })
    def bstack11lll1l1ll_opy_(self, bstack1lll1l11111_opy_, result, duration=None):
        bstack1lll1l1l11l_opy_ = bstack1l1llll1_opy_()
        if bstack1lll1l11111_opy_ is not None and self.meta.get(bstack1lllll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᔪ")):
            step = next(filter(lambda st: st[bstack1lllll1_opy_ (u"ࠨ࡫ࡧࠫᔫ")] == bstack1lll1l11111_opy_, self.meta[bstack1lllll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᔬ")]), None)
            step.update({
                bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᔭ"): bstack1lll1l1l11l_opy_,
                bstack1lllll1_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ᔮ"): duration if duration else bstack11l111111l_opy_(step[bstack1lllll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᔯ")], bstack1lll1l1l11l_opy_),
                bstack1lllll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᔰ"): result.result,
                bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᔱ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1lll1l1lll1_opy_):
        if self.meta.get(bstack1lllll1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᔲ")):
            self.meta[bstack1lllll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᔳ")].append(bstack1lll1l1lll1_opy_)
        else:
            self.meta[bstack1lllll1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᔴ")] = [ bstack1lll1l1lll1_opy_ ]
    def bstack1lll1l1ll11_opy_(self):
        return {
            bstack1lllll1_opy_ (u"ࠫࡺࡻࡩࡥࠩᔵ"): self.bstack1l11111l1l_opy_(),
            **self.bstack1lll1l1ll1l_opy_(),
            **self.bstack1lll1l111l1_opy_(),
            **self.bstack1lll1l111ll_opy_()
        }
    def bstack1lll1l11lll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᔶ"): self.bstack1lll1l1l11l_opy_,
            bstack1lllll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᔷ"): self.duration,
            bstack1lllll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᔸ"): self.result.result
        }
        if data[bstack1lllll1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᔹ")] == bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᔺ"):
            data[bstack1lllll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᔻ")] = self.result.bstack11ll111lll_opy_()
            data[bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᔼ")] = [{bstack1lllll1_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᔽ"): self.result.bstack11l1111l11_opy_()}]
        return data
    def bstack1lll1l11l1l_opy_(self):
        return {
            bstack1lllll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᔾ"): self.bstack1l11111l1l_opy_(),
            **self.bstack1lll1l1ll1l_opy_(),
            **self.bstack1lll1l111l1_opy_(),
            **self.bstack1lll1l11lll_opy_(),
            **self.bstack1lll1l111ll_opy_()
        }
    def bstack1l111l1111_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1lllll1_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨᔿ") in event:
            return self.bstack1lll1l1ll11_opy_()
        elif bstack1lllll1_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᕀ") in event:
            return self.bstack1lll1l11l1l_opy_()
    def bstack11lllll111_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1lll1l1l11l_opy_ = time if time else bstack1l1llll1_opy_()
        self.duration = duration if duration else bstack11l111111l_opy_(self.bstack11llll1111_opy_, self.bstack1lll1l1l11l_opy_)
        if result:
            self.result = result
class bstack1l11111l11_opy_(bstack11llllllll_opy_):
    def __init__(self, hooks=[], bstack1l11111111_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l11111111_opy_ = bstack1l11111111_opy_
        super().__init__(*args, **kwargs, bstack11111ll11_opy_=bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺࠧᕁ"))
    @classmethod
    def bstack1lll1l1l1l1_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1lllll1_opy_ (u"ࠪ࡭ࡩ࠭ᕂ"): id(step),
                bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡸࡵࠩᕃ"): step.name,
                bstack1lllll1_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ᕄ"): step.keyword,
            })
        return bstack1l11111l11_opy_(
            **kwargs,
            meta={
                bstack1lllll1_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧᕅ"): {
                    bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᕆ"): feature.name,
                    bstack1lllll1_opy_ (u"ࠨࡲࡤࡸ࡭࠭ᕇ"): feature.filename,
                    bstack1lllll1_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧᕈ"): feature.description
                },
                bstack1lllll1_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬᕉ"): {
                    bstack1lllll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᕊ"): scenario.name
                },
                bstack1lllll1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᕋ"): steps,
                bstack1lllll1_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨᕌ"): bstack1llll11l11l_opy_(test)
            }
        )
    def bstack1lll11lllll_opy_(self):
        return {
            bstack1lllll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᕍ"): self.hooks
        }
    def bstack1lll1l11ll1_opy_(self):
        if self.bstack1l11111111_opy_:
            return {
                bstack1lllll1_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧᕎ"): self.bstack1l11111111_opy_
            }
        return {}
    def bstack1lll1l11l1l_opy_(self):
        return {
            **super().bstack1lll1l11l1l_opy_(),
            **self.bstack1lll11lllll_opy_()
        }
    def bstack1lll1l1ll11_opy_(self):
        return {
            **super().bstack1lll1l1ll11_opy_(),
            **self.bstack1lll1l11ll1_opy_()
        }
    def bstack11lllll111_opy_(self):
        return bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫᕏ")
class bstack1l111l11ll_opy_(bstack11llllllll_opy_):
    def __init__(self, hook_type, *args, **kwargs):
        self.hook_type = hook_type
        super().__init__(*args, **kwargs, bstack11111ll11_opy_=bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᕐ"))
    def bstack11llllll1l_opy_(self):
        return self.hook_type
    def bstack1lll1l1111l_opy_(self):
        return {
            bstack1lllll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᕑ"): self.hook_type
        }
    def bstack1lll1l11l1l_opy_(self):
        return {
            **super().bstack1lll1l11l1l_opy_(),
            **self.bstack1lll1l1111l_opy_()
        }
    def bstack1lll1l1ll11_opy_(self):
        return {
            **super().bstack1lll1l1ll11_opy_(),
            **self.bstack1lll1l1111l_opy_()
        }
    def bstack11lllll111_opy_(self):
        return bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧᕒ")