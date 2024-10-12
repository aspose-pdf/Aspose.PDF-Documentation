---
title: العمل مع القطع الأثرية في C++
linktitle: العمل مع القطع الأثرية
type: docs
weight: 110
url: /cpp/artifacts/
description: تصف هذه الصفحة كيفية العمل مع فئة Artifact باستخدام Aspose.PDF لـ C++. تعرض مقتطفات التعليمات البرمجية كيفية إضافة صورة خلفية إلى صفحات PDF وكيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF.
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## كيفية الحصول على العلامة المائية في PDF؟

**ما هو القطعة الأثرية في PDF؟**

وفقًا لمرجع PDF / UA ISO، يجب اعتبار المحتوى الذي ليس مهمًا أو لا يظهر في الخلفية ولا يحمل معلومات ذات صلة كقطعة أثرية حتى تتمكن التقنيات المساعدة من تجاهله.
إذا لم يكن من الممكن تحديد القطع الأثرية في البرنامج لإنشاءها، فيجب القيام بذلك يدويًا باستخدام Aspose.PDF لـ C++.

تحتوي فئة [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) على الخصائص التالية:

- **Artifact.Type** – يحصل على نوع القطعة الأثرية (يدعم القيم من تعداد Artifact.ArtifactType حيث تشمل القيم خلفية، تخطيط، صفحة، ترقيم وغير محدد).
- **Artifact.Subtype** – يحصل على النوع الفرعي للقطعة الأثرية (يدعم القيم لتعداد Artifact.ArtifactSubtype حيث تشمل القيم الخلفية، التذييل، الرأس، غير محدد، العلامة المائية).

{{% alert color="primary" %}}

يرجى ملاحظة أن العلامات المائية التي تم إنشاؤها باستخدام Adobe Acrobat لها نوع الترقيم والنوع الفرعي علامة مائية.

{{% /alert %}}

- **Artifact.Contents** – يحصل على مجموعة من مشغلي القطعة الأثرية الداخلية. نوعه المدعوم هو System.Collections.ICollection.
- **Artifact.Form** – يحصل على XForm للقطعة الأثرية (إذا تم استخدام XForm). تحتوي القطع الأثرية للعلامات المائية والرأس والتذييل على XForm الذي يظهر جميع محتويات القطعة الأثرية.
- **Artifact.Image** – يحصل على صورة القطعة الأثرية (إذا كانت الصورة موجودة، وإلا فالقيمة فارغة).
- **Artifact.Text** – يحصل على نص القطعة الأثرية.
- **Artifact.Rectangle** – يحصل على موضع القطعة الأثرية على الصفحة.
- **Artifact.Rotation** – يحصل على دوران القطعة الأثرية (بالدرجات، تشير القيمة الموجبة إلى الدوران عكس اتجاه عقارب الساعة).
- **Artifact.Opacity** – يحصل على شفافية القطعة الأثرية. قيم محتملة تكون في النطاق 0...1، حيث 1 تعني غير شفاف تمامًا.

كمثال على العمل مع العناصر في ملف PDF، دعونا نأخذ علامة مائية.

العلامة المائية التي تم إنشاؤها بدعم من Adobe Acrobat يشار إليها كعنصر (كما هو موضح في 14.8.2.2 عرض محتوى العناصر ومواصفات PDF). للعمل مع العناصر يحتوي Aspose.PDF على فئتين:
[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) و [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

من أجل الحصول على جميع العناصر في صفحة معينة، تحتوي فئة [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) على خاصية Artifacts. يظهر هذا الموضوع كيفية العمل مع العنصر المائي في ملفات PDF.

يوضح المثال البرمجي التالي كيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF باستخدام C++:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
void Artifacts::SetWatermark() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto artifact = MakeObject<WatermarkArtifact>();
    String text(u"WATERMARK");    
    artifact->set_Text(text);
    artifact->get_TextState()->set_ForegroundColor(Color::get_Blue());
    artifact->get_TextState()->set_FontSize(72);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(_dataDir + u"watermark.pdf");
}
```
خلفيات الصور يمكن استخدامها لإضافة علامات مائية أو تصاميم حصرية إلى مستندات PDF. يستخدم Aspose.PDF for C++ فئة [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) لإضافة صورة خلفية إلى كائن الصفحة.

يوضح لك مقطع الكود التالي كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact:

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // افتح المستند
    auto pdfDocument = MakeObject<Document>();

    // أضف صفحة إلى كائن المستند
    auto page = pdfDocument->get_Pages()->Add();

    // إنشاء كائن خلفية
    auto background = MakeObject<BackgroundArtifact>();

    // تحديد الصورة لكائن الخلفية
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // أضف كائن الخلفية إلى مجموعة الآثار في الصفحة
    page->get_Artifacts()->Add(background);

    // احفظ ملف PDF المعدل
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### أمثلة برمجية: الحصول على العلامات المائية

يظهر مقطع الشيفرة التالي كيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF.

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // فتح المستند
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // تكرار والحصول على النوع الفرعي والنص وموقع الكائن
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### أمثلة برمجية: حساب الكائنات من نوع معين

لحساب العدد الإجمالي للكائنات من نوع معين (على سبيل المثال، العدد الإجمالي للعلامات المائية)، استخدم الشيفرة التالية:

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // فتح المستند
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // إذا كان نوع الكائن هو علامة مائية، زيادة العداد
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"Page contains {0} watermarks", count);
}
```