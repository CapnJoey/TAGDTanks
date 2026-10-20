import heapq as lIII1IIl1l1l
import math as IIl1lllIIlII
import random as ll11llI11lll
import numpy as Il1l11lIll11
from maps import *
from collections import deque as I1I1IIlIlI1I
lIl1lll11I1l = 0.5
l1lI1I1lIlI1 = 1e-09
l11II111lIII = lIl1lll11I1l * 1.25
lIllIIII1lI1 = 4
I1l11l11Illl = 3.0
II11ll11I11I = I1l11l11Illl + 0.5
I11l1l1II1l1 = I1l11l11Illl / 2
IlIIll1Il1II = 30.0
lI1Ill1lIlll = 180
II111IlI11l1 = 0.15
I1IIllI1ll1I = 15
IlII1IIl11I1 = 0.5
def I1lIIlIII1ll(llIII1I11IIl):
    return Il1l11lIll11.array([[llIII1I11IIl[l1IIIII1IIl1], llIII1I11IIl[(l1IIIII1IIl1 + 1) % len(llIII1I11IIl)]] for l1IIIII1IIl1 in range(len(llIII1I11IIl))], dtype=float)
def l11IIIIIlI1I(lIlIl1l1Illl, II111I1I1lIl, IIIIIIlIIIll, I1llI11I11I1):
    return I1lIIlIII1ll([[lIlIl1l1Illl, II111I1I1lIl], [IIIIIIlIIIll, II111I1I1lIl], [IIIIIIlIIIll, I1llI11I11I1], [lIlIl1l1Illl, I1llI11I11I1]])
def IlllIlI1I111():
    return l11IIIIIlI1I(1, 1, 19, 14)
def lllII1I1II1l():
    Il1l1I1IlIll = IlllIlI1I111()
    lII1llII1I1l = I1lIIlIII1ll([[4, 7], [9, 7], [9, 3], [11, 3], [11, 7], [16, 7], [16, 8], [11, 8], [11, 12], [9, 12], [9, 8], [4, 8]])
    return Il1l11lIll11.concatenate([Il1l1I1IlIll, lII1llII1I1l])
def lIllI1I1llll():
    Il1l1I1IlIll = IlllIlI1I111()
    lI1l11III1II = l11IIIIIlI1I(5, 3, 6, 12)
    Illl11I111l1 = l11IIIIIlI1I(15, 3, 16, 12)
    return Il1l11lIll11.concatenate([Il1l1I1IlIll, lI1l11III1II, Illl11I111l1])
def lII1IlI1l1I1():
    Il1l1I1IlIll = IlllIlI1I111()
    return Il1l11lIll11.concatenate([Il1l1I1IlIll, l11IIIIIlI1I(4, 4, 16, 11)])
def I11IIIIl1Ill(l1Il111lllII):
    lII1llII1I1l = plus_map(empty_map())
    IIlIIlI1I1I1 = bars_map(empty_map())
    l1lI11I11I11 = rect_map(empty_map())
    if Il1l11lIll11.array_equal(lII1llII1I1l, l1Il111lllII):
        return lllII1I1II1l()
    if Il1l11lIll11.array_equal(IIlIIlI1I1I1, l1Il111lllII):
        return lIllI1I1llll()
    if Il1l11lIll11.array_equal(l1lI11I11I11, l1Il111lllII):
        return lII1IlI1l1I1()
    return None
def llIIl1lI1III(l1IlIIIll1II, I11lIll11ll1):
    IIllll1I1ll1 = Il1llIIlIIII(I11lIll11ll1)
    Ill1l1IlIIlI = l1IlIIIll1II + IIllll1I1ll1 * lIl1lll11I1l
    l111lIIII111 = l1IlIIIll1II - IIllll1I1ll1 * lIl1lll11I1l
    return Il1l11lIll11.array([Ill1l1IlIIlI, l111lIIII111])
def Il1llIIlIIII(lIl1III1Illl):
    ll1III1l1II1 = IIl1lllIIlII.hypot(lIl1III1Illl[0], lIl1III1Illl[1])
    if ll1III1l1II1 < l1lI1I1lIlI1:
        return Il1l11lIll11.zeros(2)
    return Il1l11lIll11.array([-lIl1III1Illl[1] / ll1III1l1II1, lIl1III1Illl[0] / ll1III1l1II1])
def l1lIlII111lI(l1IlIIIll1II, II11I1l1Ill1):
    IIllll1I1ll1 = Il1llIIlIIII(II11I1l1Ill1[1] - II11I1l1Ill1[0])
    return l1IlIIIll1II - 2 * Il1l11lIll11.dot(l1IlIIIll1II - II11I1l1Ill1[0], IIllll1I1ll1) * IIllll1I1ll1
def lIlll1IIIlI1(lll1IIIIIIl1):
    return Il1l11lIll11.array([Il1l11lIll11.cos(lll1IIIIIIl1), Il1l11lIll11.sin(lll1IIIIIIl1)])
def l1llllI1I1Il(lIl1III1Illl):
    return float(Il1l11lIll11.degrees(Il1l11lIll11.arctan2(lIl1III1Illl[1], lIl1III1Illl[0])))
def lllllIlIIllI(I11lIll1l1II, IllIl11I111l):
    return (I11lIll1l1II - IllIl11I111l + 180) % 360 - 180
