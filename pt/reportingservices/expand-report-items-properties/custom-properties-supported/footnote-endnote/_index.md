---
title: Nota de rodapé Nota de fim
linktitle: Nota de rodapé Nota de fim
type: docs
weight: 30
url: /pt/reportingservices/footnote-endnote/
description: Adicione notas de rodapé e notas de fim aos seus relatórios PDF com Aspose.PDF for Reporting Services. Forneça referências detalhadas de documentos.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

O Report Builder não pode definir a nota de rodapé ou a nota de fim para caixas de texto. Com Aspose.Pdf for Reporting Services, você pode fazer isso facilmente adicionando propriedades personalizadas.

{{% /alert %}}

{{% alert color="primary" %}}
Nota de rodapé
**Propriedade Personalizada** **Nome**: Nota de rodapé
**Valor da Propriedade Personalizada**: *o* *valor* *deve* *ser* *uma* *string*

Nota de fim
**Propriedade Personalizada** **Nome**: Nota de fim
**Valor da Propriedade Personalizada**: *o* *valor* *deve* *ser* *uma* *string*

{{% alert color="primary" %}}
No exemplo a seguir, o relatório contém uma Textbox com o valor 'AsposePdf4RS', e queremos adicionar uma descrição suplementar na forma de uma nota de rodapé com o texto "Um renderizador PDF opcional para SSRS da Aspose Pty. Ltd.".
{{% /alert %}}

**Exemplo**

```cs
<Textbox Name="Textbox1">
...
<Paragraphs>
              <Paragraph>
                   <TextRuns>
                       <TextRun>
                            ......
                            <Value>AsposePdf4RS</Value>
                            <Style>
                               ......
                            </Style>
                    <CustomProperties>
                 <CustomProperty>
                      <Name>Footnote</Name>
                      <Value>An optional PDF renderer for SSRS from Aspose Pty. Ltd.</Value>
                      </CustomProperty>
                 </CustomProperties>
                       </TextRun>
                   </TextRuns>
</Paragraph>
</Paragraphs>
</Textbox>
```
{{% /alert %}}

