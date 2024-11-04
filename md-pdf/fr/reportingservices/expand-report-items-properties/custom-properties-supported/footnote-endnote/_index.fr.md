---
title: Note de bas de page Note de fin
type: docs
weight: 30
url: /reportingservices/footnote-endnote/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Report Builder ne peut pas définir la note de bas de page ou la note de fin pour les zones de texte. Avec Aspose.Pdf pour Reporting Services, vous pouvez le faire facilement en ajoutant des propriétés personnalisées.

{{% /alert %}}

{{% alert color="primary" %}}
Note de bas de page
**Nom de la propriété personnalisée**: Footnote
**Valeur de la propriété personnalisée**: *la* *valeur* *doit* *être* *une* *chaîne*

Note de fin
**Nom de la propriété personnalisée**: Endnote
**Valeur de la propriété personnalisée**: *la* *valeur* *doit* *être* *une* *chaîne*
{{% /alert %}}

{{% alert color="primary" %}}
Dans l'exemple suivant, le rapport contient une zone de texte avec la valeur 'AsposePdf4RS', et nous voulons ajouter une description complémentaire sous la forme d'une note de bas de page avec le texte "Un moteur de rendu PDF optionnel pour SSRS de Aspose Pty. Ltd.".
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
                      <Value>Un moteur de rendu PDF optionnel pour SSRS de Aspose Pty. Ltd.</Value>
                      </CustomProperty>
                 </CustomProperties>
                       </TextRun>
                   </TextRuns>
</Paragraph>
</Paragraphs>
</Textbox>
```