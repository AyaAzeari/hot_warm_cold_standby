#!/bin/bash
sqlite3 ~/cybersecurity/DB/orders.db ".backup '/Users/ayaazeari/cybersecurity/Backups/warm/orders_backup_$(date +"%Y%m%d%H%M%S").db'"
echo "Warm backup created at $(date)"
