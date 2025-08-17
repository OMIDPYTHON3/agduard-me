FROM adguard/adguardhome:latest
COPY AdGuardHome.yaml /opt/adguardhome/conf/AdGuardHome.yaml
CMD ["/opt/adguardhome/AdGuardHome", "-c", "/opt/adguardhome/conf/AdGuardHome.yaml", "-w", "/opt/adguardhome/work"]