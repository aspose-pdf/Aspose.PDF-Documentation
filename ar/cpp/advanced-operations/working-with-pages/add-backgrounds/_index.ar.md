---
title: إضافة خلفية إلى PDF باستخدام C++
linktitle: إضافة الخلفيات
type: docs
weight: 110
url: /cpp/add-backgrounds/
descriptions: أضف صورة خلفية إلى ملف PDF الخاص بك باستخدام C++. استخدم كائن BackgroundArtifact.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

إضافة خلفية إلى ملفات PDF يساعد في تحسين القراءة العامة للمستند. يصبح المحتوى في ملف PDF أكثر جاذبية وسيلفت انتباه القراء إذا كان لديك مظهر جيد للمستند. يمكن أيضًا استخدام الخلفية لتسليط الضوء على النقاط البارزة في ملف PDF.

يمكن استخدام صور الخلفية لإضافة علامة مائية أو تصميم دقيق آخر إلى المستندات. في Aspose.PDF لـ C++، كل مستند PDF هو مجموعة من الصفحات وكل صفحة تحتوي على مجموعة من القطع الأثرية. يمكن استخدام فئة [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) لإضافة صورة خلفية إلى كائن الصفحة.

يظهر كود المثال التالي كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact مع C++.

```cpp
void WorkingWithPages::AddBackgrounds()
{
    String _dataDir("C:\\Samples\\");

    // إنشاء كائن مستند جديد
    auto document = MakeObject<Document>();

    // إضافة صفحة جديدة إلى كائن المستند
    auto page = document->get_Pages()->Add();

    // إنشاء كائن خلفية
    auto background = MakeObject<BackgroundArtifact>();

    // تحديد الصورة لكائن الخلفية
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // إضافة كائن الخلفية إلى مجموعة الآثار في الصفحة
    page->get_Artifacts()->Add(background);

    // حفظ المستند
    document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```