---
title: إضافة خلفية إلى PDF 
linktitle: إضافة خلفيات
type: docs
weight: 110
url: /php-java/add-backgrounds/
descriptions: أضف صورة خلفية إلى ملف PDF الخاص بك باستخدام PHP. استخدم كائن BackgroundArtifact.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكن استخدام صور الخلفية لإضافة علامة مائية، أو تصميمات خفيفة أخرى، إلى المستندات. في Aspose.PDF لـ PHP عبر Java، كل مستند PDF هو مجموعة من الصفحات وكل صفحة تحتوي على مجموعة من القطع الفنية. يمكن استخدام فئة [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) لإضافة صورة خلفية إلى كائن الصفحة.

يوضح مقتطف الكود التالي كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact باستخدام PHP.

```php

    // فتح المستند
    $document = new Document($inputFile);

    // أضف صفحة جديدة إلى كائن المستند
    $page = $document->getPages()->add();

    // إنشاء كائن BackgroundArtifact    
    $background = new BackgroundArtifact();

    // تحديد الصورة لكائن backgroundArtifact
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // أضف backgroundArtifact إلى مجموعة القطع الفنية للصفحة
    $page->getArtifacts()->add($background);

    // حفظ ملف PDF المحدث
    $document->save($outputFile);
    $document->close();
```