---
title: دمج ملفات PDF في بايثون
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /ar/python-net/merge-pdf/
description: تعرف على كيفية دمج ملفات PDF متعددة في مستند واحد في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ادمج صفحات PDF باستخدام Python
Abstract: تتناول هذه المقالة الحاجة الشائعة لدمج ملفات PDF متعددة في مستند واحد، وهي عملية ذات قيمة لتنظيم وتحسين تخزين ومشاركة محتوى PDF. يستكشف استخدام Aspose.PDF لـ Python عبر .NET لدمج ملفات PDF بكفاءة، مع الاعتراف بأن دمج ملفات PDF في Python يمكن أن يكون تحديًا بدون مكتبات الطرف الثالث. توفر المقالة دليلًا تفصيليًا لتسلسل ملفات PDF - إنشاء مستند جديد ودمج الملفات وحفظ المستند المدمج. يوضح مقتطف الشفرة التنفيذ باستخدام Aspose.PDF، ويسلط الضوء على قدرة المكتبة على تبسيط عملية الدمج. بالإضافة إلى ذلك، فإنه يقدم Aspose.PDF Merger، وهي أداة عبر الإنترنت لدمج ملفات PDF، مما يتيح للمستخدمين استكشاف الوظائف في بيئة قائمة على الويب.
---

## دمج ملفات PDF باستخدام بايثون وDOM

لربط ملفين من ملفات PDF:

1. قم بإنشاء مستند جديد.
1. دمج ملفات PDF
1. احفظ المستند المدمج

دمج مستندات PDF متعددة في ملف واحد:

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## مثال مباشر

[عملية دمج Aspose.PDF](https://products.aspose.app/pdf/merger) هو تطبيق ويب مجاني عبر الإنترنت يسمح لك بالتحقيق في كيفية عمل وظيفة دمج العروض التقديمية.

[![عملية دمج Aspose.PDF](merger.png)](https://products.aspose.app/pdf/merger)

