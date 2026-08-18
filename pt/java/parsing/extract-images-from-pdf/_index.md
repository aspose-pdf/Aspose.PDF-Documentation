---
title: Extraia imagens de PDF usando Java
linktitle: Extraia imagens de PDF
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: Aprenda como extrair imagens incorporadas de arquivos PDF com Aspose.PDF para Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair imagens de PDF via Java
Abstract: Este artigo explica como extrair imagens incorporadas de um documento PDF com Aspose.PDF para Java. Mostra como abrir o PDF de origem, acessar uma imagem da coleção de recursos da página e salvar o XImage extraído em um arquivo externo.
---
Extraia imagens de páginas PDF quando precisar reutilizar gráficos incorporados, inspecionar ativos de documentos ou exportar imagens para processamento posterior.

1. Abra o PDF de origem em um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância e abra um fluxo de saída para o arquivo de imagem extraído.
1. Obtenha o alvo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) do documento e acesse seu `Resources.Images` coleção.
1. Recuperar o necessário [Imagem X](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) objeto dessa coleção de imagens por índice.
1. Chamar `image.save(outputImage)` para gravar os bytes da imagem extraída no fluxo de destino.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
