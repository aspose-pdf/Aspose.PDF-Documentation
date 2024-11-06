---
title: PDF Tooltip باستخدام C++
linktitle: PDF Tooltip
type: docs
weight: 20
url: ar/cpp/pdf-tooltip/
description: تعلم كيفية إضافة تلميح نصي إلى جزء من النص في PDF باستخدام C++ و Aspose.PDF
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة تلميح نصي إلى النص الذي تم البحث عنه بإضافة زر غير مرئي

توضح هذه المقالة كيفية إضافة تلميح نصي إلى النص في مستند PDF موجود باستخدام C++. تدعم Aspose.PDF إنشاء تلميحات نصية عن طريق إضافة زر غير مرئي فوق النص الذي تم البحث عنه من ملف PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("Tooltip_out.pdf");

    // Create sample document with text
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("ضع مؤشر الماوس هنا لعرض التلميح النصي"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("ضع مؤشر الماوس هنا لعرض تلميح نصي طويل جدًا"));

    document->Save(outputFileName);

    // Open document with text
    auto document = MakeObject<Document>(outputFileName);
    // Create TextAbsorber object to find all the phrases matching the regular expression
    auto absorber = MakeObject<TextFragmentAbsorber>("ضع مؤشر الماوس هنا لعرض التلميح النصي");
    // Accept the absorber for the document pages
    document->get_Pages()->Accept(absorber);

    // Get the extracted text fragments
    auto textFragments = absorber->get_TextFragments();

    // Loop through the fragments
    for(auto fragment : textFragments)
    {
        // Create invisible button on text fragment position
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // AlternateName value will be displayed as tooltip by a viewer application
        field->set_AlternateName (u"تلميح نصي للنص.");
        // Add button field to the document
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Next will be sample of very long tooltip
    absorber = MakeObject<TextFragmentAbsorber>("ضع مؤشر الماوس هنا لعرض تلميح نصي طويل جدًا");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // Set very long text
        field->set_AlternateName(String("لوريم إيبسوم دولار سيت أميت، كونسيكتيتور أديبيسيسينغ إيليت،\
            سيد دو إيوسمود تيمبور إنسيديديونت أوت لابوري إت دولوري ماجنا\
            أليكا. أوت إينيم أد مينيم فينيام، كويز نوسترود إكسرسيتاتيون\
            أوللامكو لابوريس نيسي أوت أليكيب إكس إي كومودو كونسيكوات.\
            ديوس أوتي إيرور دولور إن ريبريهيندريت إن فولوبات فيليت\
            إيسي سيللوم دولور يو فوجيات نولا بارياتور. إكسسيبتور سينت\
            أوكايكات كيوبيداتات نون برويدنت، سونت إن كولبا كي أوفيسيا\
            ديزيرونت موليت أنيم إيد إيست لابوروم."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Save document
    document->Save(outputFileName);

}
```


## إنشاء كتلة نصية مخفية وإظهارها عند تحريك الماوس

يطبق Aspose.PDF for C++ وظيفة إخفاء الإجراءات، والتي يمكنك من خلالها إظهار/إخفاء حقل نصي (أو أي نوع آخر من التعليقات التوضيحية) عند دخول/خروج الماوس فوق زر غير مرئي. للقيام بذلك، استخدم فئة Aspose.Pdf.Annotations.HideAction لتعيين إجراء إخفاء/إظهار للكتلة النصية. استخدم الكود التالي لإظهار/إخفاء الكتلة النصية عند إدخال/إخراج الماوس.

لاحظ أيضًا أن إجراءات PDF على المستندات تعمل بشكل جيد في قراءاتها الخاصة (مثل Adobe Reader)، ولكنها لا تقدم أي ضمانات للقراء PDF الآخرين (مثل ملحقات المستعرضات). قمنا بتحقيق قصير ووجدنا:

- جميع تطبيقات إجراء الإخفاء في مستندات PDF تعمل بشكل جيد في Internet Explorer v.11.0.
- جميع تطبيقات إجراء الإخفاء تعمل أيضًا في Opera v.12.14، لكننا لاحظنا بعض التأخير في الاستجابة عند فتح المستند لأول مرة.

- فقط التطبيق الذي يستخدم منشئ HideAction الذي يقبل اسم الحقل يعمل إذا كان Google Chrome v.61.0 يستعرض المستند؛ يرجى استخدام المنشئات المقابلة إذا كان التصفح في Google Chrome له أهمية:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // سلسلة لاسم الملف الناتج
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // إنشاء مستند نموذج مع النص
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("حرك مؤشر الماوس هنا لعرض النص العائم"));
    document->Save(outputFileName);

    // فتح المستند مع النص
    auto document = MakeObject<Document>(outputFileName);

    // إنشاء كائن TextAbsorber للعثور على جميع العبارات المطابقة للتعبير العادي
    auto absorber = MakeObject<TextFragmentAbsorber>("حرك مؤشر الماوس هنا لعرض النص العائم");
    // قبول الماص للمستند الصفحات
    document->get_Pages()->Accept(absorber);
    // الحصول على أول جزء نصي مستخرج
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // إنشاء حقل نص مخفي للنص العائم في المستطيل المحدد من الصفحة
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // تعيين النص ليتم عرضه كقيمة حقل
    floatingField->set_Value(u"هذا هو \"حقل النص العائم\".");
    // نوصي بجعل الحقل 'للقراءة فقط' لهذا السيناريو
    floatingField->set_ReadOnly(true);
    // تعيين علم 'مخفي' لجعل الحقل غير مرئي عند فتح المستند
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // تعيين اسم حقل فريد ليس ضروريًا ولكن مسموح به
    floatingField->set_PartialName (u"FloatingField_1");

    // تعيين خصائص مظهر الحقل ليس ضروريًا ولكن يجعله أفضل
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // إضافة حقل النص إلى المستند
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // إنشاء زر غير مرئي على موقع جزء النص
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // إنشاء إجراء إخفاء جديد للحقل المحدد (التعليق التوضيحي) وعلم عدم الظهور.
    // (يمكنك أيضًا الإشارة إلى الحقل العائم بالاسم إذا قمت بتحديده أعلاه.)
    // إضافة الإجراءات عند إدخال/خروج الماوس في حقل الزر غير المرئي
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // إضافة حقل الزر إلى المستند
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // حفظ المستند
    document->Save(outputFileName);
}
```