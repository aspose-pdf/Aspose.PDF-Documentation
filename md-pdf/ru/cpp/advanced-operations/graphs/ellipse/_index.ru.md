---
title: Добавить объект Эллипс в PDF файл
linktitle: Добавить Эллипс
type: docs
weight: 60
url: /cpp/add-ellipse/
description: Эта статья объясняет, как создать объект Эллипс в вашем PDF с использованием Aspose.PDF для C++.
lastmod: "2021-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавить объект Эллипс

Aspose.PDF для C++ поддерживает добавление объектов [Эллипс](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/) в PDF документы. Он также предлагает возможность заполнить объект эллипс определенным цветом.

```cpp
void ExampleEllipse() {
    // Создать экземпляр документа
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр документа
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    // Создать объект Drawing с определенными размерами
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Установить границу для объекта Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(150, 100, 120, 60);
    ellipse1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    ellipse1->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>("Эллипс"));
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(50, 50, 18, 300);
    ellipse2->get_GraphInfo()->set_Color(Color::get_DarkRed());

    graph->get_Shapes()->Add(ellipse2);

    // Добавить объект Graph в коллекцию абзацев страницы
    page->get_Paragraphs()->Add(graph);

    // Сохранить PDF файл
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");

}
```

![Add Ellipse](ellipse.png)

## Создание объекта заполненного эллипса

Следующий фрагмент кода показывает, как добавить объект [Ellipse](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/), заполненный цветом.

```csharp
void ExampleFilledEllipse() {
    // Создание экземпляра документа
    String _dataDir("C:\\Samples\\");
    // Создание экземпляра документа
    auto document = MakeObject<Document>();

    // Добавление страницы в коллекцию страниц PDF-файла
    auto page = document->get_Pages()->Add();

    // Создание объекта Drawing с определенными размерами
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Установка границы для объекта Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    // Добавление объекта Graph в коллекцию абзацев страницы
    page->get_Paragraphs()->Add(graph);

    // Сохранение PDF-файла
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");
}
```

![Заполненный Эллипс](fill_ellipse.png)

## Добавить текст внутри эллипса

Aspose.PDF для C++ поддерживает добавление текста внутри графического объекта. Свойство Text графического объекта предоставляет возможность установить текст графического объекта.

Следующий фрагмент кода показывает, как добавить текст внутри объекта Прямоугольник.

```cpp
void ExampleEllipseWithText() {
    // Создать экземпляр документа
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр документа
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    // Создать объект рисунка с определенными размерами
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Установить границу для объекта рисунка
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto textFragment = MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse");
    textFragment->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Helvetica"));
    textFragment->get_TextState()->set_FontSize(24);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    ellipse1->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    ellipse2->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse2);

    // Добавить объект Graph в коллекцию параграфов страницы
    page->get_Paragraphs()->Add(graph);

    // Сохранить PDF файл
    document->Save(_dataDir + u"DrawingEllipseText_out.pdf");
}
```

К сожалению, я не могу просматривать или переводить изображения. Пожалуйста, предоставьте текст в виде текста, и я помогу с его переводом.