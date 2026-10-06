---
title: Anotações Interativas usando Java
linktitle: Anotações Interativas
type: docs
weight: 30
url: /pt/java/pdfannotationeditor-class/interactive-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de link em documentos PDF usando Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Trabalhe com anotações PDF interativas em Java
Abstract: Este artigo explica como trabalhar com anotações de link interativas em arquivos PDF usando Java. Ele aborda localizar texto, criar uma anotação de link sobre a área de texto correspondida, ler anotações de link existentes e excluí-las.
---
## Adicionar uma anotação de link

1. Carregue o documento PDF de origem e pesquise a primeira página pelo texto alvo.
2. Use o retângulo de texto correspondente para criar um `LinkAnnotation` e atribua o URI de destino.
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
