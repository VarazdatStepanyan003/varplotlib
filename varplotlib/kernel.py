from matplotlib.pyplot import figure, plot as mplot, show as mshow, savefig as msavefig, xlabel, ylabel, xticks, yticks, rc, ylim, legend

def plot(X, Y, label="plot", col="black", lineWidth=2.5, xLabel="x", yLabel="y", yLimMin=0, yLimMax=0, lineStyle="-", figSize=(8, 6), fontsize=18, legendsize=15, yRot=0, axWidth=2):
    figure(figsize=figSize)
    mplot(X, Y, label=label, color=col, linewidth=lineWidth, linestyle=lineStyle)

    rest(fontsize, legendsize, xLabel, yLabel, yRot, axWidth, yLimMin, yLimMax)

    return figure


def plots(X, Y, label=["plot","plot","plot","plot"], col=["black", "blue", "red", "green"], lineWidth=[2.5, 2.5, 2.5, 2.5], lineStyle=["-","--","-.",":"], xLabel="x", yLabel="y", yLimMin=0, yLimMax=0, figSize=(8, 6), fontsize=18, legendsize=15, yRot=0, axWidth=2):
    figure(figsize=figSize)

    for i in range(len(Y)):
        mplot(X[i], Y[i], label=label[i], color=col[i], linewidth=lineWidth[i], linestyle=lineStyle[i])

    rest(fontsize, legendsize, xLabel, yLabel, yRot, axWidth, yLimMin, yLimMax)

    return figure


def rest(fontsize, legendsize, xLabel, yLabel, yRot, axWidth, yLimMin, yLimMax):
    legend(fontsize=legendsize)
    xlabel(xLabel, fontsize=fontsize)
    ylabel(yLabel, fontsize=fontsize, rotation=yRot)
    xticks(fontsize=fontsize)
    yticks(fontsize=fontsize)
    rc("axes", linewidth=axWidth)
    if yLimMax > yLimMin:
        ylim(yLimMin, yLimMax)


def show():
    mshow()

def savefig(a):
    msavefig(a)
