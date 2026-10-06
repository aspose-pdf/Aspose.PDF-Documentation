---
title: Obter e definir propriedades de página PDF em Java
linktitle: Obter e definir propriedades de página
type: docs
weight: 90
url: /pt/java/get-and-set-page-properties/
description: Saiba como inspecionar propriedades de página PDF, como contagem, caixas, rotação e informações de cor, em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspecione a contagem de páginas, caixas e tipo de cor em arquivos PDF com Java
Abstract: Este artigo explica como inspecionar as propriedades da página usando Aspose.PDF for Java. Ele abrange a leitura da contagem de páginas, a geração de parágrafos e a verificação da contagem resultante antes de salvar, a impressão de todos os principais valores das caixas de página e a identificação do tipo de cor de cada página.
---
Aspose.PDF for Java pode inspecionar a contagem de páginas, caixas de página, rotação e tipo de cor da página.

## Obter a contagem de páginas

Use este exemplo quando precisar ler o número total de páginas em um PDF.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Leia o tamanho da coleção de páginas.
1. Exiba a contagem total de páginas.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## Obter a contagem de páginas antes de salvar

Use este exemplo quando precisar saber quantas páginas o conteúdo gerado produzirá antes de escrever o arquivo.

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione conteúdo a uma página.
1. Processar os parágrafos para forçar o cálculo de layout.
1. Leia a contagem de páginas resultante e exibi‑la.

```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## Obter propriedades da caixa da página

Use este exemplo quando precisar inspecionar todas as principais dimensões da caixa e os valores de rotação da página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e acesse a página de destino.
1. Colete os valores da caixa da página em um mapa.
1. Exiba as dimensões e as informações de rotação da página.

```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## Obter o tipo de cor de cada página

Use este exemplo quando precisar identificar se as páginas são preto e branco, escala de cinza ou RGB.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere por todas as páginas e leia cada página [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
1. Converta o valor do enum em texto legível e exiba o resultado.

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```
