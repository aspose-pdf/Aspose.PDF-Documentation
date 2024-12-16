---
title: Ajout d'actions Javascript PDF 
type: docs
weight: 10
url: /fr/net/adding-javascript-actions/
description: Cette section explique comment ajouter des actions Javascript à un fichier PDF existant avec Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) présente dans le package Aspose.Pdf.Facades offre la flexibilité d'ajouter des actions Javascript à un fichier PDF. Vous pouvez créer un lien avec les actions en série correspondant à l'exécution d'un élément de menu dans le visualiseur PDF. Cette classe offre également la possibilité de créer des actions supplémentaires pour les événements du document.

Tout d'abord, un objet est dessiné dans le [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), dans notre exemple un [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle). Et définissez l'action [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) sur le Rectangle. Après, vous pouvez enregistrer votre document.

```csharp
  public static void AddingJavascriptActions()
        {
            PdfContentEditor editor = new PdfContentEditor();
            editor.BindPdf(_dataDir + "sample.pdf");
            // créer un lien Javascript
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
            String code = "app.alert('Bienvenue chez Aspose!');";
            editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
            // enregistrer le fichier de sortie
            editor.Save(_dataDir + "JavaScriptAdded_output.pdf");
        }
```