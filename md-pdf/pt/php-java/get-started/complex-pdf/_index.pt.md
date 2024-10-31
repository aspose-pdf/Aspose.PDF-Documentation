---
title: Criando um PDF complexo
linktitle: Criando um PDF complexo
type: docs
weight: 60
url: /php-java/complex-pdf-example/
description: Aspose.PDF para PHP via Java permite criar documentos mais complexos que contêm imagens, fragmentos de texto e tabelas em um único documento.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

O exemplo [Hello, World](/pdf/php-java/hello-world-example/) mostrou etapas simples para criar um documento PDF usando Aspose.PDF. Neste artigo, vamos dar uma olhada em como criar um documento mais complexo com Aspose.PDF para PHP via Java. Como exemplo, usaremos um documento de uma empresa fictícia que opera serviços de balsa para passageiros.

Se criarmos um documento do zero, precisamos seguir certas etapas:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Nesta etapa, criaremos um documento PDF vazio com alguns metadados, mas sem páginas.

1. Adicione uma [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) ao objeto do documento. Agora, nosso documento terá uma página.
1. Adicione uma [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). É uma operação complexa baseada em ações de baixo nível com operadores PDF.
    - Carregar imagem de um stream
    - Adicionar imagem à coleção de Imagens dos Recursos da Página
    - Usando o operador GSave: este operador salva o estado atual dos gráficos.
    - Crie um objeto [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Usando o operador ConcatenateMatrix: define como a imagem deve ser colocada.
    - Usando o operador Do: este operador desenha a imagem.
    - Usando o operador GRestore: este operador restaura o estado dos gráficos.
1. Crie um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para o cabeçalho. Para o cabeçalho, usaremos a fonte Arial com tamanho 24pt e alinhamento centralizado.

1. Adicionar cabeçalho à página [Parágrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Criar um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para a descrição. Para a descrição, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento centralizado.
1. Adicionar (descrição) aos Parágrafos da página.
1. Criar uma tabela, adicionar propriedades à tabela.
1. Adicionar (tabela) aos [Parágrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) da página.
1. Salvar um documento "Complex.pdf".

```php

    $document = new Document();
    //Adicionar página
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // Adicionar imagem
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // Adicionar Cabeçalho
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("Novas rotas de ferry no outono de 2020");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // Adicionar descrição
    $descriptionText = "Os visitantes devem comprar ingressos online e os ingressos são limitados a 5.000 por dia. O serviço de ferry está operando com metade da capacidade e em horário reduzido. Espere filas.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // Adicionar tabela
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("Sai da Cidade");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("Sai da Ilha");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```