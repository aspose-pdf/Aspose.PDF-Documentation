---
title: Alterar o tamanho da página PDF em Java
linktitle: Alterando o tamanho da página
type: docs
weight: 40
url: /java/change-page-size/
description: Aprenda como ler e alterar as dimensões da página PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Leia e atualize dimensões e caixas de páginas com Java
Abstract: Este artigo demonstra como ler e modificar dimensões de páginas PDF usando Aspose.PDF para Java. Abrange a obtenção do tamanho da página, a medição do tamanho da página com a rotação aplicada e a atualização da primeira página para um novo tamanho enquanto imprime as dimensões da caixa antes e depois da alteração.
---
Aspose.PDF para Java pode relatar dimensões de páginas e atualizá-las.

## Alterar o tamanho da página

Use este exemplo quando precisar redimensionar uma página existente e inspecionar as caixas da página antes e depois da alteração.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtenha o alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e imprima seus valores de caixa atuais.
1. Defina o novo tamanho da página e salve o documento.

```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## Obtenha o tamanho da página

Use este exemplo quando precisar ler as dimensões visíveis de uma página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtenha o retângulo da página com a manipulação de rotação habilitada.
1. Produza a largura e a altura da página.

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## Obtenha o tamanho da página com rotação aplicada

Use este exemplo quando precisar comparar as dimensões da página antes e depois de contabilizar a rotação.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Gire a [Página] de destino (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Leia o retângulo da página com e sem manipulação de rotação e produza ambos os valores.

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```
