---
title: استخراج النص من جميع صفحات مستند PDF باستخدام Python
linktitle: استخراج النص من جميع صفحات مستند PDF باستخدام Python
type: docs
weight: 30
url: /ar/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-10-05"
description: يشرح كيفية استخراج النص من صفحات PDF في Python باستخدام واجهة برمجة تطبيقات تنسيق ملف PDF.
---
## استخراج النص من PDF باستخدام Python

لاستخراج TextrFrom جميع صفحات مستند Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة استدعِ وحدة **ExtractTextFromAllPages**.

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

**تنزيل الشفرة القابلة للتشغيل**

تحميل\u0412\u00A0**استخراج النص من جميع الصفحات (Aspose.PDF)**\u0412\u00A0من\u0412\u00A0أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
