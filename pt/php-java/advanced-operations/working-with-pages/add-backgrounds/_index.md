---
title: Adicionar fundo ao PDF 
linktitle: Adicionar fundos
type: docs
weight: 110
url: /pt/php-java/add-backgrounds/
descriptions: Adicione uma imagem de fundo ao seu arquivo PDF usando PHP. Use o objeto BackgroundArtifact.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Imagens de fundo podem ser usadas para adicionar uma marca d'água ou outro design sutil aos documentos. No Aspose.PDF para PHP via Java, cada documento PDF é uma coleção de páginas e cada página contém uma coleção de artefatos. A classe [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) pode ser usada para adicionar uma imagem de fundo a um objeto de página.

O snippet de código a seguir mostra como adicionar uma imagem de fundo a páginas PDF usando o objeto BackgroundArtifact com PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Adicionar uma nova página ao objeto do documento
    $page = $document->getPages()->add();

    // Criar objeto BackgroundArtifact    
    $background = new BackgroundArtifact();

    // Especificar a imagem para o objeto backgroundArtifact
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // Adicionar backgroundArtifact à coleção de artefatos da página
    $page->getArtifacts()->add($background);

    // Salvar arquivo PDF atualizado
    $document->save($outputFile);
    $document->close();
```