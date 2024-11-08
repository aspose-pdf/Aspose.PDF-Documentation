---
title: تحويل PDF إلى نص في بايثون
linktitle: تحويل PDF إلى تنسيقات أخرى
type: docs
weight: 90
url: /ar/python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: تحويل, PDF, EPUB, LaText, نص, XPS, بايثون
description: يوضح هذا الموضوع كيفية تحويل ملف PDF إلى تنسيقات ملفات أخرى مثل النص باستخدام بايثون.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF إلى نص

يدعم **Aspose.PDF for Python** تحويل مستند PDF بالكامل وصفحة واحدة إلى ملف نصي.

### تحويل مستند PDF إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام فئة 'TextDevice'.

1. إنشاء مسار الملف المدخلات والمخرجات
1. إنشاء مثيل لواجهة استخراج PDF باستخدام [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. ربط ملف PDF بالمستخرج باستخدام [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)

1. استخراج النص من ملف PDF باستخدام [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. كتابة النص المستخرج إلى ملف الإخراج
1. حفظ ملف PDF الناتج باستخدام طريقة 'document.save'.

يوضح مقتطف الشيفرة التالي كيفية استخراج النصوص من جميع الصفحات.

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```