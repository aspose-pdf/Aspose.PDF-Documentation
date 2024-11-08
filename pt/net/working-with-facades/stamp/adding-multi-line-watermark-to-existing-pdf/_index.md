---
title: Adicionando marca d'água de várias linhas
type: docs
weight: 10
url: /pt/net/adding-multi-line-watermark-to-existing-pdf/
description: Esta seção explica como adicionar marca d'água de várias linhas a um PDF existente usando a Classe FormattedText.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Muitos usuários desejam marcar seus documentos PDF com texto de várias linhas. Eles geralmente tentam usar `\n` e `<br>`, mas esses tipos de caracteres não são suportados pelo namespace Aspose.Pdf.Facades. Portanto, para tornar isso possível, adicionamos outro método chamado [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) na classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) do namespace Aspose.Pdf.Facades.

{{% /alert %}}

## Implementação

Por favor, consulte o seguinte trecho de código para adicionar marca d'água de várias linhas em um PDF existente.

```csharp

// Instanciar um objeto de carimbo
Stamp logoStamp = new Stamp();

// Instanciar um objeto da classe FormattedText
FormattedText formatText = new FormattedText("Hello World!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// Adicionar outra linha para o carimbo
formatText.AddNewLineText("Good Luck");
// Vincular logotipo ao PDF
logoStamp.BindLogo(formatText);
```