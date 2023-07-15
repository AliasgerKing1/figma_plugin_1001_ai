figma.showUI(__html__);
figma.ui.resize(1000, 700);

figma.ui.onmessage = (msg) => {
  if (msg.type === "cancel") {
    figma.closePlugin();
  }
};
