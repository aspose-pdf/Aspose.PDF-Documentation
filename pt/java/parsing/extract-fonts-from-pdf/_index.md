---
title: Extraia fontes de PDF via Java
linktitle: Extraia fontes de PDF
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: Use Aspose.PDF for Java para inspecionar e extrair as fontes usadas em um documento PDF.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair fontes de PDF usando Java
Abstract: Este artigo explica como inspecionar as fontes usadas em um documento PDF com Aspose.PDF para Java. Ele mostra como abrir um PDF, chamar `getFontUtilities().getAllFonts()` e percorrer os objetos de fonte resultantes para ler seus nomes.
---
Use a extração de fontes quando precisar auditar a tipografia de documentos, inspecionar recursos incorporados ou verificar o uso de fontes antes da conversão ou dos fluxos de trabalho de arquivamento.

1. Abra o PDF de origem em uma instância [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame `document.getFontUtilities().getAllFonts()` para coletar todos os recursos [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) referenciados pelo documento.
1. Itere através dos objetos [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) extraídos e leia cada nome de fonte nos metadados da fonte.
1. Imprima os nomes das fontes para que a tipografia do documento possa ser auditada ou exportada.

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
