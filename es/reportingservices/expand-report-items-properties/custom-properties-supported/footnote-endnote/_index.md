---
title: Nota al pie
linktitle: Nota al pie
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: Agregue notas al pie y notas finales a sus informes PDF con Aspose.PDF para Reporting Services. Proporcionar referencias documentales detalladas.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

El Generador de informes no puede establecer la nota al pie o la nota final para los cuadros de texto. Con Aspose.PDF para Reporting Services, puede hacerlo fácilmente agregando propiedades personalizadas.

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

En el siguiente ejemplo, el informe contiene un cuadro de texto con el valor `AsposePdf4RS` y queremos agregar una descripción complementaria en forma de nota al pie con el texto "Un procesador de PDF opcional para SSRS de Aspose Pty. Ltd."

## Ejemplo

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
