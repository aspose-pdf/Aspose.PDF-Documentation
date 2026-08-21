---
title: Liste des timbres
linktitle: Liste des timbres
type: docs
weight: 20
url: /java/list-stamps/
description: Découvrez comment répertorier les tampons en caoutchouc sur une page en Java à l'aide de la façade PdfContentEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Liste des tampons en caoutchouc PDF en Java
Abstract: Cet article montre comment lier un PDF, récupérer les tampons sur une page et inspecter la collection résultante à l'aide de la façade PdfContentEditor dans Aspose.PDF pour Java.
---
## Liste des tampons sur une page


1. 
Liez le PDF source à la façade `PdfContentEditor`.

2. 
Appelez `getStamps(pageNumber)` pour récupérer les tampons sur la page cible.

3. 
Inspectez la collection `StampInfo[]` résultante.

```java
public static void listStamps(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        StampInfo[] stamps = editor.getStamps(1);
        System.out.println("Stamps on page 1: " + stamps.length);
    } finally {
        editor.close();
    }
}
```
