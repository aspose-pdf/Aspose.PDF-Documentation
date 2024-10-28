---
title: إضافة سلسلة HTML باستخدام DOM في بايثون
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2021-06-05"
keywords: html dom python, python html dom library
description: يوضح كيفية إضافة سلسلة HTML في DOM باستخدام بايثون مع مكتبة تنسيق ملفات PDF
---

## إضافة سلسلة HTML في PDF DOM باستخدام بايثون
لإضافة سلسلة HTML في مستند Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء وحدة **AddHtml**.

```python

# إنشاء كائن Document
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# تعيين معلومات الهوامش
title.setMargin(margin)

# إضافة جزء HTML إلى مجموعة الفقرات في الصفحة
page.getParagraphs().add(title)

# حفظ ملف PDF
doc.save(self.dataDir + 'html.output.pdf')

print "تمت إضافة HTML بنجاح"
```

**تحميل الكود التشغيلي**

حمل **Add HTML (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)