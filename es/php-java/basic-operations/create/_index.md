---
title: Crear Documento PDF
linktitle: Crear
type: docs
weight: 10
url: /es/php-java/create-document/
description: Aprende cómo crear un archivo PDF en Aspose.PDF para PHP a través de Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para PHP a través de Java** API permite a los desarrolladores de aplicaciones integrar la funcionalidad de procesamiento de documentos PDF en sus aplicaciones. Se puede utilizar para crear y leer archivos PDF sin la necesidad de ningún otro software instalado en la máquina subyacente. Aspose.PDF para PHP a través de Java se puede utilizar en una variedad de tipos de aplicaciones como aplicaciones de Escritorio, JSP y JSF.

## Cómo crear un archivo PDF usando PHP a través de Java

Para crear un archivo PDF usando PHP a través de Java, se pueden seguir los siguientes pasos.

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Agregar una [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) al objeto del documento

1. Crear un objeto [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)
1. Agregar [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) a la colección de [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) de la página
1. Guardar el documento PDF resultante

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("¡Hola Mundo!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```