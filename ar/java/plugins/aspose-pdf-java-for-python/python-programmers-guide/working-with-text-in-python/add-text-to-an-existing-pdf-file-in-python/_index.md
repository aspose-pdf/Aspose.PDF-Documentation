---
title: إضافة نص إلى ملف PDF موجود باستخدام Python
linktitle: إضافة نص إلى ملف PDF موجود باستخدام Python
type: docs
weight: 20
url: /ar/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-10-05"
description: مثال على الكود لكيفية إضافة أو كتابة نص في مستند PDF باستخدام Python مع مكتبة PDF.
---
## كتابة أو إضافة نص في PDF باستخدام Python

لإضافة سلسلة نصية في مستند PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء وحدة **AddText**.

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

**تنزيل الشفرة القابلة للتشغيل**

Download **Add Text (Aspose.PDF)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
