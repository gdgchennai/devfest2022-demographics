import json
import os

import pandas
from gutils.services.spreadsheets.v4.objects.others import ValueRange

from demographics.cloudflare import update_counter
from demographics.sheets import update_sheet
from demographics.townscript import Townscript

if __name__ == "__main__":
    
    print("Getting all registrations")
    pending_data, approved_data = Townscript.get_pending(), Townscript.get_approved()

    pending_json_dump = json.dumps(pending_data)
    approved_json_dump = json.dumps(approved_data)
    
    pending_data_frame = pandas.read_json(pending_json_dump)
    approved_data_frame = pandas.read_json(approved_json_dump)

    pending_csv_dump, approved_csv_dump = [], []

    pending_list = pending_data_frame.columns.tolist()
    pending_list = [" ".join(item.split("_")).title() for item in pending_list]

    approved_list = approved_data_frame.columns.tolist()
    approved_list = [" ".join(item.split("_")).title() for item in approved_list]
    
    pending_csv_dump.append(pending_list)
    approved_csv_dump.append(approved_list)

    pending_csv_dump += pending_data_frame.values.tolist()
    approved_csv_dump += approved_data_frame.values.tolist()

    pending_body, approved_body = ValueRange(values=pending_csv_dump), ValueRange(values=approved_csv_dump)

    print("Updating sheets of all pending invites")
    update_sheet(sheet_id=os.getenv('SHEET_ID'), data=pending_body, worksheet_name="PendingInvites")
    print("Updating sheets of all approved invites")
    update_sheet(sheet_id=os.getenv('SHEET_ID'), data=approved_body, worksheet_name="ApprovedInvites")
 

    counter = len(pending_data) + len(approved_data)
    print("Updating CF KV store")
    update_counter(counter)
    print("Process completed!")
