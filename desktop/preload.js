"use strict";
const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("pegasus", {
  status: () => ipcRenderer.invoke("status"),
  connect: (code) => ipcRenderer.invoke("connect", code),
  openExternal: (url) => ipcRenderer.invoke("open-external", url),
});
