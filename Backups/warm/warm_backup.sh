#!/bin/bash
while true
do
    backup_path="/Users/ayaazeari/cybersecurity/Backups/warm/orders_backup_$(date +%Y%m%d%H%M%S).db"
    sqlite3 ~/cybersecurity/DB/orders.db ".backup '${backup_path}'"
    echo "Warm backup created at ${backup_path}"
    sleep 600  # 10 minutes
done
