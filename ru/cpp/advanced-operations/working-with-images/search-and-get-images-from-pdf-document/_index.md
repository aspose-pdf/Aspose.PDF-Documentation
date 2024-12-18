---
title: Поиск и Извлечение Изображений из PDF Документа с использованием C++
linktitle: Поиск и Извлечение Изображений
type: docs
weight: 60
url: /ru/cpp/search-and-get-images-from-pdf-document/
description: Этот раздел объясняет, как искать и извлекать изображения из PDF документа с библиотекой Aspose.PDF.
lastmod: "2021-12-18"
---

ImagePlacementAbsorber позволяет искать среди изображений на всех страницах в PDF документе.

Чтобы произвести поиск изображений во всем документе:

1. Вызовите метод [Accept](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f) коллекции [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection). Метод Accept принимает объект [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/) в качестве параметра. Это возвращает коллекцию объектов ImagePlacement.
1. Пройдитесь по объектам ImagePlacements и получите их свойства (изображение, размеры, разрешение и так далее).

Следующий фрагмент кода показывает, как искать в документе все его изображения.

```cpp
используя пространство имен System;
используя пространство имен Aspose::Pdf;
используя пространство имен Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // Создать объект ImagePlacementAbsorber для выполнения поиска размещения изображений
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Принять абсорбер для всех страниц
    document->get_Pages()->Accept(abs);

    // Перебрать все ImagePlacements, получить изображение и свойства ImagePlacement
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Получить изображение, используя объект ImagePlacement
        auto image = imagePlacement->get_Image();

        // Отобразить свойства размещения изображений для всех размещений
        Console::WriteLine(u"ширина изображения: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"высота изображения:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX изображения:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY изображения:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"горизонтальное разрешение изображения:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"вертикальное разрешение изображения:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```