---
title: إضافة خلفية إلى PDF
linktitle: إضافة خلفيات
type: docs
weight: 110
url: ar/java/add-backgrounds/
descriptions: أضف صورة خلفية إلى ملف PDF الخاص بك باستخدام Java. استخدم كائن BackgroundArtifact.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكن استخدام صور الخلفية لإضافة علامة مائية أو تصميم خفيف إلى المستندات. في Aspose.PDF for Java، كل مستند PDF هو مجموعة من الصفحات وكل صفحة تحتوي على مجموعة من القطع الفنية. يمكن استخدام فئة [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) لإضافة صورة خلفية إلى كائن الصفحة.

يعرض مقطع الشيفرة التالي كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact مع Java.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        String myDir = "";
        // قم بإنشاء كائن مستند جديد
        Document doc = new Document();
        // أضف صفحة جديدة إلى كائن المستند
        Page page = doc.getPages().add();
        // إنشاء كائن BackgroundArtifact
        BackgroundArtifact background = new BackgroundArtifact();
        // تحديد الصورة لكائن backgroundartifact
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // إضافة backgroundartifact إلى مجموعة القطع الفنية للصفحة
        page.getArtifacts().add(background);
        // حفظ المستند
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```