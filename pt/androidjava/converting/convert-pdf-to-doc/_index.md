---
title: Converter PDF para DOC
linktitle: Converter PDF para DOC
type: docs
weight: 70
url: /pt/androidjava/convert-pdf-to-doc/
lastmod: "2026-07-01"
description: Converta arquivos PDF para o formato DOC com facilidade e total controle usando Aspose.PDF for Android via Java. Saiba mais sobre como otimizar a conversão de arquivos Microsoft Word Doc para PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Um dos recursos mais populares é a conversão de PDF para Microsoft Word DOC, que facilita a manipulação do conteúdo. Aspose.PDF for Android via Java permite converter arquivos PDF para DOC.

**Aspose.PDF for Android via Java** pode criar documentos PDF do zero e é um excelente conjunto de ferramentas para atualizar, editar e manipular documentos PDF existentes. Um recurso importante é a capacidade de converter páginas e documentos PDF completos em imagens. Outro recurso popular é a conversão de PDF para Microsoft Word DOC, que facilita a manipulação do conteúdo. (A maioria dos usuários não pode editar documentos PDF, mas pode trabalhar facilmente com tabelas, texto e imagens no Microsoft Word.)

Para tornar as coisas simples e compreensíveis, Aspose.PDF for Android via Java fornece um código de duas linhas para transformar um arquivo PDF de origem em um arquivo DOC.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

O trecho de código a seguir mostra o processo de conversão de um arquivo PDF para o formato DOC.

```java
 public void convertPDFtoDOC() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Save the file into MS document format
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


