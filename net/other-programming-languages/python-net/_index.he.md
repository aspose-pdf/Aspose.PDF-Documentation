---
title: שימוש ב-Aspose.PDF עבור .NET עם Python
linktitle: אינטגרציה עם Python
type: docs
weight: 100
url: /net/python-net/
description: במדריך זה תגלה את הדרכים השונות ליצירה ושינוי קבצי PDF ב-Python.
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

מאמר זה מתאר דוגמאות קצרות איך ליצור PDF באמצעות אינטגרציה של Aspose.PDF עבור .NET עם Python.

## דרישות מוקדמות

כדי להשתמש ב-Aspose.PDF עבור .NET ב-Python אנא השתמש ב-`requirments.txt` הבא:

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

כמו כן, עליך לשים את `Aspose.PDF.dll` בתיקייה הרצויה.

## יצירת PDF פשוט באמצעות Python

לעבודה נצטרך לאינטגרט [PythonNet](https://github.com/pythonnet/pythonnet) ליישום שלנו ולבצע כמה הגדרות.

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```
### צור מסמך פשוט

בואו ניצור PDF פשוט עם הטקסט הקלאסי "שלום, עולם". להסבר מפורט יותר, אנא עקבו אחרי [דף זה](https://docs.aspose.com/pdf/net/hello-world-example/)

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # Initialize document object
        document = Document()
        # Add page
        page = document.Pages.Add()
        # Add text to new page
        textFragment = TextFragment("Hello,world!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # Create TextBuilder object
        textBuilder = TextBuilder(page)

        # Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment)

        document.Save("HelloWorld_out.pdf")
```
## יצירת מסמך PDF מורכב באמצעות פייתון

הדוגמאות הבאות מראות כיצד אפשר ליצור מסמך PDF מורכב עם תמונות וטבלאות. הדוגמה מבוססת על [הדף הבא](https://docs.aspose.com/pdf/net/complex-pdf-example/).

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... דילוג ...

    # יצירת מסמך מורכב
    def run_complex(self):

        # אתחול אובייקט מסמך
        document = Document()
        # הוספת דף
        page = document.Pages.Add()

        # הוספת תמונה
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # הוספת כותרת
        header = TextFragment("מסלולי מעבורת חדשים בסתיו 2020")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # הוספת תיאור
        descriptionText = "על המבקרים לרכוש כרטיסים באינטרנט ומספר הכרטיסים מוגבל ל-5,000 ליום. \
        שירות המעבורת פועל בחצי קיבולת ולוח זמנים מצומצם. צפויות תורים."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)


        # הוספת טבלה
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("עיר יציאה")
        headerRow.Cells.Add("אי יציאה")

        i=0
        while(i<headerRow.Cells.Count):
            headerRow.Cells[i].BackgroundColor = Color.Gray
            headerRow.Cells[i].DefaultCellTextState.ForegroundColor = Color.WhiteSmoke
            i+=1

        time = TimeSpan(6, 0, 0)
        incTime = TimeSpan(0, 30, 0)

        i=0
        while (i<10):
            dataRow = table.Rows.Add()
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            time=time.Add(incTime)
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            i+=1

        page.Paragraphs.Add(table)

        document.Save(self.dataDir + "Complex.pdf")
```
## איך להריץ יצירת PDFs בWindows

קטע זה מראה איך להריץ את הדוגמאות לעיל במחשב Windows. הנחנו ש- `class HelloWorld` נמצאת בקובץ `example_get_started.py`.
אם אתה מריץ את הגרסה הניסיונית של Aspose.PDF ל-.NET, עליך להעביר מחרוזת ריקה כ- `license_path`.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```
