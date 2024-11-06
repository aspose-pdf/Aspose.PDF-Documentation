---
title: تعيين اسم الخط الافتراضي باستخدام C++
linktitle: تعيين اسم الخط الافتراضي
type: docs
weight: 90
url: ar/cpp/set-default-font-name/
description: يصف هذا القسم كيفية تعيين اسم الخط الافتراضي باستخدام مكتبة C++.
lastmod: "2021-12-18"
---

تتيح لك واجهة برمجة التطبيقات **Aspose.PDF for C++** تعيين اسم خط افتراضي عندما لا يكون الخط متاحًا في المستند. يمكنك استخدام خاصية DefaultFontName الخاصة بفئة RenderingOptions لتعيين اسم الخط الافتراضي. في حالة تعيين DefaultFontName إلى `nullptr` سيتم استخدام خط **Times New Roman**. يوضح مقطع الشيفرة التالي كيفية تعيين اسم خط افتراضي عند حفظ PDF كصورة:

```cpp
void WorkingWithImages::ExampleSetDefaultFontName()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    auto imageStream = System::IO::File::OpenWrite(_dataDir + u"SetDefaultFontName.png");

    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);
    auto pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    auto ro = MakeObject<RenderingOptions>();
    ro->set_DefaultFontName(u"Arial");
    pngDevice->set_RenderingOptions(ro);
    pngDevice->Process(document->get_Pages()->idx_get(1), imageStream);
}
```