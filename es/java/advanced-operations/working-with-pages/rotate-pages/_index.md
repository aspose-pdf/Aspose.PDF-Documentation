---
title: Rotar páginas PDF en Java
linktitle: Rotar páginas PDF
type: docs
weight: 110
url: /java/rotate-pages/
description: Aprenda a rotar páginas PDF y cambiar la orientación de la página en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotar páginas PDF con Java
Abstract: Este artículo explica cómo rotar páginas PDF usando Aspose.PDF para Java. El ejemplo recorre en iteración todas las páginas de un documento, aplica una rotación de 90 grados y guarda el PDF actualizado.
---
Utilice la API de rotación de páginas cuando necesite cambiar la orientación en una o más páginas.


## 
Girar todas las páginas 90 grados.



Utilice este ejemplo cuando cada página del documento deba girarse en el sentido de las agujas del reloj.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Itere a través de todos los objetos [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y establezca el valor de rotación.
1. Guarde el PDF actualizado.

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```
