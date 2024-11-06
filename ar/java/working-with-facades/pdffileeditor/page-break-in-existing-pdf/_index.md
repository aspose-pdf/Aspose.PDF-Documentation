---
title: فاصل الصفحة في PDF موجود
type: docs
weight: 30
url: ar/java/page-break-in-existing-pdf/
description: يشرح هذا القسم كيفية إضافة فاصل صفحات في ملف PDF موجود باستخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

كتخطيط افتراضي، يتم إضافة المحتويات داخل ملفات PDF في تخطيط من الأعلى إلى اليسار وصولاً إلى الأسفل إلى اليمين. بمجرد أن تتجاوز المحتويات حافة الصفحة السفلية، يحدث فاصل الصفحة. ومع ذلك، قد تواجه متطلبًا لإدراج فاصل صفحة بناءً على الحاجة. تمت إضافة طريقة تسمى AddPageBreak(...) في فئة [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) لتحقيق هذا المتطلب.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-com.aspose.pdf.IDocument-com.aspose.pdf.IDocument-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)

1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-java.lang.String-java.lang.String-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html?is-external=true)

- src هو مستند المصدر/مسار المستند/تيار مع مستند المصدر
- dest هو مستند الوجهة/مسار حيث سيتم حفظ المستند/تيار حيث سيتم حفظ المستند
- PageBreak هو مصفوفة من كائنات فواصل الصفحات. لديها خاصيتان: مؤشر الصفحة حيث يجب وضع فاصل الصفحة والموقع العمودي لفاصل الصفحة على الصفحة.

## مثال 1 (إضافة فاصل صفحة)

```java
   public static void PageBrakeExample01() {
        // إنشاء مثيل للمستند
        Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
        // إنشاء مثيل مستند فارغ
        Document dest = new Document();
        // إنشاء كائن PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        // حفظ الملف الناتج
        dest.Save(_dataDir + "PageBreak_out.pdf");
    }
```


## مثال 2

```java
  public static void PageBrakeExample02() {
        // إنشاء كائن PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();

        fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf", _dataDir + "PageBreakWithDestPath_out.pdf",
                new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
    }
```

## مثال 3

```java
 public static void PageBrakeExample03() {
        Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
        Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(src, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        dest.Close();
        src.Close();
    }
```