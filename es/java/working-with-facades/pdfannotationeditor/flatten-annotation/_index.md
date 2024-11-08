---
title: Flatten Annotation from PDF File to XFDF (facades)
type: docs
weight: 40
url: /es/java/flatten-annotation/
description: Esta sección explica cómo exportar anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

El proceso de aplanamiento significa que cuando una anotación se elimina de un documento, su representación visual se mantiene intacta. Una anotación aplanada sigue siendo visible pero ya no es editable por sus usuarios ni por su aplicación. Esto se puede usar, por ejemplo, para aplicar anotaciones permanentemente a su documento o para hacer que las anotaciones sean visibles para los espectadores que de otra manera no podrían mostrar anotaciones. Si no se especifica, una exportación mantendrá todas las anotaciones tal como están.

Cuando se selecciona esta opción, sus anotaciones se incluirán en su PDF exportado como anotaciones estándar de PDF.

Vea cómo se utiliza el método [flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--) en el siguiente fragmento de código.

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        FlattenSettings flattenSettings = new FlattenSettings();
        flattenSettings.setApplyRedactions(true); // Aplicar redacciones
        flattenSettings.setCallEvents(false); // No llamar eventos
        flattenSettings.setHideButtons(true); // Ocultar botones
        flattenSettings.setUpdateAppearances(true); // Actualizar apariencias
        annotationEditor.flatteningAnnotations(flattenSettings);
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf");
    }
```