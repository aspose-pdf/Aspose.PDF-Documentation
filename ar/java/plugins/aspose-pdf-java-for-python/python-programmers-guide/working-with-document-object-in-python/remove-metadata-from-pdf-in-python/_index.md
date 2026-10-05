---
title: إزالة البيانات الوصفية من PDF في Python
linktitle: إزالة البيانات الوصفية من PDF في Python
type: docs
weight: 70
url: /ar/java/remove-metadata-from-pdf-in-python/
description: اكتشف كيفية إزالة البيانات الوصفية من مستندات PDF في Python باستخدام Aspose.PDF، مع ضمان الخصوصية وأمان البيانات.
lastmod: "2026-10-05"
---
لإزالة البيانات الوصفية من مستند PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء الفئة **RemoveMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# save update document with new information
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Removed metadata successfully, please check output file."

```

**تنزيل الشفرة القابلة للتشغيل**

تحميل **Remove Metadata (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
