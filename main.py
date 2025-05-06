import os
import re
import shutil

def sort_and_rename_scanned_pages(source_folder):
    """
    فایل‌های اسکن شده با فرمت IMG_XXXX.jpg را از پوشه مبدأ مرتب کرده،
    نام آن‌ها را به ترتیب شماره صفحه تغییر داده و به پوشه 'result' منتقل می‌کند.
    شماره فایل‌ها مطابق با شماره صفحات خواهد بود و صفحات اسکن نشده نادیده گرفته می‌شوند.
    """
    all_files = [f for f in os.listdir(source_folder) if f.startswith("IMG_") and f.endswith(".jpg")]
    if not all_files:
        print(f"هیچ فایل با فرمت IMG_XXXX.jpg در پوشه '{source_folder}' پیدا نشد.")
        return

    scanned_pages = {}

    for filename in all_files:
        match = re.search(r"IMG_(\d+)\.jpg", filename)
        if match:
            file_number = int(match.group(1))

            if 1 <= file_number <= 28:
                page_number = 286 - 2 * (file_number - 1)
                scanned_pages[filename] = page_number
            elif 29 <= file_number <= 139:
                page_number = 226 - 2 * (file_number - 29)
                scanned_pages[filename] = page_number
            elif 140 <= file_number <= 280:
                page_number = 5 + 2 * (file_number - 140)
                scanned_pages[filename] = page_number

    # ایجاد پوشه result اگر وجود نداشته باشد
    result_folder = os.path.join(source_folder, "result")
    os.makedirs(result_folder, exist_ok=True)

    for original_filename, page_number in scanned_pages.items():
        if page_number != 228 and page_number != 230:
            new_filename = f"{page_number}.jpg"
            old_filepath = os.path.join(source_folder, original_filename)
            new_filepath = os.path.join(result_folder, new_filename)
            try:
                shutil.copy2(old_filepath, new_filepath) # کپی با حفظ метадата
            except FileNotFoundError:
                print(f"فایل '{old_filepath}' پیدا نشد.")

    print("مرتب سازی و تغییر نام فایل ها با موفقیت انجام شد. شماره فایل ها مطابق با شماره صفحات است و صفحات اسکن نشده نادیده گرفته شده اند. فایل های مرتب شده در پوشه 'result' قرار دارند.")

if __name__ == "__main__":
    source_directory = input("لطفاً مسیر پوشه حاوی فایل های اسکن شده را وارد کنید: ")
    sort_and_rename_scanned_pages(source_directory)