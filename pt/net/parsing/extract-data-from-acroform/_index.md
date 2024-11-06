---
title:  Extrair dados de AcroForm usando C#
linktitle:  Extrair dados de AcroForm
type: docs
weight: 50
url: pt/net/extract-data-from-acroform/
description: Aspose.PDF facilita a extração de dados de campos de formulário de arquivos PDF. Aprenda como extrair dados de AcroForms e salvá-los em formato JSON, XML ou FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair campos de formulário de documento PDF

Além de permitir que você gere campos de formulário e preencha campos de formulário, o Aspose.PDF para .NET facilita a extração de dados de campos de formulário ou informações sobre campos de formulário de arquivos PDF.

No código de exemplo abaixo, demonstramos como iterar por cada página em um PDF para extrair informações sobre todos os AcroForm no PDF, bem como os valores dos campos de formulário. Este código de exemplo presume que você não conhece o nome dos campos de formulário antecipadamente.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // Obter valores de todos os campos
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("Nome do Campo : {0} ", formField.PartialName);
        Console.WriteLine("Valor : {0} ", formField.Value);
    }
}
```
Se você conhece o nome dos campos do formulário dos quais deseja extrair valores, então pode usar o indexador na coleção Documents.Form para recuperar rapidamente esses dados. Veja no final deste artigo um exemplo de código sobre como usar essa função.

## Recuperar valor do campo do formulário pelo título

A propriedade Value do campo do formulário permite obter o valor de um campo específico. Para obter o valor, pegue o campo do formulário da coleção Form do objeto Document. Este exemplo seleciona um TextBoxField e recupera seu valor usando a propriedade Value.

## Extrair campos de formulário de um documento PDF para JSON

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```
## Extrair Dados para XML de um Arquivo PDF

A classe Form permite que você exporte dados para um arquivo XML a partir do arquivo PDF usando o método ExportXml. Para exportar dados para XML, você precisa criar um objeto da classe Form e então chamar o método ExportXml usando o objeto FileStream. Finalmente, você pode fechar o objeto FileStream e descartar o objeto Form. O seguinte trecho de código mostra como exportar dados para um arquivo XML.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// Abrir documento
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// Criar arquivo xml.
System.IO.FileStream xmlOutputStream = new FileStream( dataDir + "input.xml", FileMode.Create);
// Exportar dados
form.ExportXml(xmlOutputStream);
// Fechar fluxo de arquivo
xmlOutputStream.Close();

// Fechar o documento
form.Dispose();
```
## Exportar Dados para FDF de um Arquivo PDF

A classe Form permite que você exporte dados para um arquivo FDF a partir do arquivo PDF usando o método ExportFdf. Para exportar dados para FDF, você precisa criar um objeto da classe Form e então chamar o método ExportFdf usando o objeto FileStream. Finalmente, você pode salvar o arquivo PDF usando o método Save da classe Form. O seguinte trecho de código mostra como exportar dados para um arquivo FDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Abrir Documento
form.BindPdf(dataDir + "input.pdf");

// Criar arquivo fdf.
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// Exportar dados
form.ExportFdf(fdfOutputStream);

// Fechar fluxo de arquivo
fdfOutputStream.Close();

// Salvar documento atualizado
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```
## Exportar Dados para XFDF de um Arquivo PDF

A classe Form permite que você exporte dados para um arquivo XFDF a partir do arquivo PDF usando o método ExportXfdf. Para exportar dados para XFDF, você precisa criar um objeto da classe Form e então chamar o método ExportXfdf usando o objeto FileStream. Finalmente, você pode salvar o arquivo PDF usando o método Save da classe Form. O seguinte trecho de código mostra como exportar dados para um arquivo XFDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Abrir Documento
form.BindPdf(dataDir + "input.pdf");

// Criar arquivo xfdf.
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// Exportar dados
form.ExportXfdf(xfdfOutputStream);

// Fechar fluxo de arquivo
xfdfOutputStream.Close();

// Salvar documento atualizado
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```

