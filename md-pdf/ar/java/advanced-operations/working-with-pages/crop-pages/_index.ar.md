---
title: اقتصاص صفحات PDF برمجياً
linktitle: اقتصاص الصفحات
type: docs
weight: 80
url: /java/crop-pages/
description: يمكنك الحصول على خصائص الصفحة، مثل العرض، الارتفاع، وعلبة النزيف، الاقتصاص، والتقليم باستخدام Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF لديها عدد من الخصائص، مثل العرض، الارتفاع، وعلبة النزيف، الاقتصاص، والتقليم. يتيح لك Aspose.PDF for Java الوصول إلى هذه الخصائص.

- **علبة الوسائط**: علبة الوسائط هي أكبر علبة صفحة. تتوافق مع حجم الصفحة (على سبيل المثال A4، A5، الرسالة الأمريكية، إلخ) المحددة عند طباعة المستند إلى PostScript أو PDF. بعبارة أخرى، تحدد علبة الوسائط الحجم الفيزيائي للوسائط التي يتم عرض مستند PDF أو طباعته عليها.
- **علبة النزيف**: إذا كان للمستند نزيف، سيكون للـ PDF أيضًا علبة نزيف.
 Bleed هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما بعد حافة الصفحة. يتم استخدامه لضمان أنه عند طباعة المستند وقطعه إلى الحجم المطلوب ("مشذب")، ستصل الحبر إلى حافة الصفحة. حتى لو كانت الصفحة مقطوعة بشكل غير دقيق - مقطوعة قليلاً عن علامات القطع - لن تظهر أي حواف بيضاء على الصفحة.
- **صندوق القطع**: يشير صندوق القطع إلى الحجم النهائي للمستند بعد الطباعة والقطع.
- **صندوق الفن**: صندوق الفن هو المربع المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يتم استخدام هذا الصندوق عند استيراد مستندات PDF في تطبيقات أخرى.
- **صندوق الاقتصاص**: صندوق الاقتصاص هو حجم "الصفحة" الذي يتم عرض مستند PDF الخاص بك به في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق الاقتصاص فقط في Adobe Acrobat. للحصول على وصف مفصل لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، خاصة القسم 10.10.1 حدود الصفحة.
- **Page.Rect**: تقاطع (المستطيل المرئي عادة) بين MediaBox و DropBox. الصورة أدناه توضح هذه الخصائص.  
لمزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

المقتطف أدناه يوضح كيفية اقتصاص الصفحة:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleCropPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    // فتح المستند
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    public static void CropPagesPDF() {
        Document pdfDocument = new Document("crop_page.pdf");
        Page page = pdfDocument.getPages().get_Item(1);

        System.out.println(page.getCropBox());
        System.out.println(page.getTrimBox());
        System.out.println(page.getArtBox());
        System.out.println(page.getBleedBox());
        System.out.println(page.getMediaBox());

        // إنشاء مستطيل جديد Box
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520);

        page.setCropBox(newBox);
        page.setTrimBox(newBox);
        page.setArtBox(newBox);
        page.setBleedBox(newBox);

        // حفظ المستند الناتج
        pdfDocument.save(_dataDir + "crop_page_modified.pdf");
    }
}
```

In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the الشكل 1.
![الشكل 1. الصفحة المقصوصة](crop_page.png)

After the change, the page will look like الشكل 2.
![الشكل 2. الصفحة المقصوصة](crop_page2.png)