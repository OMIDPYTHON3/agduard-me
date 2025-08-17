import os
import requests
from flask import Flask, request, Response

app = Flask(__name__)

# لیست بلاک (هاست‌ها)
blocklist = set()

# آپدیت لیست بلاک از اینترنت
def update_blocklist():
    global blocklist
    urls = [
        "https://adaway.org/hosts.txt",
        "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
        "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"
    ]
    newlist = set()
    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            for line in r.text.splitlines():
                if line and not line.startswith("#"):
                    parts = line.split()
                    if len(parts) >= 2:
                        newlist.add(parts[1].strip().lower())
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    blocklist = newlist
    print(f"Blocklist updated: {len(blocklist)} domains")

# اولین بار آپدیت
update_blocklist()

@app.route("/dns-query", methods=["POST", "GET"])
def doh_query():
    q = request.get_data()

    # اینجا خیلی ساده → باید decode کنیم که چه دامنه‌ایه
    # ولی برای تست میشه raw کوئری رو به کلودفلر فوروارد کنیم
    # و بعد نتیجه رو بدیم (فیلتر کامل نیاز به dnslib یا dns.message داره)

    # فوروارد مستقیم به کلودفلر
    r = requests.post(
        "https://cloudflare-dns.com/dns-query",
        headers={"Content-Type": "application/dns-message"},
        data=q,
        timeout=5
    )
    return Response(r.content, content_type="application/dns-message")

@app.route("/update-blocklist")
def manual_update():
    update_blocklist()
    return "Blocklist updated"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)