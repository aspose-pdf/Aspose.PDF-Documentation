---
title: Mesclar PDF programaticamente
linktitle: Mesclar arquivos PDF
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: Esta página explica como mesclar documentos PDF em um único arquivo PDF com Java.
lastmod: "2021-06-05"
---

Agora, mesclar arquivos PDF é uma das tarefas mais demandadas.
Este artigo mostra como mesclar vários arquivos PDF em um único documento PDF usando Aspose.PDF para Java. O exemplo é escrito em Java, mas a API pode ser usada em outras linguagens de programação. Os arquivos PDF são mesclados de forma que o primeiro seja unido ao final do outro documento.

## Mesclar arquivos PDF usando Java

{{% alert color="primary" %}}

Você pode mesclar arquivos PDF usando Aspose.PDF e obter os resultados online neste link: [products.aspose.app/pdf/merger](https://products.aspose.app/pdf/merger)

{{% /alert %}}

Para concatenar dois arquivos PDF:

1. Crie dois objetos [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document), cada um contendo um dos arquivos PDF de entrada.

1. Em seguida, chame o método Add da coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) para o objeto Document ao qual você deseja adicionar o outro arquivo PDF.
1. Passe a coleção PageCollection do segundo objeto Document para o método Add da primeira coleção PageCollection.
1. Finalmente, salve o arquivo PDF de saída usando o método Save.

O trecho de código a seguir mostra como concatenar arquivos PDF com Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMerge {
    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void Merge() {
        
        // Abrir o primeiro documento
        Document pdfDocument1 = new Document(_dataDir + "Concat1.pdf");
        // Abrir o segundo documento
        Document pdfDocument2 = new Document(_dataDir + "Concat2.pdf");

        // Adicionar páginas do segundo documento ao primeiro
        pdfDocument1.getPages().add(pdfDocument2.getPages());

        // Salvar arquivo de saída concatenado
        pdfDocument1.save(_dataDir+"ConcatenatePdfFiles_out.pdf");

    }

}
```