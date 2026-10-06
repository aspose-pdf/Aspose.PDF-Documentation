---
title: Extrair imagens de PDF usando Java
linktitle: Extrair imagens de PDF
type: docs
weight: 20
url: /pt/java/extract-images-from-the-pdf-file/
description: Aprenda como extrair imagens incorporadas de arquivos PDF com Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair imagens de PDF via Java
Abstract: Este artigo explica como extrair imagens incorporadas de um documento PDF com Aspose.PDF for Java. Ele mostra como abrir o PDF de origem, acessar uma imagem da coleção de recursos da página e salvar o XImage extraído em um arquivo externo.
---
Extrair imagens das páginas de PDF quando precisar reutilizar gráficos incorporados, inspecionar os recursos do documento ou exportar imagens para processamento subsequente.

1. Abra o PDF de origem em uma instância de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e abra um fluxo de saída para o arquivo de imagem extraído.
1. Obtenha a página de destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) do documento e acesse-o `Resources.Images` coleção.
1. Recupere o necessário objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) dessa coleção de imagens por índice.
1. Chame `image.save(outputImage)` para gravar os bytes da imagem extraídos no fluxo de destino.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
