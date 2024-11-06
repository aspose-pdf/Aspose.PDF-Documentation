---
title: تقسيم ملفات PDF برمجياً باستخدام بايثون
linktitle: تقسيم ملفات PDF
type: docs
weight: 20
url: ar/python-cpp/split-pdf-document/
keywords: تقسيم pdf إلى ملفات متعددة، تقسيم pdf إلى ملفات منفصلة، تقسيم pdf بايثون
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات بايثون الخاصة بك عبر C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكن أن يكون تقسيم صفحات PDF ميزة مفيدة لأولئك الذين يرغبون في تقسيم ملف كبير إلى صفحات منفصلة أو مجموعات من الصفحات.

## مثال حي

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) هو تطبيق ويب مجاني عبر الإنترنت يتيح لك استكشاف كيفية عمل وظيفة تقسيم العروض التقديمية.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات بايثون C++ الخاصة بك. لتقسيم صفحات PDF إلى ملفات PDF ذات صفحة واحدة باستخدام بايثون، يمكن اتباع الخطوات التالية:

يقوم المقطع البرمجي بإعداد الدلائل والمسارات اللازمة للملفات، ويفتح مستند PDF، ثم يقوم بالدوران عبر كل صفحة في المستند.
 لكل صفحة، يتم إنشاء مستند جديد، ونسخ الصفحة الحالية إلى المستند الجديد، وحفظ المستند الجديد كملف PDF منفصل بتسمية محددة.

1. افتح المستند المدخل
1. قم بتهيئة عدد الصفحات
1. حلقة تمر عبر جميع صفحات المستند

## تقسيم ملف PDF إلى ملفات متعددة أو ملفات PDF منفصلة في بايثون

يوضح مقتطف الشيفرة التالي في بايثون كيفية تقسيم صفحات PDF إلى ملفات PDF فردية.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # فتح المستند
    document = apw.Document(inputFile)

    pageCount = 1

    # حلقة تمر عبر جميع الصفحات

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```