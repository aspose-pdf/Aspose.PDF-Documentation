---
title: حفظ مستند PDF
linktitle: حفظ
type: docs
weight: 30
url: ar/java/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF باستخدام مكتبة Aspose.PDF لـ Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## حفظ مستند PDF في نظام الملفات

يمكنك حفظ مستند PDF الذي تم إنشاؤه أو التلاعب به في نظام الملفات باستخدام طريقة Save من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
عندما لا تقدم نوع التنسيق (الخيارات)، يتم حفظ المستند بتنسيق Aspose.PDF v.1.7 (*.pdf).

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // إجراء بعض التعديلات، مثل إضافة صفحة فارغة جديدة
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```


## حفظ مستند PDF إلى دفق

يمكنك أيضًا حفظ مستند PDF الذي تم إنشاؤه أو التلاعب به إلى دفق باستخدام التحميل الزائد لطرق الحفظ.

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // إجراء بعض التلاعب، مثل إضافة صفحة فارغة جديدة
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
```

## حفظ مستند PDF في تطبيقات الويب

لحفظ المستندات في تطبيقات الويب، يمكنك استخدام الطرق المقترحة أعلاه. بالإضافة إلى ذلك، تحتوي فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) على طريقة حفظ محملة فوقها.
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // الحصول على الملف الخاص بك كـ InputStream
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // نسخه إلى OutputStream الخاص بالاستجابة
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("خطأ في كتابة الملف إلى دفق الإخراج. كان اسم الملف '{}'", fileName, ex);
    //         throw new RuntimeException("خطأ إدخال/إخراج في كتابة الملف إلى دفق الإخراج");
    //     }
    // }
```


للحصول على تفسير أكثر تفصيلاً، يرجى متابعة القسم [عرض]().

## حفظ بصيغة PDF/A أو PDF/X

PDF/A هو إصدار قياسي من ISO لصيغة المستندات المحمولة (PDF) للاستخدام في أرشفة وحفظ الوثائق الإلكترونية على المدى الطويل. يختلف PDF/A عن PDF في أنه يحظر الميزات غير المناسبة للأرشفة طويلة الأمد، مثل ربط الخطوط (على العكس من تضمين الخطوط) والتشفير. تشمل متطلبات ISO لمشاهدي PDF/A إرشادات إدارة الألوان، دعم الخطوط المدمجة، وواجهة مستخدم لقراءة التعليقات التوضيحية المدمجة.

PDF/X هو جزء من معيار ISO لـ PDF. الغرض من PDF/X هو تسهيل تبادل الرسوميات، وبالتالي فإنه يحتوي على سلسلة من المتطلبات المتعلقة بالطباعة التي لا تنطبق على ملفات PDF القياسية.

في كلا الحالتين، يتم استخدام طريقة الحفظ لتخزين الوثائق، بينما يجب إعداد الوثائق باستخدام طريقة التحويل.

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```