---
title: Извлечение изображений из PDF
linktitle: Извлечение изображений из PDF
type: docs
weight: 20
url: ru/cpp/extract-images-from-the-pdf-file/
description: Как извлечь часть изображения из PDF с использованием Aspose.PDF для C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Также востребованной задачей при работе с PDF-документами является извлечение изображений из файла PDF. Например, вы получили PDF по электронной почте с множеством отличных изображений, которые вы хотели бы извлечь как отдельные файлы.

Библиотека Aspose.PDF позволяет извлекать изображения из PDF с помощью следующего фрагмента кода:

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Извлечь конкретное изображение
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Сохранить выходное изображение
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```