---
title: Trabalhando com Metadados de Arquivo PDF
linktitle: Metadados de Arquivo PDF
type: docs
weight: 140
url: pt/java/pdf-file-metadata/
description: Esta seção explica como obter informações de arquivo PDF, como obter Metadados XMP de um arquivo PDF, definir Informações de Arquivo PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Informações de Arquivo PDF

Para obter informações específicas de arquivo sobre um arquivo PDF, primeiro obtenha o objeto [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Uma vez que o objeto [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) é recuperado, você pode obter os valores das propriedades individuais.

O seguinte trecho de código mostra como definir informações de arquivo PDF.

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // Criar um novo documento PDF
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // Obter informações do documento
        DocumentInfo docInfo = pdfDocument.getInfo();
        // Mostrar informações do documento
        System.out.println("Autor: " + docInfo.getAuthor());
        System.out.println("Data de Criação: " + docInfo.getCreationDate());
        System.out.println("Palavras-chave: " + docInfo.getKeywords());
        System.out.println("Data de Modificação: " + docInfo.getModDate());
        System.out.println("Assunto: " + docInfo.getSubject());
        System.out.println("Título: " + docInfo.getTitle());
    }
```


## Definir Informações do Arquivo PDF

Aspose.PDF para Java permite que você defina informações específicas para um arquivo PDF, como autor, data de criação, assunto e título.

Para definir esta informação:

1. Crie um objeto [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo).
1. Defina os valores das propriedades.
1. Salve o documento atualizado usando o método [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

{{% alert color="primary" %}}

Por favor, note que você não pode definir valores para os campos **Producer** e **Creator**, porque Aspose.PDF para Java x.x.x será exibido nesses campos.

{{% /alert %}}

O seguinte trecho de código mostra como definir informações do arquivo PDF.

```java
 public static void SetPDFFileInformation() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Especificar informações do documento
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("Informações do PDF");
        docInfo.setTitle("Definindo Informações do Documento PDF");

        // Salvar documento de saída
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```


## Obter Metadados XMP de um Arquivo PDF

Aspose.PDF para Java permite que você acesse os metadados XMP de um arquivo PDF.

Para obter os metadados de um arquivo PDF,

1. Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e abra o arquivo PDF de entrada.
1. Use a propriedade [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) para obter os metadados.

O seguinte trecho de código mostra como obter metadados do arquivo PDF.

```java
   public static void GetXMPMetadata() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## Definir Metadados XMP em um Arquivo PDF

Aspose.PDF para Java permite que você defina metadados em um arquivo PDF.
 Para definir metadados:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Defina os valores de metadados usando a propriedade [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--).
1. Salve o documento atualizado usando o método [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O trecho de código a seguir mostra como definir metadados em um arquivo PDF.

```java
    public static void SetXMPMetadata() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Definir propriedades
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // Salvar documento
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## Inserir Metadados com Prefixo

Alguns desenvolvedores precisam criar um novo namespace de metadados com um prefixo. O trecho de código a seguir mostra como inserir metadados com prefixo.

```java
    public static void InsertMetadataWithPrefix() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("alternative title"));        
        // Salvar documento
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```