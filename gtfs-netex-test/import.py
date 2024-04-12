import duckdb
<<<<<<< Updated upstream
import csv


# Example usage
column_mapping = {
    'stop_lat': 'FLOAT',
    'stop_lon': 'FLOAT',
    'location_type': 'INTEGER',
    'wheelchair_boarding': 'INTEGER',
    'route_type': 'INTEGER',
    'continuous_pickup': 'INTEGER',
    'continuous_drop_off': 'INTEGER',
    'direction_id': 'INTEGER',
    'bikes_allowed': 'INTEGER',
    'arrival_time': 'VARCHAR(8)',
    'departure_time': 'VARCHAR(8)',
    'start_pickup_drop_off_window': 'VARCHAR(8)',
    'end_pickup_drop_off_window': 'VARCHAR(8)',
    'start_time': 'VARCHAR(8)',
    'end_time': 'VARCHAR(8)',
    'prior_notice_last_time': 'VARCHAR(8)',
    'prior_notice_start_time': 'VARCHAR(8)',
    'pickup_type': 'INTEGER',
    'drop_off_type': 'INTEGER',
    'shape_dist_traveled': 'FLOAT',
    'timepoint': 'INTEGER',
    'monday': 'INTEGER',
    'tuesday': 'INTEGER',
    'wednesday': 'INTEGER',
    'thursday': 'INTEGER',
    'friday': 'INTEGER',
    'saturday': 'INTEGER',
    'sunday': 'INTEGER',
    'start_date': 'VARCHAR(8)',
    'end_date': 'VARCHAR(8)',
    'date': 'VARCHAR(8)',
    'exception_type': 'INTEGER',
    'price': 'FLOAT',
    'payment_method': 'INTEGER',
    'transfers': 'INTEGER',
    'transfer_duration': 'INTEGER',
    'fare_media_type': 'INTEGER',
    'amount': 'FLOAT',
    'transfer_count': 'INTEGER',
    'duration_limit': 'INTEGER',
    'duration_limit_type': 'INTEGER',
    'fare_transfer_type': 'INTEGER',
    'shape_pt_lat': 'FLOAT',
    'shape_pt_lon': 'FLOAT',
    'shape_pt_sequence': 'INTEGER',
    'headway_secs': 'INTEGER',
    'exact_times': 'INTEGER',
    'transfer_type': 'INTEGER',
    'min_transfer_time': 'INTEGER',
    'pathway_mode': 'INTEGER',
    'is_bidirectional': 'INTEGER',
    'length': 'FLOAT',
    'traversal_time': 'INTEGER',
    'stair_count': 'INTEGER',
    'max_slope': 'FLOAT',
    'min_width': 'FLOAT',
    'level_index': 'FLOAT',
    'booking_type': 'INTEGER',
    'prior_notice_duration_min': 'INTEGER',
    'prior_notice_duration_max': 'INTEGER',
    'prior_notice_last_day': 'INTEGER',
    'prior_notice_start_day': 'INTEGER',
    'feed_start_date': 'VARCHAR(8)',
    'feed_end_date': 'VARCHAR(8)',
    'is_producer': 'INTEGER',
    'is_operator': 'INTEGER',
    'is_authority': 'INTEGER'
}
=======
import glob
from chardet.universaldetector import UniversalDetector
from os.path import exists
FOLDER="gtfs/"

def detectencoding(filename):
    detector = UniversalDetector()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    return detector.result

files= ["feed_info","agency","calendar_dates","routes","stops","shapes","trips","transfers","stop_times"]

con = duckdb.connect(database='gtfs2.duckdb')
with duckdb.cursor(con) as cur:
    for file in files:

        dtstring="""DROP TABLE IF EXISTS """+ file;
        cur.execute(dtstring)
        if exists(FOLDER+file+".txt"):
            encoding=detectencoding(FOLDER+file+".txt")
            if (encoding["encoding"]!="utf-8" and encoding["encoding"]!="UTF-8-SIG"):
                print ("encoding faulty for duckdb.read_csv. Can only safely process UTF-8: "+file)
            crstring="CREATE TABLE "+file+" AS SELECT * FROM read_csv('"+FOLDER+file+".txt', delim=',', header=true, auto_detect=true, normalize_names=true, ignore_errors=true)"
            #normalize_names should ignore the BOM in the header
            #ignore_errors generates an error table for later processing
            cur.execute(crstring)
        else:
            print("file missing: "+file)
>>>>>>> Stashed changes

import os
import json
def handle_file(filename: str, column_mapping: dict):
    if not os.path.isfile(filename):
        # TODO create sql for mandatory files
        return

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)

    this_mapping = {}
    for column in header:
        this_mapping[column] = column_mapping.get(column, 'VARCHAR')

    table = filename.split('/')[-1].replace('.txt', '')
    this_mapping_str = json.dumps(this_mapping)
    con = duckdb.connect(database='gtfs2.duckdb')
    with duckdb.cursor(con) as cur:
        cur.execute(f"""DROP TABLE IF EXISTS {table};""")
        cur.execute(f"""CREATE TABLE {table} AS SELECT * FROM read_csv('{filename}', delim=',', header=true, auto_detect=true, columns = {this_mapping_str});""")

    con.close()

handle_file('gtfs/feed_info.txt', column_mapping)
handle_file('gtfs/agency.txt', column_mapping)
handle_file('gtfs/calendar_dates.txt', column_mapping)
handle_file('gtfs/calendar.txt', column_mapping)
handle_file('gtfs/routes.txt', column_mapping)
handle_file('gtfs/stops.txt', column_mapping)
handle_file('gtfs/shapes.txt', column_mapping)
handle_file('gtfs/trips.txt', column_mapping)
handle_file('gtfs/transfers.txt', column_mapping)
handle_file('gtfs/stop_times.txt', column_mapping)

#    cur.execute("""ALTER TABLE shapes ADD COLUMN shape_dist_traveled FLOAT;""")

