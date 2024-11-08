---
title: Aplatir l'Annotation du PDF vers XFDF 
type: docs
weight: 40
url: /fr/net/flatten-annotation/
description: Cette section explique comment exporter des annotations d'un fichier PDF vers XFDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Le processus d'aplatissement signifie qu'une annotation est supprimée d'un document, mais sa représentation visuelle est conservée. Une annotation aplatie est toujours visible mais n'est plus éditable par vos utilisateurs ou par votre application. Cela peut être utilisé, par exemple, pour appliquer de manière permanente des annotations à votre document ou pour rendre les annotations visibles aux spectateurs qui autrement ne peuvent pas afficher les annotations. Si non spécifié, une exportation conservera toutes les annotations telles qu'elles sont.

Lorsque cette option est sélectionnée, vos annotations seront incluses dans votre PDF exporté en tant qu'annotations standard PDF.

Consultez comment la méthode [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) est utilisée dans l'extrait de code suivant.

```csharp
public static void Flattening()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            FlattenSettings flattenSettings = new FlattenSettings
            {
                ApplyRedactions = true,
                CallEvents = false,
                HideButtons = true,
                UpdateAppearances = true
            };
            annotationEditor.FlatteningAnnotations(flattenSettings);
            annotationEditor.Save(_dataDir + "FlattenAnnotation.pdf");
        }
```