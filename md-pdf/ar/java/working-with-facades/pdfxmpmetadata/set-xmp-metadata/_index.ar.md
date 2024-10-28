---
title: ضبط بيانات XMP الوصفية لملف PDF موجود - الواجهات
type: docs
weight: 20
url: /java/set-xmp-metadata/
description: تشرح هذه القسم كيفية ضبط بيانات XMP الوصفية باستخدام Aspose.PDF Facades باستخدام فئة PdfXmpMetadata.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

من أجل ضبط بيانات XMP الوصفية في ملف PDF، تحتاج إلى إنشاء كائن [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) وربط ملف PDF باستخدام طريقة [bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-).
 يمكنك استخدام طريقة setByDefaultMetadataProperties(..) من فئة [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) لإضافة خصائص مختلفة. أخيراً، قم باستدعاء طريقة [save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) من فئة [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata).

يوضح لك مقتطف الشيفرة التالي كيفية إضافة بيانات تعريف XMP في ملف PDF.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}