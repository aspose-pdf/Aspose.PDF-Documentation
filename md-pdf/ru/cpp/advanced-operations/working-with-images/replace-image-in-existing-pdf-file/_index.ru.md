---
title: Замена изображения в существующем PDF файле с использованием C++
linktitle: Замена изображения
type: docs
weight: 70
url: /cpp/replace-image-in-existing-pdf-file/
description: Этот раздел описывает замену изображения в существующем PDF файле с использованием библиотеки ++.
lastmod: "2021-12-18"
---

Метод Replace коллекции Images позволяет заменить изображение в существующем PDF файле.

Коллекция Images находится в коллекции Resources страницы. Чтобы заменить изображение:

1. Откройте PDF файл, используя объект Document.
2. Замените конкретное изображение, сохраните обновленный PDF файл, используя метод Save объекта Document.

Следующий фрагмент кода показывает, как заменить изображение в PDF файле.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // Замените конкретное изображение
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // Сохраните обновленный PDF файл
    document->Save(_dataDir + u"output.pdf");
}
```