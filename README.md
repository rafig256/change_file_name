# مرتب‌ساز اسکن صفحات کتاب / Book Scan Page Sorter

## توضیحات فارسی / Persian Description


این یک تجربه ی شخصی است. من قصد داشتم یک کتاب 286 صفحه ای رو اسکن کنم. قرار بود اسکن از صفحه ی 5 تا 286 باشد. اما اسکنر من تک رو بود و می توانست در هر مرتبه یک روی برگه را اسکن کند. من یک مرتبه صفحات زوج را از انتهای کتاب اسکن کردم. سپس یک مرتبه هم از ابتدای کتاب تا انتها فقط صفحات فرد رو اسکن کردم. بعد از اسکن متوجه شدم که دو صفحه ی 228 و 230 جا افتاده اند. 

مرتب کردن این صفحات به صورت دستی کار طاقت فرسایی بود. پس دست به کار شدم تا یک کد ساده ی پایتون مشکل را حل کند. این رو به اشتراک می گذارم تا اگر مشکل مشابهی داشتید با تغییر فرمولها (در حال حاضر سه قسمت است) برای شما هم قابلیت استفاده داشته باشد

این یک اسکریپت ساده پایتون است که برای مرتب‌سازی و تغییر نام فایل‌های اسکن شده صفحات کتاب (با فرمت JPEG) طراحی شده است. این اسکریپت قادر است سناریوهای مختلف اسکن را مدیریت کند، از جمله:

* اسکن از پشت کتاب (صفحات به ترتیب نزولی).
* اسکن صفحات فرد به صورت جداگانه.
* ترکیب این دو نوع اسکن برای مرتب‌سازی کل کتاب.
* نادیده گرفتن صفحات اسکن نشده (مانند صفحات 228 و 230 در این مورد خاص).
* تغییر نام فایل‌ها به شماره صفحه اصلی کتاب.

**نحوه استفاده:**

1.  مطمئن شوید که پایتون 3 بر روی سیستم شما نصب است.
2.  فایل اسکریپت `sort_pages.py` را در کنار پوشه‌ای که حاوی فایل‌های اسکن شده با فرمت `IMG_XXXX.jpg` است، قرار دهید.
3.  خط فرمان (Command Prompt یا Terminal) را باز کنید و به مسیری که فایل اسکریپت در آن قرار دارد، بروید.
4.  دستور زیر را اجرا کنید:
    ```bash
    python sort_pages.py
    ```
5.  هنگامی که از شما خواسته شد، مسیر پوشه حاوی فایل‌های اسکن شده را وارد کنید و Enter بزنید.
6.  پس از اتمام کار اسکریپت، فایل‌های مرتب شده و تغییر نام یافته در پوشه‌ای جدید به نام `result` در داخل پوشه اصلی قرار خواهند گرفت.

## English Description

This is a personal experience. I intended to scan a 286-page book, with the scan supposed to cover pages 5 to 286. However, my scanner was single-sided and could only scan one side of a sheet at a time. I scanned the even-numbered pages from the end of the book in one pass. Then, I scanned only the odd-numbered pages from the beginning to the end in another pass. After scanning, I realized that two pages, 228 and 230, were missing.

Manually sorting these pages was a tedious task. So, I set out to write a simple Python code to solve the problem. I am sharing this so that if you have a similar issue, you can also use it by modifying the formulas (currently in three sections) to suit your needs.

This is a simple Python script designed to sort and rename scanned book page files (in JPEG format). The script can handle various scanning scenarios, including:

* Scanning from the back of the book (pages in descending order).
* Scanning odd-numbered pages separately.
* Combining these two types of scans to sort the entire book.
* Ignoring unscanned pages (such as pages 228 and 230 in this specific case).
* Renaming the files to their original book page numbers.

**How to Use:**

1.  Ensure that Python 3 is installed on your system.
2.  Place the script file `sort_pages.py` in the same directory as the folder containing your scanned files (named in the format `IMG_XXXX.jpg`).
3.  Open your command prompt (Command Prompt or Terminal) and navigate to the directory where the script is located.
4.  Run the script using the following command:
    ```bash
    python sort_pages.py
    ```
5.  When prompted, enter the path to the folder containing the scanned files and press Enter.
6.  Once the script finishes, the sorted and renamed files will be located in a new folder named `result` within the original folder.