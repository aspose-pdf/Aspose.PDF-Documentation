---
title: استخراج النص من جميع صفحات مستند PDF في بايثون
type: docs
weight: 30
url: ar/python-java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
---

لاستخراج النص من جميع صفحات مستند PDF باستخدام **Aspose.PDF Java for Python**، قم فقط باستدعاء وحدة **ExtractTextFromAllPages**.

```python
# افتح المستند الهدف
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

**تنزيل الكود الجاري**

قم بتنزيل **استخراج النص من جميع الصفحات (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)