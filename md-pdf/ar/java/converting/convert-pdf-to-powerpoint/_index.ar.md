---
title: Convert PDF to Microsoft PowerPoint 
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
lastmod: "2021-11-19"
description: يسمح Aspose.PDF لك بتحويل PDF إلى تنسيق PowerPoint باستخدام Java. هناك طريقة لتحويل PDF إلى PPTX مع الشرائح كصور.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Java** يتيح لك تتبع تقدم تحويل PDF إلى PPTX.
لدينا واجهة برمجة تطبيقات تسمى Aspose.Slides التي تقدم ميزة إنشاء العروض التقديمية PPT/PPTX وكذلك التلاعب بها. توفر هذه الواجهة أيضًا ميزة تحويل ملفات PPT/PPTX إلى تنسيق PDF. في Aspose.PDF for Java، قمنا بتقديم ميزة لتحويل مستندات PDF إلى تنسيق PPTX. أثناء هذا التحويل، يتم تحويل الصفحات الفردية لملف PDF إلى شرائح منفصلة في ملف PPTX.

أثناء تحويل PDF إلى PPTX، يتم تقديم النص كنص حيث يمكنك تحديده/تحديثه، بدلاً من تقديمه كصورة.
 يرجى ملاحظة أنه من أجل تحويل ملفات PDF إلى تنسيق PPTX، توفر Aspose.PDF فئة باسم PptxSaveOptions. يتم تمرير كائن من فئة [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) كمعامل ثانٍ إلى طريقة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

تحقق من مقتطف الشفرة التالي لحل مهامك مع تحويل PDF إلى تنسيق PowerPoint:

```java
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_Simple();
        convertPDFtoPPTX_SlideAsImages();
        convertPDFtoPPTX_ProgresDetails();
    }

    public static void convertPDFtoPPTX_Simple() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // تحميل مستند PDF
        Document document = new Document(documentFileName);

        // إنشاء مثيل لـ PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // حفظ المخرج بتنسيق PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```

## تحويل PDF إلى PPTX مع الشرائح كصور

في حالة الحاجة إلى تحويل ملف PDF قابل للبحث إلى PPTX كصور بدلاً من النص القابل للاختيار، يوفر Aspose.PDF هذه الميزة عبر فئة [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). لتحقيق ذلك، قم بضبط خاصية SlidesAsImages لفئة [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) إلى 'true' كما هو موضح في عينة الشيفرة التالية.

يوضح مقتطف الشيفرة التالي عملية تحويل ملفات PDF إلى تنسيق PPTX مع الشرائح كصور.

```java
public static void convertPDFtoPPTX_SlideAsImages() {
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
    String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

    // تحميل مستند PDF
    Document document = new Document(documentFileName);
    // إنشاء مثيل لـ PptxSaveOptions
    PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();
    // حفظ المخرج بتنسيق PPTX
    pptxSaveOptions.setSlidesAsImages(true);

    document.save(pptxDocumentFileName, pptxSaveOptions);
    document.close();
}
```


## عرض التقدم على وحدة التحكم مع Aspose.PDF لـ Java يبدو هكذا:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.PptxSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * تحويل PDF إلى PPTX.
 */
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_ProgressDetails();
    }

    public static void convertPDFtoPPTX_ProgressDetails() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // تحميل مستند PDF
        Document document = new Document(documentFileName);

        // إنشاء مثيل PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // تحديد معالج تقدم مخصص
        pptx_save.setCustomProgressHandler(new ShowProgressOnConsole());

        // احفظ الإخراج بتنسيق PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```


## تفاصيل تقدم تحويل PPTX

تتيح لك Aspose.PDF لـ Java تتبع تقدم تحويل PDF إلى PPTX. توفر فئة [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) خاصية [CustomProgressHandler](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlSaveOptions) التي يمكن تعيينها لطريقة مخصصة لتتبع تقدم التحويل كما هو موضح في نموذج الكود التالي.

```java
package com.aspose.pdf.examples;

import java.time.LocalDateTime;

import com.aspose.pdf.ProgressEventType;
import com.aspose.pdf.UnifiedSaveOptions.ConversionProgressEventHandler;
import com.aspose.pdf.UnifiedSaveOptions.ProgressEventHandlerInfo;

class ShowProgressOnConsole extends ConversionProgressEventHandler{

    @Override
    public void invoke(ProgressEventHandlerInfo eventInfo) {        
        switch (eventInfo.EventType) {
            case ProgressEventType.TotalProgress:
                System.out.println(
                        String.format("%s  - تقدم التحويل : %d %%.", LocalDateTime.now().toString(), eventInfo.Value));
                break;
            case ProgressEventType.ResultPageCreated:
                System.out.println(String.format("%s  - تم إنشاء صفحة النتيجة %s من %d.", LocalDateTime.now().toString(),
                        eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.ResultPageSaved:
                System.out.println(String.format("%s  - تم تصدير صفحة النتيجة %d من %d.", LocalDateTime.now(), eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.SourcePageAnalysed:
                System.out.println(String.format("%s  - تم تحليل صفحة المصدر %d من %d.", LocalDateTime.now(),  eventInfo.Value, eventInfo.MaxValue));
                break;
            default:
                break;
        }
    }
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

يقدم لك Aspose.PDF for Java تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى PPTX باستخدام تطبيق مجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}