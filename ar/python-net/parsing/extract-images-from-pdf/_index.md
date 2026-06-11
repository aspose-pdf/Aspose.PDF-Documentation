---
title: استخراج الصور من PDF باستخدام Python
linktitle: استخراج الصور من PDF
type: docs
weight: 20
url: /ar/python-net/extract-images-from-the-pdf-file/
description: تعرف على كيفية استخراج الصور المضمنة من ملفات PDF باستخدام Aspose.PDF لـ Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الصور من PDF عبر Python
Abstract: تشرح هذه المقالة كيفية استخراج الصور المضمنة من مستند PDF باستخدام Aspose.PDF لـ Python. ويغطي فتح ملف PDF المصدر مع فئة المستند، والوصول إلى صورة من مجموعة موارد الصفحة، وحفظ XImage المستخرج في ملف خارجي لإعادة استخدامه أو فحصه أو معالجته النهائية.
---

استخدم [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) لفتح ملف PDF، ثم قم بالوصول إلى موارد الصفحة لاسترداد ملف [صورة](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) الكائن وحفظه كملف منفصل. هذا الأسلوب مفيد عندما تحتاج إلى إعادة استخدام الصور أو فحص الأصول المستخرجة أو إنشاء عمليات سير عمل معالجة الصور من محتوى PDF.

1. افتح ملف PDF كملف `Document`.
1. قم بالوصول إلى مورد الصورة من الصفحة المستهدفة.
1. استرجع المطلوب `XImage` من مجموعة صور الصفحة.
1. احفظ الصورة المستخرجة إلى ملف الإخراج.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
