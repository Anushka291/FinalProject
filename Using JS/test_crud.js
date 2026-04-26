const puppeteer = require("puppeteer-core");
const path = require("path");
const fs = require("fs");
 
// Path to your index.html
const filePath =
  "file://" +
  path.resolve("D:/AISSMS IOIT/Third Year/6th Semester/DEVOPS/DevOps EndSem/PS 5/index.html");
 
// Common Edge installation paths on Windows
const edgePaths = [
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
];
 
const edgeExecutable = edgePaths.find(fs.existsSync) || edgePaths[0];
 
(async () => {
  const browser = await puppeteer.launch({
    executablePath: edgeExecutable,
    headless: false,
    channel: "msedge",
    args: [
      "--no-sandbox",
      "--disable-setuid-sandbox",
      "--remote-debugging-port=9222",
      "--disable-dev-shm-usage",
      "--disable-extensions",
      "--no-first-run",
      "--no-default-browser-check",
    ],
    timeout: 60000,
  });
 
  const page = await browser.newPage();
 
  // Listen for browser console logs
  page.on("console", (msg) => {
    const text = msg.text();
 
    if (text.includes("CREATED")) {
      console.log("TC-1 | Add Student    | PASS");
    } else if (text.includes("UPDATED")) {
      console.log("TC-2 | Edit Student   | PASS");
    } else if (text.includes("DELETED")) {
      console.log("TC-3 | Delete Student | PASS");
    }
  });
 
  // Detect browser/page close
  page.on("close", () => {
    console.log("\n---------------------------");
    console.log("TC-4 | Browser Close | PASS");
    console.log("---------------------------");
    process.exit(0);
  });
 
  await page.goto(filePath);
 
  console.log("---------------------------");
  console.log("Test Started");
  console.log("---------------------------");
 
  // Keep the process alive until the browser is closed
  await new Promise((resolve) => {
    browser.on("disconnected", () => {
      resolve();
    });
  });
})();
 