---
title: Note de bas de page Note de fin
linktitle: Note de bas de page Note de fin
type: docs
weight: 30
url: /fr/reportingservices/footnote-endnote/
description: Ajoutez des notes de bas de page et des notes de fin à vos rapports PDF avec Aspose.PDF for Reporting Services. Fournissez des références détaillées aux documents.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Builder ne peut pas définir la note de bas de page ou la note de fin pour les zones de texte. Avec Aspose.Pdf for Reporting Services, vous pouvez le faire facilement en ajoutant des propriétés personnalisées.

{{% /alert %}}

{{% alert color="primary" %}}
Note de bas de page
**Propriété personnalisée** **Nom**: Note de bas de page
**Valeur de la propriété personnalisée**: *la* *valeur* *doit* *être* *une* *chaîne*

Note de fin
**Propriété personnalisée** **Nom**: Note de fin
**Valeur de la propriété personnalisée**: *la* *valeur* *doit* *être* *une* *chaîne*

{{% alert color="primary" %}}
Dans l'exemple suivant, le rapport contient une Textbox avec la valeur 'AsposePdf4RS', et nous voulons ajouter une description supplémentaire sous la forme d'une note de bas de page avec le texte "An optional PDF renderer for SSRS from Aspose Pty. Ltd.".
{{% /alert %}}

**Exemple**

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

