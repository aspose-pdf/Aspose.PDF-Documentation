---
title: استخراج الصور من ملف PDF باستخدام بايثون
linktitle: استخراج الصور من PDF
type: docs
weight: 20
url: /ar/python-net/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من ملف PDF باستخدام Aspose.PDF للبايثون
lastmod: "2023-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الصور من PDF عبر بايثون
Abstract: يوفر هذا المقال دليلًا مختصرًا حول استخراج الصور المضمنة من مستند PDF باستخدام بايثون. العملية تشمل ثلاث خطوات رئيسية - تحميل مستند PDF، الوصول إلى مورد الصورة، وحفظ الصورة إلى ملف. يستخدم مقتطف الشيفرة مكتبة Aspose.PDF لتسهيل هذه العمليات. في البداية، يتم تحميل مستند PDF من مسار محدد، ويتم الوصول إلى الصورة المطلوبة من موارد الصفحة الأولى. أخيرًا، يتم حفظ الصورة إلى ملف إخراج محدد باستخدام عملية إدخال/إخراج الملفات، مما يتيح مزيدًا من التحليل أو التحرير أو إعادة الاستخدام في مستندات أخرى.
---

يستخرج هذا المقتطف البرمجي الصور المضمنة من مستند PDF للتحليل المنفصل أو التحرير أو إعادة الاستخدام في مستندات أخرى:

1. تحميل مستند PDF
1. الوصول إلى مصدر الصورة
1. حفظ الصورة إلى ملف

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

