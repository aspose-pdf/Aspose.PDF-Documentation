title: Trabalhando com Cabeçalhos em PDF
type: docs
weight: 70
url: /pt/php-java/working-with-headings/
lastmod: "2024-06-05"
description: Crie numeração no cabeçalho do seu documento PDF usando PHP. Aspose.PDF para PHP via Java oferece diferentes tipos de estilos de numeração.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aplicar Estilo de Numeração no Cabeçalho

Os cabeçalhos são partes importantes de qualquer documento. Os escritores sempre tentam tornar os cabeçalhos mais proeminentes e significativos para seus leitores. Se houver mais de um cabeçalho em um documento, um escritor tem várias opções para organizar esses cabeçalhos. Uma das abordagens mais comuns para organizar cabeçalhos é escrever cabeçalhos no Estilo de Numeração.

Aspose.PDF para PHP via Java oferece muitos estilos de numeração predefinidos. Esses estilos de numeração predefinidos são armazenados em uma enumeração, NumberingStyle. Os valores predefinidos da enumeração NumberingStyle e suas descrições são dados abaixo:

|**Tipos de Cabeçalho**|**Descrição**|
| :- | :- |
`

|NumeralsArabic|Tipo árabe, por exemplo, 1,1.1,...|
|NumeralsRomanUppercase|Tipo romano maiúsculo, por exemplo, I,I.II, ...|
|NumeralsRomanLowercase|Tipo romano minúsculo, por exemplo, i,i.ii, ...|
|LettersUppercase|Tipo maiúsculo em inglês, por exemplo, A,A.B, ...|
|LettersLowercase|Tipo minúsculo em inglês, por exemplo, a,a.b, ...|
A propriedade [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) da classe [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) é usada para definir os estilos de numeração dos cabeçalhos.

O código-fonte, para obter a saída mostrada na figura acima, é fornecido abaixo no exemplo.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $document->getPageInfo()->setWidth(612.0);
    $document->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $page = $document->getPages()->add();
    $page->getPageInfo()->setWidth(612.0);
    $page->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $floatBox = new FloatingBox();
    $floatBox->setMargin($page->getPageInfo()->getMargin());

    $page->getParagraphs()->add($floatBox);

    $heading = new Heading(1);
    $heading->setInList(true);
    $heading->setStartNumber(1);
    $heading->setText("Lista 1");
    $heading->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading);
    $heading2 = new Heading(1);
    $heading2->setInList(true);
    $heading2->setStartNumber(13);
    $heading2->setText("Lista 2");
    $heading2->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading2->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading2);

    $heading3 = new Heading(2);
    $heading3->setInList(true);
    $heading3->setStartNumber(1);
    $heading3->setText("o valor, na data efetiva do plano, da propriedade a ser distribuída sob o plano em razão de cada permitido");
    $heading3->setStyle (NumberingStyle::$LettersLowercase);
    $heading3->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading3);
    
    $document->save($outputFile);
    $document->close();
```