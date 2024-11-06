---
title: Crear Documento PDF 
linktitle: Crear
type: docs
weight: 10
url: es/java/create-document/
description: Aprende cómo crear un archivo PDF en Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para Java** API permite a los desarrolladores de aplicaciones Java integrar la funcionalidad de procesamiento de documentos PDF en sus aplicaciones. Se puede utilizar para crear y leer archivos PDF sin necesidad de ningún otro software instalado en la máquina subyacente. Aspose.PDF para Java se puede usar en una variedad de tipos de aplicaciones Java, como aplicaciones de Escritorio, JSP y JSF.

## Cómo crear un archivo PDF usando Java

Para crear un archivo PDF usando Java, se pueden seguir los siguientes pasos.

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Agregar una [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) al objeto documento
1. Crear un objeto [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)

1. Agregar [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) a la colección de [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) de la página
1. Guardar el documento PDF resultante

```java
// Inicializar objeto documento
Document document = new Document();
 
//Agregar página
Page page = document.getPages().add();
 
// Agregar texto a la nueva página
page.getParagraphs().add(new TextFragment("¡Hola Mundo!"));
 
// Guardar PDF actualizado
document.save("HelloWorld_out.pdf");
```