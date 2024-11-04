---
title: إضافة نص إلى ملف PDF موجود في بايثون
type: docs
weight: 20
url: /python-java/add-text-to-an-existing-pdf-file-in-python/
---

لإضافة نص في مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء وحدة **AddText**.

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

**تحميل الكود القابل للتنفيذ**

قم بتحميل **Add Text (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)