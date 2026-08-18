---
title: أضف نصًا إلى ملف PDF الموجود باستخدام Python
linktitle: أضف نصًا إلى ملف PDF الموجود باستخدام Python
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-06-09"
description: مثال على التعليمات البرمجية حول كيفية إضافة نص أو كتابته في مستند Pdf باستخدام Python مع مكتبة PDF.
---
## كتابة أو إضافة نص في PDF باستخدام بايثون

لإضافة سلسلة نصية في مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء وحدة **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("main text")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# Save PDF file
doc.save(self.dataDir + "Text_Added.pdf")
print "Text added successfully"
```

** تنزيل كود التشغيل **

تنزيلВ **إضافة نص (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
