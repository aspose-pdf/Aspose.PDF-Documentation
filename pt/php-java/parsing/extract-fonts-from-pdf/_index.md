---
title: Extrair fontes de PDF
linktitle: Extrair fontes
type: docs
weight: 30
url: pt/php-java/extract-fonts-from-pdf/
description: Como extrair fonte de PDF usando Aspose.PDF para PHP
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Caso você queira obter todas as fontes de um documento PDF, você pode usar o método [Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--) fornecido na classe Document. Por favor, veja o seguinte trecho de código para obter todas as fontes de um documento PDF existente:

```php

    // Crie uma nova instância da classe License e defina o arquivo de licença.
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Defina o caminho para o diretório que contém o documento PDF e o diretório de saída para as fontes extraídas.
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // Inicialize a variável de dados de resposta.
    $responseData = "";

    try {
        // Carregue o documento PDF.
        $document = new Document($inputFile);

        // Obtenha todas as fontes usadas no documento PDF.
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // Itere sobre cada fonte e salve-a como um arquivo de fonte TrueType.
        foreach ($fonts as $font) {
            // Defina o caminho do arquivo de saída para o arquivo de fonte.
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // Crie um objeto FileOutputStream para escrever o arquivo de fonte.
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // Salve a fonte como um arquivo de fonte TrueType.
            $font->save($fontStream);

            // Feche o fluxo de fonte.
            $fontStream->close();

            // Anexe o nome da fonte aos dados de resposta.
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // Feche o documento PDF.
        $document->close();
    }
```