---
title: Trabalhando com Formulários XFA em PDF
linktitle: Formulários XFA
type: docs
weight: 20
url: /pt/java/xfa-forms/
description: Com Aspose.PDF para Java, você pode criar um formulário do zero, preencher o campo do formulário em um documento PDF, extrair dados do formulário, adicionar ou remover campos no formulário existente.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA significa Arquitetura de Formulários XML. É um conjunto de especificações XML proprietárias originalmente criado para uso com formulários da web em 1999 e, desde então, tornou-se disponível para PDF.

## Converter Formulário XFA Dinâmico para AcroForm Padrão

Formulários dinâmicos são baseados em uma especificação XML conhecida como XFA, a "Arquitetura de Formulários XML". Ele também pode converter formulário XFA dinâmico para Acroform padrão. A informação sobre o formulário (no que diz respeito ao PDF) é muito vaga – especifica que há campos, com propriedades e eventos JavaScript, mas não especifica nenhuma renderização. Os objetos do formulário XFA são desenhados no momento de carregar o documento.

Atualmente, o PDF suporta dois métodos diferentes para integrar dados e formulários PDF:

- AcroForms (também conhecidos como formulários Acrobat), introduzidos e incluídos na especificação do formato PDF 1.2.

- Formulários da Arquitetura de Formulários XML da Adobe (XFA), introduzidos na especificação do formato PDF 1.5 como um recurso opcional. (A especificação XFA não está incluída na especificação PDF, ela é apenas referenciada.)

Não é possível extrair ou manipular páginas de Formulários XFA, porque o conteúdo do formulário é gerado em tempo de execução (durante a visualização do formulário XFA) dentro do aplicativo que tenta exibir ou renderizar o formulário XFA. O Aspose.PDF possui um recurso que permite aos desenvolvedores converter formulários XFA em AcroForms padrão.

```java
// Carregar formulário XFA dinâmico
Document document = new Document("XFAform.pdf");
// Definir o tipo de campos do formulário como AcroForm padrão
document.getForm().setType(FormType.Standard);
// Salvar o PDF resultante
document.save("Standard_AcroForm.pdf");
```