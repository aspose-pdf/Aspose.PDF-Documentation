---
title: Flatten Annotation from PDF to XFDF 
type: docs
weight: 40
url: es/net/flatten-annotation/
description: Esta sección explica cómo exportar anotaciones de un archivo PDF a XFDF con Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

El proceso de aplanamiento significa que cuando una anotación se elimina de un documento, su representación visual se mantiene intacta. Una anotación aplanada sigue siendo visible pero ya no es editable por sus usuarios o por su aplicación. Esto se puede usar, por ejemplo, para aplicar permanentemente anotaciones a su documento o para hacer visibles las anotaciones a los espectadores que de otro modo no podrían mostrar anotaciones. Si no se especifica, una exportación mantendrá todas las anotaciones tal como están.

Cuando se selecciona esta opción, sus anotaciones se incluirán en su PDF exportado como anotaciones estándar de PDF.

Consulte cómo se utiliza el método [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) en el siguiente fragmento de código.

```csharp
public static void Flattening()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "muestra_gatos_perros.pdf");
            FlattenSettings flattenSettings = new FlattenSettings
            {
                ApplyRedactions = true,
                CallEvents = false,
                HideButtons = true,
                UpdateAppearances = true
            };
            annotationEditor.FlatteningAnnotations(flattenSettings);
            annotationEditor.Save(_dataDir + "AplanarAnotación.pdf");
        }
```