---
title: تحويل PDF إلى Microsoft PowerPoint
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /ar/php-java/convert-pdf-to-powerpoint/
lastmod: "2024-05-20"
description: يسمح لك Aspose.PDF بتحويل PDF إلى تنسيق PowerPoint باستخدام PHP. هناك طريقة تتيح إمكانية تحويل PDF إلى PPTX مع شرائح كصور.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يسمح لك **Aspose.PDF for PHP** بتتبع تقدم تحويل PDF إلى PPTX. لدينا واجهة برمجة تطبيقات تسمى Aspose.Slides توفر ميزة لإنشاء وتعديل عروض PPT/PPTX التقديمية. توفر هذه الواجهة أيضًا ميزة لتحويل ملفات PPT/PPTX إلى تنسيق PDF. في Aspose.PDF for PHP، قمنا بإدخال ميزة لتحويل مستندات PDF إلى تنسيق PPTX. خلال هذا التحويل، يتم تحويل الصفحات الفردية لملف PDF إلى شرائح منفصلة في ملف PPTX.

خلال تحويل PDF إلى PPTX، يتم عرض النص كنص يمكنك تحديده/تحديثه، بدلاً من عرضه كصورة.
 يرجى ملاحظة أنه من أجل تحويل ملفات PDF إلى تنسيق PPTX، توفر Aspose.PDF فئة باسم PptxSaveOptions. يتم تمرير كائن من فئة [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) كوسيط ثاني إلى طريقة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

تحقق من مقتطف الشيفرة التالي لحل مهامك مع تحويل PDF إلى تنسيق PowerPoint:

```php
// تحميل مستند PDF المدخل
$document = new Document($inputFile);

// إنشاء مثيل من PptxSaveOptions
$saveOption = new PptxSaveOptions();

// حفظ مستند PDF كملف PPTX
$document->save($outputFile, $saveOption);
```

## تحويل PDF إلى PPTX مع شرائح كصور

في حالة إذا كنت بحاجة إلى تحويل PDF قابل للبحث إلى PPTX كصور بدلاً من نص قابل للتحديد، توفر Aspose.PDF مثل هذه الميزة عبر فئة [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). لتحقيق ذلك، قم بتعيين خاصية SlidesAsImages في فئة [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) إلى 'true' كما هو موضح في نموذج الكود التالي.

يظهر مقتطف الكود التالي عملية تحويل ملفات PDF إلى تنسيق PPTX (الشرائح كصور).

```php
// تحميل مستند PDF المدخل
$document = new Document($inputFile);

// إنشاء مثيل من PptxSaveOptions
$saveOption = new PptxSaveOptions();
$saveOption->setSlidesAsImages(true);

// حفظ مستند PDF كملف PPTX
$document->save($outputFile, $saveOption);

    public static void ConvertPDFtoPPTX_SlideAsImages() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX_out.pptx").toString();

        // تحميل مستند PDF
        Document doc = new Document(pdfDocumentFileName);
        // إنشاء مثيل من PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();
        // حفظ الناتج بتنسيق PPTX
        pptx_save.setSlidesAsImages(true);

        doc.save(pptxDocumentFileName, pptx_save);
    }
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

يقدم لك Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى PPTX باستخدام تطبيق مجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}