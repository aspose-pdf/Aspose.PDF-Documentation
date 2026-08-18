---
title: Adicionar imagem ao PDF usando Java
linktitle: Adicionar imagem
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: Aprenda como adicionar imagens a arquivos PDF existentes em Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Adicione imagens a arquivos PDF existentes com Java
Abstract: Este artigo mostra como adicionar imagens a documentos PDF usando Aspose.PDF para Java. Abrange colocar uma imagem em coordenadas fixas, adicionar imagens por meio de operadores de página de baixo nível, definir texto alternativo para acessibilidade e incorporar dados de imagem com compactação Flate.
---
Aspose.PDF para Java suporta posicionamento de imagem de alto nível e desenho baseado em operador de baixo nível.

## Adicione uma imagem com coordenadas de página

Use este exemplo quando precisar colocar uma imagem em uma posição fixa em uma página PDF.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Chame `page.addImage()` com o caminho da imagem de origem e o retângulo de destino.
1. Salve o arquivo PDF gerado.

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## Adicione uma imagem com operadores de página

Use este exemplo quando precisar de controle de baixo nível sobre o posicionamento e dimensionamento da imagem por meio de operadores de página.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e abra o fluxo de imagem de origem.
1. Adicione a imagem aos recursos da página e calcule o retângulo de destino.
1. Escreva os operadores gráficos necessários e salve o documento.

```java
public static void addImageUsingOperators(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream);
        XImage xImage = resourcesImages.get_Item(resourcesImages.size());

        Rectangle rectangle = new Rectangle(
                0,
                0,
                page.getMediaBox().getWidth(),
                (page.getMediaBox().getWidth() * xImage.getHeight()) / xImage.getWidth(),
                true);

        page.getContents().add(new GSave());

        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLX() + (page.getMediaBox().getHeight() - rectangle.getHeight()) / 2);
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```

## Adicione uma imagem e defina um texto alternativo

Use este exemplo quando a imagem incluir metadados de acessibilidade para leitores de tela.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione a imagem à página.
1. Obtenha o [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) inserido nos recursos da página.
1. Defina o texto alternativo e salve o PDF.

```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        boolean result = xImage.trySetAlternativeText("Alternative text for image", page);
        if (result) {
            System.out.println("Text has been added successfuly");
        }
        document.save(outputFile.toString());
    }
}
```

## Adicione uma imagem com compactação Flate

Use este exemplo quando desejar incorporar dados de imagem usando a compactação Flate.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e abra o fluxo de imagens.
1. Adicione a imagem aos recursos da página com `ImageFilterType.Flate`.
1. Desenhe a imagem através de operadores de página e salve o resultado.

```java
public static void addImageToPdfWithFlateCompression(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream, ImageFilterType.Flate);

        page.getContents().add(new GSave());

        Rectangle rectangle = new Rectangle(0, 0, 600, 600, true);
        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY());

        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```
