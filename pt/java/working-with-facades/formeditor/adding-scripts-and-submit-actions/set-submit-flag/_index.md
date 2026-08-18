---
title: Definir sinalizador de envio
linktitle: Definir sinalizador de envio
type: docs
weight: 40
url: /java/set-submit-flag/
description: Revise a cobertura Java atual para definir um sinalizador de envio em um botão de formulário PDF com a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Enviar configuração de sinalizador em exemplos Java FormEditor
Abstract: The current Java sample set does not expose submit-flag configuration as a separate standalone example method. Instead, it is demonstrated together with submit URL configuration in `setSubmitUrl(...)`.
---
O método Java `FormEditorExamples.setSubmitUrl(...)` inclui:

## Configurar um sinalizador de envio

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Defina o URL de envio para o campo do botão.
3. Defina o sinalizador de envio para o formato necessário.
4. Salve o documento atualizado.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

Use esse exemplo combinado como fluxo de trabalho Java baseado na origem para configurar um sinalizador de envio neste repositório.
