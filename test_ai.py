import heapq as Illl1lI1l1II
import math as lIllIII11lI1
import random as II1Ill1II1lI
import numpy as IlIl11l111Il
from maps import *
llII11lllI11 = 0.5
lIIl1I11ll1l = 1e-09
l11l1I111lll = llII11lllI11 * 1.25
I1ll1Illl1ll = 4
l11lIIIlIIIl = 3.0
I1lI1IIIll1l = l11lIIIlIIIl + 0.5
I1l1Ill1lI11 = l11lIIIlIIIl / 2
IlI11lIIIlIl = 30.0
II1l1Il11l1l = 180
II1lIl1Il1ll = 0.15
l1lIll11l11I = 15
II1lIl1l1Il1 = 0.5
def IIll1l11lI1I(Ill1IlllI11I):
    return IlIl11l111Il.array([[Ill1IlllI11I[l1IllI11lll1], Ill1IlllI11I[(l1IllI11lll1 + 1) % len(Ill1IlllI11I)]] for l1IllI11lll1 in range(len(Ill1IlllI11I))], dtype=float)
def ll11IlIl1l1I(IIIlIl1IIllI, llIIll1IlIII, lIl1I11lI1I1, lIl1Il1IlI1I):
    return IIll1l11lI1I([[IIIlIl1IIllI, llIIll1IlIII], [lIl1I11lI1I1, llIIll1IlIII], [lIl1I11lI1I1, lIl1Il1IlI1I], [IIIlIl1IIllI, lIl1Il1IlI1I]])
def I1II111IIIl1():
    return ll11IlIl1l1I(1, 1, 19, 14)
def II1llIlIIIl1():
    lI1lII1III1l = I1II111IIIl1()
    IlI1lI1ll11I = IIll1l11lI1I([[4, 7], [9, 7], [9, 3], [11, 3], [11, 7], [16, 7], [16, 8], [11, 8], [11, 12], [9, 12], [9, 8], [4, 8]])
    return IlIl11l111Il.concatenate([lI1lII1III1l, IlI1lI1ll11I])
def I11lIIl1IlI1():
    lI1lII1III1l = I1II111IIIl1()
    I11IIlIIlIll = ll11IlIl1l1I(5, 3, 6, 12)
    IlII1IIlII1I = ll11IlIl1l1I(15, 3, 16, 12)
    return IlIl11l111Il.concatenate([lI1lII1III1l, I11IIlIIlIll, IlII1IIlII1I])
def I1lI1l1Il11I():
    lI1lII1III1l = I1II111IIIl1()
    return IlIl11l111Il.concatenate([lI1lII1III1l, ll11IlIl1l1I(4, 4, 16, 11)])
def IIlllIIII1l1(l1Ill1l111l1):
    IlI1lI1ll11I = plus_map(empty_map())
    I1lIlll1lIll = bars_map(empty_map())
    lIlIlI11lI11 = rect_map(empty_map())
    if IlIl11l111Il.array_equal(IlI1lI1ll11I, l1Ill1l111l1):
        return II1llIlIIIl1()
    if IlIl11l111Il.array_equal(I1lIlll1lIll, l1Ill1l111l1):
        return I11lIIl1IlI1()
    if IlIl11l111Il.array_equal(lIlIlI11lI11, l1Ill1l111l1):
        return I1lI1l1Il11I()
    return None
def II1l1l1l1IlI(Il11IIlIlI1I, ll1l1lI11I1l):
    IlIIIIlIIIl1 = l1l111IlIlIl(ll1l1lI11I1l)
    l11lIl1I11I1 = Il11IIlIlI1I + IlIIIIlIIIl1 * llII11lllI11
    lI11IIIllI11 = Il11IIlIlI1I - IlIIIIlIIIl1 * llII11lllI11
    return IlIl11l111Il.array([l11lIl1I11I1, lI11IIIllI11])
def l1l111IlIlIl(l1l111l1l1lI):
    l11l1I11Illl = lIllIII11lI1.hypot(l1l111l1l1lI[0], l1l111l1l1lI[1])
    if l11l1I11Illl < lIIl1I11ll1l:
        return IlIl11l111Il.zeros(2)
    return IlIl11l111Il.array([-l1l111l1l1lI[1] / l11l1I11Illl, l1l111l1l1lI[0] / l11l1I11Illl])
def II1lI1Il1lII(Il11IIlIlI1I, lII11I111lI1):
    IlIIIIlIIIl1 = l1l111IlIlIl(lII11I111lI1[1] - lII11I111lI1[0])
    return Il11IIlIlI1I - 2 * IlIl11l111Il.dot(Il11IIlIlI1I - lII11I111lI1[0], IlIIIIlIIIl1) * IlIIIIlIIIl1
def llIlI1lIIlII(l1lIl1I1lll1):
    return IlIl11l111Il.array([IlIl11l111Il.cos(l1lIl1I1lll1), IlIl11l111Il.sin(l1lIl1I1lll1)])
def I1ll1lIIl11l(l1l111l1l1lI):
    return float(IlIl11l111Il.degrees(IlIl11l111Il.arctan2(l1l111l1l1lI[1], l1l111l1l1lI[0])))
