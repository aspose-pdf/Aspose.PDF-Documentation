---
title: Extrair Conteúdo Marcado de PDFs em Java
linktitle: Extrair Conteúdo Marcado
type: docs
weight: 20
url: /pt/java/extract-tagged-content-from-tagged-pdfs/
description: Aprenda como inspecionar o conteúdo de Tagged PDF em Java com Aspose.PDF, incluindo acesso ao conteúdo marcado, acesso à estrutura raiz e elementos de estrutura filho.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Use estas APIs quando precisar inspecionar a árvore de estrutura lógica de um Tagged PDF e examinar ou atualizar os metadados dos elementos de estrutura.

## Obter metadados de conteúdo marcado

Use este exemplo quando precisar acessar o contêiner de conteúdo marcado e desejar definir metadados básicos do documento, como título e idioma.

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obter o [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) objeto do documento.
1. Defina os metadados de conteúdo marcado e salve o arquivo de saída.

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

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e obter seu conteúdo marcado.
1. Defina os metadados do documento necessários.
1. Leia e imprima a raiz da árvore de estrutura e o elemento raiz lógico, então salve o arquivo.

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

## Acesse e atualize os elementos de estrutura filho

Use este exemplo quando precisar iterar pelos elementos filhos na árvore de estrutura, inspecionar suas propriedades e atualizar metadados selecionados.

1. Abra o PDF marcado de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Leia os elementos filhos a partir da raiz da árvore de estrutura e imprima as propriedades disponíveis.
1. Acesse os elementos filhos do primeiro filho da raiz, atualize seus metadados e salve o documento.

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
