---
title: استخراج النص من جميع صفحات وثيقة PDF في بايثون
linktitle: استخراج النص من جميع صفحات وثيقة PDF في بايثون
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-06-09"
description: يشرح كيفية استخراج النص من صفحات PDF في بايثون باستخدام API بتنسيق ملف PDF.
---
## استخراج النص من PDF باستخدام بايثون

لاستخراج مستند TextrFrom All Pages Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء وحدة **ExtractTextFromAllPages**.

```python

# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

** تنزيل كود التشغيل **

تنزيلВ **استخراج النص من جميع الصفحات (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
