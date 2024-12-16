---
title: PDF Multimedia Annotation using C++
linktitle: Multimedia Annotation
type: docs
weight: 40
url: /ar/cpp/multimedia-annotation/
description: Aspose.PDF for C++ يسمح لك بإضافة التعليقات التوضيحية المتعددة الوسائط والحصول عليها وحذفها من مستند PDF الخاص بك.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

إضافة الفيديو والصوت والمحتوى التفاعلي تحول ملفات PDF إلى أدوات اتصال متعددة الأبعاد تزيد من الاهتمام والتفاعل مع مستنداتك. يسمى هذا المحتوى في ملفات PDF بتعليقات توضيحية متعددة الوسائط.

التعليقات التوضيحية في مستند PDF موجودة في مجموعة التعليقات التوضيحية لكائن [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). تحتوي هذه المجموعة على جميع التعليقات التوضيحية لتلك الصفحة الفردية فقط: كل صفحة لها مجموعة تعليقات توضيحية خاصة بها. لإضافة تعليق توضيحي إلى صفحة معينة، أضفه إلى مجموعة التعليقات التوضيحية لتلك الصفحة باستخدام طريقة Add.

استخدم فئة [ScreenAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.screen_annotation) في مساحة الأسماء Aspose.PDF.InteractiveFeatures.Annotations لتضمين ملفات SWF كتعليقات توضيحية في مستند PDF بدلاً من ذلك. 
تحدد توضيحات الشاشة منطقة من الصفحة حيث يمكن تشغيل مقاطع الوسائط.

عندما تحتاج إلى إضافة رابط فيديو خارجي في مستند PDF، يمكنك استخدام [MovieAnnotaiton](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.movie_annotation).
تحتوي توضيحات الفيلم على رسومات متحركة وصوت ليتم عرضها على شاشة الكمبيوتر وعبر مكبرات الصوت.

يجب أن يكون [Sound Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.sound_annotation) مماثلاً للتعليقات النصية باستثناء أنه بدلاً من ملاحظة نصية، يحتوي على صوت مسجل من ميكروفون الكمبيوتر أو مستورد من ملف. عندما يتم تفعيل التعليق، سيتم تشغيل الصوت. يجب أن يتصرف التعليق مثل التعليقات النصية في معظم النواحي، مع أيقونة مختلفة (افتراضيًا، مكبر صوت) للإشارة إلى أنه يمثل صوتًا.

ومع ذلك، عندما تكون هناك حاجة لتضمين الوسائط داخل مستند PDF، تحتاج إلى استخدام [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.rich_media_annotation).
```
## إضافة تعليق الشاشة

يوضح مقطع الشيفرة التالي كيفية إضافة تعليق شاشة إلى ملف PDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MultimediaAnnotations::AddScreenAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"input.swf";

    // إنشاء تعليق الشاشة
    auto screenAnnotation = MakeObject<ScreenAnnotation>(page, MakeObject<Rectangle>(170, 190, 470, 380), mediaFile);
    page->get_Annotations()->Add(screenAnnotation);

    document->Save(_dataDir + u"sample_swf.pdf");
}
```

## إضافة تعليق الصوت

يوضح مقطع الشيفرة التالي كيفية إضافة تعليق صوتي إلى ملف PDF:

```cpp
  void MultimediaAnnotations::AddSoundAnnotation()
{

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"file_example_WAV_1MG.wav";

    // إنشاء تعليق الصوت
    auto soundAnnotation = MakeObject<SoundAnnotation>(page, new Rectangle(20, 700, 60, 740), mediaFile);
    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"عرض توضيحي لتعليق الصوت");
    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(document));

    page->get_Annotations()->Add(soundAnnotation);

    document->Save(_dataDir + u"sample_wav.pdf");
}

```

## إضافة RichMediaAnnotation

يوضح مقتطف الشيفرة التالي كيفية إضافة RichMediaAnnotation إلى ملف PDF:

