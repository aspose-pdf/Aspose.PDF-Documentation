---
title: Adicionar Texto ao Arquivo PDF
linktitle: Adicionar Texto ao Arquivo PDF
type: docs
weight: 10
url: /php-java/add-text-to-pdf-file/
description: Este artigo descreve vários aspectos do trabalho com texto no Aspose.PDF. Aprenda como adicionar texto ao PDF, adicionar fragmentos HTML ou usar fontes OTF personalizadas.
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para adicionar texto a um arquivo PDF existente:

1. Abra o PDF de entrada usando o objeto Documento.
2. Obtenha a página específica à qual você deseja adicionar o texto.
3. Crie um fragmento de texto com o conteúdo "Aspose.PDF".
4. Defina a posição do fragmento de texto na página.
5. Defina as propriedades de texto do fragmento de texto.
6. Crie um objeto TextBuilder para a página.
7. Anexe o fragmento de texto à página do PDF.
8. Salve o documento PDF resultante no arquivo de saída.

## Adicionando Texto

O trecho de código a seguir mostra como adicionar texto em um arquivo PDF existente.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // obter página específica
    $page = $document->getPages()->add();
    
    // criar fragmento de texto
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // definir propriedades de texto
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // criar objeto TextBuilder
    $textBuilder = new TextBuilder($page);
    // anexar o fragmento de texto à página do PDF
    $textBuilder->appendText($textFragment);

    // Salvar documento PDF resultante.    
    $document->save($outputFile);
    $document->close();
```