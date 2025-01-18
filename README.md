# Hot, Warm, and Cold Standby for SQLite Databases

This project demonstrates three database recovery strategies for an SQLite database (`orders.db`) simulating an e-commerce scenario. 



## **Project Structure**
```
hot_warm_cold_standby/
├── DB/
│   └── orders.db       # Primary database 
├── Backups/
│   ├── cold/           # Stores Cold Standby backups
│   ├── warm/           # Stores Warm Standby backups
│   └── hot/            # Stores Hot Standby backups
├── simulate_activity.py # Simulates database activity
├── cold_backup.sh       # Script for Cold Standby
├── warm_backup.sh       # Script for Warm Standby
├── hot_standby.py       # Script for Hot Standby
```




## Implementation

**1. Database Setup**

We created a directory structure to organize the database and backups. The `DB` folder stores the active database (`orders.db`), while the `Backups` folder holds subdirectories for each standby method. Inside `orders.db`, we defined two tables: `orders` (stores transactions) and `reviews` (stores user reviews).

**2. Simulating Database Activity**

A Python script (`simulate_activity.py`) generates random transactions and reviews, adding them to the database every 10 seconds. which helps simulate real-world database activity.

**3. Recovery Strategies**

The project implements three recovery strategies with varying trade-offs between data loss and recovery time:

* **Cold Standby (Manual Backups):**
    - Involves creating full database backups periodically (e.g., daily).
    - Implemented using the `cold_backup.sh` script, which can be run manually or scheduled via cron.
    -  **Run the Script Manually**:
```bash
./cold_backup.sh
```


* **Warm Standby (Incremental Backups):**
    - Creates periodic backups that capture changes since the last backup (in our case every 10 minutes).
    - Implemented using the `warm_backup.sh` script
      
    - **Run the Script Manually**:
```bash
./warm_backup.sh
```
* **Hot Standby (Real-time Backups):**
    - Continuously creates backups of the database (every 1 second)
    - Implemented using the `hot_standby.py` script, which continuously copies the database.
    - **Run the Script**:
```bash
python3 hot_standby.py
```

**Simulate a Failure**:
Delete or corrupt the primary database file:
```bash
rm DB/orders.db
```

**Recovery Process**:
1. **Cold Standby**:
   Restore the latest snapshot from the `Backups/cold/` folder:

   ```cp Backups/cold/orders_<timestamp>.db DB/orders.db```

3. **Warm Standby**:
   Restore the most recent backup from the `Backups/warm/` folder:

   ```cp Backups/warm/orders_backup_<timestamp>.db DB/orders.db```

4. **Hot Standby**:
   Restore the real-time backup from the `Backups/hot/` folder:
   ```cp Backups/hot/orders.db DB/orders.db```
