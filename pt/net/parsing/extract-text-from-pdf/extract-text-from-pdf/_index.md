---
title: Extrair texto de PDF C#
linktitle: Extrair texto de PDF
type: docs
weight: 10
url: pt/net/extract-text-from-all-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF em C#. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Todas as Páginas de um Documento PDF

Extrair texto de um documento PDF é uma necessidade comum. Neste exemplo, você verá como Aspose.PDF para .NET permite a extração de texto de todas as páginas de um documento PDF. Você precisa criar um objeto da classe **TextAbsorber**. Depois, abra o PDF usando a classe **Document** e chame o método **Accept** da coleção **Pages**. A classe **TextAbsorber** absorve o texto do documento e retorna na propriedade **Text**. O seguinte trecho de código mostra como extrair texto de todas as páginas de um documento PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Criar objeto TextAbsorber para extrair texto
TextAbsorber textAbsorber = new TextAbsorber();
// Aceitar o absorvedor para todas as páginas
pdfDocument.Pages.Accept(textAbsorber);
// Obter o texto extraído
string extractedText = textAbsorber.Text;
// Criar um escritor e abrir o arquivo
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Escrever uma linha de texto no arquivo
tw.WriteLine(extractedText);
// Fechar o fluxo
tw.Close();
```
Chame o método **Accept** em uma página específica do objeto Documento. O Índice é o número específico da página de onde o texto precisa ser extraído.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// Criar objeto TextAbsorber para extrair texto
TextAbsorber textAbsorber = new TextAbsorber();
 
// Aceitar o absorvedor para uma página específica
pdfDocument.Pages[1].Accept(textAbsorber);

// Obter o texto extraído
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// Criar um escritor e abrir o arquivo
TextWriter tw = new StreamWriter(dataDir);

// Escrever uma linha de texto no arquivo
tw.WriteLine(extractedText);

// Fechar o fluxo
tw.Close();
```
## Extrair Texto das Páginas usando Text Device

Você pode usar a classe **TextDevice** para extrair texto de um arquivo PDF. TextDevice usa TextAbsorber em sua implementação, assim, na verdade, eles fazem a mesma coisa, mas TextDevice é implementado para unificar a abordagem "Device" para extrair qualquer coisa da página ImageDevice, PageDevice, etc. TextAbsorber pode extrair texto da Página, do PDF inteiro ou de XForm, sendo este TextAbsorber mais universal

### Extrair texto de todas as páginas

Os seguintes passos e trecho de código mostram como extrair texto de um PDF usando o dispositivo de texto.

1. Crie um objeto da classe Document com o arquivo PDF de entrada especificado
1. Crie um objeto da classe TextDevice
1. Use o objeto da classe TextExtractOptions para especificar as opções de extração
1. Use o método Process da classe TextDevice para converter conteúdos em texto
1. Salve o texto no arquivo de saída

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// String para manter o texto extraído
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // Criar dispositivo de texto
        TextDevice textDevice = new TextDevice();

        // Definir opções de extração de texto - definir modo de extração de texto (Raw ou Pure)
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // Converter uma página específica e salvar o texto no stream
        textDevice.Process(pdfPage, textStream);
        // Converter uma página específica e salvar o texto no stream
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // Fechar stream de memória
        textStream.Close();

        // Obter texto do stream de memória
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// Salvar o texto extraído no arquivo de texto
File.WriteAllText(dataDir, builder.ToString());
```
## Extrair Texto de uma região específica da página

A classe **TextAbsorber** oferece a capacidade de extrair texto de uma ou todas as páginas de um documento PDF. Esta classe retorna o texto extraído na propriedade **Text**. No entanto, se tivermos a necessidade de extrair texto de uma região específica da página, podemos usar a propriedade **Rectangle** de **TextSearchOptions**. A propriedade Rectangle recebe um objeto Rectangle como valor e, usando essa propriedade, podemos especificar a região da página da qual precisamos extrair o texto.

O método **Accept** de uma página é chamado para extrair o texto. Crie objetos das classes **Document** e **TextAbsorber**. Chame o método **Accept** na página individual, como **Page** Index, do objeto **Document**. O **Index** é o número da página específica de onde o texto precisa ser extraído. Você pode obter texto da propriedade **Text** da classe **TextAbsorber**. O seguinte trecho de código mostra como extrair texto de uma página individual.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Criar objeto TextAbsorber para extrair texto
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// Aceitar o absorvedor para a primeira página
pdfDocument.Pages[1].Accept(absorber);

// Obter o texto extraído
string extractedText = absorber.Text;
// Criar um escritor e abrir o arquivo
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Escrever uma linha de texto no arquivo
tw.WriteLine(extractedText);
// Fechar o fluxo
tw.Close();
```

