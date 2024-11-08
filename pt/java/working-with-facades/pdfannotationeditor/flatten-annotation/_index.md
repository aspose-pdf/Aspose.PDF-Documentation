---
title: Flatten Annotation from PDF File to XFDF (facades)
type: docs
weight: 40
url: /pt/java/flatten-annotation/
description: Esta seção explica como exportar anotações de um arquivo PDF para XFDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

O processo de achatamento significa que, quando uma anotação é removida de um documento, sua representação visual é mantida intacta. Uma anotação achatada ainda é visível, mas não é mais editável por seus usuários ou por seu aplicativo. Isso pode ser usado, por exemplo, para aplicar permanentemente anotações ao seu documento ou para tornar anotações visíveis para visualizadores que, de outra forma, não poderiam exibir anotações. Se não especificado, uma exportação manterá todas as anotações como estão.

Quando esta opção é selecionada, suas anotações serão incluídas no seu PDF exportado como anotações padrão do PDF.

Veja como o método [flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--) é usado no próximo trecho de código.

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        FlattenSettings flattenSettings = new FlattenSettings();
        flattenSettings.setApplyRedactions(true); // Definir redações aplicáveis
        flattenSettings.setCallEvents(false); // Definir eventos de chamada
        flattenSettings.setHideButtons(true); // Definir para ocultar botões
        flattenSettings.setUpdateAppearances(true); // Definir para atualizar aparências
        annotationEditor.flatteningAnnotations(flattenSettings);
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf");
    }
```