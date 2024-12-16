---
title: Извлечение ссылок из PDF файла
linktitle: Извлечение ссылок
type: docs
weight: 30
url: /ru/cpp/extract-links/
description: Извлечение ссылок из PDF с использованием C#. Эта тема объясняет, как извлечь ссылки с помощью класса AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение ссылок из PDF файла

Ссылки представлены как аннотации в PDF файле, поэтому для извлечения ссылок извлеките все объекты [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).

1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Получите [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page), с которой вы хотите извлечь ссылки.
1. Используйте класс [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/), чтобы извлечь все объекты [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) с указанной страницы.
1. Передайте объект [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) методу Accept объекта Page.
1. Получите все выбранные аннотации ссылок в объект IList, используя свойство Selected объекта [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).

Следующий фрагмент кода показывает, как извлечь ссылки из PDF файла.

```cpp
void ExtractLinksFromThePDFFile() {
   
    // Загрузите PDF файл
    String _dataDir("C:\\Samples\\");

    // Создайте экземпляр документа
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Добавьте страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->idx_get(1);


    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"Аннотация расположена: {0}", annot->get_Rect());
    }
}
```