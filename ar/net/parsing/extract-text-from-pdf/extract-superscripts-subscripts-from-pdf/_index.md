---
title: استخراج النصوص الفوقية والسفلية من ملف PDF
linktitle: استخراج النصوص الفوقية والسفلية
type: docs
weight: 30
url: /ar/net/extract-superscripts-subscripts-from-pdf/
description: يصف هذا المقال الطرق المختلفة لاستخراج النصوص الفوقية والسفلية من ملف PDF باستخدام Aspose.PDF في C#.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النصوص الفوقية والسفلية

استخراج النصوص من مستند PDF أمر شائع. ومع ذلك، في مثل هذه النصوص، عند استخراجها، قد لا يتم عرض النصوص الفوقية والسفلية المحتواة فيها، والتي تكون نمطية للوثائق الفنية والمقالات. النص السفلي أو الفوقي هو حرف، رقم، أو حرف يوضع أسفل أو أعلى خط نص عادي. وعادة ما يكون أصغر من بقية النص.

**النصوص السفلية والفوقية** تستخدم غالباً في الصيغ، التعبيرات الرياضية، ومواصفات المركبات الكيميائية.
**المراجع والمؤشرات العلوية** تُستخدم غالبًا في الصيغ، والتعبيرات الرياضية، ومواصفات المركبات الكيميائية.
في إحدى الإصدارات الأخيرة، أضافت مكتبة **Aspose.PDF لـ .NET** دعمًا لاستخراج نصوص المراجع العلوية والسفلية من ملفات PDF.

استخدم فئة **TextFragmentAbsorber** ويمكنك بالفعل القيام بأي شيء مع النص الموجود، أي يمكنك ببساطة استخدام النص بأكمله. جرب قطعة الكود التالية:

قطعة الكود التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

أو استخدم **TextFragments** بشكل منفصل وقم بكل أنواع التلاعب بها، مثل الفرز حسب الإحداثيات أو حسب الحجم.

قطعة الكود التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).
الشفرة التالية تعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```
