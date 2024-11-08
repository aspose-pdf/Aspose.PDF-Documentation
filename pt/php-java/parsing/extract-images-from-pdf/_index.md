---
title: Extrair Imagens do PDF 
linktitle: Extrair Imagens
type: docs
weight: 20
url: /pt/php-java/extract-images-from-the-pdf-file/
description: Como extrair uma parte da imagem do PDF usando Aspose.PDF para PHP
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Cada página no documento PDF contém recursos (imagens, formulários e fontes). Podemos acessar esses recursos chamando o método [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). A classe [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contém [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) e podemos obter a lista de imagens chamando o método [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Assim, para extrair uma imagem de uma página, precisamos obter referência à página, depois aos recursos da página e por último à coleção de imagens. Podemos extrair uma imagem específica, por exemplo, pelo índice.

O índice da imagem retorna um objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
Este objeto fornece um método [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) que pode ser usado para salvar a imagem extraída. O snippet de código a seguir mostra como extrair imagens de um arquivo PDF.

```php

    // Carregar o documento PDF
    $document = new Document($inputFile);

    // Obter a primeira página do documento
    $page = $document->getPages()->get_Item(1);

    // Obter a coleção de imagens na página
    $xImageCollection = $page->getResources()->getImages();

    // Obter a primeira imagem da coleção
    $xImage = $xImageCollection->get_Item(1);

    // Criar um novo objeto FileOutputStream para salvar a imagem
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // Salvar a imagem no arquivo de saída
    $xImage->save($outputImage);

    // Fechar o arquivo de imagem de saída
    $outputImage->close();
```