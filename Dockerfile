# از ایمیج رسمی AdGuard Home استفاده می‌کنیم
FROM adguard/adguardhome:latest

# مسیر پیش‌فرض کانفیگ
VOLUME ["/opt/adguardhome/work", "/opt/adguardhome/conf"]

# AdGuard روی پورت 3000 (پنل) و 53/80/443 گوش می‌ده
EXPOSE 53/udp
EXPOSE 53/tcp
EXPOSE 80
EXPOSE 443
EXPOSE 3000

CMD ["/opt/adguardhome/AdGuardHome", "-c", "/opt/adguardhome/conf/AdGuardHome.yaml", "-w", "/opt/adguardhome/work"]