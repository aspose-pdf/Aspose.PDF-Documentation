---
title: Adicionar Números de página ao PDF em Java
linktitle: Adicionar número de página
type: docs
weight: 30
url: /pt/java/add-page-number/
description: Aprenda como adicionar carimbos de número de página a documentos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar carimbos de número de página a arquivos PDF com Java
Abstract: Este artigo explica como adicionar carimbos de número de página usando Aspose.PDF for Java. Ele aborda a numeração padrão de páginas com estilo de fonte personalizado e a numeração em algarismos romanos com um número inicial configurável.
---
## Adicionar um carimbo de número de página

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o objeto [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. Configure a colocação do selo necessária e as opções de numeração.
1. Defina as opções de formatação de texto necessárias, incluindo [FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) e [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Adicione o configurado [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) para o destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Salve o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```
