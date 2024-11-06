---
title: Obter informações do arquivo PDF
type: docs
weight: 50
url: pt/net/get-pdf-file-information/
description: Esta seção explica como obter informações do arquivo PDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Para obter informações específicas de um arquivo PDF, você precisa criar um objeto da classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Após isso, você pode obter valores das propriedades individuais como Assunto, Título, Palavras-chave e Criador etc.

O trecho de código a seguir mostra como obter informações do arquivo PDF.

```csharp
 public static void GetPdfInfo()
        {
            // Abrir documento
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
            // Obter informações do PDF
            Console.WriteLine("Assunto: {0}", fileInfo.Subject);
            Console.WriteLine("Título: {0}", fileInfo.Title);
            Console.WriteLine("Palavras-chave: {0}", fileInfo.Keywords);
            Console.WriteLine("Criador: {0}", fileInfo.Creator);
            Console.WriteLine("Data de Criação: {0}", fileInfo.CreationDate);
            Console.WriteLine("Data de Modificação: {0}", fileInfo.ModDate);
            // Verificar se é um PDF válido e se está criptografado também
            Console.WriteLine("É PDF Válido: {0}", fileInfo.IsPdfFile);
            Console.WriteLine("Está Criptografado: {0}", fileInfo.IsEncrypted);

            Console.WriteLine("Largura da página:{0}", fileInfo.GetPageWidth(1));
            Console.WriteLine("Altura da página:{0}", fileInfo.GetPageHeight(1));
        }
```

## Obter Informações Meta

Para obter informações, usamos a propriedade [Header](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/header). Com 'Hashtable' obtemos todos os valores possíveis.

```csharp
public static void GetMetaInfo()
        {
            // Criar instância do objeto PdfFileInfo
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");
            // Recuperar todos os atributos personalizados existentes
            Hashtable hTable = new Hashtable(fInfo.Header);

            IDictionaryEnumerator enumerator = hTable.GetEnumerator();
            while (enumerator.MoveNext())
            {
                string output = enumerator.Key.ToString() + " " + enumerator.Value;
                Console.WriteLine(output);
            }

            // Recuperar um atributo personalizado
            Console.WriteLine(fInfo.GetMetaInfo("Reviewer"));
```