## Extrair texto baseado em colunas

Um arquivo PDF pode ser composto por elementos de Texto, Imagem, Anotações, Anexos, Gráficos, etc e o Aspose.PDF para .NET oferece a funcionalidade de Adicionar, bem como manipular todos esses elementos.
Um arquivo PDF pode conter elementos como Texto, Imagem, Anotações, Anexos, Gráficos, etc. e o Aspose.PDF para .NET oferece recursos para Adicionar e manipular todos esses elementos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // Necessário reduzir o tamanho da fonte pelo menos para 70%
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```
### Segunda abordagem - Usando ScaleFactor

Nesta nova versão, também introduzimos várias melhorias no TextAbsorber e no mecanismo interno de formatação de texto. Agora, durante a extração de texto usando o modo ‘Pure’, você pode especificar a opção ScaleFactor, que pode ser outra abordagem para extrair texto de um documento PDF de várias colunas além da abordagem mencionada acima. Esse fator de escala pode ser configurado para ajustar a grade que é usada para o mecanismo interno de formatação de texto durante a extração de texto. Especificar os valores de ScaleFactor entre 1 e 0.1 (incluindo 0.1) tem o mesmo efeito que a redução de fonte.

Especificar os valores de ScaleFactor entre 0.1 e -0.1 é tratado como valor zero, mas faz com que o algoritmo calcule o fator de escala necessário durante a extração de texto automaticamente.
Especificar os valores de ScaleFactor entre 0.1 e -0.1 é tratado como valor zero, mas faz com que o algoritmo calcule o fator de escala necessário durante a extração automática de texto.

Propomos o uso de autoescala (ScaleFactor = 0) ao processar um grande número de arquivos PDF para extração de conteúdo de texto. Ou defina manualmente a redução redundante da largura da grade (cerca de ScaleFactor = 0,5). No entanto, você não deve determinar se o escalonamento é necessário para documentos concretos ou não. Se você definir uma redução redundante da largura da grade para o documento (que não precisa dela), o conteúdo de texto extraído permanecerá totalmente adequado. Por favor, dê uma olhada no seguinte trecho de código.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// Definir o fator de escala para 0,5 é suficiente para dividir colunas na maioria dos documentos
// Definir zero permite que o algoritmo escolha o fator de escala automaticamente
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText( dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```
{{% alert color="primary" %}}

Observe que não há uma correspondência direta entre o novo ScaleFactor e o antigo coeficiente de redução manual do tamanho da fonte. No entanto, por padrão, o algoritmo leva em conta o valor do tamanho da fonte que já foi reduzido por alguns motivos internos. Por exemplo, reduzir o tamanho da fonte de 10 para 7 tem o mesmo efeito que definir um fator de escala para 5/8 (= 0,625).

{{% /alert %}}

## Extrair Texto Destacado de um Documento PDF

Em vários cenários de extração de texto de um documento PDF, você pode ter a necessidade de extrair apenas o texto destacado do documento PDF. Para implementar essa funcionalidade, adicionamos os métodos TextMarkupAnnotation.GetMarkedText() e TextMarkupAnnotation.GetMarkedTextFragments() na API. Você pode extrair o texto destacado de um documento PDF filtrando TextMarkupAnnotation e usando os métodos mencionados. O seguinte trecho de código mostra como você pode extrair o texto destacado de um documento PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// Percorrer todas as anotações
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // Filtrar TextMarkupAnnotation
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // Recuperar fragmentos de texto destacados
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // Exibir texto destacado
            Console.WriteLine(tf.Text);
        }
    }
}
```

## Acessar Fragmentos de Texto e Elementos de Segmento a partir de XML

Às vezes precisamos acessar itens de TextFragement ou TextSegment quando processamos documentos PDF gerados a partir de XML.
Às vezes, precisamos acessar itens TextFragement ou TextSegment ao processar documentos PDF gerados a partir de XML.

O trecho de código a seguir também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```
