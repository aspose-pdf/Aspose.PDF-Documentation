---
title: إضافة نص إلى ملف PDF موجود باستخدام Python
type: docs
weight: 20
url: /ar/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2021-06-05"
keywords: إضافة نص pdf بايثون، كتابة نص pdf بايثون
description: مثال على الكود لكيفية إضافة أو كتابة نص في مستند Pdf باستخدام Python مع مكتبة PDF.
---

## كتابة أو إضافة نص في PDF باستخدام Python

لإضافة سلسلة نصية في مستند Pdf باستخدام **Aspose.PDF Java for Python**، قم باستدعاء وحدة **AddText** ببساطة.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("النص الرئيسي")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# حفظ ملف PDF
doc.save(self.dataDir + "Text_Added.pdf")
print "تمت إضافة النص بنجاح"
```


**تنزيل الكود الجاري**

قم بتنزيل **إضافة نص (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)