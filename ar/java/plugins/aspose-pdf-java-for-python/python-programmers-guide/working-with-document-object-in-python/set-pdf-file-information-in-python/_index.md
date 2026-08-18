---
title: قم بتعيين معلومات ملف PDF في بايثون
linktitle: قم بتعيين معلومات ملف PDF في بايثون
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
description: تعرف على كيفية تعيين معلومات ملف PDF مثل المؤلف والعنوان والمزيد في Python باستخدام Aspose.PDF لتنظيم المستندات.
lastmod: "2026-06-09"
---
لتحديث معلومات مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **SetPdfFileInfo**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF Information");
doc_info.setTitle("Setting PDF Document Information");

# save update document with new information

doc.save(self.dataDir + "Updated_Information.pdf")
print "Update document information, please check output file."
```

** تنزيل كود التشغيل **

تنزيلВ **تعيين معلومات ملف PDF (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
