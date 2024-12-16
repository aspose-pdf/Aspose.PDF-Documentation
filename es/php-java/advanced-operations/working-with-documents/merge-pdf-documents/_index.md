---
title: Fusionar PDF programáticamente
linktitle: Fusionar archivos PDF
type: docs
weight: 50
url: /es/php-java/merge-pdf-documents/
description: Esta página explica cómo fusionar documentos PDF en un solo archivo PDF usando PHP.
lastmod: "2024-06-05"
---

Ahora, la fusión de archivos pdf es una de las tareas más demandadas.
Este artículo muestra cómo fusionar múltiples archivos PDF en un solo documento PDF utilizando Aspose.PDF para PHP a través de Java. El ejemplo está escrito en Java, pero el API puede ser utilizado en otros lenguajes de programación. Los archivos PDF se fusionan de tal manera que el primero se une al final del otro documento.

## Fusionar archivos PDF usando PHP

{{% alert color="primary" %}}

Puede fusionar archivos PDF usando Aspose.PDF y obtener los resultados en línea en este enlace: [Merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Para concatenar dos archivos PDF:

1. Cree dos objetos [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), cada uno conteniendo uno de los archivos PDF de entrada.

1. Luego llame al método Add de la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) para el objeto Document al que desea agregar el otro archivo PDF.
1. Pase la colección PageCollection del segundo objeto Document al método Add de la primera colección PageCollection.
1. Finalmente, guarde el archivo PDF de salida usando el método Save.

El siguiente fragmento de código muestra cómo concatenar archivos PDF usando PHP.

```php
    // Abrir el primer documento
    $document1 = new Document($inputFile1);
    
    // Abrir el segundo documento
    $document2 = new Document($inputFile2);

    // Agregar páginas del segundo documento al primero
    $document1->getPages()->add($document2->getPages());

    // Guardar el archivo de salida concatenado
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```