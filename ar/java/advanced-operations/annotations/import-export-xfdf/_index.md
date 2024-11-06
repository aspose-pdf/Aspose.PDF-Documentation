---
title: استيراد وتصدير التعليقات التوضيحية إلى تنسيق XFDF
linktitle: استيراد وتصدير التعليقات التوضيحية إلى تنسيق XFDF
type: docs
weight: 40
url: ar/java/import-export-xfdf/
description: يمكنك استيراد وتصدير التعليقات باستخدام تنسيق XFDF باستخدام مكتبة Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF تعني تنسيق بيانات النماذج XML. إنه تنسيق ملف يعتمد على XML. يُستخدم هذا التنسيق لتمثيل بيانات النماذج أو التعليقات التوضيحية الموجودة في نموذج PDF. يمكن استخدام XFDF لأغراض عديدة مختلفة، ولكن في حالتنا، يمكن استخدامه إما لإرسال أو استقبال بيانات النماذج أو التعليقات التوضيحية إلى أجهزة كمبيوتر أو خوادم أخرى وما إلى ذلك، أو يمكن استخدامه لأرشفة بيانات النماذج أو التعليقات التوضيحية. في هذه المقالة، سنرى كيف أخذ Aspose.Pdf.Facades هذا المفهوم بعين الاعتبار وكيف يمكننا استيراد وتصدير بيانات التعليقات إلى ملف XFDF.

{{% /alert %}}

**Aspose.PDF for Java** هو مكون غني بالميزات عندما يتعلق الأمر بتحرير مستندات PDF.
 كما نعلم، يعتبر XFDF جانباً مهماً في التعامل مع نماذج PDF، وقد أخذ Aspose.Pdf.Facades في Aspose.PDF for Java هذا الأمر بعين الاعتبار جيداً، وقد وفر طرقاً لاستيراد وتصدير بيانات التعليقات التوضيحية إلى ملفات XFDF.

تحتوي فئة [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) على طريقتين للعمل مع استيراد وتصدير التعليقات التوضيحية إلى ملف XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) توفر الطريقة إمكانية تصدير التعليقات التوضيحية من مستند PDF إلى ملف XFDF، بينما [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) تتيح لك الطريقة استيراد التعليقات التوضيحية من ملف XFDF موجود. من أجل استيراد أو تصدير التعليقات التوضيحية، نحتاج إلى تحديد أنواع التعليقات التوضيحية. يمكننا تحديد هذه الأنواع في شكل تعداد ثم تمرير هذا التعداد كحجة لأي من هذه الطرق. بهذه الطريقة، سيتم استيراد أو تصدير التعليقات التوضيحية للأنواع المحددة فقط إلى ملف XFDF.

يوضح لك مقتطف الشفرة التالي كيفية تصدير التعليقات التوضيحية إلى ملف XFDF:

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * استيراد التعليقات التوضيحية من ملف XFDF XML Forms Data Format (XFDF)
     * تم إنشاؤه بواسطة Adobe Acrobat، وهو تطبيق تأليف PDF؛ يخزن أوصاف
     * عناصر نموذج الصفحة وقيمها، مثل الأسماء والقيم لحقول النص؛
     * يستخدم لحفظ بيانات النموذج التي يمكن استيرادها إلى مستند PDF.
     * يمكنك استيراد بيانات التعليقات التوضيحية من ملف XFDF إلى PDF باستخدام
     * طريقة ImportAnnotationsFromXfdf في فئة PdfAnnotationEditor.
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // إنشاء كائن PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // ربط مستند PDF بمحرر التعليقات التوضيحية
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // تصدير التعليقات التوضيحية
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

يوضح مقطع الشيفرة التالي كيفية استيراد التعليقات إلى ملف XFDF:

```java
public static void ImportAnnotationXFDF()
{
    // إنشاء كائن PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // إنشاء مستند PDF جديد
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // استيراد التعليقات
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // حفظ ملف PDF الناتج
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## طريقة أخرى لتصدير/استيراد التعليقات دفعة واحدة

في الشيفرة أدناه، تتيح طريقة ImportAnnotations استيراد التعليقات مباشرةً من مستند PDF آخر.

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // إنشاء كائن PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // إنشاء مستند PDF جديد
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // يسمح محرر التعليقات باستيراد التعليقات من عدة مستندات PDF،
        // ولكن في هذا المثال، نستخدم مستند واحد فقط.
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // حفظ ملف PDF الناتج
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```