---
title: تحويل PDF إلى TXT باستخدام بايثون
linktitle: تحويل PDF إلى TXT
type: docs
weight: 20
url: ar/python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: تتيح لك مكتبة Aspose.PDF for Python عبر C++ تحويل ملفات PDF إلى تنسيق TXT باستخدام بايثون.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تحويل PDF إلى TXT

تدعم مكتبة Aspose.PDF for Python عبر C++ تحويل مستندات PDF إلى ملفات نصية عبر الخطوات التالية:

1. إنشاء مسار ملف الإدخال والإخراج
1. إنشاء مثيل لواجهة استخراج PDF باستخدام [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. ربط ملف PDF بالمستخرج باستخدام [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)
1. استخراج النص من ملف PDF باستخدام [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. كتابة النص المستخرج إلى ملف الإخراج
1. حفظ ملف PDF الناتج باستخدام طريقة 'document.save'.

يظهر مقطع الكود أدناه كيفية تحويل صورة JPG إلى PDF باستخدام بايثون عبر C++:

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # إنشاء مسار دليل البيانات
    dataDir = os.path.join(os.getcwd(), "samples")

    # إنشاء مسار الملف المدخل
    input_file = os.path.join(dataDir, "sample.pdf")

    # إنشاء مسار الملف المخرج
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # إنشاء مثيل من واجهة استخراج PDF
    extactor = apCore.facades_pdf_extractor_create()

    # ربط ملف PDF مع المستخرج
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # استخراج النص من ملف PDF
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # كتابة النص المستخرج إلى الملف المخرج
    with open(output_file, 'w') as f:
        f.write(text)
```