def l1llI1IIllII(I1IllIl111I1, Il1l1l1Il1II):
    IllI1I1lll11 = I1IllIl111I1[1] - I1IllIl111I1[0]
    ll111lllI1lI = Il1l1l1Il1II[1] - Il1l1l1Il1II[0]
    Ill1lI1I1I11 = IllllllI11I1(IllI1I1lll11, ll111lllI1lI)
    if abs(Ill1lI1I1I11) < l1lI1I1lIlI1:
        return None
    return I1IllIl111I1[0] + IllllllI11I1(Il1l1l1Il1II[0] - I1IllIl111I1[0], ll111lllI1lI) / Ill1lI1I1I11 * IllI1I1lll11
def l11I1II1l11I(IIlIIIIlI111, II11I1l1Ill1):
    l1llIllI11ll = II11I1l1Ill1[1] - II11I1l1Ill1[0]
    return Il1l11lIll11.dot(IIlIIIIlI111 - II11I1l1Ill1[0], l1llIllI11ll) / Il1l11lIll11.dot(l1llIllI11ll, l1llIllI11ll)
def lI11II1lIlIl(l1IlIII1lII1, IIlIIIIlI111):
    IIllll1I1ll1 = Il1llIIlIIII(l1IlIII1lII1[1] - l1IlIII1lII1[0])
    return (l1IlIII1lII1[0], IIllll1I1ll1 * Il1l11lIll11.sign(Il1l11lIll11.dot(IIlIIIIlI111 - l1IlIII1lII1[0], IIllll1I1ll1)))
def l11I1I111Il1(II11I1l1Ill1, lIIlIll1I1Il, llI1111Il11l):
    IlIIlI111Ill = Il1l11lIll11.dot(II11I1l1Ill1[0] - lIIlIll1I1Il, llI1111Il11l)
    I11IIIlllI1l = Il1l11lIll11.dot(II11I1l1Ill1[1] - lIIlIll1I1Il, llI1111Il11l)
    if IlIIlI111Ill < l1lI1I1lIlI1 and I11IIIlllI1l < l1lI1I1lIlI1:
        return None
    if IlIIlI111Ill >= 0 and I11IIIlllI1l >= 0:
        return II11I1l1Ill1
    IllllIlII1Il = II11I1l1Ill1[0] + (II11I1l1Ill1[1] - II11I1l1Ill1[0]) * IlIIlI111Ill / (IlIIlI111Ill - I11IIIlllI1l)
    if IlIIlI111Ill >= 0:
        return Il1l11lIll11.array([II11I1l1Ill1[0], IllllIlII1Il])
    return Il1l11lIll11.array([IllllIlII1Il, II11I1l1Ill1[1]])
def Il1IIII1lI1l(II11I1l1Ill1, l1IlIII1lII1, IIlIIIIlI111):
    return l11I1I111Il1(II11I1l1Ill1, *lI11II1lIlIl(l1IlIII1lII1, IIlIIIIlI111))
def IllllllI11I1(IIlllllll1l1, IllI1Il1l1l1):
    return IIlllllll1l1[0] * IllI1Il1l1l1[1] - IIlllllll1l1[1] * IllI1Il1l1l1[0]
def I1II1IlIIl1l(I1IllIl111I1, Il1l1l1Il1II):
    lIll1l1111I1, IllI1I1lll11 = (Il1l11lIll11.asarray(I1IllIl111I1[0], dtype=float), Il1l11lIll11.asarray(I1IllIl111I1[1], dtype=float) - I1IllIl111I1[0])
    IIl1llI1IIl1, ll111lllI1lI = (Il1l11lIll11.asarray(Il1l1l1Il1II[0], dtype=float), Il1l11lIll11.asarray(Il1l1l1Il1II[1], dtype=float) - Il1l1l1Il1II[0])
    Il1l1IIIIII1 = 1e-09
    Ill1lI1I1I11 = IllllllI11I1(IllI1I1lll11, ll111lllI1lI)
    I1lIIlIl1Ill = IIl1llI1IIl1 - lIll1l1111I1
    if abs(Ill1lI1I1I11) < Il1l1IIIIII1:
        if abs(IllllllI11I1(I1lIIlIl1Ill, IllI1I1lll11)) > Il1l1IIIIII1:
            return None
        lllI111l1l1I = Il1l11lIll11.dot(IllI1I1lll11, IllI1I1lll11)
        if lllI111l1l1I < Il1l1IIIIII1:
            return lIll1l1111I1 if Il1l11lIll11.allclose(lIll1l1111I1, IIl1llI1IIl1) else None
        I11ll1lI1III = Il1l11lIll11.dot(I1lIIlIl1Ill, IllI1I1lll11) / lllI111l1l1I
        llIl1lI11IlI = I11ll1lI1III + Il1l11lIll11.dot(ll111lllI1lI, IllI1I1lll11) / lllI111l1l1I
        lI11I11I111l, lI1ll1l11IlI = (max(0.0, min(I11ll1lI1III, llIl1lI11IlI)), min(1.0, max(I11ll1lI1III, llIl1lI11IlI)))
        if lI11I11I111l > lI1ll1l11IlI:
            return None
        return lIll1l1111I1 + lI11I11I111l * IllI1I1lll11
    IlIlllIl1I1l = IllllllI11I1(I1lIIlIl1Ill, ll111lllI1lI) / Ill1lI1I1I11
    ll1lIl1l1Il1 = IllllllI11I1(I1lIIlIl1Ill, IllI1I1lll11) / Ill1lI1I1I11
    if -Il1l1IIIIII1 <= IlIlllIl1I1l <= 1 + Il1l1IIIIII1 and -Il1l1IIIIII1 <= ll1lIl1l1Il1 <= 1 + Il1l1IIIIII1:
        return lIll1l1111I1 + IlIlllIl1I1l * IllI1I1lll11
    return None
