---
title: Aplatir l'Annotation d'un Fichier PDF vers XFDF (facades)
type: docs
weight: 40
url: fr/java/flatten-annotation/
description: Cette section explique comment exporter des annotations d'un fichier PDF vers XFDF avec Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Le processus d'aplatissement signifie qu'une annotation est retirée d'un document, mais que sa représentation visuelle est conservée. Une annotation aplatie est toujours visible mais n'est plus modifiable par vos utilisateurs ou par votre application. Cela peut être utilisé, par exemple, pour appliquer de manière permanente des annotations à votre document ou pour rendre les annotations visibles aux spectateurs qui autrement ne peuvent pas afficher les annotations. Si ce n'est pas spécifié, un export conservera toutes les annotations telles qu'elles sont.

Lorsque cette option est sélectionnée, vos annotations seront incluses dans votre PDF exporté en tant qu'annotations standard PDF.

Vérifiez comment la méthode [flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--) est utilisée dans l'extrait de code suivant.

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        FlattenSettings flattenSettings = new FlattenSettings();
        flattenSettings.setApplyRedactions(true); // Appliquer les rédactions
        flattenSettings.setCallEvents(false); // Ne pas appeler les événements
        flattenSettings.setHideButtons(true); // Masquer les boutons
        flattenSettings.setUpdateAppearances(true); // Mettre à jour les apparences
        annotationEditor.flatteningAnnotations(flattenSettings);
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf");
    }
```