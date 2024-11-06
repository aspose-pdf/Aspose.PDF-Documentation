---
title: Criar Documento PDF 
linktitle: Criar
type: docs
weight: 10
url: pt/php-java/create-document/
description: Aprenda a criar arquivo PDF no Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para PHP via Java** API permite que desenvolvedores de aplicações integrem a funcionalidade de processamento de documentos PDF em suas aplicações. Ele pode ser usado para criar e ler arquivos PDF sem a necessidade de qualquer outro software instalado na máquina subjacente. Aspose.PDF para PHP via Java pode ser usado em diversos tipos de aplicações, como aplicações Desktop, JSP e JSF.

## Como criar um arquivo PDF usando PHP via Java

Para criar um arquivo PDF usando PHP via Java, os seguintes passos podem ser utilizados.

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Adicionar uma [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) ao objeto documento

1. Crie um objeto [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)
1. Adicione [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) à coleção [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) da página
1. Salve o documento PDF resultante

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Olá Mundo!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```