def III1I1l1lIII(II11I1l1111I, IIlIIIIlI111, I1II1lI1lI1I):
    IIl1IllIIII1 = l1llI1IIllII(Il1l11lIll11.array([II11I1l1111I, IIlIIIIlI111]), I1II1lI1lI1I)
    if IIl1IllIIII1 is None:
        return Il1l11lIll11.sign(Il1l11lIll11.dot(IIlIIIIlI111 - II11I1l1111I, I1II1lI1lI1I[1] - I1II1lI1lI1I[0])) * Il1l11lIll11.inf
    return l11I1II1l11I(IIl1IllIIII1, I1II1lI1lI1I)
def IIlII11lll11(II11I1l1111I, I1II1lI1lI1I, III11l1I1111, ll1lll1II11l=None):
    IIllIlIIllll = [(0.0, 1.0)]
    l1llIllI11ll = I1II1lI1lI1I[1] - I1II1lI1lI1I[0]
    l1lI1lIlIllI = (I1II1lI1lI1I[0] + I1II1lI1lI1I[1]) / 2
    l1l1lIlIIlll = [lI11II1lIlIl(I1II1lI1lI1I, II11I1l1111I), lI11II1lIlIl(Il1l11lIll11.array([II11I1l1111I, II11I1l1111I + l1llIllI11ll]), l1lI1lIlIllI)]
    if ll1lll1II11l is not None:
        l1l1lIlIIlll.append(lI11II1lIlIl(ll1lll1II11l, l1lI1lIlIllI))
    for III1111l1l11 in III11l1I1111:
        for lIIlIll1I1Il, llI1111Il11l in l1l1lIlIIlll:
            III1111l1l11 = l11I1I111Il1(III1111l1l11, lIIlIll1I1Il, llI1111Il11l)
            if III1111l1l11 is None:
                break
        if III1111l1l11 is None:
            continue
        l1IlllIIl1Il, lIIl1I1lIIl1 = sorted((III1I1l1lIII(II11I1l1111I, lI1IIII1I11I, I1II1lI1lI1I) for lI1IIII1I11I in III1111l1l11))
        IIllIlIIllll = [l111lIl1I1I1 for lI11I11I111l, lI1ll1l11IlI in IIllIlIIllll for l111lIl1I1I1 in ((lI11I11I111l, min(lI1ll1l11IlI, l1IlllIIl1Il)), (max(lI11I11I111l, lIIl1I1lIIl1), lI1ll1l11IlI)) if l111lIl1I1I1[1] - l111lIl1I1I1[0] > l1lI1I1lIlI1]
        if not IIllIlIIllll:
            return None
    lI11I11I111l, lI1ll1l11IlI = max(IIllIlIIllll, key=lambda l111lIl1I1I1: l111lIl1I1I1[1] - l111lIl1I1I1[0])
    return Il1l11lIll11.array([I1II1lI1lI1I[0] + lI11I11I111l * l1llIllI11ll, I1II1lI1lI1I[0] + lI1ll1l11IlI * l1llIllI11ll])
def I1I1I11IlllI(I1ll1Il1I111, I11lIll1l1II, III11l1I1111):
    Il1lI1l1lIII = I11lIll1l1II - I1ll1Il1I111
    if Il1l11lIll11.linalg.norm(Il1lI1l1lIII) < l1lI1I1lIlI1:
        Il1lI1l1lIII = Il1l11lIll11.array([1.0, 0.0])
    l1l1lIlIIlll = llIIl1lI1III(I11lIll1l1II, Il1lI1l1lIII)
    return IIlII11lll11(I1ll1Il1I111, l1l1lIlIIlll, III11l1I1111)
def lII1lIlIlI11(l1Il111lllII, IlIIIl11l1II, llIl1l1lI1l1):
    return not (0 <= IlIIIl11l1II < l1Il111lllII.shape[0] and 0 <= llIl1l1lI1l1 < l1Il111lllII.shape[1]) or bool(l1Il111lllII[IlIIIl11l1II][llIl1l1lI1l1])
