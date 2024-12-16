---
title: Работа с размещением изображений с использованием C++
linktitle: Работа с размещением изображений
type: docs
weight: 50
url: /ru/cpp/working-with-image-placement/
description: Этот раздел описывает функции работы с размещением изображений в PDF файле с использованием библиотеки C++.
lastmod: "2021-12-18"
---

**Aspose.PDF для C++** поддерживает [ImagePlacement](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber) и [ImagePlacementCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection), которые предоставляют аналогичные возможности, как и описанные выше классы, для получения разрешения и позиции изображения в PDF документе.

- ImagePlacementAbsorber выполняет поиск использования изображения в виде коллекции объектов ImagePlacement.
- ImagePlacement предоставляет члены Resolution и Rectangle, которые возвращают фактические значения размещения изображения.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // Загрузить исходный PDF документ
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Загрузить содержимое первой страницы
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Получить свойства изображения
        Console::WriteLine(u"ширина изображения: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"высота изображения: {0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX изображения: {0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY изображения: {0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"горизонтальное разрешение изображения: {0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"вертикальное разрешение изображения: {0}", imagePlacement->get_Resolution()->get_Y());

        // Извлечь изображение с видимыми размерами
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // Извлечь изображение из ресурсов
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // Создать bitmap с фактическими размерами
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```