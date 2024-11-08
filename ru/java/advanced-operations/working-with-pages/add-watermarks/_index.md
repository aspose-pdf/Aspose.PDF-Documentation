---
title: Добавление водяного знака в PDF
linktitle: Добавление водяного знака
type: docs
weight: 90
url: /ru/java/add-watermarks/
description: Эта статья объясняет функции работы с артефактами и получения водяных знаков в PDF программно с использованием Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** позволяет добавлять водяные знаки в ваш PDF-документ с использованием артефактов. Пожалуйста, ознакомьтесь с этой статьей, чтобы решить вашу задачу.

Водяной знак, созданный с помощью Adobe Acrobat, называется артефактом (как описано в разделе 14.8.2.2 Реальное содержание и артефакты спецификации PDF). Для работы с артефактами Aspose.PDF имеет два класса: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) и [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

Для получения всех артефактов на конкретной странице класс [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) имеет свойство Artifacts.
 This topic explains how to work with artifact in PDF files.

## Работа с артефактами

Класс [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) содержит следующие свойства:

**Artifact.Type** – получает тип артефакта (поддерживает значения перечисления Artifact.ArtifactType, где значения включают Background, Layout, Page, Pagination и Undefined).
**Artifact.Subtype** – получает подтип артефакта (поддерживает значения перечисления Artifact.ArtifactSubtype, где значения включают Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Обратите внимание, что водяные знаки, созданные с помощью Adobe Acrobat, имеют тип Pagination и подтип Watermark.

{{% /alert %}}

**Artifact.Contents** – получает коллекцию внутренних операторов артефакта. Поддерживаемый тип – System.Collections.ICollection.
**Artifact.Form** – получает XForm артефакта (если используется XForm). Артефакты водяных знаков, заголовка и нижнего колонтитула содержат XForm, который показывает все содержимое артефакта.

**Artifact.Image** – получает изображение артефакта (если изображение присутствует, иначе null).**Artifact.Text** – Получает текст артефакта.  
**Artifact.Rectangle** – Получает позицию артефакта на странице.  
**Artifact.Rotation** – Получает угол поворота артефакта (в градусах, положительное значение указывает на поворот против часовой стрелки).  
**Artifact.Opacity** – Получает непрозрачность артефакта. Возможные значения находятся в диапазоне 0…1, где 1 — полностью непрозрачный.

## Примеры программирования: Получение водяных знаков

Следующий фрагмент кода показывает, как получить каждый водяной знак на первой странице PDF файла с помощью Java.

```java
 package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.EncodingType;
import com.aspose.pdf.facades.FontStyle;
import com.aspose.pdf.facades.FormattedText;

public class ExampleWatermark {
    // Путь к директории с документами.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Split() {

        // Открыть документ
        Document doc = new Document(_dataDir + "text.pdf");      
        FormattedText formattedText = new FormattedText("Watermark", java.awt.Color.BLUE,FontStyle.Courier, EncodingType.Identity_h, true, 72.0F);
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(formattedText);        
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }

}  
```