def llIl1lIll111(l1Il111lllII):
    I11lll1l1l1l, l1l1II1l1lll = l1Il111lllII.shape
    Il1l1I1IlIll = []
    for llIl1l1lI1l1 in range(l1l1II1l1lll + 1):
        lIl11II11111 = None
        for IlIIIl11l1II in range(I11lll1l1l1l + 1):
            llll1III1II1 = IlIIIl11l1II < I11lll1l1l1l and lII1lIlIlI11(l1Il111lllII, IlIIIl11l1II, llIl1l1lI1l1 - 1) != lII1lIlIlI11(l1Il111lllII, IlIIIl11l1II, llIl1l1lI1l1)
            I11ll111Il1l = IlIIIl11l1II < I11lll1l1l1l and lII1lIlIlI11(l1Il111lllII, IlIIIl11l1II, llIl1l1lI1l1)
            if lIl11II11111 is not None and (not llll1III1II1 or I11ll111Il1l != lIl11II11111[1]):
                Il1l1I1IlIll.append([[lIl11II11111[0], llIl1l1lI1l1], [IlIIIl11l1II, llIl1l1lI1l1]])
                lIl11II11111 = None
            if llll1III1II1 and lIl11II11111 is None:
                lIl11II11111 = (IlIIIl11l1II, I11ll111Il1l)
    for IlIIIl11l1II in range(I11lll1l1l1l + 1):
        lIl11II11111 = None
        for llIl1l1lI1l1 in range(l1l1II1l1lll + 1):
            llll1III1II1 = llIl1l1lI1l1 < l1l1II1l1lll and lII1lIlIlI11(l1Il111lllII, IlIIIl11l1II - 1, llIl1l1lI1l1) != lII1lIlIlI11(l1Il111lllII, IlIIIl11l1II, llIl1l1lI1l1)
            I11ll111Il1l = llIl1l1lI1l1 < l1l1II1l1lll and lII1lIlIlI11(l1Il111lllII, IlIIIl11l1II, llIl1l1lI1l1)
            if lIl11II11111 is not None and (not llll1III1II1 or I11ll111Il1l != lIl11II11111[1]):
                Il1l1I1IlIll.append([[IlIIIl11l1II, lIl11II11111[0]], [IlIIIl11l1II, llIl1l1lI1l1]])
                lIl11II11111 = None
            if llll1III1II1 and lIl11II11111 is None:
                lIl11II11111 = (llIl1l1lI1l1, I11ll111Il1l)
    return Il1l11lIll11.array(Il1l1I1IlIll, dtype=float).reshape(-1, 2, 2)
def I111III11I1l(l1Il111lllII):
    I11lll1l1l1l, l1l1II1l1lll = l1Il111lllII.shape
    ll111II1lI1l = []
    for IlIIIl11l1II in range(I11lll1l1l1l + 1):
        for llIl1l1lI1l1 in range(l1l1II1l1lll + 1):
            lll1IlIll1l1 = [(lI11lI1Illl1, l11I11IIIlI1) for lI11lI1Illl1 in (-1, 0) for l11I11IIIlI1 in (-1, 0) if lII1lIlIlI11(l1Il111lllII, IlIIIl11l1II + lI11lI1Illl1, llIl1l1lI1l1 + l11I11IIIlI1)]
            if len(lll1IlIll1l1) != 1:
                continue
            lI11lI1Illl1, l11I11IIIlI1 = lll1IlIll1l1[0]
            lI1I11lIIIII = Il1l11lIll11.array([1.0 if lI11lI1Illl1 == -1 else -1.0, 1.0 if l11I11IIIlI1 == -1 else -1.0])
            ll111II1lI1l.append(Il1l11lIll11.array([IlIIIl11l1II, llIl1l1lI1l1], dtype=float) + lI1I11lIIIII * l11II111lIII)
    return ll111II1lI1l
def l1I11lIllI11(llIII1I11IIl, IIlllllll1l1, IllI1Il1l1l1):
    l1llIllI11ll = IllI1Il1l1l1 - IIlllllll1l1
    I1IIIl1ll11l = Il1l11lIll11.maximum(Il1l11lIll11.sum(l1llIllI11ll * l1llIllI11ll, axis=-1), l1lI1I1lIlI1)
    IlIlllIl1I1l = Il1l11lIll11.clip(Il1l11lIll11.sum((llIII1I11IIl - IIlllllll1l1) * l1llIllI11ll, axis=-1) / I1IIIl1ll11l, 0.0, 1.0)
    return Il1l11lIll11.linalg.norm(IIlllllll1l1 + IlIlllIl1I1l[..., None] * l1llIllI11ll - llIII1I11IIl, axis=-1)
def ll11IlIII11l(IIlllllll1l1, IllI1Il1l1l1, III11l1I1111):
    if len(III11l1I1111) == 0:
        return Il1l11lIll11.inf
    lllI1lII1I1l, l11IlIII11lI = (III11l1I1111[:, 0], III11l1I1111[:, 1])
    IIl1lIIlllII = IllI1Il1l1l1 - IIlllllll1l1
    lIl1I1l1Il11, lIlIlI1l1IlI = (IllllllI11I1(IIl1lIIlllII, (lllI1lII1I1l - IIlllllll1l1).T), IllllllI11I1(IIl1lIIlllII, (l11IlIII11lI - IIlllllll1l1).T))
    l1ll1IIl1I11, III11111IlII = (IllllllI11I1((l11IlIII11lI - lllI1lII1I1l).T, (IIlllllll1l1 - lllI1lII1I1l).T), IllllllI11I1((l11IlIII11lI - lllI1lII1I1l).T, (IllI1Il1l1l1 - lllI1lII1I1l).T))
    if Il1l11lIll11.any((lIl1I1l1Il11 * lIlIlI1l1IlI < 0) & (l1ll1IIl1I11 * III11111IlII < 0)):
        return 0.0
    return float(min(l1I11lIllI11(IIlllllll1l1, lllI1lII1I1l, l11IlIII11lI).min(), l1I11lIllI11(IllI1Il1l1l1, lllI1lII1I1l, l11IlIII11lI).min(), l1I11lIllI11(III11l1I1111.reshape(-1, 2), IIlllllll1l1, IllI1Il1l1l1).min()))