def l1III1I1llIl(llI1lIlllIIl, I1111I1ll1II):
    return (llI1lIlllIIl - I1111I1ll1II + 180) % 360 - 180
def lI1IllI1II1l(IlI1I11l1II1, Il111l1l11Il):
    IIIl111I1I1l = IlI1I11l1II1[1] - IlI1I11l1II1[0]
    l1II11I1l1l1 = Il111l1l11Il[1] - Il111l1l11Il[0]
    I1IIlII1lII1 = IlIIlI1II1II(IIIl111I1I1l, l1II11I1l1l1)
    if abs(I1IIlII1lII1) < lIIl1I11ll1l:
        return None
    return IlI1I11l1II1[0] + IlIIlI1II1II(Il111l1l11Il[0] - IlI1I11l1II1[0], l1II11I1l1l1) / I1IIlII1lII1 * IIIl111I1I1l
def I1lIllIlIl1l(l1IIIl11Ill1, lII11I111lI1):
    llIIllllIllI = lII11I111lI1[1] - lII11I111lI1[0]
    return IlIl11l111Il.dot(l1IIIl11Ill1 - lII11I111lI1[0], llIIllllIllI) / IlIl11l111Il.dot(llIIllllIllI, llIIllllIllI)
def I1lII11I11II(II1IIIlI1IlI, l1IIIl11Ill1):
    IlIIIIlIIIl1 = l1l111IlIlIl(II1IIIlI1IlI[1] - II1IIIlI1IlI[0])
    return (II1IIIlI1IlI[0], IlIIIIlIIIl1 * IlIl11l111Il.sign(IlIl11l111Il.dot(l1IIIl11Ill1 - II1IIIlI1IlI[0], IlIIIIlIIIl1)))
def IIIl1Ill1II1(lII11I111lI1, lll1lIIIII1I, lI1IlI1lIlll):
    ll11lllI1lII = IlIl11l111Il.dot(lII11I111lI1[0] - lll1lIIIII1I, lI1IlI1lIlll)
    Il11IIl1llII = IlIl11l111Il.dot(lII11I111lI1[1] - lll1lIIIII1I, lI1IlI1lIlll)
    if ll11lllI1lII < lIIl1I11ll1l and Il11IIl1llII < lIIl1I11ll1l:
        return None
    if ll11lllI1lII >= 0 and Il11IIl1llII >= 0:
        return lII11I111lI1
    IIlIlI1111Il = lII11I111lI1[0] + (lII11I111lI1[1] - lII11I111lI1[0]) * ll11lllI1lII / (ll11lllI1lII - Il11IIl1llII)
    if ll11lllI1lII >= 0:
        return IlIl11l111Il.array([lII11I111lI1[0], IIlIlI1111Il])
    return IlIl11l111Il.array([IIlIlI1111Il, lII11I111lI1[1]])
def IIll1lllIlI1(lII11I111lI1, II1IIIlI1IlI, l1IIIl11Ill1):
    return IIIl1Ill1II1(lII11I111lI1, *I1lII11I11II(II1IIIlI1IlI, l1IIIl11Ill1))
def IlIIlI1II1II(ll1IIIIlIlI1, IIll1II1IIl1):
    return ll1IIIIlIlI1[0] * IIll1II1IIl1[1] - ll1IIIIlIlI1[1] * IIll1II1IIl1[0]
def Il111I1IIIIl(IlI1I11l1II1, Il111l1l11Il):
    IIllI1l1l1l1, IIIl111I1I1l = (IlIl11l111Il.asarray(IlI1I11l1II1[0], dtype=float), IlIl11l111Il.asarray(IlI1I11l1II1[1], dtype=float) - IlI1I11l1II1[0])
    I11l1II1lIlI, l1II11I1l1l1 = (IlIl11l111Il.asarray(Il111l1l11Il[0], dtype=float), IlIl11l111Il.asarray(Il111l1l11Il[1], dtype=float) - Il111l1l11Il[0])
    Il1lIlllIIlI = 1e-09
    I1IIlII1lII1 = IlIIlI1II1II(IIIl111I1I1l, l1II11I1l1l1)
    II1l1II11IIl = I11l1II1lIlI - IIllI1l1l1l1
    if abs(I1IIlII1lII1) < Il1lIlllIIlI:
        if abs(IlIIlI1II1II(II1l1II11IIl, IIIl111I1I1l)) > Il1lIlllIIlI:
            return None
        IIlI11Il1lI1 = IlIl11l111Il.dot(IIIl111I1I1l, IIIl111I1I1l)
        if IIlI11Il1lI1 < Il1lIlllIIlI:
            return IIllI1l1l1l1 if IlIl11l111Il.allclose(IIllI1l1l1l1, I11l1II1lIlI) else None
        lII1llllI1I1 = IlIl11l111Il.dot(II1l1II11IIl, IIIl111I1I1l) / IIlI11Il1lI1
        I1IlIlllI1I1 = lII1llllI1I1 + IlIl11l111Il.dot(l1II11I1l1l1, IIIl111I1I1l) / IIlI11Il1lI1
        l111III1lIIl, l1111Il1l1ll = (max(0.0, min(lII1llllI1I1, I1IlIlllI1I1)), min(1.0, max(lII1llllI1I1, I1IlIlllI1I1)))
        if l111III1lIIl > l1111Il1l1ll:
            return None
        return IIllI1l1l1l1 + l111III1lIIl * IIIl111I1I1l
    ll1I11111Il1 = IlIIlI1II1II(II1l1II11IIl, l1II11I1l1l1) / I1IIlII1lII1
    lIllI1111Il1 = IlIIlI1II1II(II1l1II11IIl, IIIl111I1I1l) / I1IIlII1lII1
    if -Il1lIlllIIlI <= ll1I11111Il1 <= 1 + Il1lIlllIIlI and -Il1lIlllIIlI <= lIllI1111Il1 <= 1 + Il1lIlllIIlI:
        return IIllI1l1l1l1 + ll1I11111Il1 * IIIl111I1I1l
    return None
