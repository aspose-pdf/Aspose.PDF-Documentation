---
title: Extraia conteúdo marcado de PDFs em Java
linktitle: Extrair conteúdo marcado
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Aprenda como inspecionar conteúdo PDF marcado em Java com Aspose.PDF, incluindo acesso a conteúdo marcado, acesso à estrutura raiz e elementos de estrutura filho.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Use essas APIs quando precisar inspecionar a árvore da estrutura lógica de um PDF marcado e examinar ou atualizar metadados de elementos de estrutura.

## Obtenha metadados de conteúdo marcado

Use este exemplo quando precisar de acesso ao contêiner de conteúdo marcado e quiser definir metadados básicos do documento, como título e idioma.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtenha o objeto [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) do documento.
1. Defina os metadados do conteúdo marcado e salve o arquivo de saída.

```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## Obtenha a estrutura raiz de um PDF marcado

Este exemplo mostra como inspecionar os objetos raiz que representam a árvore de estrutura de um PDF marcado.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e obtenha seu conteúdo marcado.
1. Defina os metadados do documento necessários.
1. Leia e imprima a raiz da árvore de estrutura e o elemento raiz lógico e salve o arquivo.

```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## Acessar e atualizar elementos da estrutura filho

Use este exemplo quando precisar iterar através de elementos filhos na árvore de estrutura, inspecionar suas propriedades e atualizar os metadados selecionados.

1. Abra o PDF com a fonte marcada [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Leia os elementos filhos da raiz da árvore de estrutura e imprima as propriedades disponíveis.
1. Acesse os elementos filho do primeiro filho raiz, atualize seus metadados e salve o documento.

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```
