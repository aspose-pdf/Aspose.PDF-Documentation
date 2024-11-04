---
title: Создание ссылок в PDF файле с C++
linktitle: Создание ссылок
type: docs
weight: 10
url: /cpp/create-links/
description: Этот раздел объясняет, как создавать ссылки в вашем PDF документе с помощью C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Создание ссылок

Добавляя ссылку на приложение в документ, можно ссылаться на приложения из документа. Это полезно, когда вы хотите, чтобы читатели предприняли определенное действие в конкретный момент в учебнике, например, или чтобы создать документ с богатым функционалом. Чтобы создать ссылку на приложение:

1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Получите [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page), к которой вы хотите добавить ссылку.
1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/), используя объекты Page и [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Установите атрибуты ссылки, используя объект [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. Также установите свойство Action объекта [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/).
1. При создании объекта [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/) укажите приложение, которое вы хотите запустить.
1. Добавьте ссылку в свойство [Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations) объекта Page.
1. Наконец, сохраните обновленный PDF, используя метод Save объекта Document.

Следующий фрагмент кода показывает, как создать ссылку на приложение в PDF файле.

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр Document
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // Сохранить обновленный документ
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```
### Создание ссылки на PDF-документ в PDF-файле

Aspose.PDF для C++ позволяет добавить ссылку на внешний PDF-файл, чтобы связать несколько документов вместе. Для создания ссылки на PDF-документ:

1. Сначала создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Затем получите определенную [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page), на которую хотите добавить ссылку.
1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) с использованием объектов Page и [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Установите атрибуты ссылки, используя объект [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. Установите свойство Action объекту [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/).
1. При создании объекта GoToRemoteAction укажите PDF файл, который должен запускаться, а также номер страницы, которую он должен открыть.
1. Добавьте ссылку в коллекцию Аннотации объекта Page.
1. Сохраните обновленный PDF, используя метод Save объекта Document.

Следующий фрагмент кода показывает, как создать ссылку на документ PDF в PDF файле.

 ```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // Создать экземпляр Document
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->idx_get(1);


    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // Сохранить обновленный документ
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```