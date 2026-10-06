---
title: Dividir arquivos PDF em Java
linktitle: Dividir arquivos PDF
type: docs
weight: 60
url: /pt/java/split-pdf/
description: Aprenda como dividir um PDF em arquivos PDF de página única em Java usando Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividindo páginas PDF usando Java
Abstract: Este artigo mostra como dividir um documento PDF em arquivos PDF de página única separados em Java usando Aspose.PDF. O exemplo abre o documento de origem, percorre suas páginas, cria um novo documento para cada página e salva cada página como um arquivo PDF individual.
---
Dividir um PDF em arquivos separados é útil quando você precisa exportar cada página para revisão, armazenamento ou processamento posterior.

## Exemplo ao vivo

[Divisor Aspose.PDF](https://products.aspose.app/pdf/splitter) é um aplicativo online gratuito para testar a divisão de PDF em um navegador.

[![Aspose Dividir PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este exemplo usa o [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) classe para abrir um arquivo PDF e iterar pelas suas páginas. Para cada [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), cria um novo documento, adiciona a página a ele e salva o resultado como um arquivo PDF separado.

Para dividir um PDF em arquivos de página individuais em Java:

1. Abra o PDF de origem com o [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) construtor.
1. Iterar através do [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objetos retornados por `document.getPages()`.
1. Criar um novo vazio [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para cada página.
1. Adicionar o atual [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao novo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Salvar o novo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) com um nome de arquivo único.
1. Fechar ambos [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos quando o processamento estiver concluído.

## Dividir PDF em arquivos de página única

O exemplo Java a seguir é baseado em `SplitDocumentExamples.java` e salva páginas como `Page_1.pdf`, `Page_2.pdf`, e assim por diante.

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```
