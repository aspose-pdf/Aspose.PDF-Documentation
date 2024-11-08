---
title: Extrair Parágrafo de PDF
linktitle: Extrair Parágrafo
type: docs
weight: 20
url: /pt/php-java/extract-paragraph-from-pdf/
description: Este artigo descreve como usar o ParagraphAbsorber - uma ferramenta especial no Aspose.PDF para extrair texto de documentos PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair Texto de Documento PDF em Forma de Parágrafos

Podemos obter texto de um documento PDF pesquisando um texto específico (usando "texto simples" ou "expressões regulares") de uma única página ou de todo o documento, ou podemos obter o texto completo de uma única página, intervalo de páginas ou documento completo. No entanto, em alguns casos, você precisa extrair parágrafos de um documento PDF ou texto na forma de Parágrafos. Implementamos a funcionalidade para pesquisar seções e parágrafos no texto das páginas do documento PDF. Introduzimos a Classe ParagraphAbsorber (como TextFragmentAbsorber e TextAbsorber), que pode ser usada para extrair parágrafos de documentos PDF.

### Iterando pela coleção de parágrafos e obtendo o texto deles

```php

// Abrir um arquivo PDF existente
$document = new Document($inputFile);
// Instanciar ParagraphAbsorber
$absorber = new ParagraphAbsorber();
$absorber->visit($document);
$responseData = "";

foreach ($absorber->getPageMarkups() as $markup) {
    $i = 1;

    foreach ($markup->getSections() as $section) {
        $j = 1;

        foreach ($section->getParagraphs() as $paragraph) {
            $paragraphText = "\r\n";

            foreach ($paragraph->getLines() as $line) {
                foreach ($line as $fragment) {
                    $paragraphText = $paragraphText . $fragment->getText();
                }
                $paragraphText = $paragraphText . "\r\n";
            }
            $paragraphText = $paragraphText . "\r\n";

            $responseData = $responseData . "Parágrafo " . $j++ . " da seção " . $i++ . " na página" . ":" . markup->getNumber();
            $responseData = $responseData . $paragraphText;
            $j++;
        }
        $i++;
    }
}

// Salvar o texto extraído no arquivo de saída.
file_put_contents($outputFile, $responseData);
```