---
title: إضافة سلسلة HTML باستخدام DOM في بايثون
type: docs
weight: 10
url: /python-java/add-html-string-using-dom-in-python/
---

لإضافة سلسلة HTML في مستند PDF باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء وحدة **AddHtml**.

```python

# إنشاء كائن Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# تعيين معلومات الهامش
title.setMargin(margin)

# إضافة القطعة HTML إلى مجموعة الفقرات في الصفحة
page.getParagraphs().add(title)

# حفظ ملف PDF
doc.save(self.dataDir + 'html.output.pdf')

print "تمت إضافة HTML بنجاح"
```

**تحميل الكود التنفيذي**

قم بتحميل **Add HTML (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)