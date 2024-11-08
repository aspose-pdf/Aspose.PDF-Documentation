---
title: Добавить объект дуги в PDF файл
linktitle: Добавить дугу
type: docs
weight: 10
url: /ru/cpp/add-arc/
description: В этой статье объясняется, как создать объект дуги в вашем PDF с использованием Aspose.PDF для C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавить объект дуги

Aspose.PDF для C++ поддерживает возможность добавления графических объектов (например, график, линия, прямоугольник и т.д.) в PDF документы. Он также предлагает возможность заполнить объект [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc) определенным цветом.

Следуйте шагам ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Создайте [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) с определенными размерами

1. Установите [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) для Drawing object

1. Добавьте объект [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) в коллекцию абзацев страницы

1. Сохраните наш PDF файл

Следующий фрагмент кода показывает, как добавить объект [Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc/).

```cpp
void ExampleArc() {
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

    auto arc1 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc1);

    auto arc2 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 90, 70, 180);
    arc2->get_GraphInfo()->set_Color(Color::get_DarkBlue());
    graph->get_Shapes()->Add(arc2);

    auto arc3 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 85, 120, 210);
    arc3->get_GraphInfo()->set_Color(Color::get_Red());
    graph->get_Shapes()->Add(arc3);

    // Добавьте объект Graph в коллекцию абзацев страницы
    page->get_Paragraphs()->Add(graph);

    // Сохраните PDF файл
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```
## Создать заполненный объект дуги

Следующий пример показывает, как добавить объект дуги, заполненный цветом и с определенными размерами.

```cpp
void ExampleFilledArc() {

    // Создать экземпляр документа
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр документа
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    // Создать объект рисования с определенными размерами
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Установить границу для объекта рисования
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<double>({ 195, 100, 100, 100, 100, 195 }));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    // Добавить объект Graph в коллекцию параграфов страницы
    page->get_Paragraphs()->Add(graph);

    // Сохранить файл PDF
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```


Давайте посмотрим на результат добавления заполненной дуги:

![Filled Arc](filled_arc.png)
```