---
title: تسلسل ملفات PDF في بايثون
linktitle: تسلسل ملفات PDF في بايثون
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-python/
description: تعرف على كيفية ربط ملفات PDF متعددة في مستند PDF واحد في Python باستخدام Aspose.PDF، مما يبسط إدارة المستندات.
lastmod: "2026-06-09"
---
لتسلسل ملفات PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Open the source document
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Add the pages of the source document to the target document
pdf1.getPages().add(pdf1.getPages())

# Save the concatenated output file (the target document)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "New document has been saved, please check the output file"
```

** تنزيل كود التشغيل **

تنزيل В ** تسلسل ملفات PDF (Aspose.PDF)** В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
