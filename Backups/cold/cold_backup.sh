#!/bin/bash
cp ~/cybersecurity/DB/orders.db ~/cybersecurity/Backups/cold/orders_$(date +"%Y%m%d%H%M%S").db
echo "Cold backup created at $(date)"
