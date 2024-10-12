---
title: Обновить ссылки в PDF
linktitle: Обновить ссылки
type: docs
weight: 20
url: /cpp/update-links/
description: Обновление ссылок в PDF программным путем с помощью Aspose.PDF для C++. Это руководство о том, как обновить ссылки в PDF файле.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Обновить ссылки в PDF файле

Как обсуждалось в Добавить гиперссылку в PDF файл, класс [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) позволяет добавлять ссылки в PDF файл. Существует также аналогичный класс, используемый для получения существующих ссылок из PDF файлов. Используйте его, если вам нужно обновить существующую ссылку. Чтобы обновить существующую ссылку:

1. Загрузите PDF файл.
1. Перейдите на определенную страницу в PDF файле.
1. Укажите назначение ссылки, используя свойство Destination объекта [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action). Целевая страница указывается с использованием конструктора [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination).

### Установить цель ссылки на страницу в том же документе

Следующий фрагмент кода показывает, как обновить ссылку в PDF-файле и установить её цель на второй странице документа.

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр документа
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Добавить страницу в коллекцию страниц PDF-файла
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Изменение ссылки: изменение назначения ссылки
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // Указать назначение для объекта ссылки
    // Представляет явное назначение, которое отображает страницу с координатами (слева, сверху), расположенными в верхнем левом углу 
    // окна, и содержимое страницы увеличено в соответствии с коэффициентом увеличения.
    // Первый параметр - номер целевой страницы. 
    // Второй - левая координата
    // Третий - верхняя координата
    // Четвертый аргумент - коэффициент увеличения при отображении соответствующей страницы. Использование 2 означает, что страница будет отображаться с увеличением 200%
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // Сохранить документ с обновленной ссылкой
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```
### Установить назначение ссылки на веб-адрес

Чтобы обновить гиперссылку так, чтобы она указывала на веб-адрес, создайте объект [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) и передайте его в свойство Action LinkAnnotation. В следующем фрагменте кода показано, как обновить ссылку в PDF-файле и установить её цель на веб-адрес.

```cpp
void SetLinkDestinationToWebAddress() 
{
    // Загрузить PDF файл
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр документа
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Изменение ссылки: изменение действия ссылки и установка цели как веб-адрес
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // Сохранить документ с обновленной ссылкой
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Установить цель ссылки на другой PDF файл

Следующий фрагмент кода показывает, как обновить ссылку в PDF файле и установить её цель на другой PDF файл.

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // Загрузить PDF файл
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр документа
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Изменение ссылки: изменить действие ссылки и установить цель как веб-адрес
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // Следующая строка обновляет пункт назначения, файл не обновляется
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // Следующая строка обновляет файл
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // Сохранить документ с обновленной ссылкой
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Обновление цвета текста аннотации ссылки

Аннотация ссылки не содержит текста. Вместо этого текст размещается в содержимом страницы под аннотацией. Поэтому, чтобы изменить цвет текста, замените цвет текста страницы, вместо того чтобы пытаться изменить цвет аннотации. Следующий фрагмент кода показывает, как обновить цвет аннотации ссылки в PDF файле.

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // Загрузить PDF файл
    String _dataDir("C:\\Samples\\");

    // Создать экземпляр Document
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // Поиск текста под аннотацией
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // Изменение цвета текста.
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // Сохранить документ с обновленной ссылкой
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```