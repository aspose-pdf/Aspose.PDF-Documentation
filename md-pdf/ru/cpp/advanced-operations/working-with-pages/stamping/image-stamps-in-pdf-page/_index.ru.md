---
title: Добавление штампов изображений в PDF программно
linktitle: Штампы изображений в PDF файле
type: docs
weight: 10
url: /cpp/image-stamps-in-pdf-page/
description: Добавьте штамп изображения в ваш PDF-документ с использованием класса ImageStamp с библиотекой Aspose.PDF для C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление штампа изображения в PDF файл

Вы можете использовать класс ImageStamp для добавления штампа изображения в PDF файл. Класс ImageStamp предоставляет свойства, необходимые для создания штампа на основе изображения, такие как высота, ширина, непрозрачность и так далее.

Чтобы добавить штамп изображения:

1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) и объект ImageStamp с использованием необходимых свойств.
1. Вызовите метод [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) класса [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) для добавления штампа в PDF.

Следующий фрагмент кода показывает, как добавить штамп изображения в PDF файл.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImageStampToPDFFile()
{    
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("AddImageStamp.pdf");

    String outputFileName("AddImageStamp_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Создать штамп изображения
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(48);
    imageStamp->set_Width(225);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);
   
    // Добавить штамп на определенную страницу    
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);

    // Сохранить выходной документ
    document->Save(_dataDir + outputFileName);
}
```

## Контроль качества изображения при добавлении штампа

При добавлении изображения в качестве объекта штампа, вы можете контролировать качество изображения. Свойство Quality класса [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) используется для этой цели. Оно указывает качество изображения в процентах (допустимые значения от 0 до 100).

```cpp
void ControlImageQualityWhenAddingStamp() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("ControlImageQuality_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Создать штамп изображения
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);    
    document->Save(_dataDir + u"ControlImageQuality_out.pdf");
}
```

## Штамп изображения как фон в плавающем блоке

Aspose.PDF API позволяет добавить штамп изображения как фон в плавающем блоке. Свойство BackgroundImage класса FloatingBox может использоваться для установки фонового изображения для плавающего блока, как показано в следующем примере кода.

```cpp
void ImageStampAsBackgroundInFloatingBox() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("AddImageStampAsBackgroundInFloatingBox_out.pdf");

    // Создание объекта Document
    auto document = MakeObject<Document>();

    // Добавление страницы в PDF документ
    auto page = document->get_Pages()->Add();

    // Создание объекта FloatingBox
    auto aBox = MakeObject<FloatingBox>(200, 100);

    // Установка левой позиции для FloatingBox
    aBox->set_Left(40);
    // Установка верхней позиции для FloatingBox
    aBox->set_Top(80);
    // Установка горизонтального выравнивания для FloatingBox
    aBox->set_HorizontalAlignment(HorizontalAlignment::Center);
    
    // Добавление текстового фрагмента в коллекцию параграфов FloatingBox    
    aBox->get_Paragraphs()->Add(MakeObject<TextFragment>(u"main text"));

    // Установка границы для FloatingBox
    aBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    // Добавление фонового изображения
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.png");
    aBox->set_BackgroundImage(image);

    // Установка фонового цвета для FloatingBox
    aBox->set_BackgroundColor(Color::get_Yellow());

    // Добавление FloatingBox в коллекцию параграфов объекта страницы
    page->get_Paragraphs()->Add(aBox);
    // Сохранение PDF документа
    document->Save(_dataDir + outputFileName);
}
```