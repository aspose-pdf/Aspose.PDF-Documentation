---
title: Добавить объект круга в PDF файл
linktitle: Добавить круг
type: docs
weight: 20
url: /ru/cpp/add-circle/
description: В этой статье объясняется, как создать объект круга в вашем PDF с помощью Aspose.PDF для C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавить объект круга

Как и столбчатые графики, круговые графики могут использоваться для отображения данных в нескольких отдельных категориях. Однако, в отличие от столбчатых графиков, круговые графики можно использовать только тогда, когда у вас есть данные для всех категорий, составляющих целое. Итак, давайте рассмотрим добавление объекта [Circle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.circle/) с Aspose.PDF для C++.

Следуйте шагам ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Создайте [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) с определенными размерами

1. Установите [границу](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) для объекта Drawing

1. Добавьте объект [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) в коллекцию абзацев страницы

1. Сохраните наш PDF файл

```cpp
void ExampleCircle() {

    // Создайте экземпляр документа
    String _dataDir("C:\\Samples\\");
    // Создайте экземпляр документа
    auto document = MakeObject<Document>();

    // Добавьте страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    // Создайте объект Drawing с определенными размерами
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    // Установите границу для объекта Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);

    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    // Добавьте объект Graph в коллекцию абзацев страницы
    page->get_Paragraphs()->Add(graph);

    // Сохраните PDF файл
    document->Save(_dataDir + u"DrawingCircle1_out.pdf");
}
```
Наш нарисованный круг будет выглядеть так:

![Рисование круга](drawing_circle.png)

## Создание объекта заполненного круга

Этот пример показывает, как добавить объект круга, который заполнен цветом.

```cpp
void ExampleFilledCircle() {
    // Создать экземпляр документа
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр документа
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц PDF-файла
    auto page = document->get_Pages()->Add();

    // Создать объект рисования с определёнными размерами
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Установить границу для объекта рисования
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());

    circle->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Круг"));

    graph->get_Shapes()->Add(circle);

    // Добавить объект Graph в коллекцию параграфов страницы
    page->get_Paragraphs()->Add(graph);

    // Сохранить PDF-файл
    document->Save(_dataDir + u"DrawingCircle2_out.pdf");
}
```

```
Давайте посмотрим на результат добавления залитого круга:

![Залитый круг](filled_circle.png)
```