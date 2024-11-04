---
title: Concatenar documentos PDF
type: docs
weight: 10
url: /java/concatenate-pdf-documents/
description: Esta seção explica como concatenar documentos PDF com com.aspose.pdf.facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Concatenar Arquivos PDF Usando Caminhos de Arquivos (Facades)

O método concatenate da classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) pode ser usado para concatenar dois arquivos PDF. O método concatenate permite que você passe três parâmetros: primeiro PDF de entrada, segundo PDF de entrada, e PDF de saída. O PDF de saída final contém ambos os arquivos PDF de entrada.

O trecho de código a seguir mostra como concatenar arquivos PDF usando caminhos de arquivos.

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // Criar objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Concatenar arquivos
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```


Em alguns casos, quando há muitos contornos, os usuários podem desativá-los configurando **CopyOutlines** para false e melhorar o desempenho da concatenação.

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // Criar objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Concatenar arquivos
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }

```

## Concatenar múltiplos arquivos PDF usando MemoryStreams

O método [Concatenate](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) da classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) leva os arquivos PDF de origem e o arquivo PDF de destino como parâmetros.
 Esses parâmetros podem ser caminhos para os arquivos PDF no disco ou podem ser MemoryStreams. Agora, para este exemplo, primeiro criaremos dois fluxos de arquivos para ler os arquivos PDF do disco. Em seguida, converteremos esses arquivos em arrays de bytes. Esses arrays de bytes dos arquivos PDF serão convertidos em MemoryStreams. Assim que obtivermos os MemoryStreams dos arquivos PDF, poderemos passá-los para o método de concatenação e mesclar em um único arquivo de saída.

O trecho de código a seguir mostra como concatenar vários arquivos PDF usando MemoryStreams:

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // Criar dois fluxos de arquivos para ler arquivos pdf
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // Criar arrays de bytes para manter o conteúdo dos arquivos PDF
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.le)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // Ler o conteúdo do arquivo PDF em arrays de bytes
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Agora, primeiro converta arrays de bytes em MemoryStreams e depois concatene esses streams
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // Criar instância da classe PdfFileEditor para concatenar streams
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // Concatenar ambos os MemoryStreams de entrada e salvar no MemoryStream de saída
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Converter MemoryStream de volta para array de bytes
                        byte[] data = pdfStream.ToArray();
                        // Criar um FileStream para salvar o arquivo PDF de saída
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // Escrever o conteúdo do array de bytes no fluxo de arquivo de saída
                        output.Write(data, 0, data.Length);
                        // Fechar arquivo de saída
                        output.Close();
                    }
                }
            }
            // Fechar arquivos de entrada
            fs1.Close();
            fs2.Close();
        }
```

## Concatenar Array de Arquivos PDF Usando Caminhos de Arquivos (Facades)

Se você quiser concatenar vários arquivos PDF, pode usar a sobrecarga do método de concatenação, que permite passar um array de caminhos de arquivos PDF. A saída final é salva como um arquivo mesclado criado a partir de todos os arquivos no array.

O trecho de código a seguir mostra como concatenar um array de arquivos PDF usando caminhos de arquivos.

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // Criar objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Array de arquivos
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // Concatenar arquivos
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## Concatenar Array de Arquivos PDF Usando Streams (Facades)

Concatenar um array de arquivos PDF não se limita apenas a arquivos residindo no disco.
 Você também pode concatenar um array de arquivos PDF a partir de streams. Se você deseja concatenar vários arquivos PDF, pode usar a sobrecarga apropriada do método Concatenate. Primeiro, você precisa criar um array de streams de entrada e um stream para o PDF de saída e, em seguida, chamar o método Concatenate. A saída será salva no stream de saída.

O snippet de código a seguir mostra como concatenar um array de arquivos PDF usando streams.

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // Criar objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Array de streams
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // Stream de saída
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // Concatenar arquivo
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## Concatenar Formulários PDF e manter nomes de campos exclusivos

A classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) no namespace [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) oferece a capacidade de concatenar os arquivos PDF.
 Agora, se os arquivos Pdf que devem ser concatenados tiverem campos de formulário com nomes de campo semelhantes, o Aspose.PDF fornece o recurso para manter os campos no arquivo Pdf resultante como únicos e também permite especificar o sufixo para tornar os nomes dos campos únicos. O método [KeepFieldsUnique](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--) de PdfFileEditor como verdadeiro tornará os nomes dos campos únicos quando os formulários Pdf forem concatenados. Além disso, o método [UniqueSuffix](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--) de PdfFileEditor pode ser usado para especificar o formato definido pelo usuário do sufixo que é adicionado ao nome do campo para torná-lo único quando os formulários são concatenados. Esta string deve conter a substring %NUM%, que será substituída por números no arquivo resultante.

Veja o seguinte trecho de código simples para alcançar essa funcionalidade.

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // Definir caminhos de arquivo de entrada e saída

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // Instanciar Objeto PdfFileEditor
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // Para manter ID de campo único para todos os campos
                KeepFieldsUnique = true,
                // Formato do sufixo que é adicionado ao nome do campo para torná-lo único quando os formulários são concatenados.
                UniqueSuffix = "_%NUM%"
            };

            // Concatenar os arquivos em um arquivo Pdf resultante
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## Concatenate Inserir página em branco

Depois que os arquivos PDF foram mesclados, podemos inserir uma página em branco no início do documento na qual podemos criar o Índice. Para cumprir este requisito, podemos carregar o arquivo mesclado no objeto Documento e precisamos chamar o método Page.Insert(…) para inserir uma página em branco.

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // Criar objeto PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // Concatenar arquivos
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```