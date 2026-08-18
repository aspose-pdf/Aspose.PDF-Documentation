---
title: Adicione carimbos de texto a PDF em Java
linktitle: Carimbos de texto em arquivo PDF
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: Aprenda como adicionar carimbos de texto a documentos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione carimbos de texto a arquivos PDF com Java
Abstract: Este artigo explica como adicionar carimbos de texto a arquivos PDF usando Aspose.PDF para Java. Abrange a criação de um carimbo de texto de fundo, seu posicionamento, rotação e personalização de fonte, tamanho, estilo e cor.
---
Use carimbos de texto quando precisar adicionar rótulos visíveis ou marcas d’água às páginas PDF.

## Adicione um carimbo de texto

Use este exemplo quando uma página exibir um carimbo de texto girado com estilo personalizado.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) e configure seu posicionamento e aparência do texto.
1. Adicione o carimbo à página de destino e salve o documento.

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```
