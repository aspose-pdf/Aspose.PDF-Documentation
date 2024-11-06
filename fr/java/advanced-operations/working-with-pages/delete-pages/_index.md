---
title: Supprimer des pages PDF par programme
linktitle: Supprimer des pages PDF
type: docs
weight: 40
url: fr/java/delete-pages/
description: Vous pouvez supprimer des pages de votre fichier PDF en utilisant la bibliothèque Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Vous pouvez supprimer des pages d'un fichier PDF en utilisant Aspose.PDF pour Java. Pour supprimer une page particulière de la [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection), appelez simplement la méthode delete() et spécifiez l'index de la page particulière que vous souhaitez supprimer. Ensuite, appelez la méthode save pour enregistrer le fichier PDF mis à jour.

## Supprimer une page d'un fichier PDF

1. Appelez la méthode Delete et spécifiez l'index de la page
1. Appelez la méthode Save pour enregistrer le fichier PDF mis à jour
Le code suivant montre comment supprimer une page particulière d'un fichier PDF en utilisant Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // Ouvrir le document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Supprimer une page particulière
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // Enregistrer le PDF mis à jour
    pdfDocument.save(_dataDir);    

  }
```