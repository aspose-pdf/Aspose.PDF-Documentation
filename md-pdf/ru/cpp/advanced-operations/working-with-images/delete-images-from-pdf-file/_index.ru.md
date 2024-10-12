---
title: Удаление Изображений из PDF Файла с использованием C++
linktitle: Удаление Изображений
type: docs
weight: 20
url: /cpp/delete-images-from-pdf-file/
description: Этот раздел объясняет, как удалить изображения из PDF файла с использованием Aspose.PDF для C++.
lastmod: "2021-12-18"
---

Чтобы удалить изображение из PDF файла:

1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) и откройте входной PDF файл.
1. Получите страницу, содержащую изображение, из [коллекции страниц](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) объекта Document.
1. Изображения находятся в коллекции Images, которая расположена в коллекции ресурсов страницы.
1. Удалите изображение с помощью метода Delete коллекции Images.
1. Сохраните результат с помощью метода Save объекта Document.

Следующий код демонстрирует, как удалить изображение из PDF файла.

```cpp
void WorkingWithImages::DeleteImagesFromPDFFile()
{
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"DeleteImages.pdf");

    // Удалить конкретное изображение
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);

    // Сохранить обновленный PDF файл
    document->Save(_dataDir + u"DeleteImages_out.pdf");
}
```