---
title: Mesclar PDF programaticamente
linktitle: Mesclar arquivos PDF
type: docs
weight: 50
url: /php-java/merge-pdf-documents/
description: Esta página explica como mesclar documentos PDF em um único arquivo PDF usando PHP.
lastmod: "2024-06-05"
---

Agora, mesclar arquivos pdf é uma das tarefas mais demandadas.
Este artigo mostra como mesclar vários arquivos PDF em um único documento PDF usando Aspose.PDF para PHP via Java. O exemplo é escrito em Java, mas a API pode ser utilizada em outras linguagens de programação. Os arquivos PDF são mesclados de modo que o primeiro é juntado ao final do outro documento.

## Mesclar Arquivos PDF usando PHP

{{% alert color="primary" %}}

Você pode mesclar arquivos PDF usando Aspose.PDF e obter os resultados online neste link: [Merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Para concatenar dois arquivos PDF:

1. Crie dois objetos [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), cada um contendo um dos arquivos PDF de entrada.

1. Em seguida, chame o método Add da coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) para o objeto Document ao qual você deseja adicionar o outro arquivo PDF.
1. Passe a coleção PageCollection do segundo objeto Document para o método Add da primeira coleção PageCollection.
1. Finalmente, salve o arquivo PDF de saída usando o método Save.

O trecho de código a seguir mostra como concatenar arquivos PDF usando PHP.

```php
    // Abrir o primeiro documento
    $document1 = new Document($inputFile1);
    
    // Abrir o segundo documento
    $document2 = new Document($inputFile2);

    // Adicionar páginas do segundo documento ao primeiro
    $document1->getPages()->add($document2->getPages());

    // Salvar arquivo de saída concatenado
    $document1->save($outputFile);
    $document1->close();
    $document2->close();
```