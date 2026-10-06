---
title: Extrair fontes de PDF via Java
linktitle: Extrair fontes de PDF
type: docs
weight: 30
url: /pt/java/extract-fonts-from-pdf/
description: Use o Aspose.PDF for Java para inspecionar e extrair as fontes usadas em um documento PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair fontes de PDF usando Java
Abstract: Este artigo explica como inspecionar as fontes usadas em um documento PDF com Aspose.PDF for Java. Ele mostra como abrir um PDF, chamar `getFontUtilities().getAllFonts()`, e percorrer os objetos de fonte resultantes para ler seus nomes.
---
Use a extração de fontes quando precisar auditar a tipografia do documento, inspecionar recursos incorporados ou verificar o uso de fontes antes de fluxos de trabalho de conversão ou arquivamento.

1. Abra o PDF de origem em um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instância.
1. Chamar `document.getFontUtilities().getAllFonts()` coletar cada [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) recurso referenciado pelo documento.
1. Iterar pelos extraídos [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) objetos e ler cada nome de fonte dos metadados da fonte.
1. Imprimir os nomes das fontes para que a tipografia do documento possa ser auditada ou exportada.

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
