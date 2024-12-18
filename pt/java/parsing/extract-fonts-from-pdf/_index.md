---
title: Extrair fontes do PDF
linktitle: Extrair fontes
type: docs
weight: 30
url: /pt/java/extract-fonts-from-pdf/
description: Como extrair fonte de PDF usando Aspose.PDF para Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Caso você queira obter todas as fontes de um documento PDF, você pode usar o método `Document.IDocumentFontUtilities.getAllFonts()` fornecido na classe Document.
Por favor, verifique o seguinte trecho de código para obter todas as fontes de um documento PDF existente:

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // O caminho para o diretório de documentos.
    String filePath = "<... insira o nome do arquivo ...>";
    
    // Carregar documento PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```