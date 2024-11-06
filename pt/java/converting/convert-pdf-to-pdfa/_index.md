---
title: Converter PDF para formatos PDF/A 
linktitle: Converter PDF para formatos PDF/A
type: docs
weight: 100
url: pt/java/convert-pdf-to-pdfa/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Java** permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A. Antes de fazer isso, o arquivo deve ser validado. Este artigo explica como.

Por favor, note que seguimos a Adobe Preflight para validar a conformidade com PDF/A. Todas as ferramentas do mercado têm sua própria "representação" da conformidade com PDF/A. Por favor, confira este artigo sobre [ferramentas de validação de PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) para referência. Escolhemos os produtos da Adobe para verificar como o Aspose.PDF produz arquivos PDF porque a Adobe está no centro de tudo o que está relacionado a PDF.

Antes de converter o PDF em um arquivo compatível com PDF/A, valide o PDF usando o método de validação.
 O resultado da validação é armazenado em um arquivo XML e, em seguida, este resultado também é passado para o método de conversão. Você também pode especificar a ação para os elementos que não podem ser convertidos usando a enumeração [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Conversão de PDF para PDF/A_1b

O seguinte trecho de código mostra como converter arquivos PDF para PDF/A-1b compatível.

```java
// Abrir documento
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Converter para documento compatível com PDF/A
// Durante o processo de conversão, a validação também é realizada
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// Salvar documento de saída
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

Para realizar apenas a validação, use a seguinte linha de código:

```java
// Abrir documento
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// Validar PDF para PDF/A-1a
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("Válido");
} else {
    System.out.println("Não válido");
}
document.close();
```

## Conversão de PDF para PDF/A_3b

A partir do [Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java), a API também suporta a conversão de arquivos PDF para o formato PDF/A_3b.

```java
// Abrir documento
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Converter para documento compatível com PDF/A
// Durante o processo de conversão, a validação também é realizada
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// Salvar documento de saída
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## Conversão de PDF para PDF/A_3a

A partir do [Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java), a API também suporta a conversão de arquivos PDF para o formato PDF/A_3a.

```java
// Abrir documento
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Converter para documento compatível com PDF/A
// Durante o processo de conversão, a validação também é realizada
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// Salvar documento de saída
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```


## Conversão de PDF para PDF/A_2a

A partir do lançamento do [Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java), a API oferece o recurso de converter arquivos PDF para o formato PDF/A3.

```java
    public static void ConvertPDFtoPDFa2a() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Converter para documento compatível com PDF/A
        // Durante o processo de conversão, a validação também é realizada
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Salvar documento de saída
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## Conversão de PDF para PDF/A_3U

A partir do lançamento do Aspose.PDF for Java 17.2.0, a API oferece o recurso de converter arquivos PDF para o formato PDF/A_3U.

```java
    public static void ConvertPDFtoPDFa3u() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Converter para documento compatível com PDF/A
        // Durante o processo de conversão, a validação também é realizada
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Salvar documento de saída
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```


## Criar PDF/A-3 e anexar arquivo XML

Aspose.PDF para Java oferece a funcionalidade de converter arquivos PDF para o formato PDF/A e também suporta as capacidades de adicionar arquivos como anexo ao documento PDF. Caso você tenha a necessidade de anexar arquivos ao formato de conformidade PDF/A, recomendamos usar o valor PDF_A_3A da enumeração com.aspose.pdf.PdfFormat, o PDF/A_3a é o formato que fornece a funcionalidade de anexar qualquer formato de arquivo como anexo a um arquivo compatível com PDF/A. No entanto, uma vez que o arquivo está anexado, você deve convertê-lo novamente para o formato Pdf-3a, a fim de corrigir os metadados. Por favor, dê uma olhada no trecho de código a seguir.

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // adicionar página ao arquivo PDF
        doc.getPages().add();
        // carregar arquivo XML
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "Arquivo xml de exemplo");
        // Adicionar anexo à coleção de anexos do documento
        doc.getEmbeddedFiles().add(fileSpecification);
        // realizar conversão para PDF/A_3a
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* ou PDF_A_3B */, ConvertErrorAction.Delete);
        // salvar arquivo PDF final
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```


{{% alert color="primary" %}}
**Tente converter PDF para PDF/A online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["PDF para PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão de Aspose.PDF de PDF para PDF/A com Aplicativo Gratuito](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}