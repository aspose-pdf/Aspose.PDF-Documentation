---
title: Trabalhando com Cabeçalhos em PDF
type: docs
weight: 70
url: /java/working-with-headings/
lastmod: "2021-06-05"
description: Crie numeração em cabeçalhos do seu documento PDF com Java. Aspose.PDF para Java oferece diferentes tipos de estilos de numeração.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aplicar Estilo de Numeração em Cabeçalhos

Os cabeçalhos são partes importantes de qualquer documento. Os escritores sempre tentam tornar os cabeçalhos mais proeminentes e significativos para seus leitores. Se houver mais de um cabeçalho em um documento, um escritor tem várias opções para organizar esses cabeçalhos. Uma das abordagens mais comuns para organizar cabeçalhos é escrevê-los no Estilo de Numeração.

Aspose.PDF para Java oferece muitos estilos de numeração pré-definidos. Esses estilos de numeração pré-definidos são armazenados em uma enumeração, NumberingStyle. Os valores pré-definidos da enumeração NumberingStyle e suas descrições são fornecidos abaixo:

|**Tipos de Cabeçalho**|**Descrição**|
| :- | :- |
|NumeralsArabic|Tipo árabe, por exemplo, 1,1.1,...|

|NumeralsRomanUppercase|Tipo romano maiúsculo, por exemplo, I,I.II, ...|
|NumeralsRomanLowercase|Tipo romano minúsculo, por exemplo, i,i.ii, ...|
|LettersUppercase|Tipo maiúsculo em inglês, por exemplo, A,A.B, ...|
|LettersLowercase|Tipo minúsculo em inglês, por exemplo, a,a.b, ...|
A propriedade [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) da classe [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) é usada para definir os estilos de numeração dos cabeçalhos.

O código-fonte, para obter a saída mostrada na figura acima, é fornecido abaixo no exemplo.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleHeading {
    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ApplyNumberingStyleinHeading() {

        Document pdfDoc = new Document();
        pdfDoc.getPageInfo().setWidth(612.0);
        pdfDoc.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        Page pdfPage = pdfDoc.getPages().add();
        pdfPage.getPageInfo().setWidth(612.0);
        pdfPage.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        FloatingBox floatBox = new FloatingBox();
        floatBox.setMargin(pdfPage.getPageInfo().getMargin());

        pdfPage.getParagraphs().add(floatBox);

        Heading heading = new Heading(1);
        heading.setInList(true);
        heading.setStartNumber(1);
        heading.setText("Lista 1");
        heading.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading.setAutoSequence(true);

        floatBox.getParagraphs().add(heading);
        Heading heading2 = new Heading(1);
        heading2.setInList(true);
        heading2.setStartNumber(13);
        heading2.setText("Lista 2");
        heading2.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading2.setAutoSequence(true);

        floatBox.getParagraphs().add(heading2);

        Heading heading3 = new Heading(2);
        heading3.setInList(true);
        heading3.setStartNumber(1);
        heading3.setText("o valor, na data efetiva do plano, da propriedade a ser distribuída sob o plano em razão de cada permitido");
        heading3.setStyle (NumberingStyle.LettersLowercase);
        heading3.setAutoSequence(true);

        floatBox.getParagraphs().add(heading3);
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDoc.save(_dataDir);

    }

}
```