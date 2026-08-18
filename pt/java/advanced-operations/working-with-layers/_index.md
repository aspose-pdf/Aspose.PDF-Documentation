---
title: Trabalhe com camadas de PDF usando Java
linktitle: Trabalhe com camadas de PDF
type: docs
weight: 50
url: /java/working-with-pdf-layers/
description: Aprenda como adicionar, bloquear, extrair, nivelar e mesclar camadas de PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerencie camadas de PDF com Java
Abstract: Este artigo explica como trabalhar com camadas PDF, também conhecidas como grupos de conteúdo opcionais, usando Aspose.PDF para Java. Aprenda como adicionar camadas a uma página, bloquear uma camada existente, extrair o conteúdo da camada para arquivos ou fluxos, nivelar o conteúdo em camadas e mesclar camadas em uma.
---
Aspose.PDF para Java expõe camadas de PDF por meio da API `Layer` em cada página. Você pode criar grupos de conteúdo opcionais, modificar seu comportamento e exportar ou nivelar seu conteúdo quando necessário.

## Adicionar camadas a uma página PDF

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie e configure os objetos [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) necessários na página.
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

O exemplo completo cria três camadas separadas com conteúdo de linha vermelha, verde e azul.

## Bloquear uma camada

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse o alvo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e obtenha sua coleção [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Bloqueie a [Camada] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
