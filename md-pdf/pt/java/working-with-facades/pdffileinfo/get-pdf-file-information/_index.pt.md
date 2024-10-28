---
title: Obter informações de arquivo PDF - fachadas
type: docs
weight: 10
url: /java/get-pdf-information/
description: Esta seção explica como obter informações de arquivo PDF com Aspose.PDF Facades usando a Classe PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para obter informações específicas de um arquivo PDF, você precisa criar um objeto da classe [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). Depois disso, você pode obter valores de propriedades individuais como Assunto, Título, Palavras-chave e Criador, etc.

O trecho de código a seguir mostra como obter informações de arquivo PDF.

```java
public static void GetPdfInfo()
    {
        // Abrir documento
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Obter informações do PDF
        System.out.println("Assunto: " + fileInfo.getSubject());
        System.out.println("Título: " + fileInfo.getTitle());
        System.out.println("Palavras-chave: " + fileInfo.getKeywords());
        System.out.println("Criador: " + fileInfo.getCreator());
        System.out.println("Data de Criação: " + fileInfo.getCreationDate());
        System.out.println("Data de Modificação: " + fileInfo.getModDate());
        // Verificar se é um PDF válido e se está criptografado também
        System.out.println("É PDF Válido: " + fileInfo.isPdfFile());
        System.out.println("Está Criptografado: " + fileInfo.isEncrypted());

        System.out.println("Largura da página:" +fileInfo.getPageWidth(1));
    }
```


## Obter Informações Meta

Para obter informações, usamos o método [getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--). Com 'Hashtable' obtemos todos os valores possíveis.

```java
public static void GetMetaInfo()
    {        
        // Criar instância do objeto PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // Recuperar todos os atributos personalizados existentes
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // obter chave
            String key = enumerator.nextElement();  
            // imprimir chave e valor correspondente a essa chave
            System.out.println(key + ": " + hTable.get(key));
        }

        // Recuperar um atributo personalizado
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```