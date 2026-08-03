---
title: Footnote Endnote
linktitle: Note de bas de page
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
description: Ajoutez des notes de bas de page et des notes de fin à vos rapports PDF avec Aspose.PDF pour Reporting Services. Fournissez des références détaillées aux documents.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Builder cannot set the footnote or endnote for textboxes. With Aspose.PDF for Reporting Services, you can do that easily by adding custom properties.

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

Dans l'exemple suivant, le rapport contient une zone de texte avec la valeur `AsposePdf4RS`, et nous souhaitons ajouter une description supplémentaire sous la forme d'une note de bas de page avec le texte « Un moteur de rendu PDF facultatif pour SSRS d'Aspose Pty. Ltd. ».

## Example

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
