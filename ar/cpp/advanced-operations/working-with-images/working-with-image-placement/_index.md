---
title: العمل مع وضع الصورة باستخدام C++
linktitle: العمل مع وضع الصورة
type: docs
weight: 50
url: ar/cpp/working-with-image-placement/
description: يصف هذا القسم ميزات العمل مع وضع الصور في ملف PDF باستخدام مكتبة C++.
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** يدعم [ImagePlacement](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement)، [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber) و [ImagePlacementCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection) التي توفر قدرة مماثلة للفئات الموضحة أعلاه للحصول على دقة الصورة وموقعها في مستند PDF.

- يقوم ImagePlacementAbsorber بإجراء بحث عن استخدام الصورة كمجموعة كائنات ImagePlacement.
- يوفر ImagePlacement الأعضاء Resolution و Rectangle الذين يعيدون قيم وضع الصورة الفعلية.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // تحميل مستند PDF المصدر
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // تحميل محتويات الصفحة الأولى
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // الحصول على خصائص الصورة
        Console::WriteLine(u"عرض الصورة: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"ارتفاع الصورة: {0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX للصورة: {0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY للصورة: {0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"دقة الصورة الأفقية: {0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"دقة الصورة الرأسية: {0}", imagePlacement->get_Resolution()->get_Y());

        // استرداد الصورة بالأبعاد المرئية
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // استرداد الصورة من الموارد
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // إنشاء صورة نقطية بالأبعاد الفعلية
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```