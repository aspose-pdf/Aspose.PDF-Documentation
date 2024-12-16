---
title: Utilizando Aspose.Pdf para .NET com Coldfusion
type: docs
weight: 300
url: /pt/net/using-aspose-pdf-for-net-with-coldfusion/
description: Você deve trabalhar com Aspose.Pdf para .NET com Coldfusion usando a classe PdfFileInfo
lastmod: "2021-07-14"
draft: false
---

{{% alert color="primary" %}}

Neste artigo, explicaremos como usar o Aspose.PDF para .NET com Coldfusion. Isso ajudará você a entender os detalhes da integração do Aspose.PDF para .Net e Coldfusion. Com a ajuda de um exemplo simples, mostrarei o processo de incorporação da funcionalidade do Aspose.PDF para .Net em suas aplicações Coldfusion.

{{% /alert %}}

## Contexto

Aspose.PDF para .NET é um componente que também oferece a capacidade de editar e manipular arquivos PDF existentes.
Aspose.PDF para .NET é um componente que também oferece a capacidade de editar e manipular arquivos PDF existentes.

## Pré-requisito

Para poder executar o Aspose.PDF para .Net com Coldfusion, você precisará do IIS, .Net 2.0 e Coldfusion. Testei o componente usando IIS 5, .Net 2.0 e Coldfusion 8. Há mais duas coisas que você precisa garantir ao instalar o Coldfusion. Primeiro, você deve especificar qual(is) site(s) sob o IIS estarão executando Coldfusion. Em segundo lugar, você terá que selecionar 'Serviços de Integração .Net' no instalador do Coldfusion. Os Serviços de Integração .Net permitem acessar a montagem de componentes .Net em aplicativos Coldfusion; neste caso, o componente será Aspose.PDF para .NET.

## Explicação

Primeiramente, você precisa copiar a DLL (Aspose.PDF.dll) para um local de onde você a acessará posteriormente; isso será definido como um caminho e atribuído ao atributo assembly da tag cfobject, conforme mostrado abaixo:

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.PDF.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```
O atributo de classe na tag acima aponta para a classe Aspose.PDF. Facades, que neste caso é PdfFileInfo. O atributo nome é o nome da instância da classe e será usado mais tarde no código para acessar métodos ou propriedades da classe. O atributo tipo especifica o tipo do componente - no nosso caso é .Net.

Um ponto importante que você deve ter em mente ao usar o componente .Net em Coldfusion é que, ao obter ou definir qualquer propriedade do objeto da classe, você deve seguir uma estrutura específica. Para definir uma propriedade, você usará a sintaxe Set_propertyname e para obter um valor de propriedade, você usará Get_propertyname.

Por exemplo

Definir um valor de propriedade:

```html
<cfset FilePath = ExpandPath("guide.pdf")>
```

Obter um valor de propriedade:

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

Um exemplo básico, mas completo para ajudá-lo a entender o processo de uso do Aspose.PDF para .NET em Coldfusion é dado abaixo.

### Vamos mostrar informações do arquivo PDF

```html
<!--- criar uma instância da classe PdfFileInfo --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.PDF.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- obter o caminho do arquivo pdf --->

<cfset FilePath = ExpandPath("guide.pdf")>

<!--- atribuir o caminho do arquivo pdf ao objeto da classe definindo sua propriedade inputfile --->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- Mostrar informações do arquivo --->

<cfoutput><b>Título:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>Assunto:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>Autor:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>Criador:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```
## Conclusão

{{% alert color="primary" %}}
Neste artigo, vimos que se seguirmos algumas regras básicas de integração entre Coldfusion e .Net, podemos incorporar muita funcionalidade e flexibilidade relacionadas à manipulação de documentos PDF, usando o Aspose.PDF para .NET em nossas aplicações Coldfusion.
{{% /alert %}}
