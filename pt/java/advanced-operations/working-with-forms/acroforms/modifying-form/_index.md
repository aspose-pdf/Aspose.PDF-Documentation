---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
weight: 45
url: /pt/java/modifying-form/
description: Modifique campos AcroForm em documentos PDF usando Aspose.PDF for Java, incluindo limpar texto, definir limites, estilizar campos e remover campos.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modifique e personalize campos de formulário PDF com Java
Abstract: Este artigo explica como modificar o conteúdo AcroForm usando Aspose.PDF for Java. Ele aborda limpar texto de recursos de formulário Typewriter, definir e ler limites de comprimento de campos de texto, alterar a aparência da Font dos campos de formulário e excluir campos específicos pelo nome.
---
A manutenção de Form frequentemente envolve tanto edições de nível de campo quanto a limpeza de recursos de página relacionados ao Form.

## Limpar texto em recursos de Form incorporados.

Use este exemplo quando o conteúdo de Form Typewriter deve ser esvaziado sem remover os próprios objetos do Form.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelos recursos de formulário da página e localize formulários Typewriter.
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

## Defina um limite de comprimento para o campo de texto

Use este exemplo quando um campo de texto deve aceitar apenas um número limitado de caracteres.

1. Criar um [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) fachada e vincular o PDF de origem.
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

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse o campo alvo a partir da coleção de formulários.
1. Leia o limite a partir do [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) e exiba-o.

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

Use este exemplo quando um campo de texto existente deve usar uma fonte ou aparência diferente.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Excluir um campo de formulário pelo nome

Use este exemplo quando um campo específico deve ser removido do AcroForm.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Exclua o campo de destino do formulário pelo nome.
1. Salve o documento atualizado.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
