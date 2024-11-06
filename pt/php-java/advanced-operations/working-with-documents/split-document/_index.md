---
title: Dividir PDF programaticamente
linktitle: Dividir arquivos PDF
type: docs
weight: 60
url: pt/php-java/split-document/
description: Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais em suas aplicações PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Você pode dividir arquivos PDF usando Aspose.PDF e obter os resultados online neste link: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Este tópico mostra como dividir páginas de PDF com Aspose.PDF para PHP via Java em arquivos PDF individuais em suas aplicações PHP. Para dividir páginas de PDF em arquivos PDF de página única usando PHP, os seguintes passos podem ser seguidos:

1. Percorra as páginas do documento PDF através da coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Para cada iteração, crie um novo objeto Documento e adicione o objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) individual ao documento vazio.
1. Salve o novo PDF usando o método Save.

O seguinte trecho de código PHP mostra como dividir páginas de um PDF em arquivos PDF individuais.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Loop através de todas as páginas
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```