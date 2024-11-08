---
title: استخراج النص من الطوابع باستخدام C#
type: docs
weight: 60
url: /ar/net/extract-text-from-stamps/
description: تعلم كيفية استخدام ميزة خاصة لـ Aspose.PDF لـ .NET - استخراج النص من تعليقات الطابع
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج النص من تعليقات الطابع

يتيح لك Aspose.PDF لـ NET استخراج النص من تعليقات الطابع. لاستخراج النص من تعليقات الطابع في ملف PDF، يمكن استخدام الخطوات التالية.

1. إنشاء كائن من فئة `Document`
1. الحصول على `Annotation` المطلوبة من قائمة تعليقات صفحة ما
1. تحديد كائن جديد من فئة `TextAbsorber`
1. استخدام طريقة الزيارة في TextAbsorber للحصول على النص

يعمل أيضًا الشفرة التالية مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```

