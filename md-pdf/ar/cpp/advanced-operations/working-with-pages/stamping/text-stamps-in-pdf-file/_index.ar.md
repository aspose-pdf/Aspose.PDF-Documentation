---
title: إضافة ختم نصي في ملف PDF
linktitle: الأختام النصية في ملف PDF
type: docs
weight: 20
url: /cpp/text-stamps-in-the-pdf-file/
description: إضافة ختم نصي إلى ملف PDF باستخدام فئة TextStamp مع C++.
lastmod: "2021-12-95"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة ختم نصي باستخدام C++

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) لإضافة ختم نصي في ملف PDF. توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، ونمط الخط، ولون الخط إلخ. من أجل إضافة ختم نصي، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة الختم في ملف PDF. يوضح لك المقتطف البرمجي التالي كيفية إضافة ختم نصي في ملف PDF.

```cpp
void AddTextStampToPDFFile() {
   
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    
    // Create text stamp
    auto textStamp =MakeObject<TextStamp>(u"Sample Stamp");

    // Set whether stamp is background
    textStamp->set_Background(true);
    // Set origin
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // Rotate stamp
    textStamp->set_Rotate(Rotation::on90);

    // Set text properties
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // Add stamp to particular page
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // Save output document
    document->Save(_dataDir + outputFileName);
}
```

## تعريف المحاذاة لكائن TextStamp

إضافة العلامات المائية إلى مستندات PDF هي واحدة من الميزات المطلوبة بشكل متكرر وAspose.PDF لـ C++ قادر تمامًا على إضافة علامات مائية من الصور وكذلك النصوص. لدينا فئة تدعى [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) التي توفر ميزة إضافة الأختام النصية على ملف PDF. مؤخرًا كان هناك طلب لدعم ميزة تحديد محاذاة النص عند استخدام كائن TextStamp. لذا من أجل تلبية هذا الطلب، قمنا بتقديم خاصية TextAlignment في فئة TextStamp. باستخدام هذه الخاصية، يمكننا تحديد المحاذاة الأفقية للنص.

تُظهر الشيفرات البرمجية التالية مثالًا عن كيفية تحميل مستند PDF موجود وإضافة TextStamp عليه.

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // سلسلة لأسم الملف المدخل
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // فتح المستند
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    
    // إنشاء كائن FormattedText مع سلسلة عينة
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // إضافة سطر نص جديد إلى FormattedText
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // إنشاء كائن TextStamp باستخدام FormattedText
    auto stamp = MakeObject<TextStamp>(text);
    // تحديد المحاذاة الأفقية لختم النص كمحاذاة مركزية
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // تحديد المحاذاة العمودية لختم النص كمحاذاة مركزية
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // تحديد المحاذاة الأفقية للنص في TextStamp كمحاذاة مركزية
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // تعيين الهامش العلوي لكائن الختم
    stamp->set_TopMargin(20);
    // إضافة الختم لجميع صفحات ملف PDF
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // حفظ المستند الناتج
    document->Save(_dataDir + outputFileName);
}
```

## ملء نص الحدود كختم في ملف PDF

لقد قمنا بتنفيذ ضبط وضع العرض لسيناريوهات إضافة النص وتحريره. لعرض نص الحدود، يرجى إنشاء كائن TextState وضبط RenderingMode إلى TextRenderingMode.StrokeText وأيضًا اختيار اللون لخاصية StrokingColor. لاحقًا، قم بربط TextState بالختم باستخدام طريقة BindTextState().

يظهر مقتطف الكود التالي إضافة نص ملء الحدود:

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Create TextState object to transfer advanced properties
    auto ts = MakeObject<TextState>();

    // Set color for stroke
    ts->set_StrokingColor(Color::get_Gray());

    // Set text rendering mode
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // Load an input PDF document
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // Bind TextState
    stamp->BindTextState(ts);

    // Set X,Y origin
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // Add Stamp
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```