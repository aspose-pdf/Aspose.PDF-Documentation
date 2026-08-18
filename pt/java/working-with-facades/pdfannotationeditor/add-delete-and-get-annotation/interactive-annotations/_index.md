---
title: Anotações interativas usando Java
linktitle: Anotações interativas
type: docs
weight: 30
url: /java/pdfannotationeditor-class/interactive-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de links em documentos PDF usando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Trabalhe com anotações interativas de PDF em Java
Abstract: Este artigo explica como trabalhar com anotações de links interativos em arquivos PDF usando Java. Abrange a localização de texto, a criação de uma anotação de link na área de texto correspondente, a leitura de anotações de link existentes e a exclusão delas.
---
## Adicionar uma anotação de link

1. Carregue o documento PDF de origem e pesquise na primeira página o texto de destino.
2. Use o retângulo de texto correspondente para criar um `LinkAnnotation` e atribuir o URI de destino.
3. Adicione a anotação à página e salve o PDF atualizado.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
