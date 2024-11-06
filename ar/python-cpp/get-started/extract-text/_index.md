---
title: استخراج النص من PDF باستخدام بايثون
linktitle: استخراج النص من PDF
type: docs
weight: 10
url: ar/python-cpp/extract-text/
description: يصف هذا القسم كيفية استخراج النص من مستند PDF باستخدام مكتبة بايثون.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

استخراج النص من PDF ليس بالأمر السهل. لا تستطيع العديد من برامج قراءة PDF استخراج النص من صور PDF أو ملفات PDF الممسوحة ضوئيًا. لكن أداة **Aspose.PDF for Python via C++** تتيح لك استخراج النص بسهولة من جميع ملفات PDF.

تحقق من مقتطف الشيفرة واتبع الخطوات لاستخراج النص من PDF الخاص بك:

1. استيراد مكتبة Aspose.PDF لبايثون
2. إنشاء كائن مستخرج جديد، والذي يستخدم لاستخراج النصوص والصور من مستندات PDF.
3. ربط كائن المستخرج بملف PDF، وهو مصدر الاستخراج.
4. استخراج جميع النصوص من مستند PDF ووضعه في بعض المتغيرات.

1. افعل ما تريد، اطبع النص المستخرج إلى وحدة التحكم، ابحث عن بعض الأجزاء إلخ

```python
from AsposePdfPython import *

extactor = Extract()
extractor_bind_pdf(extactor,"blank_pdf_document.pdf")
text = extractor_extract_text(extactor)

print(text)
```