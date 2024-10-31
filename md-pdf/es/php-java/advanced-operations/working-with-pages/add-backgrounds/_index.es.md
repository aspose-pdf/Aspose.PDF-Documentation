---
title: Añadir fondo a PDF 
linktitle: Añadir fondos
type: docs
weight: 110
url: /php-java/add-backgrounds/
descriptions: Añadir imagen de fondo a tu archivo PDF usando PHP. Usa el objeto BackgroundArtifact.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Las imágenes de fondo se pueden usar para añadir una marca de agua u otro diseño sutil a los documentos. En Aspose.PDF para PHP vía Java, cada documento PDF es una colección de páginas y cada página contiene una colección de artefactos. La clase [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) se puede usar para añadir una imagen de fondo a un objeto de página.

El siguiente fragmento de código muestra cómo añadir una imagen de fondo a las páginas de un PDF usando el objeto BackgroundArtifact con PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Añadir una nueva página al objeto documento
    $page = $document->getPages()->add();

    // Crear objeto BackgroundArtifact    
    $background = new BackgroundArtifact();

    // Especificar la imagen para el objeto backgroundArtifact
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // Añadir backgroundArtifact a la colección de artefactos de la página
    $page->getArtifacts()->add($background);

    // Guardar el archivo PDF actualizado
    $document->save($outputFile);
    $document->close();
```