def lI1lIlllI1l1(l1I111III1II, l1IIIl11Ill1, lIl1IIIIIlll):
    Il1l1lIl1lII = lI1IllI1II1l(IlIl11l111Il.array([l1I111III1II, l1IIIl11Ill1]), lIl1IIIIIlll)
    if Il1l1lIl1lII is None:
        return IlIl11l111Il.sign(IlIl11l111Il.dot(l1IIIl11Ill1 - l1I111III1II, lIl1IIIIIlll[1] - lIl1IIIIIlll[0])) * IlIl11l111Il.inf
    return I1lIllIlIl1l(Il1l1lIl1lII, lIl1IIIIIlll)
def l11l1l11Il1I(l1I111III1II, lIl1IIIIIlll, lI1lIll1l1I1, Ill1Il1Il111=None):
    l11l11IIIlll = [(0.0, 1.0)]
    llIIllllIllI = lIl1IIIIIlll[1] - lIl1IIIIIlll[0]
    l1II1lllllII = (lIl1IIIIIlll[0] + lIl1IIIIIlll[1]) / 2
    III1IllIll1I = [I1lII11I11II(lIl1IIIIIlll, l1I111III1II), I1lII11I11II(IlIl11l111Il.array([l1I111III1II, l1I111III1II + llIIllllIllI]), l1II1lllllII)]
    if Ill1Il1Il111 is not None:
        III1IllIll1I.append(I1lII11I11II(Ill1Il1Il111, l1II1lllllII))
    for II1l111l1lI1 in lI1lIll1l1I1:
        for lll1lIIIII1I, lI1IlI1lIlll in III1IllIll1I:
            II1l111l1lI1 = IIIl1Ill1II1(II1l111l1lI1, lll1lIIIII1I, lI1IlI1lIlll)
            if II1l111l1lI1 is None:
                break
        if II1l111l1lI1 is None:
            continue
        ll1I1lll1l1l, l1Ill1ll111I = sorted((lI1lIlllI1l1(l1I111III1II, l111l1I1I1Il, lIl1IIIIIlll) for l111l1I1I1Il in II1l111l1lI1))
        l11l11IIIlll = [l1l111Il11lI for l111III1lIIl, l1111Il1l1ll in l11l11IIIlll for l1l111Il11lI in ((l111III1lIIl, min(l1111Il1l1ll, ll1I1lll1l1l)), (max(l111III1lIIl, l1Ill1ll111I), l1111Il1l1ll)) if l1l111Il11lI[1] - l1l111Il11lI[0] > lIIl1I11ll1l]
        if not l11l11IIIlll:
            return None
    l111III1lIIl, l1111Il1l1ll = max(l11l11IIIlll, key=lambda l1l111Il11lI: l1l111Il11lI[1] - l1l111Il11lI[0])
    return IlIl11l111Il.array([lIl1IIIIIlll[0] + l111III1lIIl * llIIllllIllI, lIl1IIIIIlll[0] + l1111Il1l1ll * llIIllllIllI])
def I11111lII1ll(I11IlIIII11I, llI1lIlllIIl, lI1lIll1l1I1):
    I1Ill1Il11lI = llI1lIlllIIl - I11IlIIII11I
    if IlIl11l111Il.linalg.norm(I1Ill1Il11lI) < lIIl1I11ll1l:
        I1Ill1Il11lI = IlIl11l111Il.array([1.0, 0.0])
    III1IllIll1I = II1l1l1l1IlI(llI1lIlllIIl, I1Ill1Il11lI)
    return l11l1l11Il1I(I11IlIIII11I, III1IllIll1I, lI1lIll1l1I1)
def l11Illl1I1l1(l1Ill1l111l1, lII1I11IIlIl, lIIlII1ll1Il):
    return not (0 <= lII1I11IIlIl < l1Ill1l111l1.shape[0] and 0 <= lIIlII1ll1Il < l1Ill1l111l1.shape[1]) or bool(l1Ill1l111l1[lII1I11IIlIl][lIIlII1ll1Il])
