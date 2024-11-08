---
title: Nota de Rodapé Nota de Fim
type: docs
weight: 30
url: /pt/reportingservices/footnote-endnote/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O Report Builder não pode definir a nota de rodapé ou nota de fim para caixas de texto. Com Aspose.Pdf para Reporting Services, você pode fazer isso facilmente adicionando propriedades personalizadas.

{{% /alert %}}

{{% alert color="primary" %}}
Nota de Rodapé
**Nome da Propriedade Personalizada**: Footnote
**Valor da Propriedade Personalizada**: *o* *valor* *deve* *ser* *uma* *string*

Nota de Fim
**Nome da Propriedade Personalizada**: Endnote
**Valor da Propriedade Personalizada**: *o* *valor* *deve* *ser* *uma* *string*

{{% alert color="primary" %}}
No exemplo a seguir, o relatório contém uma Caixa de Texto com o valor 'AsposePdf4RS', e queremos adicionar uma descrição suplementar na forma de uma nota de rodapé com o texto "Um renderizador PDF opcional para SSRS da Aspose Pty. Ltd.".
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
                      <Value>Um renderizador PDF opcional para SSRS da Aspose Pty. Ltd.</Value>
                      </CustomProperty>
                 </CustomProperties>
                       </TextRun>
                   </TextRuns>
</Paragraph>
</Paragraphs>
</Textbox>
```
{{% /alert %}}