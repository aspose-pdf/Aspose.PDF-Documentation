---
title: Criando um PDF compatível com PDF/A-3 e anexando uma fatura ZUGFeRD em C#
linktitle: Anexar ZUGFeRD ao PDF
type: docs
weight: 10
url: pt/net/attach-zugferd/
description: Aprenda a gerar um documento PDF com ZUGFeRD no Aspose.PDF para .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Anexar ZUGFeRD ao PDF

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Recomendamos seguir os seguintes passos para anexar ZUGFeRD ao PDF:

* Defina uma variável de caminho que aponte para uma pasta onde os arquivos PDF de entrada e saída estão localizados.
* Crie um objeto de documento carregando um arquivo PDF existente (por exemplo, "ZUGFeRD-test.pdf") a partir do caminho.
* Crie um objeto [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) fornecendo o caminho e a descrição de outro arquivo chamado "factur-x.xml", que contém metadados de fatura conforme o padrão ZUGFeRD.
* Adicione propriedades ao objeto de especificação de arquivo, como a descrição, tipo MIME e relação AF.
* Adicione propriedades ao objeto de especificação de arquivo, como a descrição, tipo MIME e relação AF.
* Adicione o objeto de especificação de arquivo à coleção de arquivos embutidos do documento. O nome do arquivo deve ser especificado conforme o padrão ZUGFeRD, por exemplo, "factur-x.xml".
* Converta o documento para o formato PDF/A-3U, um subconjunto do PDF que garante a preservação de longo prazo dos documentos eletrônicos. O PDF/A-3U permite a incorporação de arquivos de qualquer formato em documentos PDF.
* Salve o documento convertido como um novo arquivo PDF (por exemplo, "ZUGFeRD-res.pdf").

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// Configurar novo arquivo para ser adicionado como anexo
var description = "Metadados de fatura conforme o padrão ZUGFeRD";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// Adicionar anexo à coleção de arquivos embutidos do documento
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```
O método convert recebe um stream, um formato PDF e uma ação de erro de conversão como parâmetros. O parâmetro stream pode ser usado para salvar o log de conversão. O parâmetro de ação de erro de conversão especifica o que fazer se ocorrer algum erro durante a conversão. Neste caso, está definido como "Delete", o que significa que quaisquer elementos que não estejam em conformidade com o formato PDF/A-3U serão excluídos do documento.
