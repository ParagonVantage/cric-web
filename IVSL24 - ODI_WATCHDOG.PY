import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import re

# Define the path to your Excel file and HTML file
excel_file_path = r'C:\Users\agney\OneDrive\Desktop\gg\cric-web\IND_TOUR_SL_ODI.xlsx'
html_file_path = r'C:\Users\agney\OneDrive\Desktop\gg\cric-web\IVSL24 - ODI.HTML'

# Function to read data from Excel and update the HTML file
def update_html():
    try:
        # Read Excel file
        df_careerbat = pd.read_excel(excel_file_path, sheet_name='CAREERBAT')
        df_careerbwl = pd.read_excel(excel_file_path, sheet_name='CAREERBWL')
        df_IVSLD1bat = pd.read_excel(excel_file_path, sheet_name='SERIESBAT')
        df_IVSLD1bwl = pd.read_excel(excel_file_path, sheet_name='SERIESBWL')

        # Convert dataframes to HTML tables
        careerbat_table = df_careerbat.to_html(index=False, classes='dataTable')
        careerbwl_table = df_careerbwl.to_html(index=False, classes='dataTable')
        IVSLD1bat_table = df_IVSLD1bat.to_html(index=False, classes='dataTable')
        IVSLD1bwl_table = df_IVSLD1bwl.to_html(index=False, classes='dataTable')

        # Read the HTML template
        with open(html_file_path, 'r') as file:
            html_content = file.read()

        # Update the HTML content with new tables using regex to find the correct table ids
        new_html_content = re.sub(
            r'<table id="careerbat_table">.*?</table>',
            f'<table id="careerbat_table">{careerbat_table}</table>',
            html_content,
            flags=re.DOTALL
        )
        new_html_content = re.sub(
            r'<table id="careerbwl_table">.*?</table>',
            f'<table id="careerbwl_table">{careerbwl_table}</table>',
            new_html_content,
            flags=re.DOTALL
        )
        new_html_content = re.sub(
            r'<table id="gt20bat_table">.*?</table>',
            f'<table id="gt20bat_table">{IVSLD1bat_table}</table>',
            new_html_content,
            flags=re.DOTALL
        )
        new_html_content = re.sub(
            r'<table id="gt20bwl_table">.*?</table>',
            f'<table id="gt20bwl_table">{IVSLD1bwl_table}</table>',
            new_html_content,
            flags=re.DOTALL
        )

        # Write the updated HTML content back to the file
        with open(html_file_path, 'w') as file:
            file.write(new_html_content)

        print("Successfully updated the HTML file.")
    except Exception as e:
        print(f"Error updating the HTML file: {e}")

# Watchdog event handler to detect file changes
class ExcelFileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == excel_file_path:
            print(f"{event.src_path} has been modified. Updating HTML file...")
            update_html()

# Set up the watchdog observer
observer = Observer()
event_handler = ExcelFileEventHandler()
# Ensure the directory path is correct
directory_to_watch = os.path.dirname(excel_file_path)
observer.schedule(event_handler, path=directory_to_watch, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
