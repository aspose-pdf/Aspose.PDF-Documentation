---
title: ASP - JScript via COM Interop
type: docs
weight: 40
url: /pt/net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

Esta é uma aplicação ASP simples que mostra como adicionar uma string de texto simples a um arquivo PDF usando [Aspose.PDF for .NET](/pdf/pt/net/) e JScript via COM Interop.

{{% /alert %}}

Exemplo:

{{% alert color="primary" %}}

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title> Usando Aspose.PDF for .NET em exemplo clássico de ASP</title>
    </head>
    <body>
        <h3>Criação de um documento PDF de exemplo usando Aspose.PDF for .NET com ASP clássico e JScript</h3>
<%
// definir licença
var lic = Server.CreateObject("Aspose.PDF.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// Instanciar Pdf por meio de seu construtor vazio
var pdf = Server.CreateObject("Aspose.PDF.Document");

// Criar uma nova Página no objeto PDF
var pdfpage = pdf.Pages.Add();

// Criar objeto Fragmento de Texto
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// Atribuir algum conteúdo ao Fragmento
sampleText.Text = "HelloWorld usando ASP e JScript";

// Adicionar parágrafo de Texto à coleção de parágrafos de uma seção
pdfpage.Paragraphs.Add(sampleText);

// Salvar o documento PDF
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```

{{% /alert %}}
