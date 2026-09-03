---
title: Rotar páginas PDF en Java
linktitle: Rotación de páginas PDF
type: docs
weight: 110
url: /es/java/rotate-pages/
description: Aprenda cómo rotar páginas PDF y cambiar la orientación de la página en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotar páginas PDF con Java
Abstract: Este artículo explica cómo rotar páginas PDF utilizando Aspose.PDF for Java. El ejemplo recorre todas las páginas de un documento, aplica una rotación de 90 grados y guarda el PDF actualizado.
---
Utilice la API de rotación de páginas cuando necesite cambiar la orientación en una o más páginas.

## Rotar todas las páginas 90 grados

Utilice este ejemplo cuando cada página del documento deba rotarse en sentido horario.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de todos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objetos y establece el valor de rotación.
1. Guarda el PDF actualizado.

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
