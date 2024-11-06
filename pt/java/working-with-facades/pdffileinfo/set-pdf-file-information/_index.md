---
title: Definir informações do arquivo PDF - facades
type: docs
weight: 20
url: pt/java/set-pdf-information/
description: Esta seção explica como definir informações do arquivo PDF com Aspose.PDF Facades usando a classe PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A classe [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) permite que você defina informações específicas do arquivo de um documento PDF. Você precisa criar um objeto da classe [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) e, em seguida, definir diferentes propriedades específicas do arquivo, como Autor, Título, Palavra-chave e Criador, etc. Por fim, salve o arquivo PDF atualizado usando o método [saveNewInfo(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) do objeto [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo).

O trecho de código a seguir mostra como definir informações do arquivo PDF.

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Definir informações do PDF
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Hello World!");
        fileInfo.setKeywords("Peace and Development");
        fileInfo.setCreator ("Aspose");
        
        // Salvar arquivo atualizado
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```


## Definir Informações de Meta

O método [setMetaInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) permite que você adicione qualquer informação. Em nosso exemplo, adicionamos um campo. Confira o próximo trecho de código:

```java
   public static void SetMetaInfo()
    {
        // Criar instância do objeto PdfFileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // Definir novo atributo de cliente como meta informação
        fInfo.setMetaInfo("Reviewer", "Usuário do Aspose.PDF");

        // Salvar arquivo atualizado
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```