---
title: Добавить водяной знак в PDF с использованием C++
linktitle: Добавить водяной знак
type: docs
weight: 90
url: /cpp/add-watermarks/
description: В этой статье объясняются функции работы с артефактами и получения водяных знаков в PDF программным способом с использованием C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Водяной знак — это полупрозрачное изображение, которое обычно содержит логотип или печать для идентификации того, кто создал документ или изображение.

**Aspose.PDF for C++** позволяет добавлять водяные знаки в ваш PDF документ с использованием класса Artifact. Пожалуйста, ознакомьтесь с этой статьей, чтобы решить вашу задачу.

Водяной знак, созданный с помощью Adobe Acrobat, называется артефактом (как описано в разделе 14.8.2.2 Настоящее содержание и артефакты спецификации PDF). Для работы с артефактами Aspose.PDF имеет два класса: [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) и [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Для получения всех артефактов на конкретной странице класс [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) имеет свойство Artifacts. Этот раздел объясняет, как работать с артефактами в PDF-файлах.

## Работа с артефактами

Класс [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) содержит следующие свойства:

**Artifact.Type** – получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, где значения включают Background, Layout, Page, Pagination и Undefined).
**Artifact.Subtype** – получает подтип артефакта (поддерживает значения перечисления Artifact.ArtifactSubtype, где значения включают Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Обратите внимание, что водяные знаки, созданные с помощью Adobe Acrobat, имеют тип Pagination и подтип Watermark.

{{% /alert %}}

**Artifact.Contents** – Получает коллекцию внутренних операторов артефакта. Поддерживаемый тип - System.Collections.ICollection.
**Artifact.Form** – Получает XForm артефакта (если используется XForm). Артефакты водяных знаков, заголовков и нижних колонтитулов содержат XForm, который показывает все содержимое артефакта.

**Artifact.Image** – Получает изображение артефакта (если изображение присутствует, иначе null).**Artifact.Text** – Получает текст артефакта.  
**Artifact.Rectangle** – Получает позицию артефакта на странице.  
**Artifact.Rotation** – Получает вращение артефакта (в градусах, положительное значение указывает на вращение против часовой стрелки).  
**Artifact.Opacity** – Получает непрозрачность артефакта. Возможные значения находятся в диапазоне 0…1, где 1 означает полностью непрозрачный.

## Примеры программирования: Как добавить водяной знак в PDF файлы

Следующий фрагмент кода показывает, как получить каждый водяной знак на первой странице PDF файла с помощью C++.

```cpp
void GettingWatermarks() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("watermark.pdf");
    String outputFileName("watermark_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto artifact = MakeObject<WatermarkArtifact>();
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(72);
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_Font(FontRepository::FindFont(u"Courier"));
    artifact->SetTextAndState(u"WATERMARK", textState);
    artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);

    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);

    document->Save(_dataDir + outputFileName);
}
```