def l1111I1I1l1l(l1Ill1l111l1):
    I11IIIIII111, lllIII111II1 = l1Ill1l111l1.shape
    lI1lII1III1l = []
    for lIIlII1ll1Il in range(lllIII111II1 + 1):
        I1l11lllIl11 = None
        for lII1I11IIlIl in range(I11IIIIII111 + 1):
            IllllII1lII1 = lII1I11IIlIl < I11IIIIII111 and l11Illl1I1l1(l1Ill1l111l1, lII1I11IIlIl, lIIlII1ll1Il - 1) != l11Illl1I1l1(l1Ill1l111l1, lII1I11IIlIl, lIIlII1ll1Il)
            l1ll1IIl1ll1 = lII1I11IIlIl < I11IIIIII111 and l11Illl1I1l1(l1Ill1l111l1, lII1I11IIlIl, lIIlII1ll1Il)
            if I1l11lllIl11 is not None and (not IllllII1lII1 or l1ll1IIl1ll1 != I1l11lllIl11[1]):
                lI1lII1III1l.append([[I1l11lllIl11[0], lIIlII1ll1Il], [lII1I11IIlIl, lIIlII1ll1Il]])
                I1l11lllIl11 = None
            if IllllII1lII1 and I1l11lllIl11 is None:
                I1l11lllIl11 = (lII1I11IIlIl, l1ll1IIl1ll1)
    for lII1I11IIlIl in range(I11IIIIII111 + 1):
        I1l11lllIl11 = None
        for lIIlII1ll1Il in range(lllIII111II1 + 1):
            IllllII1lII1 = lIIlII1ll1Il < lllIII111II1 and l11Illl1I1l1(l1Ill1l111l1, lII1I11IIlIl - 1, lIIlII1ll1Il) != l11Illl1I1l1(l1Ill1l111l1, lII1I11IIlIl, lIIlII1ll1Il)
            l1ll1IIl1ll1 = lIIlII1ll1Il < lllIII111II1 and l11Illl1I1l1(l1Ill1l111l1, lII1I11IIlIl, lIIlII1ll1Il)
            if I1l11lllIl11 is not None and (not IllllII1lII1 or l1ll1IIl1ll1 != I1l11lllIl11[1]):
                lI1lII1III1l.append([[lII1I11IIlIl, I1l11lllIl11[0]], [lII1I11IIlIl, lIIlII1ll1Il]])
                I1l11lllIl11 = None
            if IllllII1lII1 and I1l11lllIl11 is None:
                I1l11lllIl11 = (lIIlII1ll1Il, l1ll1IIl1ll1)
    return IlIl11l111Il.array(lI1lII1III1l, dtype=float).reshape(-1, 2, 2)
def lllll1II1I11(l1Ill1l111l1):
    I11IIIIII111, lllIII111II1 = l1Ill1l111l1.shape
    l111III11lll = []
    for lII1I11IIlIl in range(I11IIIIII111 + 1):
        for lIIlII1ll1Il in range(lllIII111II1 + 1):
            I111I1II111l = [(llIll1lI11ll, lll1I1IllIII) for llIll1lI11ll in (-1, 0) for lll1I1IllIII in (-1, 0) if l11Illl1I1l1(l1Ill1l111l1, lII1I11IIlIl + llIll1lI11ll, lIIlII1ll1Il + lll1I1IllIII)]
            if len(I111I1II111l) != 1:
                continue
            llIll1lI11ll, lll1I1IllIII = I111I1II111l[0]
            IIlll1I111Il = IlIl11l111Il.array([1.0 if llIll1lI11ll == -1 else -1.0, 1.0 if lll1I1IllIII == -1 else -1.0])
            l111III11lll.append(IlIl11l111Il.array([lII1I11IIlIl, lIIlII1ll1Il], dtype=float) + IIlll1I111Il * l11l1I111lll)
    return l111III11lll
def IllI1IIllIIl(Ill1IlllI11I, ll1IIIIlIlI1, IIll1II1IIl1):
    llIIllllIllI = IIll1II1IIl1 - ll1IIIIlIlI1
    llIl1IIlIlll = IlIl11l111Il.maximum(IlIl11l111Il.sum(llIIllllIllI * llIIllllIllI, axis=-1), lIIl1I11ll1l)
    ll1I11111Il1 = IlIl11l111Il.clip(IlIl11l111Il.sum((Ill1IlllI11I - ll1IIIIlIlI1) * llIIllllIllI, axis=-1) / llIl1IIlIlll, 0.0, 1.0)
    return IlIl11l111Il.linalg.norm(ll1IIIIlIlI1 + ll1I11111Il1[..., None] * llIIllllIllI - Ill1IlllI11I, axis=-1)
