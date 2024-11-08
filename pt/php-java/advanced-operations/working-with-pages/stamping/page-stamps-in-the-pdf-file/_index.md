---
title: Adicionar Carimbo de Página ao PDF
linktitle: Carimbos de Página no Arquivo PDF
type: docs
weight: 30
url: /pt/php-java/page-stamps-in-the-pdf-file/
description: Adicione um carimbo de página a um arquivo PDF usando a classe PdfPageStamp com PHP.
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar Carimbo de Página

Um [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) pode ser usado quando você precisa aplicar um carimbo composto contendo gráficos, texto, tabelas. O exemplo a seguir mostra como usar um carimbo para criar papel timbrado como no uso do Adobe InDesign, Illustrator, Microsoft Word. Assuma que temos algum documento de entrada e queremos aplicar 2 tipos de borda com cores azul e ameixa.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();  
```