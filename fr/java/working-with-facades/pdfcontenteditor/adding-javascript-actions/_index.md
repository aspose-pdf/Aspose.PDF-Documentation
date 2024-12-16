---
title: Ajouter des actions Javascript à un fichier PDF existant
type: docs
weight: 10
url: /fr/java/adding-javascript-actions/
description: Cette section explique comment ajouter des actions Javascript à un fichier PDF existant avec Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) présente dans le package com.aspose.pdf.facades offre la flexibilité d'ajouter des actions Javascript à un fichier PDF. Vous pouvez créer un lien avec les actions en série correspondant à l'exécution d'un élément de menu dans le visualiseur PDF. Cette classe offre également la fonctionnalité de créer des actions supplémentaires pour les événements du document.

Tout d'abord, un objet est dessiné dans le [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), dans notre exemple un [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
 Et définissez l'action [createJavaScriptLink](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-) sur le Rectangle. Après, vous pouvez enregistrer votre document.

```java
 public static void AddingJavascriptActions() {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");
        // créer un lien Javascript
        java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
        String code = "app.alert('Bienvenue chez Aspose!');";
        editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
        // enregistrer le fichier de sortie
        editor.save(_dataDir+"JavaScriptAdded_output.pdf");
    }
```