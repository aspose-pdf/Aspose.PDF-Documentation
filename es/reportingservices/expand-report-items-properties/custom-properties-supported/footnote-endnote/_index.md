---
title: Nota al pie Nota al final
linktitle: Nota al pie Nota al final
type: docs
weight: 30
url: /es/reportingservices/footnote-endnote/
description: Agregue notas al pie y notas al final a sus informes PDF con Aspose.PDF para Reporting Services. Proporcione referencias detalladas del documento.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Builder no puede establecer la nota al pie o la nota al final para los cuadros de texto. Con Aspose.PDF para Reporting Services, puede hacerlo fácilmente agregando propiedades personalizadas.

{{% /alert %}}

{{% alert color="primary" %}}
Nota al pie
**Propiedad personalizada** **Nombre**: Nota al pie
**Valor de la propiedad personalizada**: *el*\u00A0*valor* *debe*\u00A0*ser*\u00A0*una*\u00A0*cadena*

Nota al final
**Propiedad personalizada** **Nombre**: Nota al final
**Valor de la propiedad personalizada**: *el*\u00A0*valor* *debe*\u00A0*ser* *una*\u00A0*cadena*

{{% alert color="primary" %}}
En el siguiente ejemplo, el informe contiene un Textbox con el valor 'AsposePdf4RS', y queremos añadir una descripción suplementaria en forma de nota al pie con el texto \"An optional PDF renderer for SSRS from Aspose Pty. Ltd.\".
{{% /alert %}}

**Ejemplo**

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


