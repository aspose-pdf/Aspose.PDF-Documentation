---
title: كيفية دمج ملفات PDF باستخدام بايثون
linktitle: دمج ملفات PDF
type: docs
weight: 50
url: /ar/python-net/merge-pdf-documents/
description: توضح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام بايثون.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: دمج صفحات PDF باستخدام بايثون
Abstract: يتناول هذا المقال الحاجة الشائعة إلى دمج عدة ملفات PDF في مستند واحد، وهي عملية ذات قيمة لتنظيم وتحسين التخزين ومشاركة محتوى PDF. يستكشف استخدام Aspose.PDF للبايثون عبر .NET لدمج ملفات PDF بكفاءة، مع الإشارة إلى أن دمج ملفات PDF في بايثون قد يكون صعبًا دون مكتبات طرف ثالث. يقدم المقال دليلًا خطوة بخطوة لتسلسل ملفات PDF - إنشاء مستند جديد، دمج الملفات، وحفظ المستند المدمج. يظهر مقطع كود تنفيذ العملية باستخدام Aspose.PDF، مبرزًا قدرة المكتبة على تبسيط عملية الدمج. بالإضافة إلى ذلك، يقدم Aspose.PDF Merger، أداة عبر الإنترنت لدمج ملفات PDF، مما يتيح للمستخدمين استكشاف الوظيفة في بيئة ويب.
---

## دمج أو تجميع ملفات PDF متعددة في ملف PDF واحد باستخدام بايثون

يُعَد دمج ملفات PDF استفسارًا شائعًا بين المستخدمين. يمكن أن يكون ذلك مفيدًا عندما يكون لديك عدة ملفات PDF تريد مشاركتها أو تخزينها معًا كمستند واحد.

يمكن أن يساعدك دمج ملفات PDF على تنظيم مستنداتك، وتوفير مساحة تخزين على جهاز الكمبيوتر الخاص بك، ومشاركة عدة ملفات PDF مع الآخرين عن طريق دمجها في مستند واحد.

إن دمج PDF في بايثون عبر .NET ليست مهمة بسيطة دون استخدام مكتبة طرف ثالث.
يظهر هذا المقال كيفية دمج عدة ملفات PDF في مستند PDF واحد باستخدام Aspose.PDF للبايثون عبر .NET.

## دمج ملفات PDF باستخدام بايثون و DOM

لدمج ملفي PDF معًا:

1. إنشاء مستند جديد.
1. دمج ملفات PDF
1. حفظ المستند المدمج

دمج عدة مستندات PDF في ملف واحد:

```python

    import aspose.pdf as apdf
    import aspose.pydrawing as asdrw
    from io import FileIO
    from os import path

    path_infile1 = path.join(self.dataDir, infile1)
    path_infile2 = path.join(self.dataDir, infile2)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document()
    document.merge(files=[path_infile1, path_infile2])
    document.save(path_outfile)
```

## مثال حي

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) هو تطبيق ويب مجاني عبر الإنترنت يتيح لك استكشاف كيفية عمل وظيفة دمج العروض التقديمية.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)


