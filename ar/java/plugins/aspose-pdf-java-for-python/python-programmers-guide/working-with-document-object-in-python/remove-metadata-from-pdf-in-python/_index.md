---
title: إزالة البيانات الوصفية من PDF في بايثون
linktitle: إزالة البيانات الوصفية من PDF في بايثون
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
description: تعرف على كيفية إزالة البيانات التعريفية من مستندات PDF في Python باستخدام Aspose.PDF، مما يضمن الخصوصية وأمن البيانات.
lastmod: "2026-06-09"
---
لإزالة البيانات الوصفية من مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **RemoveMetadata**.

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

** تنزيل كود التشغيل **

تنزيلВ **إزالة البيانات الوصفية (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