class lI1lll1II11l:
    def __init__(self, l1Il111lllII):
        self.map = l1Il111lllII.copy()
        self.III11l1I1111 = llIl1lIll111(l1Il111lllII)
        self.ll111II1lI1l = [IlI1llllIIll for IlI1llllIIll in I111III11I1l(l1Il111lllII) if self.II1I1l1IllII(IlI1llllIIll, IlI1llllIIll) >= lIl1lll11I1l - l1lI1I1lIlI1]
        self.lIll1111II1I = {l1IIIII1IIl1: [] for l1IIIII1IIl1 in range(len(self.ll111II1lI1l))}
        for l1IIIII1IIl1 in range(len(self.ll111II1lI1l)):
            for l11I11lI11Il in range(l1IIIII1IIl1 + 1, len(self.ll111II1lI1l)):
                if self.I1l1lII11Il1(self.ll111II1lI1l[l1IIIII1IIl1], self.ll111II1lI1l[l11I11lI11Il]):
                    l1lIII1ll11I = float(Il1l11lIll11.linalg.norm(self.ll111II1lI1l[l1IIIII1IIl1] - self.ll111II1lI1l[l11I11lI11Il]))
                    self.lIll1111II1I[l1IIIII1IIl1].append((l11I11lI11Il, l1lIII1ll11I))
                    self.lIll1111II1I[l11I11lI11Il].append((l1IIIII1IIl1, l1lIII1ll11I))
    def II1I1l1IllII(self, IIlllllll1l1, IllI1Il1l1l1):
        return ll11IlIII11l(IIlllllll1l1, IllI1Il1l1l1, self.III11l1I1111)
    def I1l1lII11Il1(self, IIlllllll1l1, IllI1Il1l1l1, ll11III1IIII=lIl1lll11I1l):
        return self.II1I1l1IllII(IIlllllll1l1, IllI1Il1l1l1) >= ll11III1IIII - l1lI1I1lIlI1
    def lII111lIIlIl(self, ll1lll1II11l, lI1IIII1I11I):
        ll1lll1II11l, lI1IIII1I11I = (Il1l11lIll11.asarray(ll1lll1II11l, dtype=float), Il1l11lIll11.asarray(lI1IIII1I11I, dtype=float))
        ll11III1IIII = min(lIl1lll11I1l, self.II1I1l1IllII(ll1lll1II11l, ll1lll1II11l), self.II1I1l1IllII(lI1IIII1I11I, lI1IIII1I11I))
        if self.I1l1lII11Il1(ll1lll1II11l, lI1IIII1I11I, ll11III1IIII):
            return [ll1lll1II11l, lI1IIII1I11I]
        IlI1llllIIll = len(self.ll111II1lI1l)
        llIII1I11IIl = {l1IIIII1IIl1: self.ll111II1lI1l[l1IIIII1IIl1] for l1IIIII1IIl1 in range(IlI1llllIIll)}
        llIII1I11IIl[-1], llIII1I11IIl[-2] = (ll1lll1II11l, lI1IIII1I11I)
        IlI11lI1Il1l = {l1IIIII1IIl1: float(Il1l11lIll11.linalg.norm(lI1IIII1I11I - self.ll111II1lI1l[l1IIIII1IIl1])) for l1IIIII1IIl1 in range(IlI1llllIIll) if self.I1l1lII11Il1(self.ll111II1lI1l[l1IIIII1IIl1], lI1IIII1I11I, ll11III1IIII)}
        def I1lII1I1lII1(l1IIIII1IIl1):
            if l1IIIII1IIl1 == -1:
                return [(l11I11lI11Il, float(Il1l11lIll11.linalg.norm(self.ll111II1lI1l[l11I11lI11Il] - ll1lll1II11l))) for l11I11lI11Il in range(IlI1llllIIll) if self.I1l1lII11Il1(ll1lll1II11l, self.ll111II1lI1l[l11I11lI11Il], ll11III1IIII)]
            lIlI11llI1lI = list(self.lIll1111II1I[l1IIIII1IIl1])
            if l1IIIII1IIl1 in IlI11lI1Il1l:
                lIlI11llI1lI.append((-2, IlI11lI1Il1l[l1IIIII1IIl1]))
            return lIlI11llI1lI
        l111lII1lIIl, lIIIlII111ll = ({-1: 0.0}, {})
        lIllIll1l1I1 = [(0.0, -1)]
        while lIllIll1l1I1:
            l1llIllI11ll, l1IIIII1IIl1 = lIII1IIl1l1l.heappop(lIllIll1l1I1)
            if l1IIIII1IIl1 == -2:
                break
            if l1llIllI11ll > l111lII1lIIl[l1IIIII1IIl1]:
                continue
            for l11I11lI11Il, l1lIII1ll11I in I1lII1I1lII1(l1IIIII1IIl1):
                if l1llIllI11ll + l1lIII1ll11I < l111lII1lIIl.get(l11I11lI11Il, Il1l11lIll11.inf):
                    l111lII1lIIl[l11I11lI11Il], lIIIlII111ll[l11I11lI11Il] = (l1llIllI11ll + l1lIII1ll11I, l1IIIII1IIl1)
                    lIII1IIl1l1l.heappush(lIllIll1l1I1, (l1llIllI11ll + l1lIII1ll11I, l11I11lI11Il))
        if -2 not in l111lII1lIIl:
            return []
        lI1l11IIIIIl = [-2]
        while lI1l11IIIIIl[-1] != -1:
            lI1l11IIIIIl.append(lIIIlII111ll[lI1l11IIIIIl[-1]])
        return [llIII1I11IIl[l1IIIII1IIl1] for l1IIIII1IIl1 in reversed(lI1l11IIIIIl)]
