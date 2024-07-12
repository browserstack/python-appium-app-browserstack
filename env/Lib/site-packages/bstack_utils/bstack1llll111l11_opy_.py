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
import threading
bstack1lll1llll11_opy_ = 1000
bstack1lll1lll1l1_opy_ = 5
bstack1llll1111ll_opy_ = 30
bstack1lll1lll1ll_opy_ = 2
class bstack1llll11111l_opy_:
    def __init__(self, handler, bstack1lll1llllll_opy_=bstack1lll1llll11_opy_, bstack1lll1lll11l_opy_=bstack1lll1lll1l1_opy_):
        self.queue = []
        self.handler = handler
        self.bstack1lll1llllll_opy_ = bstack1lll1llllll_opy_
        self.bstack1lll1lll11l_opy_ = bstack1lll1lll11l_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack1lll1llll1l_opy_()
    def bstack1lll1llll1l_opy_(self):
        self.timer = threading.Timer(self.bstack1lll1lll11l_opy_, self.bstack1llll111111_opy_)
        self.timer.start()
    def bstack1lll1lllll1_opy_(self):
        self.timer.cancel()
    def bstack1llll1111l1_opy_(self):
        self.bstack1lll1lllll1_opy_()
        self.bstack1lll1llll1l_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack1lll1llllll_opy_:
                t = threading.Thread(target=self.bstack1llll111111_opy_)
                t.start()
                self.bstack1llll1111l1_opy_()
    def bstack1llll111111_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack1lll1llllll_opy_]
        del self.queue[:self.bstack1lll1llllll_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack1lll1lllll1_opy_()
        while len(self.queue) > 0:
            self.bstack1llll111111_opy_()