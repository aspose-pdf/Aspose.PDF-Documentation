---
title: تحويل PDF إلى PowerPoint
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 110
url: /ar/androidjava/convert-pdf-to-powerpoint/
description: تتيح لك Aspose.PDF تحويل PDF إلى تنسيق PowerPoint. هناك طريقة تتيح إمكانية تحويل PDF إلى PPTX مع الشرائح كصور.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

لدينا واجهة برمجة تطبيقات تسمى Aspose.Slides توفر ميزة إنشاء وتعديل عروض PPT/PPTX. هذه الواجهة أيضاً توفر ميزة تحويل ملفات PPT/PPTX إلى تنسيق PDF. في Aspose.PDF for Java، قدمنا ميزة تحويل مستندات PDF إلى تنسيق PPTX. أثناء هذا التحويل، يتم تحويل الصفحات الفردية لملف PDF إلى شرائح منفصلة في ملف PPTX.

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

أثناء التحويل من PDF إلى PPTX، يتم عرض النص كنص يمكن تحديده/تحديثه، بدلاً من عرضه كصورة. يرجى ملاحظة أنه من أجل تحويل ملفات PDF إلى تنسيق PPTX، توفر Aspose.PDF فئة تسمى PptxSaveOptions. كائن من الـ [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) يتم تمرير الفئة كمعامل ثانٍ إلى [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) طريقة.

تحقق من مقتطف الشفرة التالي لحل مهامك المتعلقة بتحويل PDF إلى تنسيق PowerPoint:

```java
 public void convertPDFtoPowerPoint() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Save the output in PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Save the file into PPTX format
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