```cpp
       void MultimediaAnnotations::AddRichMediaAnnotation()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();

    String pathToAdobeApp (u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins");
    auto page = document->get_Pages()->Add();

    // قم بإعطاء اسم لبيانات الفيديو. سيتم تضمين هذه البيانات في المستند بهذا
    // الاسم ويُشار إليها من متغيرات الفلاش بهذا الاسم.
    // يجب ألا يحتوي videoName على مسار الملف؛ هذا بالأحرى "مفتاح" للوصول إلى
    // البيانات داخل مستند PDF

    String videoName (u"file_example_MP4_480_1_5MG.mp4");
    String posterName (u"file_example_MP4_480_1_5MG_poster.jpg");

    // كما نستخدم الجلد لمشغل الفيديو
    String skinName (u"SkinOverAllNoFullNoCaption.swf");

    auto rma = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600));

    // هنا يجب أن نحدد التدفق الذي يحتوي على كود مشغل الفيديو
    rma->set_CustomPlayer(System::IO::File::OpenRead(pathToAdobeApp + u"Players\\" + u"Videoplayer.swf"));

    // قم بتكوين خط متغيرات الفلاش للمشغل. يرجى ملاحظة أن المشغلات المختلفة
    // قد يكون لديها تنسيق مختلف لخط متغيرات الفلاش.
    // راجع الوثائق لمشغلك.
    rma->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);

    // أضف كود الجلد.
    rma->AddCustomData(skinName, System::IO::File::OpenRead(pathToAdobeApp + u"SkinOverAllNoFullNoCaption.swf"));
    // تعيين الملصق للفيديو
    rma->SetPoster(System::IO::File::OpenRead(_dataDir + posterName));

    // تعيين محتوى الفيديو
    rma->SetContent(videoName, System::IO::File::OpenRead(_dataDir + videoName));

    // تعيين نوع المحتوى (فيديو)
    rma->set_Type(RichMediaAnnotation::ContentType::Video);

    // تفعيل المشغل بالنقر
    rma->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);

    // تحديث بيانات التعليق التوضيحي. يجب استدعاء هذه الطريقة بعد جميع
    // التعيينات/الإعدادات. تقوم هذه الطريقة بتهيئة بنية بيانات التعليق التوضيحي
    // وتضمين البيانات المطلوبة.
    rma->Update();

    // أضف التعليق التوضيحي على الصفحة.
    page->get_Annotations()->Add(rma);

    document->Save(_dataDir + u"RichMediaAnnotation.pdf");
}
```

### الحصول على MultimediaAnnotation

يرجى محاولة استخدام جزء الشيفرة التالي للحصول على MultimediaAnnotation من مستند PDF.

```cpp
void MultimediaAnnotations::GetMultimediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        Console::WriteLine(u"{0} {1}", ma->get_AnnotationType(), ma->get_Rect());
    }
}
```

### حذف MultimediaAnnotation

يعرض جزء الشيفرة التالي كيفية حذف MultimediaAnnotation من ملف PDF.

```cpp
void MultimediaAnnotations::DeleteRichMediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        page->get_Annotations()->Delete(ma);
    }
    document->Save(_dataDir + u"RichMediaAnnotation_del.pdf");
}
```

## إضافة تعليق توضيحي ثلاثي الأبعاد

اليوم، يمكن أن تحتوي ملفات PDF على مجموعة متنوعة من المحتويات بخلاف النصوص والرسومات البسيطة، بما في ذلك الهياكل المنطقية، والعناصر التفاعلية مثل التعليقات التوضيحية وحقول النماذج، والطبقات، والوسائط المتعددة (بما في ذلك محتوى الفيديو)، والكائنات ثلاثية الأبعاد.

يمكن عرض هذا المحتوى ثلاثي الأبعاد في ملف PDF باستخدام التعليقات التوضيحية ثلاثية الأبعاد.

توضح هذه القسم الخطوات الأساسية لإنشاء تعليق توضيحي ثلاثي الأبعاد في مستند PDF باستخدام مكتبة C++ من Aspose.PDF.

يتم إضافة التعليق التوضيحي ثلاثي الأبعاد باستخدام نموذج تم إنشاؤه بتنسيق U3D.

1. إنشاء [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) جديد
1. تحميل بيانات النموذج ثلاثي الأبعاد المطلوب (في حالتنا "Ring.u3d") لإنشاء [PDF3DContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_content/)
1. إنشاء كائن [3dArtWork](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_artwork/) وربطه بالمستند و3DContent
1. ضبط كائن pdf3dArtWork:

```cpp
void MultimediaAnnotation::Add3DAnnottaion()
{
    public static void Add3dAnnotation()
    {
        // Load the PDF file
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        var page = document.getPages().add();

        var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName("Ring.u3d");
        //set preview image if needed
        //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
        document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

        document.save(_dataDir + "sample_3d.pdf");
    }
}
```

هذا المثال البرمجي أظهر لنا نموذجًا كهذا:

![3D Annotation demo](3d_demo.png)

## إضافة توضيح الويدجت

يمثل توضيح الويدجت مظهر حقول النماذج في نموذج PDF التفاعلي.

منذ إصدار PDF 1.2 يمكننا استخدام توضيحات الويدجت. هذه هي عناصر النموذج التفاعلي التي يمكننا إضافتها إلى PDF لتسهيل إدخال أو إرسال المعلومات أو تنفيذ بعض الإجراءات الأخرى مع المستخدم. على الرغم من أن الويدجت عبارة عن نوع خاص من التوضيحات، لا يمكننا إنشاؤها كتوضيحات مباشرة، لأن توضيحات الويدجت هي تمثيل رسومي لحقل نموذج على صفحات محددة.

