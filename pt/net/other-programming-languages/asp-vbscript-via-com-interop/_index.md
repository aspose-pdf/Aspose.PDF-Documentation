---
title: ASP - VBScript via COM Interop
type: docs
weight: 30
url: /pt/net/asp-vbscript-via-com-interop/
---

## Pré-requisitos

{{% alert color="primary" %}}

    Por favor, verifique o artigo chamado Use Aspose.pdf para .NET via COM Interop.

{{% /alert %}}

## Exemplo Hello World! em VB Script

{{% alert color="primary" %}}

Esta é uma aplicação ASP simples que mostra como criar um arquivo PDF com texto de exemplo usando [Aspose.PDF para .NET](/pdf/pt/net/) e VBScript via COM Interop.

{{% /alert %}}

```vb

<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title> usando Aspose.PDF para .NET em exemplo clássico de ASP</title>
    </head>
<body>

<h3>criação de um documento PDF de exemplo usando Aspose.PDF para .NET com ASP clássico e VBScript</h3>

<%

'set license
Dim lic
Set lic = CreateObject("Aspose.PDF.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'Instantiate Pdf instance by calling its empty constructor
Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

'Create a new section in the Pdf object
Dim pdfsection
Set pdfsection = CreateObject("Aspose.PDF.Generator.Section")

'Add section to Pdf object
pdf.Sections.Add(pdfsection)

' Create Text object
Dim SampleText
Set SampleText = CreateObject("Aspose.PDF.Generator.Text")

'Add Text Segment to text object
Dim seg1
Set seg1 = CreateObject("Aspose.PDF.Generator.Segment")

'Assign some content to the segment
seg1.Content = "HelloWorld usando ASP e VBScript"

'Add segment (with red text color) to the paragraph
SampleText.Segments.Add(seg1)

' Add Text paragraph to paragraphs collection of a section
pdfsection.Paragraphs.Add(SampleText)

' Save the PDF document
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")

%>

    </body>
</html>
```
## Extraindo Texto usando VBScript

{{% alert color="primary" %}}
    Este exemplo de VBScript extrai texto de um documento PDF existente via COM Interop.
    Erro ao renderizar macro 'code' : Valor inválido especificado para o parâmetro lang
{{% /alert %}}
