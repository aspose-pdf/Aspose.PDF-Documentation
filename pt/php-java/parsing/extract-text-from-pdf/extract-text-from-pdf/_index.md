---
title: Extraindo texto bruto de arquivo PDF 
linktitle: Extrair texto de PDF
type: docs
weight: 10
url: pt/php-java/extract-text-from-all-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF para PHP. De páginas inteiras, de uma parte específica, com base em colunas, etc.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair Texto de Todas as Páginas de um Documento PDF

Extrair texto de um documento PDF é um requisito comum. Neste exemplo, você verá como Aspose.PDF para PHP permite extrair texto de todas as páginas de um documento PDF.
Para extrair texto de todas as páginas do PDF:

1. Crie um objeto da classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Abra o PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e chame o método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) da coleção [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. A classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) absorve o texto do documento e retorna no [método getText()](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--).

O trecho de código a seguir mostra como extrair texto de todas as páginas de um documento PDF.

```php

    // Cria um novo objeto Document a partir do arquivo PDF de entrada.
    $document = new Document($inputFile);

    // Cria um novo objeto TextAbsorber para extrair texto do documento.
    $textAbsorber = new TextAbsorber();

    // Extrai texto do documento.
    $textAbsorber->visit($document);

    // Obtém o conteúdo do texto extraído.
    $content = $textAbsorber->getText();

    // Salva o texto extraído no arquivo de saída.
    file_put_contents($outputFile, $content);
```