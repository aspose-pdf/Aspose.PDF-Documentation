---
title: البحث والحصول على الصور من مستند PDF باستخدام C++
linktitle: البحث والحصول على الصور
type: docs
weight: 60
url: /ar/cpp/search-and-get-images-from-pdf-document/
description: يشرح هذا القسم كيفية البحث والحصول على الصور من مستند PDF باستخدام مكتبة Aspose.PDF.
lastmod: "2021-12-18"
---

يسمح لك ImagePlacementAbsorber بالبحث بين الصور على جميع الصفحات في مستند PDF.

للبحث في مستند كامل عن الصور:

1. استدعاء طريقة [Accept](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f) لمجموعة [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection). تأخذ طريقة Accept كائن [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/) كمعامل. هذا يعيد مجموعة من كائنات ImagePlacement.
1. قم بالتكرار عبر كائنات ImagePlacements واحصل على خصائصها (الصورة، الأبعاد، الدقة وما إلى ذلك).

يوضح مقطع الشيفرة التالي كيفية البحث في مستند عن جميع صوره.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // افتح المستند
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // قم بإنشاء كائن ImagePlacementAbsorber لأداء بحث وضع الصورة
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // قبول الماص لجميع الصفحات
    document->get_Pages()->Accept(abs);

    // قم بالتكرار عبر جميع ImagePlacements، الحصول على الصورة وخصائص ImagePlacement
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // احصل على الصورة باستخدام كائن ImagePlacement
        auto image = imagePlacement->get_Image();

        // عرض خصائص وضع الصورة لجميع المواضع
        Console::WriteLine(u"عرض الصورة: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"ارتفاع الصورة:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX الصورة:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY الصورة:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"الدقة الأفقية للصورة:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"الدقة العمودية للصورة:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```