---
title: تقسيم ملفات PDF برمجيًا باستخدام بايثون
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /ar/python-net/split-pdf-document/
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF منفصلة في تطبيقات بايثون الخاصة بك.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تقسيم صفحات PDF باستخدام بايثون
Abstract: تناقش المقالة عملية تقسيم صفحات PDF إلى ملفات منفصلة باستخدام بايثون، مع إبراز فائدة هذه الميزة لإدارة مستندات PDF الكبيرة. وتشير إلى Aspose.PDF Splitter، وهي أداة عبر الإنترنت صُممت لتوضيح وظيفة تقسيم PDF. تقدم المقالة طريقة مفصلة لتحقيق ذلك في تطبيقات بايثون، تشمل iterating عبر صفحات مستند PDF عبر مجموعة `PageCollection` لكائن `Document`. لكل صفحة، يتم إنشاء كائن `Document` جديد، تُضاف الصفحة إليه، ويتم حفظ ملف PDF الجديد باستخدام طريقة `save()`. يوضح مقطع كود بايثون المرفق هذه العملية، مع عرض الخطوات اللازمة لتقسيم مستند PDF إلى ملفات منفصلة عن طريق iterating عبر صفحاته وحفظ كل واحدة كملف PDF منفصل.
---

يمكن أن تكون ميزة تقسيم صفحات PDF مفيدة لأولئك الذين يرغبون في تقسيم ملف كبير إلى صفحات منفصلة أو مجموعات من الصفحات.

## مثال حي

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) هو تطبيق ويب مجاني على الإنترنت يتيح لك استكشاف كيفية عمل وظيفة تقسيم المستند.

[![Aspose تقسيم PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF منفصلة في تطبيقات بايثون الخاصة بك. لتقسيم صفحات PDF إلى ملفات PDF بصفحة واحدة باستخدام بايثون، يمكن اتباع الخطوات التالية:

1. تجول خلال صفحات مستند PDF عبر مجموعة [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. في كل تكرار، أنشئ كائن Document جديد وأضف كائن [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) الفردي إلى المستند الفارغ.
1. احفظ ملف PDF الجديد باستخدام طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

## تقسيم PDF إلى ملفات متعددة أو ملفات PDF منفصلة باستخدام بايثون

يُظهر مقطع كود بايثون التالي كيفية تقسيم صفحات PDF إلى ملفات PDF منفصلة.

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