يمثل كل حقل نموذج لكل موقع في المستند توضيح ويدجت واحد. يتم إضافة بيانات التوضيح الخاصة بالموقع للويدجت إلى صفحة محددة. يحتوي كل حقل نموذج على عدة خيارات. يمكن أن يكون الزر تبديلًا أو مربع اختيار أو زر. يمكن أن تكون ويدجت التحديد عبارة عن مربع قائمة أو مربع تركيبة.

تسمح لك Aspose.PDF for C++ بإضافة هذا التوضيح باستخدام فئة [Widget Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.widget_annotation/).

لإضافة زر إلى الصفحة، نحتاج إلى استخدام مقتطف الشيفرة التالي:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;

void ExampleWidgetAnnotation::AddButton() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto rect = MakeObject<Rectangle>(72, 748, 164, 768);

    auto printButton = MakeObject<ButtonField>(page, rect);
    printButton->set_AlternateName(u"طباعة المستند الحالي");
    printButton->set_Color(Color::get_Black());
    printButton->set_PartialName(u"printBtn1");
    printButton->set_NormalCaption(u"طباعة المستند");

    auto border = MakeObject<Border>(printButton);
    border->set_Style(BorderStyle::Solid);
    border->set_Width(2);

    printButton->set_Border(border);
    printButton->get_Characteristics()->set_Border(System::Drawing::Color::FromArgb(255, 0, 0, 255));
    printButton->get_Characteristics()->set_Background(System::Drawing::Color::FromArgb(255, 0, 191, 255));
    auto wa = System::DynamicCast<Field>(printButton);
    document->get_Form()->Add(wa);

    document->Save(_dataDir + u"sample_widgetannot.pdf");
}
```

### استخدام إجراءات التنقل في المستند

يوضح هذا المثال كيفية إنشاء 4 أزرار:

```cpp
void ExampleWidgetAnnotation::AddDocumentNavigationActions() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"JSON Fundamenals.pdf");

    auto buttons = MakeArray<System::SmartPtr<ButtonField>>(4);
    auto alternateNames = MakeArray<String>({ u"انتقل إلى الصفحة الأولى", u"انتقل إلى الصفحة السابقة", u"انتقل إلى الصفحة التالية", u"انتقل إلى الصفحة الأخيرة" });
    auto normalCaptions = MakeArray<String>({ u"الأول", u"السابق", u"التالي", u"الأخير" });
    PredefinedAction actions[] = { PredefinedAction::FirstPage, PredefinedAction::PrevPage,
                                    PredefinedAction::NextPage, PredefinedAction::LastPage };
    auto clrBorder = System::Drawing::Color::FromArgb(255, 0, 255, 0);
    auto clrBackGround = System::Drawing::Color::Color::FromArgb(255, 0, 96, 70);

// ينبغي علينا إنشاء الأزرار بدون ربطها بالصفحة.

    for (int i = 0; i < 4; i++) {
        buttons[i] = MakeObject<ButtonField>(document, MakeObject<Rectangle>(32 + i * 80, 28, 104 + i * 80, 68));
        buttons[i]->set_AlternateName(alternateNames[i]);
        buttons[i]->set_Color(Color::get_White());
        buttons[i]->set_NormalCaption(normalCaptions[i]);
        buttons[i]->set_OnActivated(new NamedAction(actions[i]));
        auto border = MakeObject<Border>(buttons[i]);
        border->set_Style(BorderStyle::Solid);
        border->set_Width(2);
        buttons[i]->set_Border(border);
        buttons[i]->get_Characteristics()->set_Border(clrBorder);
        buttons[i]->get_Characteristics()->set_Background(clrBackGround);
    }

// ينبغي علينا تكرار هذه المجموعة من الأزرار على كل صفحة في المستند.

    for (int pageIndex = 1; pageIndex <= 4; pageIndex++)
        for (int i = 0; i < 4; i++)
            document->get_Form()->Add(buttons[i], String::Format(u"btn{0}_{1}", pageIndex,(i + 1)), pageIndex);

    document->get_Form()->idx_get(u"btn1_1")->set_ReadOnly(true);
    document->get_Form()->idx_get(u"btn1_2")->set_ReadOnly(true);

    document->get_Form()->idx_get(String::Format(u"btn{0}_3", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->get_Form()->idx_get(String::Format(u"btn{0}_4", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->Save(_dataDir + u"sample_widgetannot_2.pdf");
}
```

### حذف تعليق الودجت

```cpp
void ExampleWidgetAnnotation::DeleteWidgetAnnotation() {

    String _dataDir("C:\\Samples\\");

    // تحميل ملف PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_widgetannot.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(MakeObject<ButtonField>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto buttonFields = annotationSelector->get_Selected();

    // حذف التعليقات
    for (auto wa : buttonFields) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_widgetannot_del.pdf");
}
```