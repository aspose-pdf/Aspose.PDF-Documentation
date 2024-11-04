---
title: إنشاء ملف PDF معقد
linktitle: إنشاء ملف PDF معقد
type: docs
weight: 60
url: /java/complex-pdf-example/
description: Aspose.PDF ل Java يسمح لك بإنشاء مستندات أكثر تعقيدًا تحتوي على صور وقطع نصية وجداول في مستند واحد.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

مثال [Hello, World](/pdf/java/hello-world-example/) أظهر خطوات بسيطة لإنشاء مستند PDF باستخدام Java وAspose.PDF. في هذه المقالة، سنلقي نظرة على إنشاء مستند أكثر تعقيدًا باستخدام Java وAspose.PDF ل Java. كمثال، سنأخذ مستندًا من شركة خيالية تعمل في خدمات العبارات للركاب.
سيحتوي مستندنا على صورة وقطعتين نصيتين (عنوان وفقرة) وجدول. لبناء مثل هذا المستند، سنستخدم نهج يعتمد على DOM. يمكنك قراءة المزيد في قسم [أساسيات API الخاص بـ DOM](/pdf/java/basics-of-dom-api/).

إذا أنشأنا مستندًا من الصفر، نحتاج إلى اتباع خطوات معينة:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). في هذه الخطوة، سنقوم بإنشاء مستند PDF فارغ مع بعض البيانات الوصفية ولكن بدون صفحات.
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) إلى كائن المستند. الآن، سيكون لمستندنا صفحة واحدة.
1. إضافة [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). إنها عملية معقدة تعتمد على الإجراءات منخفضة المستوى مع مشغلي PDF.
    - تحميل الصورة من التدفق
    - إضافة الصورة إلى مجموعة الصور لموارد الصفحة
    - استخدام مشغل GSave: هذا المشغل يحفظ حالة الرسوميات الحالية.
    - إنشاء كائن [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - استخدام مشغل ConcatenateMatrix: يحدد كيفية وضع الصورة.
    - استخدام مشغل Do: هذا المشغل يرسم الصورة.
    - استخدام مشغل GRestore: هذا المشغل يستعيد حالة الرسوميات.

1. إنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) للرأس. بالنسبة للرأس، سنستخدم خط Arial بحجم 24 نقطة ومحاذاة في الوسط.
1. إضافة الرأس إلى [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) الصفحة.
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) للوصف. بالنسبة للوصف، سنستخدم خط Arial بحجم 24 نقطة ومحاذاة في الوسط.
1. إضافة (الوصف) إلى فقرات الصفحة.
1. إنشاء جدول، إضافة خصائص الجدول.
1. إضافة (الجدول) إلى [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) الصفحة.
1. حفظ الوثيقة "Complex.pdf".

```java
package com.aspose.pdf.examples;

/**
 * مثال معقد
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // تهيئة كائن الوثيقة
        Document document = new Document();
        // إضافة صفحة
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // إضافة صورة
        Path imageFileName = Paths.get(_dataDir.toString(),"logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // إضافة الصورة إلى مجموعة الصور في موارد الصفحة
        page.getResources().getImages().add(imageStream);

        // استخدام المشغل GSave: هذا المشغل يحفظ حالة الرسومات الحالية
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // إنشاء كائن Matrix
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // استخدام المشغل ConcatenateMatrix (دمج المصفوفة): يحدد كيفية وضع الصورة
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // استخدام المشغل Do: هذا المشغل يرسم الصورة
        page.getContents().add(new Do(ximage.getName()));
        // استخدام المشغل GRestore: هذا المشغل يستعيد حالة الرسومات
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // إضافة رأس
        TextFragment header = new TextFragment("مسارات العبارات الجديدة في خريف 2020");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // إضافة وصف
        String descriptionText = "يجب على الزوار شراء التذاكر عبر الإنترنت ويتم تحديد عدد التذاكر إلى 5000 تذكرة في اليوم. تعمل خدمة العبارات بنصف السعة وعلى جدول زمني مخفض. توقع الطوابير.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // إضافة جدول
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("يغادر المدينة");
        headerRow.getCells().add("يغادر الجزيرة");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```