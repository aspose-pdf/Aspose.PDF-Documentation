---
title: Nota final
linktitle: Footnote Endnote
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: Adicione notas de rodapé e notas finais aos seus relatórios PDF com Aspose.PDF for Reporting Services. Forneça referências detalhadas de documentos.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O Report Builder não pode definir notas de rodapé ou notas finais para caixas de texto. Com Aspose.PDF for Reporting Services, você pode fazer isso facilmente adicionando propriedades personalizadas.

{{% /alert %}}

```text
Footnote
Custom Property `Name`: Footnote
Custom Property Value: `the` `value` `should` `be` `a` `string`
```

```text
Endnote
Custom Property `Name`: Endnote
Custom Property Value: `the` `value` `should` `be` `a` `string`
```

No exemplo a seguir, o relatório contém uma caixa de texto com o valor `AsposePdf4RS`, e queremos adicionar uma descrição suplementar na forma de uma nota de rodapé com o texto "Um renderizador PDF opcional para SSRS da Aspose Pty. Ltd.".

## Exemplo

```xml
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
