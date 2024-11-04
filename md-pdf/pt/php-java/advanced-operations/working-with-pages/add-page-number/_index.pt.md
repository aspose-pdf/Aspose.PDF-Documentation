---
title: Adicionar Número de Página ao PDF
linktitle: Adicionar Número de Página
type: docs
weight: 100
url: /php-java/adicionar-numero-pagina/
description: Aspose.PDF para PHP via Java permite que você adicione um Carimbo de Número de Página ao seu arquivo PDF usando a classe PageNumber Stamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Todos os documentos devem ter números de página. O número da página facilita para o leitor localizar diferentes partes do documento.
**Aspose.PDF para PHP via Java** permite que você adicione números de página com PageNumberStamp.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão do Aspose.PDF e ver os resultados online neste link [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

Você pode usar a classe [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) para adicionar um carimbo de número de página em um documento PDF.
 O [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) class fornece métodos para criar um carimbo baseado em número de página, como formato, margens, alinhamentos, número inicial, etc. Para adicionar um carimbo de número de página, você precisa criar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e um objeto [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) com as propriedades de texto necessárias. Depois disso, você pode chamar o método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) da classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para adicionar o carimbo no arquivo PDF. Você também pode definir os atributos de fonte do carimbo de número de página.

O trecho de código a seguir mostra como adicionar números de página em um arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Criar carimbo de número de página
    $pageNumberStamp = new PageNumberStamp();

    // Se o carimbo é em segundo plano
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Página # de " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // Definir propriedades do texto
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // Adicionar carimbo a uma página específica
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```