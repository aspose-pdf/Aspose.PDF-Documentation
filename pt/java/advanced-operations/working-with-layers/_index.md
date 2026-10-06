---
title: Trabalhar com camadas PDF usando Java
linktitle: Trabalhar com camadas PDF
type: docs
weight: 50
url: /pt/java/working-with-pdf-layers/
description: Aprenda a adicionar, bloquear, extrair, achatar e mesclar camadas PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerenciar camadas PDF com Java
Abstract: Este artigo explica como trabalhar com camadas PDF, também conhecidas como Grupos de Conteúdo Opcional, usando Aspose.PDF for Java. Aprenda a adicionar camadas a uma página, bloquear uma camada existente, extrair o conteúdo da camada para arquivos ou streams, achatar o conteúdo em camadas e mesclar camadas em uma única.
---
Aspose.PDF for Java expõe camadas de PDF através da API `Layer` em cada página. Você pode criar grupos de conteúdo opcional, modificar seu comportamento e exportar ou achatar seu conteúdo quando necessário.

## Adicionar camadas a uma página PDF

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie e configure o necessário objetos [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) na página.
1. Salve o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLayers(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Layer layer = new Layer("oc1", "Red Line");
        layer.getContents().add(new SetRGBColorStroke(1, 0, 0));
        layer.getContents().add(new MoveTo(500, 700));
        layer.getContents().add(new LineTo(400, 700));
        layer.getContents().add(new Stroke());
        page.getLayers().add(layer);

        document.save(outputFile.toString());
    }
}
```

O exemplo completo cria três camadas separadas com conteúdo de linhas vermelha, verde e azul.

## Bloquear uma camada

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse a página de destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e obtenha seu [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) coleção.
1. Bloqueie o alvo [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Salve o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void lockLayer(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        if (!page.getLayers().isEmpty()) {
            Layer layer = page.getLayers().getFirst();
            layer.lock();
            document.save(outputFile.toString());
        }
    }
}
```
