---
title: Page Break in existing PDF
type: docs
weight: 30
url: /net/page-break-in-existing-pdf/
description: يوضح هذا القسم كيفية فصل الصفحات في ملف PDF موجود باستخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

كمخطط افتراضي، يتم إضافة المحتويات داخل ملفات PDF من الأعلى إلى اليسار إلى الأسفل إلى اليمين. بمجرد أن تتجاوز المحتويات هامش الصفحة السفلي، يحدث فاصل الصفحة. ومع ذلك قد تواجه متطلبًا لإدراج فاصل صفحة حسب الحاجة. تم إضافة طريقة تسمى AddPageBreak(...) في فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) لتحقيق هذا المتطلب.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2) 1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/addpagebreak)

- src هو المستند المصدر/مسار المستند/التدفق مع المستند المصدر
- dest هو المستند الوجهة/المسار حيث سيتم حفظ المستند/التدفق حيث سيتم حفظ المستند
- PageBreak هو مصفوفة من كائنات فواصل الصفحات. يحتوي على خاصيتين: مؤشر الصفحة حيث يجب وضع فاصل الصفحة والموقع الرأسي لفاصل الصفحة على الصفحة.

## مثال 1 (إضافة فاصل صفحة)

```csharp
public static void PageBrakeExample01()
{
    // إنشاء مثيل للمستند
    Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
    // إنشاء مثيل لمستند فارغ
    Document dest = new Document();
    // إنشاء كائن PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[]
    {
        new PdfFileEditor.PageBreak(1, 450)
    });
    // حفظ الملف الناتج
    dest.Save(_dataDir + "PageBreak_out.pdf");
}
```
## مثال 2

```csharp
public static void PageBrakeExample02()
{
    // إنشاء كائن PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();

    fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf",
        _dataDir + "PageBreakWithDestPath_out.pdf",
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
}
```

## مثال 3

```csharp
public static void PageBrakeExample03()
{
    Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
    Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(src, dest,
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
    dest.Close();
    src.Close();
}
```