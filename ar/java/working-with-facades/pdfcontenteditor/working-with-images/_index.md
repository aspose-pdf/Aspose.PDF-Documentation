---
title: العمل مع الصور
type: docs
weight: 30
url: /ar/java/working-with-image/
description: يشرح هذا القسم كيفية استبدال الصور باستخدام Aspose.PDF Facades - مجموعة أدوات للعمليات الشائعة مع PDF.
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## حذف الصور من صفحة معينة في PDF (Facades)

تسمح لك فئة [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) باستبدال الصور في ملف PDF موجود.
 [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) تساعدك هذه الطريقة في تحقيق هذا الهدف. تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) وربط ملف PDF المدخل باستخدام طريقة bindPdf. بعد ذلك، تحتاج إلى استدعاء طريقة [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) مع ثلاثة معلمات: رقم الصفحة، مؤشر الصورة المراد استبدالها، ومسار الصورة التي سيتم استبدالها.

يظهر لك مقتطف الشيفرة التالي كيفية استبدال صورة في ملف PDF موجود.

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        // حذف الصورة من الصفحة 2، والمؤشرات 1 و3
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## حذف جميع الصور من ملف PDF (واجهات)

يمكن حذف جميع الصور من ملف PDF باستخدام طريقة [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) من [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). قم باستدعاء طريقة [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) – التحميل الزائد بدون أي معلمات – لحذف جميع الصور، ثم قم بحفظ ملف PDF المحدث باستخدام طريقة Save.

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## استبدال الصور في ملف PDF (واجهات)

يمكنك استبدال الصور في ملف PDF باستخدام طريقة [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) من [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
   public static void ReplaceImage()
    {
        // تحرير محتوى PDF
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        // استبدال الصورة في الصفحة الثانية
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        // حفظ المستند بعد التعديل
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```