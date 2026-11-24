"""Build ../index.html from template.html.
Placeholders: %%PHOTO%% (face.jpg, pilot + ID card) and %%BODY%% (illia.webp, cutout for postcards).
Run: python3 src/build.py   (from the repo root)"""
import base64, os
D = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(D, "template.html"), encoding="utf-8").read()
face = "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(D, "face.jpg"), "rb").read()).decode()
body = "data:image/webp;base64," + base64.b64encode(open(os.path.join(D, "illia.webp"), "rb").read()).decode()
full = s.replace("%%PHOTO%%", face).replace("%%BODY%%", body)
head, rest = full.split("</style>", 1)
PRE = '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="theme-color" content="#5fb4f0">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="Illias Flug">\n<link rel="apple-touch-icon" href="icon-180.png">\n<link rel="icon" href="icon-180.png">\n'
open(os.path.join(D, "..", "index.html"), "w", encoding="utf-8").write(PRE + head + "</style>\n</head>\n<body>\n" + rest + "\n</body>\n</html>\n")
print("index.html written")
