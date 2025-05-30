---
title: Добавить водяной знак в PDF 
linktitle: Добавить водяной знак
type: docs
weight: 90
url: /ru/php-java/add-watermarks/
description: В этой статье объясняются особенности работы с артефактами и получения водяных знаков в PDF с использованием PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF для PHP через Java** позволяет добавлять водяные знаки в ваш PDF-документ, используя артефакты. Пожалуйста, ознакомьтесь с этой статьей, чтобы решить вашу задачу.

Водяной знак, созданный с помощью Adobe Acrobat, называется артефактом (как описано в разделе 14.8.2.2 Реальное содержимое и артефакты спецификации PDF). Для работы с артефактами Aspose.PDF имеет два класса: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) и [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

Для получения всех артефактов на конкретной странице, класс [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) имеет свойство Artifacts.
 Этот раздел объясняет, как работать с артефактами в PDF файлах.

## Работа с артефактами

Класс [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) содержит следующие свойства:

**Artifact.Type** – получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, где значения включают Background, Layout, Page, Pagination и Undefined).
**Artifact.Subtype** – получает подтип артефакта (поддерживает значения перечисления Artifact.ArtifactSubtype, где значения включают Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Обратите внимание, что водяные знаки, созданные с помощью Adobe Acrobat, имеют тип Pagination и подтип Watermark.

{{% /alert %}}

**Artifact.Contents** – получает коллекцию внутренних операторов артефакта. Поддерживаемый тип – System.Collections.ICollection.
**Artifact.Form** – получает XForm артефакта (если используется XForm). Водяные знаки, заголовки и нижние колонтитулы содержат XForm, который показывает все содержимое артефакта.

**Artifact.Image** – получает изображение артефакта (если изображение присутствует, иначе null).**Artifact.Text** – Получает текст артефакта.  
**Artifact.Rectangle** – Получает позицию артефакта на странице.  
**Artifact.Rotation** – Получает поворот артефакта (в градусах, положительное значение указывает на поворот против часовой стрелки).  
**Artifact.Opacity** – Получает непрозрачность артефакта. Возможные значения находятся в диапазоне 0…1, где 1 — полностью непрозрачный.

## Примеры программирования: Получение водяных знаков

Следующий фрагмент кода показывает, как получить каждый водяной знак на первой странице PDF-файла с помощью PHP.

```php

    // Открыть документ
    $document = new Document($inputFile);
            
    $formattedText = new FormattedText("Watermark", 
        (new Color())->getBlue()->getRgb(),
        (new facades_FontStyle())->getCourier(), 
        facades_EncodingType::$Identity_h, 
        true, 72.0);

    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    $artifact = new WatermarkArtifact();        
    $artifact->setText($formattedText);        
    $artifact->setArtifactHorizontalAlignment ($horizontalAlignment->getCenter());
    $artifact->setArtifactVerticalAlignment ($verticalAlignment->getCenter());
    $artifact->setRotation(45);
    $artifact->setOpacity(0.5);
    $artifact->setBackground(true);
    $document->getPages()->get_Item(1)->getArtifacts()->add($artifact);
    
    // Сохранить выходной документ
    $document->save($outputFile);
    $document->close();
```