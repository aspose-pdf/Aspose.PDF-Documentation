---
title: Extrair e Salvar um Anexo 
linktitle: Extrair e Salvar um Anexo
type: docs
weight: 20
url: pt/java/extract-and-save-an-attachment/
description: Aspose.PDF para Java permite obter todos os anexos de um documento PDF. Além disso, você pode obter um anexo individual do seu documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Anexos de um Documento PDF

Com o Aspose.PDF, é possível obter todos os anexos de um documento PDF. Isso é útil tanto quando você deseja salvar os documentos separadamente do PDF, quanto se precisar remover anexos de um PDF.

Os seguintes trechos de código mostram como obter todos os anexos de um documento PDF.

```java
   public static void GetAttachmentsFromPDFDocument() {
// Abrir documento
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Obter arquivo incorporado específico
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Obter as propriedades do arquivo
  System.out.printf("Nome: - " + fileSpecification.getName());
  System.out.printf("\nDescrição: - " + fileSpecification.getDescription());
  System.out.printf("\nTipo Mime: - " + fileSpecification.getMIMEType());
  // Obter anexo do arquivo PDF
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // Criar caminho para o arquivo a partir do pdf
   file.getParentFile().mkdirs();
   // Criar e extrair arquivo do pdf
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // Fechar objeto InputStream
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // Fechar objeto Document
  pdfDocument.dispose();
        
    }

```


## Obter Informações do Anexo

Conforme mencionado em [Obter Anexos de um Documento PDF](/pdf/java/get-attachments-from-a-pdf-document/), as informações do anexo são mantidas no objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification), reunidas com outros anexos na coleção EmbeddedFiles do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) fornece métodos que obtêm informações sobre o anexo, por exemplo:

- getName() – obtém o nome do arquivo.
- [getDescription()](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – obtém a descrição do arquivo.
- getMIMEType() – obtém o tipo MIME do arquivo.
- getParams() – informações sobre os parâmetros do arquivo, por exemplo CheckSum, CreationDate, ModDate e Size.

Para obter esses parâmetros, primeiro certifique-se de que o método getParams() não retorne nulo.

Você pode percorrer todos os anexos na coleção EmbeddedFiles usando um loop for, ou obter um anexo individual especificando seu valor de índice.
 O seguinte trecho de código mostra como obter informações sobre um anexo específico.

```java
    public static void GetAttachmentInformation() {
  // Abrir documento
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Obter arquivo incorporado específico
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Obter as propriedades do arquivo
  System.out.println("Nome:-" + fileSpecification.getName());
  System.out.println("Descrição:- " + fileSpecification.getDescription());
  System.out.println("Tipo Mime:-" + fileSpecification.getMIMEType());
  // Verificar se o objeto de parâmetro contém os parâmetros
  if (fileSpecification.getParams() != null) {
   System.out.println("CheckSum:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Data de Criação:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Data de Modificação:- " + fileSpecification.getParams().getModDate());
   System.out.println("Tamanho:- " + fileSpecification.getParams().getSize());
  } 
```