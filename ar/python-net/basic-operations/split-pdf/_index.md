---
title: تقسيم ملفات PDF في بايثون
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /ar/python-net/split-pdf/
description: تعرف على كيفية تقسيم صفحات PDF إلى ملفات PDF منفصلة في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تقسيم صفحات PDF باستخدام بايثون
Abstract: تتناول المقالة عملية تقسيم صفحات PDF إلى ملفات فردية باستخدام Python، مع تسليط الضوء على فائدة هذه الميزة لإدارة مستندات PDF الكبيرة. وهي تشير إلى Aspose.PDF Splitter، وهي أداة عبر الإنترنت مصممة لإظهار وظيفة تقسيم PDF. توفر المقالة طريقة مفصلة لتحقيق ذلك في تطبيقات Python، بما في ذلك التكرار من خلال صفحات مستند PDF عبر «PageCollection» لكائن «المستند». لكل صفحة، يتم إنشاء كائن `Document` جديد، وتضاف الصفحة إليه، ويتم حفظ ملف PDF الجديد باستخدام طريقة `save () `. يوضح مقتطف شفرة Python المصاحب هذه العملية، ويعرض الخطوات اللازمة لتقسيم مستند PDF إلى ملفات منفصلة عن طريق التكرار في صفحاته وحفظ كل منها كملف PDF فردي.
---

يمكن أن يكون تقسيم صفحات PDF ميزة مفيدة لأولئك الذين يريدون تقسيم ملف كبير إلى صفحات منفصلة أو مجموعات من الصفحات.

استخدم سير العمل هذا عندما تحتاج إلى تقسيم ملفات PDF الكبيرة إلى ملفات ذات صفحة واحدة أو مجموعات مستندات أصغر للتوزيع أو المراجعة أو المعالجة النهائية.

## مثال مباشر

[موزع ملفات Aspose.PDF](https://products.aspose.app/pdf/splitter) هو تطبيق ويب مجاني عبر الإنترنت يسمح لك بالتحقيق في كيفية عمل وظيفة تقسيم العروض التقديمية.

[![أسبوز سبليت PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية في تطبيقات Python الخاصة بك. لتقسيم صفحات PDF إلى ملفات PDF ذات صفحة واحدة باستخدام Python، يمكن اتباع الخطوات التالية:

1. قم بالتمرير عبر صفحات مستند PDF من خلال [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) الكائنات [مجموعة الصفحات](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) مجموعة
1. لكل تكرار، قم بإنشاء كائن مستند جديد وإضافة الفرد [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) كائن في المستند الفارغ
1. احفظ ملف PDF الجديد باستخدام [حفظ ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة

## قم بتقسيم PDF إلى ملفات متعددة أو ملفات PDF منفصلة في Python

يوضح لك مقتطف شفرة Python التالي كيفية تقسيم صفحات PDF إلى ملفات PDF فردية.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```

## موضوعات المستندات ذات الصلة

- [العمل مع مستندات PDF في بايثون](/pdf/ar/python-net/working-with-documents/)
- [دمج ملفات PDF في بايثون](/pdf/ar/python-net/merge-pdf-documents/)
- [تحسين ملفات PDF في بايثون](/pdf/ar/python-net/optimize-pdf/)
- [معالجة مستندات PDF في Python](/pdf/ar/python-net/manipulate-pdf-document/)

