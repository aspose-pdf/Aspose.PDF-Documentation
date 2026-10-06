---
title: Definir Bandeira de Envio
linktitle: Definir Bandeira de Envio
type: docs
weight: 40
url: /pt/java/set-submit-flag/
description: Revisar a cobertura atual do Java para definir uma bandeira de envio em um botão de formulário PDF com a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Configuração da bandeira de envio em exemplos Java do FormEditor
Abstract: O conjunto atual de exemplos Java não expõe a configuração da bandeira de envio como um método de exemplo independente. Em vez disso, ela é demonstrada juntamente com a configuração da URL de envio em `setSubmitUrl(...)`.
---
O Java `FormEditorExamples.setSubmitUrl(...)` método inclui:

## Configurar uma bandeira de envio

1. Vincule o PDF de origem ao `FormEditor` fachada.
2. Defina a URL de envio para o campo de botão.
3. Defina a flag de envio para o formato necessário.
4. Salve o documento atualizado.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

Use esse exemplo combinado como o fluxo de trabalho Java com suporte de origem para configurar uma bandeira de envio neste repositório.
