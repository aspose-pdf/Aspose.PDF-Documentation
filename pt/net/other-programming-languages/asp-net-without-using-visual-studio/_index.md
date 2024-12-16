---
title: ASP.NET sem usar o Visual Studio
type: docs
weight: 60
url: /pt/net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/pt/net/) pode ser usado para desenvolver páginas ou aplicativos ASP.NET sem usar o Visual Studio. Neste exemplo, escreveremos HTML e o código C# ou VB.NET em um único arquivo .aspx; isso é comumente conhecido como ASP.NET Instantâneo.

{{% /alert %}}

## Detalhes de implementação

{{% alert color="primary" %}}

Crie uma aplicação web de exemplo e copie Aspose.PDF.dll para um diretório chamado "Bin" no diretório do seu site ( *se a pasta bin não existir, crie uma* ). Em seguida, crie sua página .aspx e copie o seguinte código para ela.
Este exemplo mostra como usar [Aspose.PDF for .NET](/pdf/pt/net/) com código inline em uma página ASP.NET para criar um documento PDF simples com algum texto de exemplo dentro dele.
{{% /alert %}}

```cs

<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> usando Aspose.PDF para .NET com ASP.NET Inline</title>
    </head>
    <body>
        <h3>criação de um documento PDF simples enquanto usa Aspose.PDF para .NET com ASP.NET Inline</h3>
<%
    // definir licença
    Aspose.PDF.License lic = new Aspose.PDF.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // Inicializar objeto de documento
    Document document = new Document();
    // Adicionar página
    Page page = document.Pages.Add();
    // Adicionar texto à nova página
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Olá Mundo!"));
    // Salvar PDF atualizado
    var outputFileName = Path.Combine(_dataDir, "HelloWorld_out.pdf");
    document.Save( outputFileName );
%>

    </body>
</html>
```


