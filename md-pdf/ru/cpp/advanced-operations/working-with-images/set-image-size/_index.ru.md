---
title: Установить размер изображения с помощью C++
linktitle: Установить размер изображения
type: docs
weight: 80
url: /cpp/set-image-size/
description: Этот раздел описывает, как установить размер изображения в PDF файле с использованием библиотеки C++.
lastmod: "2021-12-18"
---

Можно установить размер изображения, добавляемого в PDF файл. Чтобы установить размер, вы можете использовать свойства [FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e) и [FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa) класса [Aspose.Pdf.Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image).

Следующий фрагмент кода демонстрирует, как установить размер изображения:

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр объекта Document
    auto document = MakeObject<Document>();
    // добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();
    // Создать экземпляр изображения
    auto img = MakeObject<Image>();
    // Установить ширину и высоту изображения в пунктах
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // Установить тип изображения как SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // Путь к исходному файлу
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    // Установить свойства страницы
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // сохранить полученный PDF файл
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```
```