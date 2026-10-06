---
title: Adicionar Selos de Texto ao PDF em Java
linktitle: Selos de texto em Arquivo PDF
type: docs
weight: 20
url: /pt/java/text-stamps-in-the-pdf-file/
description: Saiba como adicionar selos de texto a documentos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar selos de texto a arquivos PDF com Java
Abstract: Este artigo explica como adicionar selos de texto a arquivos PDF usando Aspose.PDF for Java. Ele aborda a criação de um selo de texto de fundo, seu posicionamento, rotação e a personalização da Font, tamanho, estilo e cor.
---
Use selos de texto quando precisar adicionar rótulos visíveis ou marcas d'água às páginas PDF.

## Adicionar um TextStamp

Use este exemplo quando uma página deve exibir um TextStamp girado com estilo personalizado.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar um [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) e configure sua posição e aparência do texto.
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
