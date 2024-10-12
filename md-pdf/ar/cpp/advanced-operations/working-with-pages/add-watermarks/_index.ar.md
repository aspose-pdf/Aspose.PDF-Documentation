---
title: إضافة علامة مائية إلى PDF باستخدام C++
linktitle: إضافة علامة مائية
type: docs
weight: 90
url: /cpp/add-watermarks/
description: توضح هذه المقالة ميزات العمل مع القطع الأثرية والحصول على العلامات المائية في ملفات PDF باستخدام البرمجة بلغة C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

العلامة المائية هي صورة شفافة تحتوي عادةً على شعار أو ختم لتحديد من قام بإنشاء المستند أو الصورة.

يتيح لك **Aspose.PDF for C++** إضافة علامات مائية إلى مستند PDF الخاص بك باستخدام فئة Artifact. يرجى مراجعة هذه المقالة لحل مهمتك.

العلامة المائية التي يتم إنشاؤها باستخدام Adobe Acrobat تُعرف بالقطعة الأثرية (كما هو موضح في القسم 14.8.2.2 من مواصفات PDF عن المحتوى الحقيقي والقطع الأثرية). للعمل مع القطع الأثرية، يحتوي Aspose.PDF على فئتين: [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) و [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

للحصول على جميع القطع الأثرية في صفحة معينة، تحتوي فئة [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) على خاصية Artifacts. هذا الموضوع يشرح كيفية العمل مع الأداة في ملفات PDF.

## العمل مع الأدوات

تحتوي فئة [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) على الخصائص التالية:

**Artifact.Type** – تحصل على نوع الأداة (تدعم القيم من تعداد Artifact.ArtifactType حيث تشمل القيم الخلفية والتخطيط والصفحة والترقيم وغير محدد).
**Artifact.Subtype** – تحصل على نوع الأداة الفرعي (تدعم القيم من تعداد Artifact.ArtifactSubtype حيث تشمل القيم الخلفية والتذييل والرأس وغير محدد والعلامة المائية).

{{% alert color="primary" %}}

يرجى ملاحظة أن العلامات المائية التي تم إنشاؤها باستخدام Adobe Acrobat لها نوع الترقيم ونوع فرعي هو العلامة المائية.

{{% /alert %}}

**Artifact.Contents** – يحصل على مجموعة من المشغلين الداخليين للأداة. نوعها المدعوم هو System.Collections.ICollection.
**Artifact.Form** – يحصل على XForm الخاص بأداة (إذا تم استخدام XForm). تحتوي الأدوات مثل العلامات المائية والرأس والتذييل على XForm الذي يعرض جميع محتويات الأداة.

**Artifact.Image** – يحصل على صورة الأداة (إذا كانت الصورة موجودة، وإلا تكون فارغة).**Artifact.Text** – يحصل على نص الأداة الفنية.
**Artifact.Rectangle** – يحصل على موضع الأداة الفنية على الصفحة.
**Artifact.Rotation** – يحصل على دوران الأداة الفنية (بالدرجات، القيمة الموجبة تشير إلى دوران عكس اتجاه عقارب الساعة).
**Artifact.Opacity** – يحصل على شفافية الأداة الفنية. القيم الممكنة تتراوح بين 0…1، حيث 1 تعني تعتيمًا تامًا.

## عينات برمجة: كيفية إضافة علامة مائية على ملفات PDF

يعرض مقطع الشيفرة التالي كيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF باستخدام C++.

```cpp
void GettingWatermarks() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("watermark.pdf");
    String outputFileName("watermark_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto artifact = MakeObject<WatermarkArtifact>();
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(72);
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_Font(FontRepository::FindFont(u"Courier"));
    artifact->SetTextAndState(u"WATERMARK", textState);
    artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);

    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);

    document->Save(_dataDir + outputFileName);
}
```