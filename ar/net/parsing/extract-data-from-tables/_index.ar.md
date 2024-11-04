---
title: استخراج البيانات من جدول في PDF باستخدام C#
linktitle: استخراج البيانات من جدول
type: docs
weight: 40
url: /net/extract-data-from-table-in-pdf/
description: تعلم كيفية استخراج الجداول من PDF باستخدام Aspose.PDF لـ .NET في C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الجداول من PDF برمجيًا

استخراج الجداول من ملفات PDF ليس مهمة سهلة لأن الجدول يمكن أن يتم إنشاؤه بطرق متعددة.

Aspose.PDF لـ .NET لديه أداة لتسهيل استرجاع الجداول. لاستخراج بيانات الجدول يجب أن تقوم بالخطوات التالية:

1. فتح المستند - إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)؛
1. إنشاء كائن [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber).

1. `TableList` هي قائمة من [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). للحصول على التاريخ قم بالتنقل خلال `TableList` وتعامل مع [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) و [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist)
2. تحتوي كل [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) على مجموعة [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments). يمكنك معالجتها لأغراضك الخاصة.

يعمل الشفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

المثال التالي يظهر استخراج الجدول من جميع الصفحات:

```csharp
public static void Extract_Table()
{
    // تحميل مستند PDF المصدر
    var filePath="<... أدخل مسار ملف pdf هنا ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);                       
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Table");
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {                                 
                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                            sb.Append(seg.Text);
                        Console.Write($"{sb.ToString()}|");
                    }                           
                }
                Console.WriteLine();
            }
        }
    }
}
```
```
## استخراج جدول في منطقة محددة من صفحة PDF

كل جدول ممتص له خاصية [مستطيل](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) التي تصف موقع الجدول على الصفحة.

لذا، إذا كنت بحاجة لاستخراج الجداول الموجودة في منطقة معينة، يجب أن تعمل مع إحداثيات محددة.

شفرة البرنامج التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

المثال التالي يوضح كيفية استخراج جدول محدد بتعليق مربع:

```csharp
public static void Extract_Marked_Table()
{
    // تحميل مستند PDF المصدر
    var filePath="<... أدخل مسار ملف pdf هنا ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);  
    var page = pdfDocument.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
    absorber.Visit(page);

    foreach (AbsorbedTable table in absorber.TableList)
    {
        var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
        (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
        (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
        (squareAnnotation.Rect.URY > table.Rectangle.URY);

        if (isInRegion)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {

                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            sb.Append(seg.Text);
                        }
                        var text = sb.ToString();
                        Console.Write($"{text}|");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
```
## استخراج بيانات الجدول من ملف PDF وتخزينها في ملف CSV

المثال التالي يوضح كيفية استخراج الجدول وتخزينه كملف CSV.
لمعرفة كيفية تحويل PDF إلى جدول بيانات Excel يرجى الرجوع إلى مقال [تحويل PDF إلى Excel](/pdf/net/convert-pdf-to-excel/).

هذا الجزء من الكود يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void Extract_Table_Save_CSV()
{
    // للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // تحميل مستند PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // إنشاء كائن خيارات حفظ Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // حفظ الناتج بتنسيق XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```
