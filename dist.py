import  streamlit as st
import numpy as np
from matplotlib import pyplot as plt
import math
import matplotlib
import seaborn as sns


st.title("Distillation Column")
st.subheader("McCabe thieli Method")
st.sidebar.title("Its all yours")
def main():
    xf = st.sidebar.slider('Feed Concentration (xf)', .04, .99, .45)
    xw = st.sidebar.slider('Bottoms concentration (xw)', .04, .99, .058)
    yd = st.sidebar.slider('Top concentration (yd)', .04, .99, .9)
    rv= st.sidebar.slider('Relative volatality', 1.5, 10.0, 3.0)
    q = st.sidebar.slider('vapour liquid ratio', .04, .99, .33)
    mul = st.sidebar.slider('Multiplies R mini', 1.0, 10.0, 2.0)
    x1 = np.linspace(0, 1, 11)
    y1 = np.linspace(0, 1, 11)
    xe = np.linspace(0, 1, 100)
    ye = rv * xe / (1 + (rv - 1) * xe)
    plt.plot(xe, ye)
    plt.plot(x1, y1)
    m1 = (-q / (1 - q))
    n1 = (xf / (1 - q))
    a = (m1 * rv - m1)
    b = (m1 + n1 * rv - n1 - rv)
    c = n1
    xd = yd
    yw = xw
    yf = xf
    x3 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x4 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if x3 > 0:
        p = x3
        l = (m1 * p) + n1
    elif x3 < 0:
        y = 0
    elif x4 > 0:
        p = x4
        l = (m1 * p) + n1
    elif x4 < 0:
        u = 0
    rm = (xd - l) / (l - p)
    R = rm * mul
    n2 = xd / (R + 1)
    m2 = (yd - n2) / yd
    mx = (n1 - n2) / (m2 - m1)
    my = (m1 * mx) + n1
    c = (my - yw) / (mx - xw)
    xs = np.linspace(xw, mx, 11)
    ys = c * (xs - xw) + yw
    xo = np.linspace(mx, yd, 11)
    yo = m2 * xo + n2
    xfe = np.linspace(mx, xf, 11)
    yfe = (m1 * xfe) + n1
    plt.plot(xfe, yfe)
    plt.plot(xo, yo)
    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")
    matplotlib.pyplot.annotate("yd", (xd, yd))
    matplotlib.pyplot.annotate("xw", (xw, yw))
    matplotlib.pyplot.annotate("xf", (xf, yf))
    h = np.zeros(20)
    t = np.zeros(20)
    c = yd
    v = (yd - my) / (yd - mx)
    z = (my - xw) / (mx - xw)
    for i in range(1, 20):
        h[0] = yd
        t[0] = yd
        h[i] = c / (rv * (1 - c) + c)
        if h[i] < xw:
            gh = i
            break;
        else:
            if h[i] > mx:
                t[i] = v * (h[i] - mx) + my
                c = t[i]
            else:
                t[i] = z * (h[i] - xw) + xw
                c = t[i]
    for i in range(gh - 1):
        gy = np.linspace(h[i + 1], h[i], gh + 1)
        hu = np.ones(gh + 1) * t[i]
        plt.plot(gy, hu, 'r')
        ay = np.linspace(t[i], t[i + 1], gh + 1)
        au = np.ones(gh + 1) * h[i + 1]
        plt.plot(au, ay, 'r')
    sns.set_style("darkgrid")
    st.pyplot()
    st.write("Number of stages required for current separation to take place=", gh - 1)
    if st.button('About'):
        st.write('Nibin joshy')
        st.write('nibin.j1721@saintgits.org')
        st.write('7902747751')
if __name__=='__main__':
    main()






