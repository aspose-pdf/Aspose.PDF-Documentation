---
title: Añadir marca de agua a PDF 
linktitle: Añadir marca de agua
type: docs
weight: 90
url: es/php-java/add-watermarks/
description: Este artículo explica las características de trabajar con artefactos y obtener marcas de agua en PDFs usando PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para PHP a través de Java** permite añadir marcas de agua a su documento PDF usando Artefactos. Por favor, revise este artículo para resolver su tarea.

Una marca de agua creada con Adobe Acrobat se llama un artefacto (como se describe en 14.8.2.2 Contenido Real y Artefactos de la especificación PDF). Para trabajar con artefactos, Aspose.PDF tiene dos clases: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) y [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/artifactcollection).

Para obtener todos los artefactos en una página particular, la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/Page) tiene la propiedad Artifacts.
 Este tema explica cómo trabajar con artefactos en archivos PDF.

## Trabajando con Artefactos

La clase [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) contiene las siguientes propiedades:

**Artifact.Type** – obtiene el tipo de artefacto (admite valores de la enumeración Artifact.ArtifactType donde los valores incluyen Background, Layout, Page, Pagination y Undefined).
**Artifact.Subtype** – obtiene el subtipo de artefacto (admite los valores de la enumeración Artifact.ArtifactSubtype donde los valores incluyen Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Tenga en cuenta que las marcas de agua creadas con Adobe Acrobat tienen el tipo Pagination y el subtipo Watermark.

{{% /alert %}}

**Artifact.Contents** – Obtiene una colección de operadores internos del artefacto. Su tipo admitido es System.Collections.ICollection.
**Artifact.Form** – Obtiene el XForm de un artefacto (si se utiliza XForm). Los artefactos de marcas de agua, encabezados y pies de página contienen XForm que muestra todos los contenidos del artefacto.

**Artifact.Image** – Obtiene la imagen de un artefacto (si hay una imagen presente, de lo contrario null).**Artifact.Text** – Obtiene el texto de un artefacto.  
**Artifact.Rectangle** – Obtiene la posición de un artefacto en la página.  
**Artifact.Rotation** – Obtiene la rotación de un artefacto (en grados, un valor positivo indica una rotación en sentido contrario a las agujas del reloj).  
**Artifact.Opacity** – Obtiene la opacidad de un artefacto. Los valores posibles están en el rango de 0…1, donde 1 es completamente opaco.

## Ejemplos de Programación: Obtener Marcas de Agua

El siguiente fragmento de código muestra cómo obtener cada marca de agua en la primera página de un archivo PDF con PHP.

```php

    // Abrir documento
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
    
    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```