class II11I1II1111:
    ...
class II1ll1IllI1l:
    ...
class l1I1lll111I1:
    def __init__(self, IlIIIl11l1II, llIl1l1lI1l1, III1II1I1llI):
        self.x = IlIIIl11l1II
        self.y = llIl1l1lI1l1
        self.III1II1I1llI = III1II1I1llI
class Gilbert:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.enemy_x = 0
        self.enemy_y = 0
        self.body_direction = 0
        self.gun_direction = 0
        self.gun_ready = False
        self.enemy_bullets = []
        self.map = Il1l11lIll11.zeros((20, 15))
        self.dt = 0
        self.body_turn_action = None
        self.gun_turn_action = None
        self.move_action = None
        self.shoot_action = False
        self.l11lll1111lI = I11IIIIl1Ill(self.map)
        self.IlllIll1llII = None
        self.llllI11lI1Il = None
        self.I1IIllll1lll = None
        self.lI1l11IIIIIl = None
        self.IllII1IlII11 = None
        self.IlIll111IIIl = 0
    def update(self):
        if self.IlllIll1llII is None or not Il1l11lIll11.array_equal(self.IlllIll1llII.map, self.map):
            self.l11lll1111lI = I11IIIIl1Ill(self.map)
            self.IlllIll1llII = lI1lll1II11l(self.map)
            self.lI1l11IIIIIl = None
        l1lIIIII11I1 = self.llII11I1III1() if self.gun_ready else []
        I1lllI1I1lll = [I1II1lI1lI1I for I1II1lI1lI1I in l1lIIIII11I1 if self.I1Il1I1I1ll1(I1II1lI1lI1I) >= II11ll11I11I]
        if self.gun_ready and len(I1lllI1I1lll) > 0:
            self.stop_move()
            self.stop_turn_body()
            self.IlI1111llll1(I1lllI1I1lll)
            return
        self.llllI11lI1Il = None
        if not self.gun_ready:
            if self.llIIlIl111lI(self.I1111111I111):
                if self.lll1Il1I11lI():
                    return
            else:
                self.I1IIllll1lll = None
                self.stop_move()
                self.stop_turn_body()
                self.I1ll1IllIIlI(self.IIIII11l1IIl)
                return
        self.I1IIllll1lll = None
        if not self.I11lII111lIl(self.IIIII11l1IIl):
            self.stop_move()
            self.stop_turn_body()
        self.I1ll1IllIIlI(self.IIIII11l1IIl)
    def llIIlIl111lI(self, IIlIIIIlI111):
        return I1I1I11IlllI(self.IIIII11l1IIl, IIlIIIIlI111, self.l11lll1111lI) is not None
    def lll1Il1I11lI(self):
        if self.I1IIllll1lll is not None and self.llIIlIl111lI(self.I1IIllll1lll):
            self.I1IIllll1lll = None
        if self.I1IIllll1lll is None:
            I1IlIII1lIll = [lIl11I1l11II for lIl11I1l11II in self.IlllIll1llII.ll111II1lI1l if not self.llIIlIl111lI(lIl11I1l11II)]
            if len(I1IlIII1lIll) > 0:
                self.I1IIllll1lll = min(I1IlIII1lIll, key=lambda lIl11I1l11II: Il1l11lIll11.linalg.norm(lIl11I1l11II - self.I1111111I111))
            else:
                self.I1IIllll1lll = Il1l11lIll11.array(self.map.shape, dtype=float) - self.IIIII11l1IIl
                if self.IlllIll1llII.II1I1l1IllII(self.I1IIllll1lll, self.I1IIllll1lll) < lIl1lll11I1l - l1lI1I1lIlI1 and len(self.IlllIll1llII.ll111II1lI1l) > 0:
                    self.I1IIllll1lll = min(self.IlllIll1llII.ll111II1lI1l, key=lambda lIl11I1l11II: Il1l11lIll11.linalg.norm(lIl11I1l11II - self.I1IIllll1lll))
        if not self.I11lII111lIl(self.I1IIllll1lll):
            return False
        self.I1ll1IllIIlI(self.IIIII11l1IIl)
        return True
    def I11lII111lIl(self, IIl11lIlI111):
        if self.lI1l11IIIIIl is None or self.IlIll111IIIl >= I1IIllI1ll1I or Il1l11lIll11.linalg.norm(IIl11lIlI111 - self.IllII1IlII11) > IlII1IIl11I1:
            self.lI1l11IIIIIl = self.IlllIll1llII.lII111lIIlIl(self.I1111111I111, IIl11lIlI111)
            self.IllII1IlII11, self.IlIll111IIIl = (IIl11lIlI111, 0)
        self.IlIll111IIIl += 1
        if len(self.lI1l11IIIIIl) < 2:
            return False
        self.lI1l11IIIIIl[0] = self.I1111111I111
        while len(self.lI1l11IIIIIl) > 2 and Il1l11lIll11.linalg.norm(self.lI1l11IIIIIl[1] - self.I1111111I111) < II111IlI11l1:
            self.lI1l11IIIIIl.pop(1)
        self.lII111111l1I(self.lI1l11IIIIIl)
        return True
    def IlI1111llll1(self, l1lIIIII11I1):
        if any((self.IIIIII1Il11l(I1II1lI1lI1I) for I1II1lI1lI1I in l1lIIIII11I1)):
            self.stop_turn_gun()
            if self.gun_ready:
                self.shoot()
            return
        if self.llllI11lI1Il is None or self.llllI11lI1Il >= len(l1lIIIII11I1):
            self.llllI11lI1Il = ll11llI11lll.randrange(len(l1lIIIII11I1))
        I1II1lI1lI1I = l1lIIIII11I1[self.llllI11lI1Il]
        self.I1ll1IllIIlI((I1II1lI1lI1I[0] + I1II1lI1lI1I[1]) / 2)
    def lII111111l1I(self, lII111lIIlIl):
        if len(lII111lIIlIl) < 2 or (len(lII111lIIlIl) == 2 and Il1l11lIll11.linalg.norm(lII111lIIlIl[1] - self.I1111111I111) < II111IlI11l1):
            self.stop_move()
            self.stop_turn_body()
            return
        I11lIl11ll1I = self.l1llI1lll111(lII111lIIlIl[1])
        if abs(I11lIl11ll1I) < IlIIll1Il1II:
            self.move_forward()
        else:
            self.stop_move()
    def I1ll1IllIIlI(self, IIlIIIIlI111):
        I11lIl11ll1I = lllllIlIIllI(l1llllI1I1Il(IIlIIIIlI111 - self.I1111111I111), self.gun_direction)
        if abs(I11lIl11ll1I) <= I11l1l1II1l1:
            self.stop_turn_gun()
            return True
        if I11lIl11ll1I > 0:
            self.turn_gun_counter_clockwise()
        else:
            self.turn_gun_clockwise()
        return False
    def l1llI1lll111(self, IIlIIIIlI111):
        I11lIl11ll1I = lllllIlIIllI(l1llllI1I1Il(IIlIIIIlI111 - self.I1111111I111), self.body_direction)
        if abs(I11lIl11ll1I) <= I11l1l1II1l1:
            self.stop_turn_body()
        elif I11lIl11ll1I > 0:
            self.turn_body_counter_clockwise()
        else:
            self.turn_body_clockwise()
        return I11lIl11ll1I
    def I1Il1I1I1ll1(self, I1II1lI1lI1I):
        return abs(lllllIlIIllI(l1llllI1I1Il(I1II1lI1lI1I[1] - self.I1111111I111), l1llllI1I1Il(I1II1lI1lI1I[0] - self.I1111111I111)))
    def IIIIII1Il11l(self, I1II1lI1lI1I):
        IIlllllll1l1 = l1llllI1I1Il(I1II1lI1lI1I[0] - self.I1111111I111)
        I1Ill1I11l1I = lllllIlIIllI(l1llllI1I1Il(I1II1lI1lI1I[1] - self.I1111111I111), IIlllllll1l1)
        IIlIlIIlll1l = lllllIlIIllI(self.gun_direction, IIlllllll1l1)
        if I1Ill1I11l1I < 0:
            I1Ill1I11l1I, IIlIlIIlll1l = (-I1Ill1I11l1I, -IIlIlIIlll1l)
        return 0 <= IIlIlIIlll1l <= I1Ill1I11l1I
    def I11ll1111l1I(self):
        ll1Il11l11I1 = []
        for ll1llI11llI1 in self.l11lll1111lI:
            IlIl1I111Il1 = Il1llIIlIIII(ll1llI11llI1[1] - ll1llI11llI1[0])
            l11Illll1lIl = Il1l11lIll11.dot(self.I1111111I111 - ll1llI11llI1[0], IlIl1I111Il1)
            IlIlIIIIlI11 = Il1l11lIll11.dot(self.IIIII11l1IIl - ll1llI11llI1[0], IlIl1I111Il1)
            if l11Illll1lIl * IlIlIIIIlI11 <= 0:
                continue
            I1lI1ll1lI11 = l1lIlII111lI(self.I1111111I111, ll1llI11llI1)
            IlIl1l1IlIl1 = llIIl1lI1III(self.IIIII11l1IIl, self.IIIII11l1IIl - I1lI1ll1lI11)
            IlIl1l1IlIl1 = Il1IIII1lI1l(IlIl1l1IlIl1, ll1llI11llI1, self.IIIII11l1IIl)
            if IlIl1l1IlIl1 is None:
                continue
            II1ll1111I1l = [l11I1II1l11I(l1llI1IIllII(Il1l11lIll11.array([I1lI1ll1lI11, I11ll111Il1l]), ll1llI11llI1), ll1llI11llI1) for I11ll111Il1l in IlIl1l1IlIl1]
            lI11I11I111l, lI1ll1l11IlI = (max(0.0, min(II1ll1111I1l)), min(1.0, max(II1ll1111I1l)))
            if lI11I11I111l >= lI1ll1l11IlI - l1lI1I1lIlI1:
                continue
            II1IlIllIll1 = Il1l11lIll11.array([ll1llI11llI1[0] + IlIlllIl1I1l * (ll1llI11llI1[1] - ll1llI11llI1[0]) for IlIlllIl1I1l in (lI11I11I111l, lI1ll1l11IlI)])
            IlllIIl1llII = Il1l11lIll11.array([l1llI1IIllII(Il1l11lIll11.array([I1lI1ll1lI11, IIl1IllIIII1]), IlIl1l1IlIl1) for IIl1IllIIII1 in II1IlIllIll1])
            IlllIIl1llII = IIlII11lll11(I1lI1ll1lI11, IlllIIl1llII, self.l11lll1111lI, ll1lll1II11l=ll1llI11llI1)
            if IlllIIl1llII is None:
                continue
            II1IlIllIll1 = Il1l11lIll11.array([l1llI1IIllII(Il1l11lIll11.array([I1lI1ll1lI11, IIl1IllIIII1]), ll1llI11llI1) for IIl1IllIIII1 in IlllIIl1llII])
            II1IlIllIll1 = IIlII11lll11(self.I1111111I111, II1IlIllIll1, self.l11lll1111lI)
            if II1IlIllIll1 is None:
                continue
            ll1Il11l11I1.append(II1IlIllIll1)
        return Il1l11lIll11.array(ll1Il11l11I1)
    def llII11I1III1(self):
        ll1Il11l11I1 = list(self.I11ll1111l1I())
        IlIl1l1IlIl1 = I1I1I11IlllI(self.I1111111I111, self.IIIII11l1IIl, self.l11lll1111lI)
        if IlIl1l1IlIl1 is not None:
            ll1Il11l11I1.append(IlIl1l1IlIl1)
        return Il1l11lIll11.array(ll1Il11l11I1)
    def Il1IlII11lll(self, IIlllllll1l1, IllI1Il1l1l1):
        for II11I1l1Ill1 in self.l11lll1111lI:
            l1I1II1ll1I1 = I1II1IlIIl1l(Il1l11lIll11.array([IIlllllll1l1, IllI1Il1l1l1]), II11I1l1Ill1)
            if l1I1II1ll1I1 is not None:
                return False
        return True
    def turn_body_clockwise(self):
        self.body_turn_action = 'clockwise'
    def turn_body_counter_clockwise(self):
        self.body_turn_action = 'counter_clockwise'
    def stop_turn_body(self):
        self.body_turn_action = None
    def turn_gun_clockwise(self):
        self.gun_turn_action = 'clockwise'
    def turn_gun_counter_clockwise(self):
        self.gun_turn_action = 'counter_clockwise'
    def stop_turn_gun(self):
        self.gun_turn_action = None
    def move_forward(self):
        self.move_action = 'forward'
    def move_backward(self):
        self.move_action = 'backward'
    def stop_move(self):
        self.move_action = None
    def shoot(self):
        self.shoot_action = True
    @property
    def I1111111I111(self):
        return Il1l11lIll11.array([self.x, self.y])
    @property
    def IIIII11l1IIl(self):
        return Il1l11lIll11.array([self.enemy_x, self.enemy_y])
    @property
    def IIIlI1lIllll(self):
        return lIlll1IIIlI1(Il1l11lIll11.deg2rad(self.body_direction))
    @property
    def IlII111IIIl1(self):
        return lIlll1IIIlI1(Il1l11lIll11.deg2rad(self.gun_direction))