def II1I1I1Il1ll(ll1IIIIlIlI1, IIll1II1IIl1, lI1lIll1l1I1):
    if len(lI1lIll1l1I1) == 0:
        return IlIl11l111Il.inf
    lIIl1l1Illl1, l1III11IIIl1 = (lI1lIll1l1I1[:, 0], lI1lIll1l1I1[:, 1])
    IlI1I11IlII1 = IIll1II1IIl1 - ll1IIIIlIlI1
    I1I1I11IlI1I, I1l1IllI1lI1 = (IlIIlI1II1II(IlI1I11IlII1, (lIIl1l1Illl1 - ll1IIIIlIlI1).T), IlIIlI1II1II(IlI1I11IlII1, (l1III11IIIl1 - ll1IIIIlIlI1).T))
    l1lI1llIl111, Il1l1lI111ll = (IlIIlI1II1II((l1III11IIIl1 - lIIl1l1Illl1).T, (ll1IIIIlIlI1 - lIIl1l1Illl1).T), IlIIlI1II1II((l1III11IIIl1 - lIIl1l1Illl1).T, (IIll1II1IIl1 - lIIl1l1Illl1).T))
    if IlIl11l111Il.any((I1I1I11IlI1I * I1l1IllI1lI1 < 0) & (l1lI1llIl111 * Il1l1lI111ll < 0)):
        return 0.0
    return float(min(IllI1IIllIIl(ll1IIIIlIlI1, lIIl1l1Illl1, l1III11IIIl1).min(), IllI1IIllIIl(IIll1II1IIl1, lIIl1l1Illl1, l1III11IIIl1).min(), IllI1IIllIIl(lI1lIll1l1I1.reshape(-1, 2), ll1IIIIlIlI1, IIll1II1IIl1).min()))
