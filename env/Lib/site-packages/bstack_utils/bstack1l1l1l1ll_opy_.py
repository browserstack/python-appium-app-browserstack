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
import json
class bstack11l1l1111l_opy_(object):
  bstack1l111l11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠪࢂࠬ།")), bstack1lllll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ༎"))
  bstack11l1l111ll_opy_ = os.path.join(bstack1l111l11_opy_, bstack1lllll1_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹ࠮࡫ࡵࡲࡲࠬ༏"))
  bstack11l1l11ll1_opy_ = None
  perform_scan = None
  bstack1lllll11ll_opy_ = None
  bstack11l111ll1_opy_ = None
  bstack11l1l1l1ll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1lllll1_opy_ (u"࠭ࡩ࡯ࡵࡷࡥࡳࡩࡥࠨ༐")):
      cls.instance = super(bstack11l1l1111l_opy_, cls).__new__(cls)
      cls.instance.bstack11l1l11l11_opy_()
    return cls.instance
  def bstack11l1l11l11_opy_(self):
    try:
      with open(self.bstack11l1l111ll_opy_, bstack1lllll1_opy_ (u"ࠧࡳࠩ༑")) as bstack1llllll11_opy_:
        bstack11l1l11l1l_opy_ = bstack1llllll11_opy_.read()
        data = json.loads(bstack11l1l11l1l_opy_)
        if bstack1lllll1_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ༒") in data:
          self.bstack11l1l1l111_opy_(data[bstack1lllll1_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫ༓")])
        if bstack1lllll1_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫ༔") in data:
          self.bstack11l1lll1l1_opy_(data[bstack1lllll1_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬ༕")])
    except:
      pass
  def bstack11l1lll1l1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack1lllll1_opy_ (u"ࠬࡹࡣࡢࡰࠪ༖")]
      self.bstack1lllll11ll_opy_ = scripts[bstack1lllll1_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪ༗")]
      self.bstack11l111ll1_opy_ = scripts[bstack1lllll1_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼ༘ࠫ")]
      self.bstack11l1l1l1ll_opy_ = scripts[bstack1lllll1_opy_ (u"ࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ༙࠭")]
  def bstack11l1l1l111_opy_(self, bstack11l1l11ll1_opy_):
    if bstack11l1l11ll1_opy_ != None and len(bstack11l1l11ll1_opy_) != 0:
      self.bstack11l1l11ll1_opy_ = bstack11l1l11ll1_opy_
  def store(self):
    try:
      with open(self.bstack11l1l111ll_opy_, bstack1lllll1_opy_ (u"ࠩࡺࠫ༚")) as file:
        json.dump({
          bstack1lllll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷࠧ༛"): self.bstack11l1l11ll1_opy_,
          bstack1lllll1_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࡷࠧ༜"): {
            bstack1lllll1_opy_ (u"ࠧࡹࡣࡢࡰࠥ༝"): self.perform_scan,
            bstack1lllll1_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥ༞"): self.bstack1lllll11ll_opy_,
            bstack1lllll1_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠦ༟"): self.bstack11l111ll1_opy_,
            bstack1lllll1_opy_ (u"ࠣࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸࠨ༠"): self.bstack11l1l1l1ll_opy_
          }
        }, file)
    except:
      pass
  def bstack1l1lll111l_opy_(self, bstack11l1l111l1_opy_):
    try:
      return any(command.get(bstack1lllll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ༡")) == bstack11l1l111l1_opy_ for command in self.bstack11l1l11ll1_opy_)
    except:
      return False
bstack1l1l1l1ll_opy_ = bstack11l1l1111l_opy_()