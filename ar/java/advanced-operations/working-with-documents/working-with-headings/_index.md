---
title: العمل مع العناوين في PDF
type: docs
weight: 70
url: ar/java/working-with-headings/
lastmod: "2021-06-05"
description: إنشاء ترقيم في عنوان مستند PDF الخاص بك باستخدام Java. يقدم Aspose.PDF for Java أنواعًا مختلفة من أنماط الترقيم.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تطبيق نمط الترقيم في العنوان

العناوين هي الأجزاء المهمة في أي مستند. يحاول الكتاب دائمًا جعل العناوين أكثر بروزًا ومعنى لقرائهم. إذا كان هناك أكثر من عنوان في مستند، فلدى الكاتب عدة خيارات لتنظيم هذه العناوين. واحدة من أكثر الطرق شيوعًا لتنظيم العناوين هي كتابة العناوين بأسلوب الترقيم.

يقدم Aspose.PDF for Java العديد من أنماط الترقيم المحددة مسبقًا. يتم تخزين هذه الأنماط المحددة مسبقًا في تعداد، NumberingStyle. القيم المحددة مسبقًا لتعداد NumberingStyle وأوصافها موضحة أدناه:

|**أنواع العناوين**|**الوصف**|
| :- | :- |
|NumeralsArabic|نوع عربي، على سبيل المثال، 1,1.1,...|

|NumeralsRomanUppercase|نوع روماني كبير، على سبيل المثال، I,I.II, ...|
|NumeralsRomanLowercase|نوع الأرقام الرومانية الصغيرة، على سبيل المثال، i,i.ii, ...|
|LettersUppercase|نوع الأحرف الإنجليزية الكبيرة، على سبيل المثال، A,A.B, ...|
|LettersLowercase|نوع الأحرف الإنجليزية الصغيرة، على سبيل المثال، a,a.b, ...|
تُستخدم خاصية [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) في فئة [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) لتعيين أنماط ترقيم العناوين.

رمز المصدر للحصول على المخرجات الموضحة في الشكل أعلاه مُدرج أدناه في المثال.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleHeading {
    // المسار إلى دليل المستندات.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ApplyNumberingStyleinHeading() {

        Document pdfDoc = new Document();
        pdfDoc.getPageInfo().setWidth(612.0);
        pdfDoc.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        Page pdfPage = pdfDoc.getPages().add();
        pdfPage.getPageInfo().setWidth(612.0);
        pdfPage.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        FloatingBox floatBox = new FloatingBox();
        floatBox.setMargin(pdfPage.getPageInfo().getMargin());

        pdfPage.getParagraphs().add(floatBox);

        Heading heading = new Heading(1);
        heading.setInList(true);
        heading.setStartNumber(1);
        heading.setText("List 1");
        heading.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading.setAutoSequence(true);

        floatBox.getParagraphs().add(heading);
        Heading heading2 = new Heading(1);
        heading2.setInList(true);
        heading2.setStartNumber(13);
        heading2.setText("List 2");
        heading2.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading2.setAutoSequence(true);

        floatBox.getParagraphs().add(heading2);

        Heading heading3 = new Heading(2);
        heading3.setInList(true);
        heading3.setStartNumber(1);
        heading3.setText("القيمة، اعتبارًا من تاريخ سريان الخطة، للملكية التي سيتم توزيعها بموجب الخطة بسبب كل ما هو مسموح به");
        heading3.setStyle (NumberingStyle.LettersLowercase);
        heading3.setAutoSequence(true);

        floatBox.getParagraphs().add(heading3);
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDoc.save(_dataDir);

    }

}
```