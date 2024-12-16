---
title: العمل مع الصور باستخدام PdfContentEditor
type: docs
weight: 50
url: /ar/net/working-with-images-in-pdf
description: يشرح هذا القسم كيفية إضافة وحذف الصور باستخدام واجهات Aspose.PDF باستخدام فئة PdfContentEditor.
lastmod: "2021-06-24"
---

## حذف الصور من صفحة معينة من ملف PDF (واجهات)

لحذف الصور من صفحة معينة، تحتاج إلى استدعاء طريقة [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) مع معلمات رقم الصفحة والفهرس. المؤشر يمثل مصفوفة من الأعداد الصحيحة - مؤشرات الصور التي سيتم حذفها. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) ثم استدعاء طريقة [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1). بعد ذلك، يمكنك حفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

يوضح لك مقتطف الشيفرة التالي كيفية حذف الصور من صفحة معينة من ملف PDF.

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## حذف جميع الصور من ملف PDF (Facades)

يمكن حذف جميع الصور من ملف PDF باستخدام طريقة [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) من [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). استدعِ [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) الطريقة – التحميل الزائد بدون أي معلمات – لحذف جميع الصور، ثم احفظ ملف PDF المحدث باستخدام [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) الطريقة.

يظهر لك المقتطف البرمجي التالي كيفية حذف جميع الصور من ملف PDF.

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## استبدال صورة في ملف PDF (Facades)

يتيح لك [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) استبدال صورتك في ملف PDF، استدعِ لهذا الغرض [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) الطريقة، واحفظ النتيجة.

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```