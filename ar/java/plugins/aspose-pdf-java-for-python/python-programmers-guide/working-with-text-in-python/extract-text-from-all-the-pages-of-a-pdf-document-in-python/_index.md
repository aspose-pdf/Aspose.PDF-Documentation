---
title: استخراج النص من جميع صفحات مستند PDF في بايثون
type: docs
weight: 30
url: /ar/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2021-06-05"
keywords: استخراج نص pdf بايثون
description: يشرح كيفية استخراج النص من صفحات PDF في بايثون باستخدام API تنسيق ملف PDF.
---

## استخراج النص من PDF باستخدام بايثون

لاستخراج النص من جميع صفحات مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء وحدة **ExtractTextFromAllPages**.

```python

# فتح المستند الهدف
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "تم استخراج النص بنجاح. تحقق من ملف الإخراج."

```

**تحميل الكود القابل للتنفيذ**

قم بتحميل **استخراج النص من جميع الصفحات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)