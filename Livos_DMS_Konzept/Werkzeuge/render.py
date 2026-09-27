"""Rendert jede Seite einer .drawio-Datei mit dem offiziellen draw.io-Viewer (headless Chromium) als PNG.
python3 render.py datei.drawio outdir [seitenindex ...]"""
import sys, json, os, re, asyncio
from html import escape as html_escape
from playwright.async_api import async_playwright
VIEWER = "https://viewer.diagrams.net/js/viewer-static.min.js"
async def main(path, outdir, only):
    xml = open(path, encoding="utf-8").read()
    n = len(re.findall(r"<diagram ", xml))
    os.makedirs(outdir, exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1800, "height": 1300})
        for i in range(n):
            if only and i not in only: continue
            cfg = json.dumps({"xml": xml, "page": i, "toolbar": "", "lightbox": False, "nav": False, "resize": True, "fit": False})
            html = f"<html><body style='margin:0;background:#fff'><div id='g' class='mxgraph' data-mxgraph=\"{html_escape(cfg, quote=True)}\"></div></body></html>"
            await pg.set_content(html)
            await pg.add_script_tag(path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'viewer.js'))
            await pg.evaluate("() => { if (window.GraphViewer) GraphViewer.processElements(); }")
            await pg.wait_for_selector("#g svg", timeout=60000)
            await pg.wait_for_timeout(600)
            el = await pg.query_selector("#g")
            await el.screenshot(path=os.path.join(outdir, f"page_{i:02d}.png"))
            print("ok", i)
        await b.close()
if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2], [int(a) for a in sys.argv[3:]]))
