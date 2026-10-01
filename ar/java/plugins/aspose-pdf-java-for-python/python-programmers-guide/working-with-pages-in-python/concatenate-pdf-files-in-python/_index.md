---
title: دمج ملفات PDF في بايثون
linktitle: دمج ملفات PDF في بايثون
type: docs
weight: 10
url: /ar/java/concatenate-pdf-files-in-python/
description: تعلم كيفية دمج ملفات PDF متعددة في مستند PDF واحد باستخدام Aspose.PDF في بايثون، لتبسيط إدارة المستندات.
lastmod: "2026-10-01"
---
لدمج ملفات PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء الفئة **ConcatenatePdfFiles**.

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

**تحميل الكود التشغيلي**

DownloadВ **دمج ملفات PDF (Aspose.PDF)**В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
