---
title: Flatten Annotation from PDF to XFDF 
type: docs
weight: 40
url: /net/flatten-annotation/
description: Esta seção explica como exportar anotações de um arquivo PDF para XFDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

O processo de "flattening" significa que, quando uma anotação é removida de um documento, sua representação visual é mantida intacta. Uma anotação achatada ainda é visível, mas não é mais editável pelos seus usuários ou pelo seu aplicativo. Isso pode ser usado, por exemplo, para aplicar permanentemente anotações ao seu documento ou para tornar anotações visíveis para visualizadores que, de outra forma, não conseguiriam mostrar anotações. Se não especificado, uma exportação manterá todas as anotações como estão.

Quando esta opção é selecionada, suas anotações serão incluídas no seu PDF exportado como anotações padrão do PDF.

Confira como o método [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) é usado no próximo trecho de código.

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