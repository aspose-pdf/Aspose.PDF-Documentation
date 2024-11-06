---
title: استخدام Aspose.PDF لـ .NET مع Python
linktitle: التكامل مع Python
type: docs
weight: 100
url: ar/net/python-net/
description: في هذا البرنامج التعليمي، ستستكشف الطرق المختلفة لإنشاء وتعديل ملفات PDF في Python.
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

يصف هذا المقال أمثلة مختصرة حول كيفية إنشاء PDF باستخدام التكامل Aspose.PDF لـ .NET مع Python.

## المتطلبات الأساسية

لاستخدام Aspose.PDF لـ .NET في Python يرجى استخدام `requirments.txt` التالي:

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

أيضًا، يجب وضع `Aspose.PDF.dll` في المجلد المطلوب.

## إنشاء PDF بسيط باستخدام Python

للعمل سنحتاج إلى دمج [PythonNet](https://github.com/pythonnet/pythonnet) في تطبيقنا وإجراء بعض الإعدادات.

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```
### إنشاء مستند بسيط

لنقم بإنشاء ملف PDF بسيط بالنص الكلاسيكي "مرحباً، العالم". للحصول على شرح مفصل، يرجى التوجه إلى [هذه الصفحة](https://docs.aspose.com/pdf/net/hello-world-example/)

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # تهيئة كائن المستند
        document = Document()
        # إضافة صفحة
        page = document.Pages.Add()
        # إضافة نص إلى الصفحة الجديدة
        textFragment = TextFragment("مرحبا، العالم!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # إنشاء كائن TextBuilder
        textBuilder = TextBuilder(page)

        # إلحاق قطعة النص بصفحة PDF
        textBuilder.AppendText(textFragment)

        document.Save("HelloWorld_out.pdf")
```

## إنشاء مستند PDF معقد باستخدام Python

توضح الأمثلة التالية كيف يمكننا إنشاء مستند PDF معقد بالصور والجداول. هذا المثال مبني على [الصفحة التالية](https://docs.aspose.com/pdf/net/complex-pdf-example/).

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... تم تخطيه ...

    # إنشاء وثيقة معقدة
    def run_complex(self):

        # تهيئة كائن الوثيقة
        document = Document()
        # إضافة صفحة
        page = document.Pages.Add()

        # إضافة صورة
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # إضافة العنوان
        header = TextFragment("مسارات العبارات الجديدة في خريف 2020")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # إضافة الوصف
        descriptionText = "يجب على الزوار شراء التذاكر عبر الإنترنت والتذاكر محدودة لـ 5000 في اليوم. \
        تعمل خدمة العبارات بنصف الطاقة وبجدول مخفض. توقع وجود طوابير."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)


        # إضافة جدول
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("مدينة المغادرة")
        headerRow.Cells.Add("جزيرة المغادرة")

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
## كيفية تشغيل توليد ملفات PDF في ويندوز

يُظهر هذا المقتطف كيفية تشغيل الأمثلة أعلاه على جهاز الكمبيوتر الشخصي ويندوز. نفترض أن `class HelloWorld` موجود في ملف `example_get_started.py`.
إذا كنت تشغل النسخة التجريبية من Aspose.PDF لـ .NET، يجب أن تمرر سلسلة فارغة كـ `license_path`.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```
