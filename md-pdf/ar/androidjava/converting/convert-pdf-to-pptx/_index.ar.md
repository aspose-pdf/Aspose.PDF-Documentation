---
title: تحويل PDF إلى PowerPoint
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 110
url: /androidjava/convert-pdf-to-powerpoint/
description: يتيح لك Aspose.PDF تحويل PDF إلى تنسيق PowerPoint. هناك طريقة لتحويل PDF إلى PPTX مع الشرائح كصور.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

لدينا API يسمى Aspose.Slides الذي يوفر ميزة إنشاء وتعديل عروض PPT/PPTX التقديمية. يقدم هذا الـ API أيضًا ميزة تحويل ملفات PPT/PPTX إلى تنسيق PDF. في Aspose.PDF for Java، قمنا بتقديم ميزة لتحويل مستندات PDF إلى تنسيق PPTX. خلال هذا التحويل، يتم تحويل الصفحات الفردية من ملف PDF إلى شرائح منفصلة في ملف PPTX.

{{% alert color="primary" %}}

جرب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

خلال تحويل PDF إلى PPTX، يتم عرض النص كنص حيث يمكنك تحديده/تحديثه، بدلاً من عرضه كصورة. يرجى ملاحظة أنه من أجل تحويل ملفات PDF إلى تنسيق PPTX، يوفر Aspose.PDF فئة باسم PptxSaveOptions. يتم تمرير كائن من فئة [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) كوسيط ثانٍ إلى طريقة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

تحقق من مقتطف الشيفرة التالي لحل مهامك مع تحويل PDF إلى تنسيق PowerPoint:

```java
 public void convertPDFtoPowerPoint() {
        // تحميل مستند PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // إنشاء كائن خيار حفظ Excel
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // حفظ المخرجات في PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // حفظ الملف بتنسيق PPTX
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```