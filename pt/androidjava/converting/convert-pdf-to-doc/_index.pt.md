---
title: Convert PDF to DOC 
linktitle: Convert PDF to DOC
type: docs
weight: 70
url: /androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: Converta arquivo PDF para o formato DOC com facilidade e controle total com Aspose.PDF para Android via Java. Saiba mais sobre como ajustar a conversão de arquivo Doc do Microsoft Word para PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Uma das funcionalidades mais populares é a conversão de PDF para Microsoft Word DOC, que facilita a manipulação do conteúdo. Aspose.PDF para Android via Java permite converter arquivos PDF para DOC.

**Aspose.PDF para Android via Java** pode criar documentos PDF do zero e é uma excelente ferramenta para atualizar, editar e manipular documentos PDF existentes.
 Uma característica importante é a capacidade de converter páginas e documentos PDF inteiros em imagens. Outra característica popular é a conversão de PDF para DOC do Microsoft Word, o que torna o conteúdo fácil de manipular. (A maioria dos usuários não pode editar documentos PDF, mas pode facilmente trabalhar com tabelas, texto e imagens no Microsoft Word.)

Para simplificar e tornar as coisas compreensíveis, o Aspose.PDF para Android via Java fornece um código de duas linhas para transformar um arquivo PDF de origem em um arquivo DOC.

{{% alert color="primary" %}}

Tente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

O trecho de código a seguir mostra o processo de conversão de um arquivo PDF em formato DOC.

```java
 public void convertPDFtoDOC() {
        // Abra o documento PDF de origem
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Salve o arquivo no formato de documento MS
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```