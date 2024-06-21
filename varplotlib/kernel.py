from matplotlib.pyplot import figure, plot as mplot, show as mshow, xlabel, ylabel, xticks, yticks, rc, ylim, legend


def plot(X, Y, label, col, lineWidth, xLabel, yLabel, yLimMin, yLimMax, figSize=(8, 6), fontsize=18, yRot=0, axWidth=2):
    figure(figsize=figSize)
    mplot(X, Y, label=label, color=col, linewidth=lineWidth)

    rest(fontsize, xLabel, yLabel, yRot, axWidth, yLimMin, yLimMax)


def plots(X, Y, label, col, lineWidth, xLabel, yLabel, yLimMin, yLimMax, figSize=(8, 6), fontsize=18, legendsize=15, yRot=0, axWidth=2):
    figure(figsize=figSize)
    for i in range(len(X)):
        mplot(X[i], Y[i], label=label[i], color=col[i], linewidth=lineWidth[i])

    rest(fontsize, legendsize, xLabel, yLabel, yRot, axWidth, yLimMin, yLimMax)


def rest(fontsize, legendsize, xLabel, yLabel, yRot, axWidth, yLimMin, yLimMax):
    legend(fontsize=legendsize)
    xlabel(xLabel, fontsize=fontsize)
    ylabel(yLabel, fontsize=fontsize, rotation=yRot)
    xticks(fontsize=fontsize)
    yticks(fontsize=fontsize)
    rc("axes", linewidth=axWidth)
    ylim(yLimMin, yLimMax)
    mshow()