class II1ll1l1IIIl:
    def __init__(self, l1Ill1l111l1):
        self.map = l1Ill1l111l1.copy()
        self.lI1lIll1l1I1 = l1111I1I1l1l(l1Ill1l111l1)
        self.l111III11lll = [l1Il1ll1111l for l1Il1ll1111l in lllll1II1I11(l1Ill1l111l1) if self.ll1Ill1111l1(l1Il1ll1111l, l1Il1ll1111l) >= llII11lllI11 - lIIl1I11ll1l]
        self.IIlI111IllI1 = {l1IllI11lll1: [] for l1IllI11lll1 in range(len(self.l111III11lll))}
        for l1IllI11lll1 in range(len(self.l111III11lll)):
            for I1l11111llIl in range(l1IllI11lll1 + 1, len(self.l111III11lll)):
                if self.lI1llll1Ill1(self.l111III11lll[l1IllI11lll1], self.l111III11lll[I1l11111llIl]):
                    lIII1IlI111I = float(IlIl11l111Il.linalg.norm(self.l111III11lll[l1IllI11lll1] - self.l111III11lll[I1l11111llIl]))
                    self.IIlI111IllI1[l1IllI11lll1].append((I1l11111llIl, lIII1IlI111I))
                    self.IIlI111IllI1[I1l11111llIl].append((l1IllI11lll1, lIII1IlI111I))
    def ll1Ill1111l1(self, ll1IIIIlIlI1, IIll1II1IIl1):
        return II1I1I1Il1ll(ll1IIIIlIlI1, IIll1II1IIl1, self.lI1lIll1l1I1)
    def lI1llll1Ill1(self, ll1IIIIlIlI1, IIll1II1IIl1, I1Il111I1lII=llII11lllI11):
        return self.ll1Ill1111l1(ll1IIIIlIlI1, IIll1II1IIl1) >= I1Il111I1lII - lIIl1I11ll1l
    def IlIllIllI11l(self, Ill1Il1Il111, l111l1I1I1Il):
        Ill1Il1Il111, l111l1I1I1Il = (IlIl11l111Il.asarray(Ill1Il1Il111, dtype=float), IlIl11l111Il.asarray(l111l1I1I1Il, dtype=float))
        I1Il111I1lII = min(llII11lllI11, self.ll1Ill1111l1(Ill1Il1Il111, Ill1Il1Il111), self.ll1Ill1111l1(l111l1I1I1Il, l111l1I1I1Il))
        if self.lI1llll1Ill1(Ill1Il1Il111, l111l1I1I1Il, I1Il111I1lII):
            return [Ill1Il1Il111, l111l1I1I1Il]
        l1Il1ll1111l = len(self.l111III11lll)
        Ill1IlllI11I = {l1IllI11lll1: self.l111III11lll[l1IllI11lll1] for l1IllI11lll1 in range(l1Il1ll1111l)}
        Ill1IlllI11I[-1], Ill1IlllI11I[-2] = (Ill1Il1Il111, l111l1I1I1Il)
        llllII1Il111 = {l1IllI11lll1: float(IlIl11l111Il.linalg.norm(l111l1I1I1Il - self.l111III11lll[l1IllI11lll1])) for l1IllI11lll1 in range(l1Il1ll1111l) if self.lI1llll1Ill1(self.l111III11lll[l1IllI11lll1], l111l1I1I1Il, I1Il111I1lII)}
        def lll1IlI111II(l1IllI11lll1):
            if l1IllI11lll1 == -1:
                return [(I1l11111llIl, float(IlIl11l111Il.linalg.norm(self.l111III11lll[I1l11111llIl] - Ill1Il1Il111))) for I1l11111llIl in range(l1Il1ll1111l) if self.lI1llll1Ill1(Ill1Il1Il111, self.l111III11lll[I1l11111llIl], I1Il111I1lII)]
            IIII1llIl1II = list(self.IIlI111IllI1[l1IllI11lll1])
            if l1IllI11lll1 in llllII1Il111:
                IIII1llIl1II.append((-2, llllII1Il111[l1IllI11lll1]))
            return IIII1llIl1II
        l11Il1l1lllI, lI111llIl1Il = ({-1: 0.0}, {})
        I11I1l1ll1ll = [(0.0, -1)]
        while I11I1l1ll1ll:
            llIIllllIllI, l1IllI11lll1 = Illl1lI1l1II.heappop(I11I1l1ll1ll)
            if l1IllI11lll1 == -2:
                break
            if llIIllllIllI > l11Il1l1lllI[l1IllI11lll1]:
                continue
            for I1l11111llIl, lIII1IlI111I in lll1IlI111II(l1IllI11lll1):
                if llIIllllIllI + lIII1IlI111I < l11Il1l1lllI.get(I1l11111llIl, IlIl11l111Il.inf):
                    l11Il1l1lllI[I1l11111llIl], lI111llIl1Il[I1l11111llIl] = (llIIllllIllI + lIII1IlI111I, l1IllI11lll1)
                    Illl1lI1l1II.heappush(I11I1l1ll1ll, (llIIllllIllI + lIII1IlI111I, I1l11111llIl))
        if -2 not in l11Il1l1lllI:
            return []
        IIl1I11l11lI = [-2]
        while IIl1I11l11lI[-1] != -1:
            IIl1I11l11lI.append(lI111llIl1Il[IIl1I11l11lI[-1]])
        return [Ill1IlllI11I[l1IllI11lll1] for l1IllI11lll1 in reversed(IIl1I11l11lI)]
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
        self.map = IlIl11l111Il.zeros((20, 15))
        self.body_turn_action = None
        self.gun_turn_action = None
        self.move_action = None
        self.shoot_action = False
        self.l1I11IIIIIIl = IIlllIIII1l1(self.map)
        self.ll1ll11l1111 = None
        self.III1IIllI1Il = None
        self.lI11l1IllI11 = None
        self.IIl1I11l11lI = None
        self.I1lIIl11lllI = None
        self.l11l1ll1I11l = 0
    def update(self):
        if self.ll1ll11l1111 is None or not IlIl11l111Il.array_equal(self.ll1ll11l1111.map, self.map):
            self.l1I11IIIIIIl = IIlllIIII1l1(self.map)
            self.ll1ll11l1111 = II1ll1l1IIIl(self.map)
            self.IIl1I11l11lI = None
        Il1IIIl1111I = self.Il1I1l11I11l() if self.gun_ready else []
        I11IlllI1lIl = [lIl1IIIIIlll for lIl1IIIIIlll in Il1IIIl1111I if self.I1l1l1l1llII(lIl1IIIIIlll) >= I1lI1IIIll1l]
        if self.gun_ready and len(I11IlllI1lIl) > 0:
            self.lI1IlIll1l1I()
            self.I11l1111II1I()
            self.lIIlIlI11llI(I11IlllI1lIl)
            return
        self.III1IIllI1Il = None
        if not self.gun_ready:
            if self.IlII1lll1l1l(self.lI1lllllIIII):
                if self.IlllII1llIll():
                    return
            else:
                self.lI11l1IllI11 = None
                self.lI1IlIll1l1I()
                self.I11l1111II1I()
                self.lIl11llIIII1(self.lllI1lI1lll1)
                return
        self.lI11l1IllI11 = None
        if not self.l11IIll1l1ll(self.lllI1lI1lll1):
            self.lI1IlIll1l1I()
            self.I11l1111II1I()
        self.lIl11llIIII1(self.lllI1lI1lll1)
    def IlII1lll1l1l(self, l1IIIl11Ill1):
        return I11111lII1ll(self.lllI1lI1lll1, l1IIIl11Ill1, self.l1I11IIIIIIl) is not None
    def IlllII1llIll(self):
        if self.lI11l1IllI11 is not None and self.IlII1lll1l1l(self.lI11l1IllI11):
            self.lI11l1IllI11 = None
        if self.lI11l1IllI11 is None:
            lIII11ll1lII = [lIII1IllllIl for lIII1IllllIl in self.ll1ll11l1111.l111III11lll if not self.IlII1lll1l1l(lIII1IllllIl)]
            if len(lIII11ll1lII) > 0:
                self.lI11l1IllI11 = min(lIII11ll1lII, key=lambda lIII1IllllIl: IlIl11l111Il.linalg.norm(lIII1IllllIl - self.lI1lllllIIII))
            else:
                self.lI11l1IllI11 = IlIl11l111Il.array(self.map.shape, dtype=float) - self.lllI1lI1lll1
                if self.ll1ll11l1111.ll1Ill1111l1(self.lI11l1IllI11, self.lI11l1IllI11) < llII11lllI11 - lIIl1I11ll1l and len(self.ll1ll11l1111.l111III11lll) > 0:
                    self.lI11l1IllI11 = min(self.ll1ll11l1111.l111III11lll, key=lambda lIII1IllllIl: IlIl11l111Il.linalg.norm(lIII1IllllIl - self.lI11l1IllI11))
        if not self.l11IIll1l1ll(self.lI11l1IllI11):
            return False
        self.lIl11llIIII1(self.lllI1lI1lll1)
        return True
    def l11IIll1l1ll(self, l11l111l11lI):
        if self.IIl1I11l11lI is None or self.l11l1ll1I11l >= l1lIll11l11I or IlIl11l111Il.linalg.norm(l11l111l11lI - self.I1lIIl11lllI) > II1lIl1l1Il1:
            self.IIl1I11l11lI = self.ll1ll11l1111.IlIllIllI11l(self.lI1lllllIIII, l11l111l11lI)
            self.I1lIIl11lllI, self.l11l1ll1I11l = (l11l111l11lI, 0)
        self.l11l1ll1I11l += 1
        if len(self.IIl1I11l11lI) < 2:
            return False
        self.IIl1I11l11lI[0] = self.lI1lllllIIII
        while len(self.IIl1I11l11lI) > 2 and IlIl11l111Il.linalg.norm(self.IIl1I11l11lI[1] - self.lI1lllllIIII) < II1lIl1Il1ll:
            self.IIl1I11l11lI.pop(1)
        self.Ill11l111l1I(self.IIl1I11l11lI)
        return True
    def lIIlIlI11llI(self, Il1IIIl1111I):
        if any((self.l1ll1IlIllIl(lIl1IIIIIlll) for lIl1IIIIIlll in Il1IIIl1111I)):
            self.ll111111lI1l()
            if self.gun_ready:
                self.llIIl1II1lII()
            return
        if self.III1IIllI1Il is None or self.III1IIllI1Il >= len(Il1IIIl1111I):
            self.III1IIllI1Il = II1Ill1II1lI.randrange(len(Il1IIIl1111I))
        lIl1IIIIIlll = Il1IIIl1111I[self.III1IIllI1Il]
        self.lIl11llIIII1((lIl1IIIIIlll[0] + lIl1IIIIIlll[1]) / 2)
    def Ill11l111l1I(self, IlIllIllI11l):
        if len(IlIllIllI11l) < 2 or (len(IlIllIllI11l) == 2 and IlIl11l111Il.linalg.norm(IlIllIllI11l[1] - self.lI1lllllIIII) < II1lIl1Il1ll):
            self.lI1IlIll1l1I()
            self.I11l1111II1I()
            return
        l1llII11Il11 = self.II11II1l1I11(IlIllIllI11l[1])
        if abs(l1llII11Il11) < IlI11lIIIlIl:
            self.IlIIllIl1Il1()
        else:
            self.lI1IlIll1l1I()
    def lIl11llIIII1(self, l1IIIl11Ill1):
        l1llII11Il11 = l1III1I1llIl(I1ll1lIIl11l(l1IIIl11Ill1 - self.lI1lllllIIII), self.gun_direction)
        if abs(l1llII11Il11) <= I1l1Ill1lI11:
            self.ll111111lI1l()
            return True
        if l1llII11Il11 > 0:
            self.l111Illl1IlI()
        else:
            self.II1III1I111I()
        return False
    def II11II1l1I11(self, l1IIIl11Ill1):
        l1llII11Il11 = l1III1I1llIl(I1ll1lIIl11l(l1IIIl11Ill1 - self.lI1lllllIIII), self.body_direction)
        if abs(l1llII11Il11) <= I1l1Ill1lI11:
            self.I11l1111II1I()
        elif l1llII11Il11 > 0:
            self.lIIIll1ll1l1()
        else:
            self.l1IIlllIlIl1()
        return l1llII11Il11
    def I1l1l1l1llII(self, lIl1IIIIIlll):
        return abs(l1III1I1llIl(I1ll1lIIl11l(lIl1IIIIIlll[1] - self.lI1lllllIIII), I1ll1lIIl11l(lIl1IIIIIlll[0] - self.lI1lllllIIII)))
    def l1ll1IlIllIl(self, lIl1IIIIIlll):
        ll1IIIIlIlI1 = I1ll1lIIl11l(lIl1IIIIIlll[0] - self.lI1lllllIIII)
        l11ll1IIIIl1 = l1III1I1llIl(I1ll1lIIl11l(lIl1IIIIIlll[1] - self.lI1lllllIIII), ll1IIIIlIlI1)
        ll11lllll111 = l1III1I1llIl(self.gun_direction, ll1IIIIlIlI1)
        if l11ll1IIIIl1 < 0:
            l11ll1IIIIl1, ll11lllll111 = (-l11ll1IIIIl1, -ll11lllll111)
        return 0 <= ll11lllll111 <= l11ll1IIIIl1
    def lllllIlIIIlI(self):
        I1IllI1I1lII = []
        for l1IlIll1IllI in self.l1I11IIIIIIl:
            II11I1llllI1 = l1l111IlIlIl(l1IlIll1IllI[1] - l1IlIll1IllI[0])
            l1IIlI1l11I1 = IlIl11l111Il.dot(self.lI1lllllIIII - l1IlIll1IllI[0], II11I1llllI1)
            l1l1lII1l11l = IlIl11l111Il.dot(self.lllI1lI1lll1 - l1IlIll1IllI[0], II11I1llllI1)
            if l1IIlI1l11I1 * l1l1lII1l11l <= 0:
                continue
            IllI11ll11ll = II1lI1Il1lII(self.lI1lllllIIII, l1IlIll1IllI)
            I1III1II1I1I = II1l1l1l1IlI(self.lllI1lI1lll1, self.lllI1lI1lll1 - IllI11ll11ll)
            I1III1II1I1I = IIll1lllIlI1(I1III1II1I1I, l1IlIll1IllI, self.lllI1lI1lll1)
            if I1III1II1I1I is None:
                continue
            llIl111ll1II = [I1lIllIlIl1l(lI1IllI1II1l(IlIl11l111Il.array([IllI11ll11ll, l1ll1IIl1ll1]), l1IlIll1IllI), l1IlIll1IllI) for l1ll1IIl1ll1 in I1III1II1I1I]
            l111III1lIIl, l1111Il1l1ll = (max(0.0, min(llIl111ll1II)), min(1.0, max(llIl111ll1II)))
            if l111III1lIIl >= l1111Il1l1ll - lIIl1I11ll1l:
                continue
            I11111l111I1 = IlIl11l111Il.array([l1IlIll1IllI[0] + ll1I11111Il1 * (l1IlIll1IllI[1] - l1IlIll1IllI[0]) for ll1I11111Il1 in (l111III1lIIl, l1111Il1l1ll)])
            I1I1l1ll1l1I = IlIl11l111Il.array([lI1IllI1II1l(IlIl11l111Il.array([IllI11ll11ll, Il1l1lIl1lII]), I1III1II1I1I) for Il1l1lIl1lII in I11111l111I1])
            I1I1l1ll1l1I = l11l1l11Il1I(IllI11ll11ll, I1I1l1ll1l1I, self.l1I11IIIIIIl, Ill1Il1Il111=l1IlIll1IllI)
            if I1I1l1ll1l1I is None:
                continue
            I11111l111I1 = IlIl11l111Il.array([lI1IllI1II1l(IlIl11l111Il.array([IllI11ll11ll, Il1l1lIl1lII]), l1IlIll1IllI) for Il1l1lIl1lII in I1I1l1ll1l1I])
            I11111l111I1 = l11l1l11Il1I(self.lI1lllllIIII, I11111l111I1, self.l1I11IIIIIIl)
            if I11111l111I1 is None:
                continue
            I1IllI1I1lII.append(I11111l111I1)
        return IlIl11l111Il.array(I1IllI1I1lII)
    def Il1I1l11I11l(self):
        I1IllI1I1lII = list(self.lllllIlIIIlI())
        I1III1II1I1I = I11111lII1ll(self.lI1lllllIIII, self.lllI1lI1lll1, self.l1I11IIIIIIl)
        if I1III1II1I1I is not None:
            I1IllI1I1lII.append(I1III1II1I1I)
        return IlIl11l111Il.array(I1IllI1I1lII)
    def Ill1lIl1lI1I(self, ll1IIIIlIlI1, IIll1II1IIl1):
        for lII11I111lI1 in self.l1I11IIIIIIl:
            II1l11II1lI1 = Il111I1IIIIl(IlIl11l111Il.array([ll1IIIIlIlI1, IIll1II1IIl1]), lII11I111lI1)
            if II1l11II1lI1 is not None:
                return False
        return True
    def l1IIlllIlIl1(self):
        self.body_turn_action = 'clockwise'
    def lIIIll1ll1l1(self):
        self.body_turn_action = 'counter_clockwise'
    def I11l1111II1I(self):
        self.body_turn_action = None
    def II1III1I111I(self):
        self.gun_turn_action = 'clockwise'
    def l111Illl1IlI(self):
        self.gun_turn_action = 'counter_clockwise'
    def ll111111lI1l(self):
        self.gun_turn_action = None
    def IlIIllIl1Il1(self):
        self.move_action = 'forward'
    def I1Il1lIlI1l1(self):
        self.move_action = 'backward'
    def lI1IlIll1l1I(self):
        self.move_action = None
    def llIIl1II1lII(self):
        self.shoot_action = True
    @property
    def lI1lllllIIII(self):
        return IlIl11l111Il.array([self.x, self.y])
    @property
    def lllI1lI1lll1(self):
        return IlIl11l111Il.array([self.enemy_x, self.enemy_y])
    @property
    def lIlI1IIl1llI(self):
        return llIlI1lIIlII(IlIl11l111Il.deg2rad(self.body_direction))
    @property
    def l1llll1I1Il1(self):
        return llIlI1lIIlII(IlIl11l111Il.deg2rad(self.gun_direction))
