---
title: Funcionalidades Avançadas
type: docs
weight: 210
url: /pt/net/advanced-features/
---

## Enviando PDF para o Navegador para Download

Às vezes, quando você está desenvolvendo uma aplicação ASP.NET, você precisa enviar arquivo(s) PDF para navegador(es) web para download sem salvá-los fisicamente. Para alcançar isso, você pode salvar o documento PDF em um objeto MemoryStream após gerá-lo e passar bytes desse MemoryStream para o objeto Response. Fazendo isso, o navegador fará o download do documento PDF gerado.

O seguinte trecho de código demonstra a funcionalidade acima:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-Examples.Web-SendPdfToBrowserForDownload.aspx-1.cs" >}}

## Extraindo arquivos embutidos de um arquivo PDF

Aspose.PDF se destaca quando se trata de funcionalidades avançadas para trabalhar com arquivos no formato PDF. Ele extrai arquivos embutidos de maneira muito mais eficaz do que outras ferramentas que oferecem essa funcionalidade.

Com o Aspose.PDF para .NET, você pode extrair eficientemente qualquer arquivo embutido, que pode ser uma fonte embutida, uma imagem, um vídeo ou um áudio.
Com o Aspose.PDF para .NET, você pode extrair eficientemente qualquer arquivo incorporado que pode ser uma fonte embutida, uma imagem, um vídeo ou um áudio.

O seguinte trecho de código extrai todos os arquivos embutidos de um arquivo PDF:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-DocumentConversion-PDFToXML-PDFToXML.cs" >}}

## Uso de Script Latex para Adicionar Expressões Matemáticas

Com Aspose.PDF, você pode adicionar expressões/formulas matemáticas dentro de um documento PDF usando script latex. Os seguintes exemplos mostram como essa funcionalidade pode ser usada de duas maneiras diferentes, para adicionar uma fórmula matemática dentro de uma célula de tabela:

### Sem preâmbulo e ambiente de documento

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript-WithoutPreambleanddocument.cs" >}}

### Com preâmbulo e ambiente de documento

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript2-WithPreambleanddocument.cs" >}}

### Suporte para Tags Latex
### Suporte para Tags Latex

O ambiente align é definido no pacote amsmath, e o ambiente proof é definido no pacote amsthm. Portanto, você deve especificar esses pacotes usando o comando \usepackage no preâmbulo do documento. E isso significa que você deve incluir o texto LaTeX dentro do ambiente do documento, conforme mostrado no seguinte exemplo de código.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Text-UseLatexScript3-UseLatexScript3.cs" >}}