class TestTank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.enemy_x = 0
        self.enemy_y = 0
        self.body_direction = 0
        self.gun_direction = 0
        self.gun_ready = False
        self.enemy_bullets = []
        self.map = Il1l11lIll11.zeros((20, 15))
        self.dt = 0
        self.body_turn_action = None
        self.gun_turn_action = None
        self.move_action = None
        self.shoot_action = False
    def update(self):
        self.move_forward()
        self.shoot()
        self.I1ll1IllIIlI(self.IIIII11l1IIl)
    def I1ll1IllIIlI(self, IIlIIIIlI111):
        I11lIl11ll1I = lllllIlIIllI(l1llllI1I1Il(IIlIIIIlI111 - self.I1111111I111), self.gun_direction)
        if abs(I11lIl11ll1I) <= I11l1l1II1l1:
            self.stop_turn_gun()
            return True
        if I11lIl11ll1I > 0:
            self.turn_gun_counter_clockwise()
            self.turn_body_counter_clockwise()
        else:
            self.turn_gun_clockwise()
            self.turn_body_clockwise()
        return False
    def turn_body_clockwise(self):
        self.body_turn_action = 'clockwise'
    def turn_body_counter_clockwise(self):
        self.body_turn_action = 'counter_clockwise'
    def stop_turn_body(self):
        self.body_turn_action = None
    def turn_gun_clockwise(self):
        self.gun_turn_action = 'clockwise'
    def turn_gun_counter_clockwise(self):
        self.gun_turn_action = 'counter_clockwise'
    def stop_turn_gun(self):
        self.gun_turn_action = None
    def move_forward(self):
        self.move_action = 'forward'
    def move_backward(self):
        self.move_action = 'backward'
    def stop_move(self):
        self.move_action = None
    def shoot(self):
        self.shoot_action = True
    @property
    def I1111111I111(self):
        return Il1l11lIll11.array([self.x, self.y])
    @property
    def IIIII11l1IIl(self):
        return Il1l11lIll11.array([self.enemy_x, self.enemy_y])
