---
title: إضافة علامة مائية إلى PDF
linktitle: إضافة علامة مائية
type: docs
weight: 90
url: ar/php-java/add-watermarks/
description: توضح هذه المقالة ميزات العمل مع القطع الأثرية والحصول على العلامات المائية في ملفات PDF باستخدام PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for PHP عبر Java** تتيح إضافة علامات مائية إلى مستند PDF الخاص بك باستخدام القطع الأثرية. يرجى التحقق من هذه المقالة لحل مهمتك.

العلامة المائية التي تم إنشاؤها باستخدام Adobe Acrobat تُسمى قطعة أثرية (كما هو موضح في 14.8.2.2 المحتوى الحقيقي والقطع الأثرية لمواصفات PDF). من أجل العمل مع القطع الأثرية، يحتوي Aspose.PDF على فئتين: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) و [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

من أجل الحصول على جميع القطع الأثرية في صفحة معينة، تحتوي فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) على خاصية القطع الأثرية.
 هذا الموضوع يشرح كيفية العمل مع الأداة في ملفات PDF.

## العمل مع الأدوات

تحتوي فئة [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) على الخصائص التالية:

**Artifact.Type** – يحصل على نوع الأداة (يدعم القيم من تعداد Artifact.ArtifactType حيث تشمل القيم Background, Layout, Page, Pagination و Undefined).
**Artifact.Subtype** – يحصل على نوع الأداة الفرعي (يدعم القيم من تعداد Artifact.ArtifactSubtype حيث تشمل القيم Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

يرجى ملاحظة أن العلامات المائية التي تم إنشاؤها باستخدام Adobe Acrobat يكون لها النوع Pagination والنوع الفرعي Watermark.

{{% /alert %}}

**Artifact.Contents** – يحصل على مجموعة من المشغلين الداخليين للأداة. نوعه المدعوم هو System.Collections.ICollection.
**Artifact.Form** – يحصل على XForm الأداة (إذا تم استخدام XForm). تحتوي الأدوات مثل العلامات المائية، الرأس، والتذييل على XForm الذي يعرض جميع محتويات الأداة.

**Artifact.Image** – يحصل على صورة الأداة (إذا كانت الصورة موجودة، وإلا تكون null).**Artifact.Text** – يحصل على نص الأداة.
**Artifact.Rectangle** – يحصل على موضع الأداة على الصفحة.
**Artifact.Rotation** – يحصل على دوران الأداة (بالدرجات، القيمة الموجبة تشير إلى دوران عكس اتجاه عقارب الساعة).
**Artifact.Opacity** – يحصل على شفافية الأداة. القيم الممكنة تتراوح بين 0…1، حيث 1 تعني غير شفاف تمامًا.

## عينات برمجة: الحصول على العلامات المائية

يُظهر مقطع الشيفرة التالي كيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF باستخدام PHP.

```php

    // افتح المستند
    $document = new Document($inputFile);
            
    $formattedText = new FormattedText("Watermark", 
        (new Color())->getBlue()->getRgb(),
        (new facades_FontStyle())->getCourier(), 
        facades_EncodingType::$Identity_h, 
        true, 72.0);

    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    $artifact = new WatermarkArtifact();        
    $artifact->setText($formattedText);        
    $artifact->setArtifactHorizontalAlignment ($horizontalAlignment->getCenter());
    $artifact->setArtifactVerticalAlignment ($verticalAlignment->getCenter());
    $artifact->setRotation(45);
    $artifact->setOpacity(0.5);
    $artifact->setBackground(true);
    $document->getPages()->get_Item(1)->getArtifacts()->add($artifact);
    
    // احفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```