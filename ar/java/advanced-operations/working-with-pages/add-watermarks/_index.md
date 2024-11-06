---
title: إضافة علامة مائية إلى PDF 
linktitle: إضافة علامة مائية
type: docs
weight: 90
url: ar/java/add-watermarks/
description: تشرح هذه المقالة ميزات العمل مع القطع الأثرية والحصول على العلامات المائية في ملفات PDF باستخدام البرمجة بلغة Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** يسمح بإضافة علامات مائية إلى مستند PDF الخاص بك باستخدام القطع الأثرية. يرجى مراجعة هذه المقالة لحل مهمتك.

تسمى العلامة المائية التي تم إنشاؤها باستخدام Adobe Acrobat قطعة أثرية (كما هو موصوف في 14.8.2.2 المحتوى الحقيقي والقطع الأثرية في مواصفات PDF). للعمل مع القطع الأثرية، يحتوي Aspose.PDF على فئتين: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) و [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

للحصول على جميع القطع الأثرية في صفحة معينة، تحتوي فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) على خاصية القطع الأثرية.
 هذا الموضوع يشرح كيفية العمل مع العناصر في ملفات PDF.

## العمل مع العناصر

تحتوي فئة [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) على الخصائص التالية:

**Artifact.Type** – تحصل على نوع العنصر (تدعم القيم لتعداد Artifact.ArtifactType حيث تشمل القيم الخلفية، التنسيق، الصفحة، الترقيم وغير محدد).
**Artifact.Subtype** – تحصل على نوع فرعي للعنصر (تدعم القيم لتعداد Artifact.ArtifactSubtype حيث تشمل القيم الخلفية، التذييل، الرأس، غير محدد، العلامة المائية).

{{% alert color="primary" %}}

يرجى ملاحظة أن العلامات المائية التي تم إنشاؤها باستخدام Adobe Acrobat لها نوع الترقيم ونوع فرعي العلامة المائية.

{{% /alert %}}

**Artifact.Contents** – تحصل على مجموعة من المشغلين الداخليين للعنصر. نوعها المدعوم هو System.Collections.ICollection.
**Artifact.Form** – تحصل على XForm للعنصر (إذا كان XForm مستخدمًا). تحتوي العناصر المائية، وعناصر الرأس والتذييل على XForm الذي يعرض جميع محتويات العنصر.

**Artifact.Image** – تحصل على صورة العنصر (إذا كانت الصورة موجودة، وإلا فتكون فارغة).**Artifact.Text** – يحصل على نص الأداة.
**Artifact.Rectangle** – يحصل على موقع الأداة على الصفحة.
**Artifact.Rotation** – يحصل على دوران الأداة (بالدرجات، القيمة الإيجابية تشير إلى دوران عكس اتجاه عقارب الساعة).
**Artifact.Opacity** – يحصل على شفافية الأداة. القيم الممكنة تتراوح بين 0…1، حيث 1 يعني غير شفاف تمامًا.

## أمثلة برمجية: الحصول على العلامات المائية

يعرض مقطع الشيفرة التالي كيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF باستخدام Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.EncodingType;
import com.aspose.pdf.facades.FontStyle;
import com.aspose.pdf.facades.FormattedText;

public class ExampleWatermark {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {

        // افتح المستند
        Document doc = new Document(_dataDir + "text.pdf");      
        FormattedText formattedText = new FormattedText("Watermark", java.awt.Color.BLUE,FontStyle.Courier, EncodingType.Identity_h, true, 72.0F);
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(formattedText);        
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }

}  
```