---
title: قص صفحات PDF برمجياً باستخدام C++
linktitle: قص الصفحات
type: docs
weight: 80
url: /cpp/crop-pages/
description: يمكنك الحصول على خصائص الصفحة، مثل العرض، الارتفاع، صندوق النزيف، القص وصندوق القطع باستخدام Aspose.PDF لـ C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF تحتوي على عدد من الخصائص، مثل العرض، الارتفاع، صندوق النزيف، القص وصندوق القطع. يتيح لك Aspose.PDF الوصول إلى هذه الخصائص.

- **صندوق الوسائط**: صندوق الوسائط هو أكبر صندوق للصفحة. يتوافق مع حجم الصفحة (على سبيل المثال A4، A5، رسالة الولايات المتحدة، إلخ) الذي تم تحديده عند طباعة المستند إلى PostScript أو PDF. بمعنى آخر، يحدد صندوق الوسائط الحجم الفيزيائي للوسائط التي يتم عرض أو طباعة مستند PDF عليها.
- **صندوق النزيف**: إذا كان المستند يحتوي على نزيف، فسيحتوي PDF أيضاً على صندوق نزيف. Bleed هو مقدار اللون (أو الأعمال الفنية) التي تمتد إلى ما بعد حافة الصفحة. يتم استخدامه للتأكد من أنه عند طباعة المستند وقصه إلى الحجم ("مقصوص")، سيمتد الحبر إلى حافة الصفحة. حتى إذا تم قص الصفحة بشكل غير دقيق - تقطع قليلاً عن علامات القطع - فلن تظهر حواف بيضاء على الصفحة.
- **Trim box**: يشير مربع القص إلى الحجم النهائي للمستند بعد الطباعة والقص.
- **Art box**: مربع الفن هو المربع المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يتم استخدام هذا المربع عند استيراد مستندات PDF في تطبيقات أخرى.
- **Crop box**: مربع الاقتصاص هو حجم "الصفحة" الذي يتم عرض مستند PDF الخاص بك في Adobe Acrobat. في العرض العادي، يتم عرض محتويات مربع الاقتصاص فقط في Adobe Acrobat. للحصول على أوصاف مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، خاصة 10.10.1 حدود الصفحة.
- **Page.Rect**: التقاطع (المستطيل المرئي عادة) لمربع الوسائط وDropBox. الصورة أدناه توضح هذه الخصائص. لمزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

المقتطف أدناه يوضح كيفية قص الصفحة:

```cpp
void CropPagesPDF()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("crop_page.pdf");
    String outputFileName("crop_page_out.pdf");

    // Open source document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

    // Create new Box Rectagle
    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox (newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox (newBox);

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```
In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
![Figure 1. Cropped Page](crop_page.png)

بعد التغيير، ستبدو الصفحة كما هو موضح في الشكل 2.  
![Figure 2. Cropped Page](crop_page2.png)