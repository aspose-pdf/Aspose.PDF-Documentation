---
title: Criando PDF conforme PDF/3-A e anexando fatura ZUGFeRD em Java
linktitle: Anexar ZUGFeRD ao PDF
type: docs
weight: 10
url: pt/java/attach-zugferd/
description: Aprenda a gerar um documento PDF com ZUGFeRD no Aspose.PDF para Java
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Anexar ZUGFeRD ao PDF

Recomendamos as seguintes etapas para anexar ZUGFeRD ao PDF:

* Defina uma variável de caminho que aponte para uma pasta onde os arquivos PDF de entrada e saída estão localizados.
* Defina uma variável de string path que armazene o caminho para o arquivo PDF que será processado. Use o método `Paths.get` para combinar partes do caminho completo.
* Crie uma declaração try-with-resources que garanta que o objeto Document criado a partir da variável de caminho seja fechado automaticamente após o término da declaração. O objeto Document representa o documento PDF que será modificado e salvo.

* Crie um objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) fornecendo o caminho e a descrição de outro arquivo, que contém metadados de fatura em conformidade com o padrão ZUGFeRD.
* Adicione propriedades ao objeto de especificação do arquivo, como a descrição, tipo MIME e AFrelationship. O AFrelationship indica como o arquivo incorporado está relacionado ao documento PDF. Neste caso, está definido como "Alternative", significando que o arquivo incorporado é uma representação alternativa do conteúdo do PDF.
* Adicione o objeto de especificação do arquivo à coleção de arquivos incorporados do documento. O nome do arquivo deve ser especificado de acordo com o padrão ZUGFeRD, por exemplo, "factor-x.xml".
* Converta o documento para o formato PDF/A-3U, um subconjunto do PDF que garante a preservação a longo prazo de documentos eletrônicos. O PDF/A-3U permite a incorporação de arquivos de qualquer formato em documentos PDF.
* Salve o documento convertido como um novo arquivo PDF (por exemplo, "ZUGFeRD-res.pdf").
* Feche a instrução try-with-resources e libere o objeto Document.

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "Metadados de fatura conforme o padrão ZUGFeRD";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // Adicionar anexo à coleção de anexos do documento
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```