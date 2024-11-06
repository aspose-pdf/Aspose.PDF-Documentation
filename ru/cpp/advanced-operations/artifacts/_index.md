---
title: Работа с артефактами в C++
linktitle: Работа с артефактами
type: docs
weight: 110
url: ru/cpp/artifacts/
description: На этой странице описывается, как работать с классом Artifact, используя Aspose.PDF для C++. Примеры кода показывают, как добавить фоновое изображение на страницы PDF и как получить каждый водяной знак на первой странице PDF-файла.
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Как получить водяной знак в PDF?

**Что такое артефакт в PDF?**

Согласно PDF / UA ISO справочнику, содержимое, которое не важно или не отображается на заднем плане, не несет актуальной информации, должно быть помечено как артефакт, чтобы вспомогательные технологии могли его игнорировать.
Если артефакты не могут быть идентифицированы в программе создания, это должно быть сделано вручную с использованием Aspose.PDF для C++.

Класс [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) содержит следующие свойства:

- **Artifact.Type** – получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, где значения включают Background, Layout, Page, Pagination и Undefined).
- **Artifact.Subtype** – получает подтип артефакта (поддерживаются значения перечисления Artifact.ArtifactSubtype, где значения включают Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Обратите внимание, что водяные знаки, созданные с помощью Adobe Acrobat, имеют тип Pagination и подтип Watermark.

{{% /alert %}}

- **Artifact.Contents** – Получает коллекцию внутренних операторов артефакта. Поддерживаемый тип – System.Collections.ICollection.
- **Artifact.Form** – Получает XForm артефакта (если используется XForm). Артефакты водяных знаков, заголовков и подвалов содержат XForm, который показывает все содержимое артефакта.
- **Artifact.Image** – Получает изображение артефакта (если изображение присутствует, иначе null).
- **Artifact.Text** – Получает текст артефакта.
- **Artifact.Rectangle** – Получает позицию артефакта на странице.
- **Artifact.Rotation** – Получает вращение артефакта (в градусах, положительное значение указывает на вращение против часовой стрелки).
- **Artifact.Opacity** – Получает непрозрачность артефакта. Возможные значения находятся в диапазоне 0...1, где 1 — полностью непрозрачный.

Для примера работы с артефактами в PDF файле возьмем водяной знак.

Водяной знак, созданный с поддержкой Adobe Acrobat, называется артефактом (как описано в 14.8.2.2 Present Content and PDF Specification Artifacts). Для работы с артефактами Aspose.PDF содержит 2 класса: [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) и [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Чтобы получить все артефакты на определенной странице, класс [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) имеет свойство Artifacts. Эта тема показывает, как работать с водяным знаком в PDF файлах.

Следующий фрагмент кода показывает, как получить каждый водяной знак на первой странице PDF файла с помощью C++:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
void Artifacts::SetWatermark() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto artifact = MakeObject<WatermarkArtifact>();
    String text(u"WATERMARK");    
    artifact->set_Text(text);
    artifact->get_TextState()->set_ForegroundColor(Color::get_Blue());
    artifact->get_TextState()->set_FontSize(72);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(_dataDir + u"watermark.pdf");
}
```
Фоновые изображения могут быть использованы для добавления водяных знаков или эксклюзивных дизайнов в PDF документы. Aspose.PDF для C++ использует класс [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) для добавления фонового изображения к объекту страницы.

Следующий фрагмент кода показывает, как добавить фоновое изображение на страницы PDF с помощью объекта BackgroundArtifact:

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto pdfDocument = MakeObject<Document>();

    // Добавить страницу к объекту документ
    auto page = pdfDocument->get_Pages()->Add();

    // Создать объект Background Artifact
    auto background = MakeObject<BackgroundArtifact>();

    // Указать изображение для объекта backgroundartifact
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Добавить BackgroundArtifact в коллекцию артефактов страницы
    page->get_Artifacts()->Add(background);

    // Сохранить измененный PDF
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### Примеры программирования: Получение водяных знаков

Следующий фрагмент кода показывает, как получить каждый водяной знак на первой странице PDF файла.

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // Перебрать и получить подтип, текст и местоположение артефакта
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### Примеры программирования: Подсчет артефактов определенного типа

Чтобы вычислить общее количество артефактов определенного типа (например, общее количество водяных знаков), используйте следующий код:

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // Если тип артефакта водяной знак, увеличить счетчик
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"На странице {0} водяных знаков", count);
}
```