---
title: حذف التعليقات التوضيحية (الواجهات)
type: docs
weight: 10
url: /ar/java/delete-annotations/
description: يشرح هذا القسم كيفية حذف التعليقات التوضيحية باستخدام Aspose.PDF Facades باستخدام فئة PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يمكنك استخدام فئة [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) لحذف التعليقات التوضيحية، حسب نوع التعليق التوضيحي المحدد، من ملف PDF الموجود.
 من أجل القيام بذلك، تحتاج إلى إنشاء كائن [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) وربط ملف PDF المدخل باستخدام طريقة bindPdf. بعد ذلك، قم باستدعاء طريقة [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-)، مع تمرير معلمة السلسلة النصية، لحذف جميع التعليقات التوضيحية من الملف؛ تمثل معلمة السلسلة النصية نوع التعليق التوضيحي الذي سيتم حذفه. أخيرًا، استخدم طريقة save لحفظ ملف PDF المحدث.

يعرض مقتطف الشيفرة التالي كيفية حذف تعليق توضيحي حسب نوع التعليق التوضيحي المحدد.

```java
public static void DeleteAnnotation() {
        // افتح المستند
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("الرجاء إدخال الرقم:");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // احفظ ملف PDF المحدث
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
    ```
[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) يتيح لك حذف جميع التعليقات التوضيحية من ملف PDF الموجود.

أولاً، قم بإنشاء [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) وربط ملف PDF المدخل باستخدام طريقة BindPdf.

بعد ذلك، قم باستدعاء طريقة [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) لحذف جميع التعليقات التوضيحية من الملف، ثم استخدم طريقة Save لحفظ ملف PDF المحدّث. يوضح لك مقتطف الشيفرة التالي كيفية حذف جميع التعليقات التوضيحية من ملف PDF.

```java
public static void DeleteAllAnnotations() {
    // فتح المستند
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
    // حذف جميع التعليقات التوضيحية
    annotationEditor.deleteAnnotations();
    // حفظ ملف PDF المحدّث
    annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
}
```