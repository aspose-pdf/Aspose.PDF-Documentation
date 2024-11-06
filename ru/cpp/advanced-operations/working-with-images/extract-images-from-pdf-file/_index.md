---
title: Извлечение изображений из PDF файла с использованием C++
linktitle: Извлечение изображений
type: docs
weight: 30
url: ru/cpp/extract-images-from-pdf-file/
description: Этот раздел показывает, как извлечь изображения из PDF файла с использованием библиотеки C++.
lastmod: "2021-12-18"
---

Вы можете использовать Aspose.PDF for C++ для извлечения всех изображений из ваших PDF документов в отдельные файлы, которые могут быть использованы в других программах.

Изображения хранятся в коллекции Resources на каждой странице, в коллекции Images. Чтобы извлечь изображение с определенной страницы, получите изображение из коллекции Images, используя определенный индекс изображения.

Индекс изображения возвращает объект [XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image). Этот объект предоставляет метод Save, который может быть использован для сохранения извлеченного изображения.

Следующий фрагмент кода показывает, как извлечь изображения из PDF файла.

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // Извлечь определенное изображение
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // Сохранить извлеченное изображение
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // Сохранить обновленный PDF файл
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```