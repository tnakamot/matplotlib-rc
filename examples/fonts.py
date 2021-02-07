import matplotlib.font_manager

for f in matplotlib.font_manager.fontManager.ttflist:
    print(f.name)
