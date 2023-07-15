
figma.showUI(__html__);
figma.ui.resize(500, 400)


figma.ui.onmessage = (msg) => {
if (msg.type === "cancel") {
  figma.closePlugin()
}
}