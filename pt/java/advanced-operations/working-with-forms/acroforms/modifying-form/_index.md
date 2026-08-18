---
title: Modificando o AcroForm
linktitle: Modificando o AcroForm
type: docs
weight: 45
url: /java/modifying-form/
description: Modifique campos AcroForm em documentos PDF usando Aspose.PDF para Java, incluindo limpeza de texto, definição de limites, estilização de campos e remoção de campos.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modifique e personalize campos de formulário PDF com Java
Abstract: Este artigo explica como modificar o conteúdo do AcroForm usando Aspose.PDF para Java. Ele cobre a limpeza de texto dos recursos de formulário da máquina de escrever, configuração e leitura de limites de comprimento de campo de texto, alteração da aparência da fonte do campo de formulário e exclusão de campos específicos por nome.
---
A manutenção de formulários geralmente envolve edições em nível de campo e limpeza de recursos de página relacionados ao formulário.

## Texto não criptografado em recursos de formulário incorporados

Use este exemplo quando o conteúdo do formulário da máquina de escrever precisar ser esvaziado sem remover os próprios objetos do formulário.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelos recursos do formulário de página e localize os formulários da máquina de escrever.
1. Limpe os fragmentos de texto absorvidos e salve o documento.

```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Definir um limite de comprimento de campo de texto

Use este exemplo quando um campo de texto aceitar apenas um número limitado de caracteres.

1. Crie uma fachada [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) e vincule o PDF de origem.
1. Defina o comprimento máximo para o campo de destino.
1. Salve o documento atualizado.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Obtenha um limite de comprimento de campo de texto

Use este exemplo quando precisar inspecionar o comprimento máximo atual de um campo de texto.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse o campo de destino da coleção de formulários.
1. Leia o limite de [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) e produza-o.

```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## Alterar a fonte de um campo de formulário

Use este exemplo quando um campo de texto existente precisar usar uma fonte ou aparência diferente.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse o alvo [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) e defina uma nova aparência padrão.
1. Salve o PDF atualizado.

```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```

## Excluir um campo de formulário por nome

Use este exemplo quando um campo específico precisar ser removido do AcroForm.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Exclua o campo de destino do formulário pelo seu nome.
1. Salve o documento atualizado.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
